import tkinter as tk
from tkinter import ttk
import re
from config import ICO_PATH

class JanelaDificuldades:

    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.window = None
        self._canvas = None
        self._scroll_frame = None
        self._difficulties = []
        self._cards = []
        self._busca_var = None

    def show(self):
        if self.window and self.window.winfo_exists():
            self.window.lift()
            self.window.focus_force()
            return
        self._criar_janela()

    def _criar_janela(self):
        self.window = tk.Toplevel(self.parent)
        self.window.withdraw()
        self.window.configure(bg="#ECECEC")

        try:
            icon = tk.PhotoImage(file=ICO_PATH)
            self.window.iconphoto(True, icon)
        except Exception:
            pass

        self.window.resizable(True, True)

        self._criar_barra_busca()
        self._criar_conteudo()

        self.window.deiconify()
        self.window.update_idletasks()
        self.window.attributes("-zoomed", True)
        self.window.focus_force()

    def _criar_barra_busca(self):
        barra = tk.Frame(self.window, bg="#F3E5F5", pady=10)
        barra.pack(fill="x", padx=0)

        inner = tk.Frame(barra, bg="#F3E5F5")
        inner.pack(padx=30)

        tk.Label(
            inner,
            text="🔍",
            font=("Segoe UI", 14),
            bg="#F3E5F5",
            fg="#7B1FA2"
        ).pack(side="left", padx=(0, 8))

        self._busca_var = tk.StringVar()
        self._busca_var.trace_add("write", self._filtrar)

        entry = tk.Entry(
            inner,
            textvariable=self._busca_var,
            font=("Segoe UI", 13),
            bg="white",
            fg="#212121",
            relief="flat",
            highlightthickness=2,
            highlightbackground="#CE93D8",
            highlightcolor="#7B1FA2",
            insertbackground="#7B1FA2",
            width=40,
        )
        entry.pack(side="left", ipady=7)

        tk.Label(
            inner,
            text="Filtre por matéria ou conteúdo",
            font=("Segoe UI", 10),
            bg="#F3E5F5",
            fg="#9E9E9E"
        ).pack(side="left", padx=(14, 0))

        self._label_resultado = tk.Label(
            inner,
            text="",
            font=("Segoe UI", 10, "italic"),
            bg="#F3E5F5",
            fg="#7B1FA2"
        )
        self._label_resultado.pack(side="right")

    def _criar_conteudo(self):
        main = tk.Frame(self.window, bg="#ECECEC")
        main.pack(fill="both", expand=True, padx=30, pady=(15, 0))

        self._canvas = tk.Canvas(main, bg="#ECECEC", highlightthickness=0)
        scrollbar = ttk.Scrollbar(main, orient="vertical", command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=scrollbar.set)

        self._scroll_frame = tk.Frame(self._canvas, bg="#ECECEC")
        self._scroll_frame.bind(
            "<Configure>",
            lambda _: self._canvas.configure(scrollregion=self._canvas.bbox("all"))
        )

        win_id = self._canvas.create_window((0, 0), window=self._scroll_frame, anchor="nw")
        self._canvas.bind(
            "<Configure>",
            lambda e: self._canvas.itemconfig(win_id, width=e.width)
        )

        self._difficulties = self.controller.get_all_difficulties()
        if not self._difficulties:
            self._mostrar_vazio()
        else:
            self._renderizar_cards(self._difficulties)

        scrollbar.pack(side="right", fill="y")
        self._canvas.pack(side="left", fill="both", expand=True)

        for w in (self.window, self._canvas, self._scroll_frame):
            self._bind_scroll(w)

    def _bind_scroll(self, widget):
        widget.bind("<MouseWheel>", self._on_scroll)
        widget.bind("<Button-4>", self._on_scroll)
        widget.bind("<Button-5>", self._on_scroll)

    def _bind_scroll_exclusivo(self, widget):
        def handler(e):
            self._on_scroll(e)
            return "break"
        widget.bind("<MouseWheel>", handler)
        widget.bind("<Button-4>", handler)
        widget.bind("<Button-5>", handler)

    def _on_scroll(self, event):
        if event.num == 4:
            self._canvas.yview_scroll(-3, "units")
        elif event.num == 5:
            self._canvas.yview_scroll(3, "units")
        else:
            self._canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _filtrar(self, *_):
        termo = self._busca_var.get().strip()
        visiveis = 0
        
        if not termo:
            for frame, materia, conteudo, tw in self._cards:
                tw.tag_remove("busca", "1.0", "end")
                frame.pack(fill="x", pady=10, padx=5)
                visiveis += 1
            self._label_resultado.config(text="")
        else:
            pattern = r'\b' + re.escape(termo) + r'\b'
            
            for frame, materia, conteudo, tw in self._cards:
                tw.tag_remove("busca", "1.0", "end")
                
                match_materia = re.search(pattern, materia, re.IGNORECASE)
                match_conteudo = re.search(pattern, conteudo, re.IGNORECASE)
                
                if match_materia or match_conteudo:
                    frame.pack(fill="x", pady=10, padx=5)
                    visiveis += 1
                    self._destacar_termo(tw, pattern)
                else:
                    frame.pack_forget()
                    
            total = len(self._cards)
            self._label_resultado.config(
                text=f"{visiveis} de {total} resultado{'s' if total != 1 else ''}"
            )
            
        self._canvas.configure(scrollregion=self._canvas.bbox("all"))
        self._canvas.yview_moveto(0)

    def _destacar_termo(self, tw, pattern):
        texto = tw.get("1.0", "end")
        for match in re.finditer(pattern, texto, re.IGNORECASE):
            start = match.start()
            end = match.end()
            tw.tag_add("busca", f"1.0+{start}c", f"1.0+{end}c")

    def _mostrar_vazio(self):
        vazio = tk.Frame(self._scroll_frame, bg="#ECECEC")
        vazio.pack(expand=True, pady=150)
        tk.Label(vazio, text="📋", font=("Segoe UI", 80), bg="#ECECEC", fg="#BDBDBD").pack(pady=15)
        tk.Label(vazio, text="Nenhuma dificuldade registrada", font=("Segoe UI", 22, "bold"), bg="#ECECEC", fg="#616161").pack(pady=10)
        tk.Label(
            vazio,
            text="Use o botão '📝 Dificuldades' durante o estudo\npara registrar seus pontos de atenção",
            font=("Segoe UI", 12), bg="#ECECEC", fg="#9E9E9E", justify="center"
        ).pack(pady=5)

    def _renderizar_cards(self, difficulties):
        self._cards.clear()
        cores = ["#E91E63", "#9C27B0", "#3F51B5", "#00BCD4", "#4CAF50", "#FF9800", "#795548", "#607D8B"]
        for idx, (materia, conteudo) in enumerate(difficulties):
            card, tw = self._criar_card(self._scroll_frame, materia, conteudo, cores[idx % len(cores)])
            self._cards.append((card, materia, conteudo, tw))

    def _criar_card(self, parent, materia, conteudo, cor):
        card = tk.Frame(parent, bg="white", relief="solid", bd=1)
        card.pack(fill="x", pady=10, padx=5)

        hdr = tk.Frame(card, bg="white")
        hdr.pack(fill="x", padx=25, pady=(18, 10))

        tk.Label(hdr, text="📚", font=("Segoe UI", 22), bg="white", fg=cor).pack(side="left", padx=(0, 12), anchor="n")

        textos = tk.Frame(hdr, bg="white")
        textos.pack(side="left", fill="x", expand=True)

        lbl_titulo = tk.Label(
            textos,
            text=materia,
            font=("Segoe UI", 16, "bold"),
            fg="#212121",
            bg="white",
            anchor="w",
            justify="left",
            wraplength=600,
        )
        lbl_titulo.pack(anchor="w", fill="x")
        textos.bind(
            "<Configure>",
            lambda e, l=lbl_titulo: l.configure(wraplength=max(e.width - 10, 100))
        )

        linhas = [l for l in conteudo.split('\n') if l.strip()]
        num = len(linhas)
        tk.Label(
            textos,
            text=f"{num} ponto{'s' if num != 1 else ''} de atenção registrado{'s' if num != 1 else ''}",
            font=("Segoe UI", 10), fg="#757575", bg="white", anchor="w"
        ).pack(anchor="w")

        tk.Frame(card, bg="#E0E0E0", height=1).pack(fill="x", padx=25)

        texto_final = conteudo.strip() or "Nenhuma dificuldade registrada para esta matéria."

        text_widget = tk.Text(
            card,
            font=("Segoe UI", 11),
            bg="#F9F9F9",
            fg="#424242",
            relief="flat",
            wrap="word",
            padx=20,
            pady=15,
            cursor="xterm",
            selectbackground="#CE93D8",
            selectforeground="#212121",
            spacing1=4,
            spacing2=2,
            spacing3=4,
            borderwidth=0,
            highlightthickness=0,
            height=1,
        )
        text_widget.insert("1.0", texto_final)
        text_widget.tag_configure(
            "busca",
            background="yellow",
            foreground="black",
            font=("Segoe UI", 11, "bold"),
        )
        text_widget.bind("<Key>", self._bloquear_edicao)
        text_widget.pack(fill="x", padx=25, pady=(10, 18))

        n = max(texto_final.count('\n') + 1, 3)
        text_widget.configure(height=n)

        self._bind_scroll_exclusivo(text_widget)
        self._bind_scroll(card)
        self._bind_scroll(hdr)
        self._bind_scroll(textos)

        return card, text_widget

    def _bloquear_edicao(self, event):
        ctrl = (event.state & 0x4) != 0
        if ctrl and event.keysym.lower() in ("c", "a"):
            return None
        if event.keysym in ("Left", "Right", "Up", "Down", "Home", "End", "Prior", "Next"):
            return None
        return "break"