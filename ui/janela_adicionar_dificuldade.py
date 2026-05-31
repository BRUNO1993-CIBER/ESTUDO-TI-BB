import tkinter as tk
from tkinter import messagebox
from config import ICO_PATH

class JanelaAdicionarDificuldade:
    """Janela para registrar dificuldades durante o estudo"""
    
    def __init__(self, parent, subject_name, callback_save):
        """
        Args:
            parent: Janela principal
            subject_name: Nome da matéria atual
            callback_save: Função a ser chamada ao salvar (recebe o texto da dificuldade)
        """
        self.callback_save = callback_save
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Registrar Dificuldade")
        self.dialog.withdraw()

    
        try:
            icon = tk.PhotoImage(file=ICO_PATH)
            self.dialog.iconphoto(True, icon)
        except:
            pass

        self.dialog.resizable(True, True)
        self.dialog.attributes("-zoomed", True)
        self.dialog.transient(parent)
        self.dialog.grab_set()

        self._build_ui(subject_name)
        self.dialog.deiconify()
    
    def _build_ui(self, subject_name):
        """Constrói a interface da janela"""
        tk.Label(
            self.dialog, 
            text=f"📚 {subject_name}", 
            font=("Arial", 11, "bold"), 
            fg="#E91E63"
        ).pack(pady=10)
        
        tk.Label(
            self.dialog, 
            text="O que você teve dificuldade neste bloco de estudo?", 
            font=("Arial", 10)
        ).pack(pady=5)
        
        # Frame do texto com scrollbar
        text_frame = tk.Frame(self.dialog)
        text_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        self.txt = tk.Text(text_frame, font=("Arial", 10), wrap="word", height=8)
        self.txt.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(text_frame, command=self.txt.yview)
        scrollbar.pack(side="right", fill="y")
        self.txt.config(yscrollcommand=scrollbar.set)
        
        # Placeholder
        placeholder = "Ex: Tive dificuldade em entender recursividade..."
        self.txt.insert("1.0", placeholder)
        self.txt.bind("<FocusIn>", lambda e: self._clear_placeholder(placeholder))
        
        # Frame dos botões
        btn_frame = tk.Frame(self.dialog)
        btn_frame.pack(pady=15)
        
        tk.Button(
            btn_frame, 
            text="💾 Salvar", 
            command=self._save_and_close, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 10, "bold"), 
            width=12,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        tk.Button(
            btn_frame, 
            text="Cancelar", 
            command=self.dialog.destroy, 
            bg="#9E9E9E", 
            fg="white", 
            font=("Arial", 10), 
            width=12,
            cursor="hand2"
        ).pack(side="left", padx=5)
    
    def _clear_placeholder(self, placeholder):
        """Remove o placeholder quando o usuário clica no campo"""
        if placeholder in self.txt.get("1.0", tk.END):
            self.txt.delete("1.0", tk.END)
    
    def _save_and_close(self):
        """Salva a dificuldade e fecha a janela"""
        difficulty = self.txt.get("1.0", tk.END).strip()
        
        if difficulty and "Ex:" not in difficulty:
            self.callback_save(difficulty)
            messagebox.showinfo("Salvo", "Dificuldade registrada com sucesso!")
            self.dialog.destroy()
        else:
            messagebox.showwarning("Atenção", "Digite uma dificuldade válida.")