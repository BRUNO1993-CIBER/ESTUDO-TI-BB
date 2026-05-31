import tkinter as tk

ORACAO = """
Senhor Deus,
fonte de toda sabedoria e verdade,

coloco diante de Ti este propósito concreto da minha vida:
a preparação e o avanço contínuo no estudo de Engenharia de Software.

Ilumina minha mente para compreender com profundidade os fundamentos técnicos,
a lógica, os algoritmos, os sistemas e cada conceito exigido nesse caminho.

Dá-me clareza de raciocínio, concentração constante e disciplina nos estudos diários.

Concede-me perseverança para enfrentar o cansaço,
humildade para reconhecer minhas limitações
e sabedoria para aprender com cada erro.

Fortalece meu ânimo diante dos desafios
e guia meu esforço para que eu estude com método, constância e honestidade.

Que meu preparo seja sólido,
meu conhecimento verdadeiro
e minha confiança fruto do trabalho bem feito.

Se for da Tua vontade, abre esse caminho profissional,
para que eu possa exercer minha vocação com responsabilidade,
servindo com competência, ética e dedicação.

Em Tuas mãos coloco este objetivo.

Amém.
"""

def abrir():
    janela = tk.Tk()
    janela.title("✠ Ordem e Disciplina ✠")
    janela.attributes("-zoomed", True)

    # 🎨 Paleta medieval
    bg_escuro = "#1b1b1b"
    pergaminho = "#f5e6c8"
    vinho = "#5a0f1c"
    dourado = "#c9a44c"

    janela.configure(bg=bg_escuro)

    # 📜 Container central
    frame = tk.Frame(
        janela,
        bg=pergaminho,
        bd=3,
        relief="ridge"
    )
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # 🏰 Título
    titulo = tk.Label(
        frame,
        text="✠ ORAÇÃO DE DISCIPLINA E ESTUDO ✠",
        font=("Times New Roman", 18, "bold"),
        bg=pergaminho,
        fg=vinho
    )
    titulo.pack(pady=(20, 10))

    # 📖 Texto
    texto = tk.Text(
        frame,
        width=100,
        height=30,
        font=("Times New Roman", 14),
        bg=pergaminho,
        fg="#2b2b2b",
        wrap="word",
        bd=0,
        highlightthickness=0
    )
    texto.pack(padx=40, pady=20)

    # Centralização horizontal real
    texto.tag_configure("center", justify="center")
    texto.insert("1.0", ORACAO, "center")

    # 🔒 Travar edição (fica só leitura)
    texto.config(state="disabled")

    janela.mainloop()


if __name__ == "__main__":
    abrir()