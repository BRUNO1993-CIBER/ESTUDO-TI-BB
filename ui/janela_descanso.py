import tkinter as tk
from tkinter import messagebox

DESCANSO = """

PROTOCOLO DE DESCOMPRESSÃO — ENGENHEIRO DE SOFTWARE EM FORMAÇÃO


1. DESCONEXÃO ATIVA (Pausa de Verdade)

Você acabou de processar conceitos densos. O cérebro precisa consolidar o que aprendeu — e faz isso no descanso, não no estudo.

A Missão: 10 minutos longe da tela e do material. Sem revisar, sem celular, sem culpa.

Ação:

Levante da cadeira e mude de ambiente (outro cômodo, corredor, área externa).

Não pense no conteúdo — se vier um pensamento de estudo, apenas observe e deixe passar.

Tome água. Hidratação afeta diretamente a concentração e a memória.

Esse intervalo não é perda de tempo: é onde a memória de longo prazo se forma.


2. DESCANSO OCULAR (Regra 20-20-20)

Você ficou 1 hora olhando para uma tela a 40cm do rosto. Seus músculos oculares estão em espasmo.

A Missão: Relaxar o cristalino e prevenir dor de cabeça no fim do dia.

Ação:

Vá até uma janela ou área aberta.

Foque em um ponto distante (árvore, prédio, horizonte) por 20 segundos.

Deixe a visão "aberta", sem fixar em nada específico.

Pisque conscientemente algumas vezes.

Simples e eficaz — engenheiro cuida do equipamento de trabalho.


3. MANUTENÇÃO DO CORPO (Calistenia Leve)

Ficar sentado por horas trava a circulação e gera sonolência. Seu cérebro recebe menos oxigênio.

A Missão: Bombear sangue para o cérebro sem gastar energia.

Ação:

Alongamento de Psoas: dê um passo à frente e desça o quadril. Essencial para quem fica sentado.

20 Agachamentos livres: rápido, só para acelerar levemente o coração.

Rotação de ombros e pescoço: tire a tensão do trapézio, onde o estresse físico acumula.

Bônus: abra a janela e respire ar fresco por 2 minutos.


4. TAREFA MECÂNICA (Terapia do Zero Pensamento)

Tarefas físicas simples liberam dopamina pela recompensa imediata, sem custo cognitivo.

A Missão: Resultado visível, mente em modo passivo.

Ação:

Lavar a xícara de café que usou.

Encher a garrafa de água.

Organizar a mesa de estudos para o próximo ciclo.

O Segredo: Preste atenção na água caindo, no barulho dos objetos. Isso é Mindfulness disfarçado de organização — e funciona.


5. RESPIRAÇÃO BOX (Reset do Sistema Nervoso)

Técnica usada por atletas de elite e engenheiros em situações de alta pressão para controlar o estresse.

A Missão: Resetar o Sistema Nervoso Autônomo antes do próximo bloco.

Ação (4-4-4-4):

Inspire pelo nariz contando até 4.

Segure o ar contando até 4.

Solte pela boca contando até 4.

Fique com o pulmão vazio contando até 4.

Repita 3 ou 4 vezes. Elimina a ansiedade de "não estou aprendendo" e prepara o foco para o próximo ciclo.


LEMBRE-SE: O domínio de Engenharia de Software é construído ciclo a ciclo. Você está no caminho certo.

"""

def abrir():

    janela = tk.Tk()    
    janela.title("🕊️")
    janela.withdraw()
    janela.resizable(True, True)
    janela.attributes("-zoomed", True)

    bg_color = "#F4F7FA"
    bb_blue = "#003DA5"
    bb_yellow = "#F9DD16"
    
    frame_main = tk.Frame(janela, padx=20, pady=20, bg=bg_color)
    frame_main.pack(expand=True, fill="both")
    janela.configure(bg=bg_color)

    lbl_header = tk.Label(
        frame_main, 
        text="DESCOMPRESSÃO - PROTOCOLO DE DESCANSO",
        font=("Arial", 14, "bold"),
        bg=bg_color,
        fg=bb_blue
    )
    lbl_header.pack(pady=(0, 5))

    frame_texto = tk.Frame(frame_main)
    frame_texto.pack(expand=True, fill="both")

    scrollbar = tk.Scrollbar(frame_texto)
    scrollbar.pack(side="right", fill="y")

    txt_prompt = tk.Text(
        frame_texto, 
        height=10, 
        font=("Arial", 12),
        yscrollcommand=scrollbar.set,
        bg="white",
        fg="#333",
        padx=10,
        pady=10,
        wrap="word",
        bd=1,
        relief="solid"
    )
    txt_prompt.pack(side="left", expand=True, fill="both")
    scrollbar.config(command=txt_prompt.yview)

    txt_prompt.insert("1.0", DESCANSO)

    janela.deiconify()
    janela.mainloop()

if __name__ == "__main__":
    abrir()