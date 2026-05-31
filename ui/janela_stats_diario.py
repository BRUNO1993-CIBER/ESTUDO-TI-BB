import tkinter as tk
from tkinter import ttk
from datetime import datetime
from config import ICO_PATH

class JanelaStatsDiario:
    """Janela que mostra estatísticas de estudo por dia"""
    
    def __init__(self, parent, daily_data, format_duration_func):
        """
        Args:
            parent: Janela principal
            daily_data: Lista de tuplas com dados diários do banco
            format_duration_func: Função para formatar duração em segundos
        """
        self.format_duration = format_duration_func
        
        self.window = tk.Toplevel(parent)
        self.window.title("📊 Estudos por Dia")
        self.window.withdraw()

        try:
            icon = tk.PhotoImage(file=ICO_PATH)
            self.window.iconphoto(True, icon)
        except:
            pass

        self._setup_window()
        self._build_ui(daily_data)
        
        self.window.deiconify()
    
    def _setup_window(self):
        self.window.resizable(True, True)
        self.window.attributes("-zoomed", True)
    
    def _build_ui(self, daily_data):
        """Constrói a interface completa"""
        self._build_summary(daily_data)
        self._build_table(daily_data)
    
    def _build_summary(self, daily_data):
        """Constrói o painel de resumo geral"""
        summary_frame = tk.Frame(self.window, bg="#E3F2FD", pady=15)
        summary_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            summary_frame, 
            text="📈 RESUMO GERAL", 
            font=("Arial", 14, "bold"), 
            bg="#E3F2FD", 
            fg="#1565C0"
        ).pack()
        
        # Calcular estatísticas
        total_days = len(daily_data)
        total_cycles = sum(row[2] for row in daily_data)
        total_time = sum(row[3] for row in daily_data)
        total_questions = sum(row[4] for row in daily_data if row[4])
        total_correct = sum(row[5] for row in daily_data if row[5])
        
        avg_time_per_day = total_time / total_days if total_days > 0 else 0
        accuracy = (total_correct / total_questions * 100) if total_questions > 0 else 0
        
        # Frame com as informações
        info_frame = tk.Frame(summary_frame, bg="#E3F2FD")
        info_frame.pack(pady=10)
        
        stats_info = [
            ("📅 Dias de Estudo:", f"{total_days}"),
            ("⏱️ Tempo Total:", f"{self.format_duration(total_time)}"),
            ("🔄 Total de Ciclos:", f"{total_cycles}"),
            ("📝 Questões Feitas:", f"{total_questions}"),
            ("✅ Taxa de Acerto:", f"{accuracy:.1f}%"),
            ("⌛ Média/Dia:", f"{self.format_duration(int(avg_time_per_day))}")
        ]
        
        for i, (label, value) in enumerate(stats_info):
            row = i // 3
            col = i % 3
            frame = tk.Frame(info_frame, bg="#E3F2FD")
            frame.grid(row=row, column=col, padx=15, pady=2)
            
            tk.Label(
                frame, 
                text=label, 
                font=("Arial", 9, "bold"), 
                bg="#E3F2FD", 
                fg="#424242"
            ).pack(side="left")
            
            tk.Label(
                frame, 
                text=value, 
                font=("Arial", 9), 
                bg="#E3F2FD", 
                fg="#1565C0"
            ).pack(side="left", padx=5)
    
    def _build_table(self, daily_data):
        """Constrói a tabela com dados por dia"""
        cols = ("Data", "Matérias", "Ciclos", "Tempo", "Questões", "Acertos", "% Acerto")
        tree = ttk.Treeview(self.window, columns=cols, show='headings', height=15)
        
        # Configurar cabeçalhos
        tree.heading("Data", text="📅 Data")
        tree.heading("Matérias", text="📚 Matérias")
        tree.heading("Ciclos", text="🔄 Ciclos")
        tree.heading("Tempo", text="⏱️ Tempo")
        tree.heading("Questões", text="📝 Questões")
        tree.heading("Acertos", text="✅ Acertos")
        tree.heading("% Acerto", text="📊 % Acerto")
        
        # Configurar largura das colunas
        tree.column("Data", width=100, anchor="center")
        tree.column("Matérias", width=80, anchor="center")
        tree.column("Ciclos", width=80, anchor="center")
        tree.column("Tempo", width=100, anchor="center")
        tree.column("Questões", width=80, anchor="center")
        tree.column("Acertos", width=80, anchor="center")
        tree.column("% Acerto", width=100, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        tree.pack(expand=True, fill="both", padx=10, pady=(0, 10))
        
        # Preencher dados
        for row in daily_data:
            study_date = row[0]
            sessions = row[1]
            cycles = row[2]
            seconds = row[3]
            questions = row[4] if row[4] else 0
            correct = row[5] if row[5] else 0
            
            perc = f"{(correct/questions)*100:.1f}%" if questions > 0 else "-"
            
            try:
                date_obj = datetime.fromisoformat(study_date)
                formatted_date = date_obj.strftime("%d/%m/%Y")
            except:
                formatted_date = study_date
            
            tree.insert("", "end", values=(
                formatted_date,
                sessions,
                cycles,
                self.format_duration(seconds),
                questions,
                correct,
                perc
            ))