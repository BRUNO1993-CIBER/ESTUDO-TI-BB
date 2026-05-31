import time
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from config import ICO_PATH

class StudySourcesApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()

    
        try:
            icon = tk.PhotoImage(file=ICO_PATH)
            self.root.iconphoto(True, icon)
        except:
            pass

        self.root.title("Fontes de Estudo - TI Elite)")
        self.root.resizable(True, True)
        self.root.attributes("-zoomed", True)
        self.root.after(0, self._mostrar_centralizada)

    def _mostrar_centralizada(self):
        self.root.deiconify()
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", rowheight=30, font=('Arial', 10))
        style.configure("Treeview.Heading", font=('Arial', 11, 'bold'))

        self.resources = [
            ("JAVA - POO", "Canal Loiane Groner", "YouTube Playlist", "https://www.youtube.com/playlist?list=PLGxZ4Rq3BOBq0KXHsp5J3CJp1uF1mwY_Y"),
            ("JAVA - POO", "DevMedia - Guia Java", "Site/Artigos", "https://www.devmedia.com.br/guia/java/38"),
            ("JAVA - DOCS", "Oracle Java Documentation", "Documentação Oficial", "https://docs.oracle.com/en/java/"),
            ("JAVA - ORACLE", "Java Tutorials (Oracle)", "Tutorial Oficial", "https://docs.oracle.com/javase/tutorial/"),
            ("BANCO DE DADOS", "Boson Treinamentos - Modelagem", "YouTube Playlist", "https://www.youtube.com/playlist?list=PLucm8g_ezqNpKht2an-G1J1xcyvVq_s0X"),
            ("BANCO DE DADOS", "Curso em Vídeo - MySQL", "YouTube Playlist", "https://www.youtube.com/playlist?list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r"),
            ("BANCO DE DADOS", "W3Schools SQL", "Site Prático", "https://www.w3schools.com/sql/"),
            ("METODOLOGIA ÁGIL", "Scrum Guide 2020", "PDF Oficial", "https://scrumguides.org/download.html"),
            ("METODOLOGIA ÁGIL", "Manifesto Ágil", "Site Oficial", "https://agilemanifesto.org/iso/ptbr/manifesto.html"),
            ("METODOLOGIA ÁGIL", "Canal Andressa Chiara", "YouTube", "https://www.youtube.com/@AndressaChiara"),
            ("APIs & WEB", "Fernanda Santos - APIs REST", "YouTube", "https://www.youtube.com/@FernandaKipper"),
            ("APIs & WEB", "Michelli Brito - Spring Boot", "YouTube", "https://www.youtube.com/@MichelliBrito"),
            ("APIs & WEB", "MDN Web Docs (HTTP/Status)", "Documentação", "https://developer.mozilla.org/pt-BR/docs/Web/HTTP"),
            ("INFRA & GIT", "Curso em Vídeo - Git e GitHub", "YouTube Playlist", "https://www.youtube.com/playlist?list=PLHz_AreHm4dm7ZULPAmadvNhH6vk9oNZA"),
            ("INFRA & DOCKER", "Fabrizio Veronez", "YouTube", "https://www.youtube.com/@FabrizioVeronez"),
            ("QUESTÕES", "QConcursos", "Banco de Questões", "https://www.qconcursos.com"),
            ("QUESTÕES", "Tec Concursos", "Banco de Questões", "https://www.tecconcursos.com.br"),
            ("PORTUGUÊS", "Professor Noslen", "YouTube", "https://www.youtube.com/@ProfessorNoslen"),
            ("PORTUGUÊS", "Português com Letícia", "YouTube", "https://www.youtube.com/@PortuguescomLeticia"),
            ("GERAL TI", "Dicionário do Programador (Código Fonte TV)", "YouTube", "https://www.youtube.com/playlist?list=PLcdfP_l_A5w3uB30gB_a6rCg4k3F7X_9C")
        ]

        self._setup_ui()

    def _center_window(self, window, width, height):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def _setup_ui(self):
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("categoria", "nome", "tipo", "link")
        self.tree = ttk.Treeview(main_frame, columns=columns, show="headings", selectmode="browse")

        self.tree.heading("categoria", text="Matéria / Tópico")
        self.tree.heading("nome", text="Nome da Fonte")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("link", text="Link (URL)")

        self.tree.column("categoria", width=150, anchor="center")
        self.tree.column("nome", width=250)
        self.tree.column("tipo", width=120, anchor="center")
        self.tree.column("link", width=400)

        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        for item in self.resources:
            self.tree.insert("", "end", values=item)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        btn_frame = tk.Frame(self.root, bg="#e0e0e0", height=60)
        btn_frame.pack(fill="x", side="bottom")

        btn_copy = tk.Button(btn_frame, text="Copiar Link", command=self.copy_link, 
                             bg="#2196F3", fg="white", font=("Arial", 12, "bold"), width=15, height=2)
        btn_copy.pack(side="right", padx=20, pady=10)

        btn_open = tk.Button(btn_frame, text="Abrir no Navegador", command=self.open_link, 
                             bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=20, height=2)
        btn_open.pack(side="right", padx=5, pady=10)

        lbl_instrucao = tk.Label(btn_frame, text="Selecione uma linha para interagir", bg="#e0e0e0", font=("Arial", 10, "italic"))
        lbl_instrucao.pack(side="left", padx=20)

    def copy_link(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione uma fonte na lista.")
            return
        
        item = self.tree.item(selected_item)
        link = item['values'][3]
        
        self.root.clipboard_clear()
        self.root.clipboard_append(link)
        messagebox.showinfo("Sucesso", "Link copiado para a área de transferência!")

    def open_link(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aviso", "Selecione uma fonte na lista.")
            return
        
        item = self.tree.item(selected_item)
        link = item['values'][3]
        webbrowser.open(link)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudySourcesApp(root)
    root.mainloop()