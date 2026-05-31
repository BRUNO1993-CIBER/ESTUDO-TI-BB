import tkinter as tk
from prompts.prompt_aula import PROMPT_AULA
from prompts.prompt_questoes import PROMPT_QUESTOES
from config import ICO_PATH

def abrir():
    janela = tk.Tk()
    janela.title("Gerador de Prompt")

    try:
        icon = tk.PhotoImage(file=ICO_PATH)
        janela.iconphoto(True, icon)
    except:
        pass

    janela.withdraw()
    janela.resizable(True, True)
    janela.attributes("-zoomed", True)

    bg_color  = "#F4F7FA"
    bb_blue   = "#003DA5"
    marrom    = "#5C3317"

    janela.configure(bg=bg_color)

    # ── Cabeçalho ──────────────────────────────────────────────────────────
    frame_header = tk.Frame(janela, bg=bg_color, padx=20, pady=12)
    frame_header.pack(fill="x")

    tk.Label(
        frame_header,
        text="MENTOR IA  (TI)",
        font=("Arial", 14, "bold"),
        bg=bg_color, fg=bb_blue
    ).pack()

    tk.Label(
        frame_header,
        text="Copie o prompt do painel desejado, cole no ChatGPT ou Claude e digite o tópico no final.",
        font=("Arial", 10),
        bg=bg_color, fg="#555"
    ).pack()

    # ── Dois painéis lado a lado ────────────────────────────────────────────
    frame_paineis = tk.Frame(janela, bg=bg_color, padx=20, pady=0)
    frame_paineis.pack(expand=True, fill="both")
    frame_paineis.columnconfigure(0, weight=1)
    frame_paineis.columnconfigure(1, weight=1)
    frame_paineis.rowconfigure(1, weight=1)

    def criar_painel(parent, col, titulo, conteudo, cor_btn, texto_btn, lado):
        # Título do painel
        tk.Label(
            parent,
            text=titulo,
            font=("Arial", 11, "bold"),
            bg=cor_btn, fg="white",
            pady=6
        ).grid(row=0, column=col, sticky="ew",
               padx=(0, 8) if lado == "esq" else (8, 0),
               pady=(0, 4))

        # Área de texto + scrollbar
        frame_txt = tk.Frame(parent, bg=bg_color)
        frame_txt.grid(row=1, column=col, sticky="nsew",
                       padx=(0, 8) if lado == "esq" else (8, 0))

        sb = tk.Scrollbar(frame_txt)
        sb.pack(side="right", fill="y")

        txt = tk.Text(
            frame_txt,
            font=("Consolas", 10),
            yscrollcommand=sb.set,
            bg="white", fg="#333",
            padx=10, pady=10,
            wrap="word",
            bd=1, relief="solid"
        )
        txt.pack(side="left", expand=True, fill="both")
        sb.config(command=txt.yview)
        txt.insert("1.0", conteudo)

        # Botão copiar
        btn = tk.Button(
            parent,
            text=texto_btn,
            font=("Arial", 11, "bold"),
            bg=cor_btn, fg="white",
            height=2, cursor="hand2", relief="flat"
        )
        btn.grid(row=2, column=col, sticky="ew",
                 padx=(0, 8) if lado == "esq" else (8, 0),
                 pady=(8, 0))

        def copiar():
            janela.clipboard_clear()
            janela.clipboard_append(conteudo)
            janela.update()
            btn.config(text=" COPIADO!", bg="#4CAF50")
            janela.after(2000, lambda: btn.config(text=texto_btn, bg=cor_btn))

        btn.config(command=copiar)

    frame_paineis.rowconfigure(2, weight=0)

    criar_painel(frame_paineis, col=0,
                 titulo="PROMPT 1 — AULA",
                 conteudo=PROMPT_AULA,
                 cor_btn=bb_blue,
                 texto_btn="COPIAR PROMPT 1 — AULA",
                 lado="esq")

    criar_painel(frame_paineis, col=1,
                 titulo="PROMPT 2 — QUESTÕES",
                 conteudo=PROMPT_QUESTOES,
                 cor_btn=marrom,
                 texto_btn="COPIAR PROMPT 2 — QUESTÕES",
                 lado="dir")

    # espaço inferior
    tk.Frame(janela, bg=bg_color, height=12).pack()

    janela.deiconify()
    janela.mainloop()

if __name__ == "__main__":
    abrir()
