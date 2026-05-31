import tkinter as tk
from tkinter import ttk
from config import ICO_PATH

class JanelaStatsDetalhado:
    def __init__(self, parent, records, format_duration_func):
        self.format_duration = format_duration_func
        self.window = tk.Toplevel(parent)
        self.window.title("📊 Histórico Detalhado de Estudos")
        self.window.withdraw()

    
        try:
            icon = tk.PhotoImage(file=ICO_PATH)
            self.window.iconphoto(True, icon)
        except:
            pass
            
        self._setup_window()
        self._build_table(records)
        self.window.deiconify()
    
    def _setup_window(self):
        self.window.resizable(True, True)
        self.window.attributes("-zoomed", True)
        self.window.configure(bg="#f5f5f5")
    
    def _wrap_text(self, text, max_chars=60):
        """Quebra o texto em múltiplas linhas"""
        if len(text) <= max_chars:
            return text
        
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word)
            if current_length + word_length + len(current_line) <= max_chars:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
                current_length = word_length
        
        if current_line:
            lines.append(" ".join(current_line))
        
        return "\n".join(lines)
    
    def _build_table(self, records):
        """Constrói a tabela com histórico detalhado usando Text widget"""
        
        # Título
        title_frame = tk.Frame(self.window, bg="#2c3e50", height=50)
        title_frame.pack(fill="x", padx=0, pady=0)
        title_frame.pack_propagate(False)
        
        # Subtítulo com total de matérias
        subtitle_frame = tk.Frame(self.window, bg="#ecf0f1", height=35)
        subtitle_frame.pack(fill="x", padx=0, pady=0)
        subtitle_frame.pack_propagate(False)
        
        total_materias = len(records)
        subtitle_label = tk.Label(subtitle_frame, 
                                 text=f"Total: {total_materias} matéria{'s' if total_materias != 1 else ''}", 
                                 font=("Segoe UI", 10), 
                                 bg="#ecf0f1", fg="#555")
        subtitle_label.pack(pady=7, padx=15, anchor="w")
        
        # Frame principal com scrollbar
        frame_container = tk.Frame(self.window, bg="white")
        frame_container.pack(expand=True, fill="both", padx=15, pady=15)
        
        # Text widget com scrollbars
        text_widget = tk.Text(frame_container, wrap="none", 
                             font=("Consolas", 10), 
                             bg="white",
                             cursor="arrow",
                             spacing1=3,
                             spacing3=3,
                             relief="flat",
                             borderwidth=0,
                             padx=10,
                             pady=10)
        
        scrollbar_y = ttk.Scrollbar(frame_container, orient="vertical", command=text_widget.yview)
        scrollbar_x = ttk.Scrollbar(frame_container, orient="horizontal", command=text_widget.xview)
        
        text_widget.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        text_widget.pack(side="left", fill="both", expand=True)
        
        # Configurar tags para formatação
        text_widget.tag_configure("header", font=("Consolas", 10, "bold"), 
                                 background="#3498db", foreground="white")
        text_widget.tag_configure("line", font=("Consolas", 10), foreground="#2c3e50")
        text_widget.tag_configure("line_alt", font=("Consolas", 10), 
                                 background="#f8f9fa", foreground="#2c3e50")
        text_widget.tag_configure("separator", foreground="#bdc3c7")
        
        # Cabeçalho com nomes completos e separadores verticais
        header = f"  {'Matéria':<62} │ {'Sessões':^8} │ {'Ciclos':^7} │ {'Tempo Total':^12} │ {'Questões':^9} │ {'Acertos':^8} │ {'% Acerto':^9}  \n"
        separator = "  " + "─" * 62 + "─┼─" + "─" * 8 + "─┼─" + "─" * 7 + "─┼─" + "─" * 12 + "─┼─" + "─" * 9 + "─┼─" + "─" * 8 + "─┼─" + "─" * 9 + "  \n"
        
        text_widget.insert("1.0", "\n", "line")
        text_widget.insert("end", header, "header")
        text_widget.insert("end", separator, "separator")
        
        # Dados com linhas alternadas
        for idx, row in enumerate(records):
            materia_original = row[0]
            materia_lines = self._wrap_text(materia_original, 60).split("\n")
            
            sessoes = row[1]
            ciclos = row[2]
            tempo_total = self.format_duration(row[3])
            q_done = row[4] if row[4] else 0
            q_correct = row[5] if row[5] else 0
            perc = f"{row[6]:.0f}%" if row[6] > 0 else "-"
            
            # Alternar cor de fundo
            tag = "line_alt" if idx % 2 == 0 else "line"
            
            # Primeira linha com todos os dados centralizados
            first_line = f"  {materia_lines[0]:<62} │ {sessoes:^8} │ {ciclos:^7} │ {tempo_total:^12} │ {q_done:^9} │ {q_correct:^8} │ {perc:^9}  \n"
            text_widget.insert("end", first_line, tag)
            
            # Linhas adicionais da matéria (se houver)
            for additional_line in materia_lines[1:]:
                continuation = f"  {additional_line:<62} │ {' ':^8} │ {' ':^7} │ {' ':^12} │ {' ':^9} │ {' ':^8} │ {' ':^9}  \n"
                text_widget.insert("end", continuation, tag)
            
            # Linha separadora entre matérias
            text_widget.insert("end", separator, "separator")
        
        text_widget.insert("end", "\n")
        
        # Tornar somente leitura
        text_widget.configure(state="disabled")