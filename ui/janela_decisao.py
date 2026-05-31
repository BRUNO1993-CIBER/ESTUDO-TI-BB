import tkinter as tk
from tkinter import font as tkfont
from config import ICO_PATH

class JanelaDecisao:
    def __init__(self, parent, subject_name, callback_next, callback_continue):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Meta Atingida!")
        self.callback_next = callback_next
        self.callback_continue = callback_continue
        
        self.dialog.withdraw()
        
    
        try:
            icon = tk.PhotoImage(file=ICO_PATH)
            self.dialog.iconphoto(True, icon)
        except:
            pass
            
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        
        self._build_ui(subject_name)
        
        self.dialog.update_idletasks()
        self._center_window()
        
        self.dialog.deiconify()
        self.dialog.grab_set()
        self.dialog.focus_force()
        
    def _center_window(self):
        width = self.dialog.winfo_reqwidth()
        height = self.dialog.winfo_reqheight()
        screen_width = self.dialog.winfo_screenwidth()
        screen_height = self.dialog.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.dialog.geometry(f'{width}x{height}+{x}+{y}')
        
    def _build_ui(self, subject_name):
        main_frame = tk.Frame(self.dialog, bg='white', padx=30, pady=25)
        main_frame.pack(fill='both', expand=True)
        
        try:
            title_font = tkfont.Font(family='Arial', size=16, weight='bold')
        except:
            title_font = tkfont.Font(family='TkDefaultFont', size=16, weight='bold')
            
        title_label = tk.Label(
            main_frame,
            text="🎉 Meta de 4 Ciclos Atingida!",
            font=title_font,
            fg="#2E7D32",
            bg='white',
            wraplength=400
        )
        title_label.pack(pady=(0, 15))
        
        try:
            subject_font = tkfont.Font(family='Arial', size=11)
        except:
            subject_font = tkfont.Font(family='TkDefaultFont', size=11)
            
        subject_label = tk.Label(
            main_frame,
            text=f"Matéria: {subject_name}",
            font=subject_font,
            fg="#424242",
            bg='white',
            wraplength=400
        )
        subject_label.pack(pady=(0, 10))
        
        try:
            message_font = tkfont.Font(family='Arial', size=10)
        except:
            message_font = tkfont.Font(family='TkDefaultFont', size=10)
            
        message_label = tk.Label(
            main_frame,
            text="O que você deseja fazer?",
            font=message_font,
            fg="#616161",
            bg='white',
            wraplength=400
        )
        message_label.pack(pady=(0, 25))
        
        btn_frame = tk.Frame(main_frame, bg='white')
        btn_frame.pack()
        
        try:
            btn_font = tkfont.Font(family='Arial', size=10, weight='bold')
        except:
            btn_font = tkfont.Font(family='TkDefaultFont', size=10, weight='bold')
        
        btn_next = tk.Button(
            btn_frame,
            text="Encerrar e Próxima",
            command=self._on_next,
            bg="#D32F2F",
            fg="white",
            font=btn_font,
            cursor="hand2",
            relief='flat',
            padx=20,
            pady=10,
            activebackground="#B71C1C",
            activeforeground="white",
            borderwidth=0,
            highlightthickness=0
        )
        btn_next.pack(side='left', padx=8)
        
        btn_continue = tk.Button(
            btn_frame,
            text="Continuar Estudando",
            command=self._on_continue,
            bg="#1976D2",
            fg="white",
            font=btn_font,
            cursor="hand2",
            relief='flat',
            padx=20,
            pady=10,
            activebackground="#1565C0",
            activeforeground="white",
            borderwidth=0,
            highlightthickness=0
        )
        btn_continue.pack(side='left', padx=8)
        
        self.dialog.bind('<Escape>', lambda e: self.dialog.destroy())
        self.dialog.protocol("WM_DELETE_WINDOW", self.dialog.destroy)
        
    def _on_next(self):
        self.dialog.destroy()
        self.callback_next()
        
    def _on_continue(self):
        self.dialog.destroy()
        self.callback_continue()