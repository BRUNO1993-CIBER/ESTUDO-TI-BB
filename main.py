#!/usr/bin/env python3
import sys
import threading
import os
from datetime import date
import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

from config import ICO_PATH

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

from ui import janela_oracao, janela_descanso, janela_prompt
from ui.fontes_estudo                import StudySourcesApp
from ui.janela_dificuldades          import JanelaDificuldades
from ui.janela_decisao               import JanelaDecisao
from ui.janela_adicionar_dificuldade import JanelaAdicionarDificuldade
from ui.janela_stats_diario          import JanelaStatsDiario
from ui.janela_stats_detalhado       import JanelaStatsDetalhado
from core.backend                    import StudyRepository, DB_NAME

# ── Paleta de cores ────────────────────────────────────────────────────────────
ENGENHARIA_GREEN      = "#00A859"
ENGENHARIA_DARK_GREEN = "#007A3D"
ENGENHARIA_YELLOW     = "#FDB813"
ENGENHARIA_BLUE       = "#003A70"
ENGENHARIA_LIGHT_BLUE = "#0066CC"
ENGENHARIA_GRAY       = "#4A4A4A"
ENGENHARIA_LIGHT_GRAY = "#E8E8E8"
BACKGROUND_MAIN       = "#F5F5F5"
REVIEW_COLOR          = "#FFF3CD"
SIMULADO_COLOR        = "#FFE5E5"
REDACAO_COLOR         = "#F3E5F5"
CODING_COLOR          = "#E0F2F1"


# ── Controller ─────────────────────────────────────────────────────────────────
class StudyController:
    def __init__(self):
        self.repo = StudyRepository(DB_NAME)
        self.repo.ensure_daily_plan_exists()
        self.current_subject_data = None
        self.ordem_blocos = [
            "Banco de Dados", "Engenharia de Software", "Requisitos",
            "Arquitetura", "Linguagens", "Qualidade e Estruturas",
            "Segurança", "Cloud Computing", "Produtividade e Dados",
            "Infraestrutura", "Governança",
        ]

    def load_active_subject(self):
        self.current_subject_data = self.repo.get_current_subject()
        return self.current_subject_data

    def complete_pomodoro(self, duration_seconds, q_done=0, q_correct=0):
        if not self.current_subject_data:
            return
        self.repo.record_cycle(self.current_subject_data['id'], duration_seconds, q_done, q_correct)
        self.load_active_subject()

    def finish_subject_and_advance(self):
        if self.current_subject_data:
            self.repo.mark_as_finished(self.current_subject_data['id'])
            self.load_active_subject()

    def continue_same_subject(self):
        self.load_active_subject()

    def get_report_data(self):
        return self.repo.get_all_stats()

    def get_daily_summary(self):
        return self.repo.get_daily_summary()

    def save_difficulty(self, difficulty_text):
        if self.current_subject_data:
            self.repo.save_difficulty(self.current_subject_data['id'], difficulty_text)

    def get_all_difficulties(self):
        return self.repo.get_difficulties_by_subject()


# ── App principal ──────────────────────────────────────────────────────────────
class StudyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ENGENHARIA - Engenharia de Software | Sistema de Estudos")
        self.root.configure(bg=BACKGROUND_MAIN)

        try:
            self._icon = tk.PhotoImage(file=ICO_PATH)
            self.root.iconphoto(True, self._icon)
        except Exception as e:
            print("Erro ao carregar ícone:", e)

        self.root.withdraw()
        self.root.attributes("-zoomed", True)
        self.root.after(0, lambda: None)
        self.root.deiconify()

        self.controller    = StudyController()
        self.timer_running = False
        self.time_elapsed  = 0
        self.timer_id      = None

        self._setup_ui()
        self._refresh_view()

    # ── Utilitários ────────────────────────────────────────────────────────
    def _format_time_elapsed(self, seconds):
        h, r = divmod(seconds, 3600)
        m, s = divmod(r, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

    def _format_duration(self, total_seconds):
        h, r = divmod(total_seconds, 3600)
        m, _  = divmod(r, 60)
        return f"{h}h {m}m" if h > 0 else f"{m} min"

    # ── Interface ──────────────────────────────────────────────────────────
    def _setup_ui(self):
        # Cabeçalho
        header = tk.Frame(self.root, bg=ENGENHARIA_BLUE, height=60)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        tk.Label(header, text="ENGENHARIA",
                 font=("Arial", 18, "bold"), bg=ENGENHARIA_BLUE, fg="white").pack(pady=(8, 0))
        tk.Label(header, text="ENGENHARIA DE SOFTWARE • SISTEMA DE ESTUDOS",
                 font=("Arial", 8), bg=ENGENHARIA_BLUE, fg=ENGENHARIA_YELLOW).pack()

        self.main_frame = tk.Frame(self.root, padx=25, pady=15, bg=BACKGROUND_MAIN)
        self.main_frame.pack(expand=True, fill="both")

        # Data e bloco
        info_frame = tk.Frame(self.main_frame, bg=BACKGROUND_MAIN)
        info_frame.pack(fill="x", pady=(0, 8))

        self.lbl_date = tk.Label(info_frame, text=f"📅 {date.today().strftime('%d/%m/%Y')}",
                                 font=("Arial", 9, "bold"), bg=BACKGROUND_MAIN, fg=ENGENHARIA_GRAY)
        self.lbl_date.pack(side="left")

        # Barra de progresso
        tk.Label(self.main_frame, text="PROGRESSO DO CICLO COMPLETO",
                 font=("Arial", 8, "bold"), bg=BACKGROUND_MAIN, fg=ENGENHARIA_GRAY).pack(anchor="w")

        progress_container = tk.Frame(self.main_frame, bg=BACKGROUND_MAIN)
        progress_container.pack(fill="x", pady=(3, 10))

        self.progress_var = tk.DoubleVar()
        style = ttk.Style()
        style.theme_use('default')
        style.configure("ENGENHARIA.Horizontal.TProgressbar",
                        troughcolor=ENGENHARIA_LIGHT_GRAY, background=ENGENHARIA_GREEN,
                        darkcolor=ENGENHARIA_DARK_GREEN, lightcolor=ENGENHARIA_GREEN,
                        bordercolor=ENGENHARIA_GRAY, thickness=18)

        ttk.Progressbar(progress_container, variable=self.progress_var, maximum=100,
                        style="ENGENHARIA.Horizontal.TProgressbar",
                        length=650).pack(side="left", fill="x", expand=True)

        self.progress_percent_label = tk.Label(progress_container, text="0%",
                                               font=("Arial", 9, "bold"), bg=BACKGROUND_MAIN,
                                               fg=ENGENHARIA_GREEN, width=5)
        self.progress_percent_label.pack(side="left", padx=(8, 0))

        # Matéria atual
        subject_container = tk.Frame(self.main_frame, bg="white", relief="solid", borderwidth=1)
        subject_container.pack(fill="x", pady=(5, 8))

        subject_header = tk.Frame(subject_container, bg=ENGENHARIA_LIGHT_BLUE, height=28)
        subject_header.pack(fill="x")
        subject_header.pack_propagate(False)
        tk.Label(subject_header, text="MATÉRIA ATUAL", font=("Arial", 9, "bold"),
                 bg=ENGENHARIA_LIGHT_BLUE, fg="white").pack(pady=6)

        self.txt_subject = tk.Text(subject_container, font=("Segoe UI", 13, "bold"),
                                   fg=ENGENHARIA_BLUE, height=2, width=50, wrap="word",
                                   relief="flat", bg="white", bd=0)
        self.txt_subject.insert("1.0", "Carregando...")
        self.txt_subject.config(state="disabled")
        self.txt_subject.pack(pady=8, padx=10)

        tk.Button(subject_container, text="📋 COPIAR", command=self.copiar_materia,
                  font=("Arial", 8, "bold"), bg=ENGENHARIA_GRAY, fg="white",
                  cursor="hand2", relief="flat", padx=12, pady=3).pack(pady=(0, 6))

        # Timer
        timer_frame = tk.Frame(self.main_frame, bg="white", relief="solid", borderwidth=1)
        timer_frame.pack(pady=8)

        self.lbl_timer = tk.Label(timer_frame, text="00:00:00",
                                  font=("Courier New", 42, "bold"), fg=ENGENHARIA_GREEN,
                                  bg="white", padx=30, pady=12)
        self.lbl_timer.pack()

        self.lbl_progress = tk.Label(self.main_frame, text="Ciclos Completos: 0",
                                     font=("Arial", 11, "bold"), bg=BACKGROUND_MAIN, fg=ENGENHARIA_BLUE)
        self.lbl_progress.pack(pady=6)

        # Controles principais
        controls_frame = tk.Frame(self.main_frame, bg=BACKGROUND_MAIN)
        controls_frame.pack(pady=8)

        self.btn_action = tk.Button(controls_frame, text="⏱ INICIAR ESTUDOS",
                                    font=("Arial", 10, "bold"), bg=ENGENHARIA_GREEN, fg="white",
                                    command=self.toggle_timer, height=1, width=22,
                                    cursor="hand2", relief="flat",
                                    activebackground=ENGENHARIA_DARK_GREEN, activeforeground="white")
        self.btn_action.pack(pady=3)

        self.btn_finish = tk.Button(controls_frame, text="✓ FINALIZAR CICLO",
                                    font=("Arial", 10, "bold"), bg=ENGENHARIA_LIGHT_BLUE, fg="white",
                                    command=self._finish_cycle_manual, height=1, width=22,
                                    cursor="hand2", state="disabled", relief="flat",
                                    activebackground=ENGENHARIA_BLUE, activeforeground="white")
        self.btn_finish.pack(pady=3)

        self.btn_skip = tk.Button(controls_frame, text="⏭ AVANÇAR MATÉRIA",
                                  font=("Arial", 10, "bold"), bg=ENGENHARIA_GRAY, fg="white",
                                  command=self._confirm_skip_subject, height=1, width=22,
                                  cursor="hand2", state="disabled", relief="flat",
                                  activebackground="#333333", activeforeground="white")
        self.btn_skip.pack(pady=3)

        # Separador
        tk.Frame(self.main_frame, bg=ENGENHARIA_LIGHT_GRAY, height=1).pack(fill="x", pady=10)
        tk.Label(self.main_frame, text="FERRAMENTAS E RECURSOS",
                 font=("Arial", 10, "bold"), bg=BACKGROUND_MAIN, fg=ENGENHARIA_GRAY).pack()

        # Grade de ferramentas (5 colunas × 2 linhas)
        secondary_frame = tk.Frame(self.main_frame, bg=BACKGROUND_MAIN)
        secondary_frame.pack(pady=6)

        buttons_config = [
            ("📊 Relatório",   self._show_stats_window,    "#5D6D7E"),
            ("📈 Diário",      self._show_daily_stats,     "#16A085"),
            ("📝 Dificuldade", self._add_difficulty,       "#E74C3C"),
            ("🎯 Ver Pontos",  self._show_difficulties,    "#8E44AD"),
            ("🤖 Prompt IA",   self.abrir_prompt_thread,   "#E67E22"),
            ("📚 Fontes",      self.abrir_material,        "#F39C12"),
            ("🙏 Oração",      self.abrir_oracao_thread,   "#7B1FA2"),
            ("🕊️ Descanso",    self.abrir_descanso_thread, "#00796B"),
        ]

        for idx, (text, cmd, color) in enumerate(buttons_config):
            tk.Button(secondary_frame, text=text, command=cmd,
                      bg=color, fg="white", font=("Arial", 10, "bold"),
                      width=13, height=1, cursor="hand2", relief="flat",
                      activebackground=color, activeforeground="white", pady=4
                      ).grid(row=idx // 4, column=idx % 4, padx=3, pady=3)

        # Status bar
        self.lbl_status = tk.Label(self.main_frame,
                                   text="Sistema pronto. Clique em INICIAR ESTUDOS para começar.",
                                   font=("Arial", 9, "italic"), wraplength=650, justify="center",
                                   bg=BACKGROUND_MAIN, fg=ENGENHARIA_BLUE)
        self.lbl_status.pack(side="bottom", pady=8)

    # ── Ações gerais ───────────────────────────────────────────────────────
    def copiar_materia(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.txt_subject.get("1.0", tk.END).strip())
        messagebox.showinfo("✓ Copiado", "O nome da matéria foi copiado.", parent=self.root)
        self.root.update()

    def abrir_prompt_thread(self):
        threading.Thread(target=self._run, args=(janela_prompt.abrir,), daemon=True).start()

    def abrir_oracao_thread(self):
        threading.Thread(target=self._run, args=(janela_oracao.abrir,), daemon=True).start()

    def abrir_descanso_thread(self):
        threading.Thread(target=self._run, args=(janela_descanso.abrir,), daemon=True).start()

    def _run(self, fn):
        try:
            fn()
        except Exception:
            pass

    def abrir_material(self):
        StudySourcesApp(tk.Toplevel(self.root))

    # ── Timer ──────────────────────────────────────────────────────────────
    def toggle_timer(self):
        if self.timer_running:
            self._stop_timer()
            self.btn_action.config(text="▶ CONTINUAR", bg="#27AE60")
            self.btn_finish.config(state="normal")
            self.lbl_status.config(text=f"⏸ Pausado em {self._format_time_elapsed(self.time_elapsed)}")
        else:
            self.timer_running = True
            self.btn_action.config(text="⏸ PAUSAR", bg="#E67E22")
            self.btn_finish.config(state="disabled")
            self.lbl_status.config(text="🎯 Estudando... Foco total no conteúdo!")
            self._tick()

    def _stop_timer(self):
        self.timer_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def _tick(self):
        if not self.timer_running:
            return
        self.time_elapsed += 1
        self.lbl_timer.config(text=self._format_time_elapsed(self.time_elapsed))
        self.timer_id = self.root.after(1000, self._tick)

    # ── Ciclo de estudo ────────────────────────────────────────────────────
    def _finish_cycle_manual(self):
        if self.time_elapsed < 300:
            if not messagebox.askyesno("Confirmar Registro",
                                       f"⚠️ Você estudou apenas {self._format_time_elapsed(self.time_elapsed)}.\n\nDeseja registrar mesmo assim?",
                                       parent=self.root):
                return

        self._stop_timer()
        self.lbl_timer.config(text="00:00:00")

        q_done = q_correct = 0
        if messagebox.askyesno("Registro de Performance", "📝 Você resolveu questões de fixação neste ciclo?", parent=self.root):
            q_done = simpledialog.askinteger("Questões Realizadas", "Quantas questões você fez?",
                                             minvalue=0, maxvalue=500, parent=self.root)
            if q_done and q_done > 0:
                q_correct = simpledialog.askinteger("Acertos", f"Das {q_done} questões, quantas você acertou?",
                                                    minvalue=0, maxvalue=q_done, parent=self.root)

        self.controller.complete_pomodoro(self.time_elapsed, q_done or 0, q_correct or 0)
        data = self.controller.load_active_subject()

        if data and data['cycles'] >= 4:
            messagebox.showinfo("✅ Matéria Concluída!",
                                f"Você completou 4 ciclos de:\n\n{data['name']}\n\nAvançando para próxima matéria!",
                                parent=self.root)
            self.controller.finish_subject_and_advance()

        self.time_elapsed = 0
        self.btn_finish.config(state="disabled")
        self.btn_action.config(text="⏱ INICIAR ESTUDOS", bg=ENGENHARIA_GREEN)
        self._refresh_view()

    def _confirm_skip_subject(self):
        data = self.controller.current_subject_data
        if not data:
            messagebox.showwarning("Atenção", "Nenhuma matéria ativa.", parent=self.root)
            return

        if data['cycles'] == 0:
            msg = "⚠️ Você ainda não estudou esta matéria.\n\nDeseja realmente pular?"
        else:
            tempo = self._format_duration(self.controller.repo.get_subject_total_time(data['name']))
            ciclos = self.controller.repo.get_subject_total_cycles(data['name'])
            msg = f"📊 Tempo já estudado: {tempo}\n📚 Ciclos completos: {ciclos}\n\n✓ Avançar para próxima matéria?"

        if messagebox.askyesno("Confirmar Avanço", msg, parent=self.root):
            if self.timer_running:
                self._stop_timer()
                self.btn_action.config(text="⏱ INICIAR ESTUDOS", bg=ENGENHARIA_GREEN)
            self.controller.finish_subject_and_advance()
            self._refresh_view()

    # ── Refresh da view ────────────────────────────────────────────────────
    def _refresh_view(self):
        data    = self.controller.load_active_subject()
        total   = self.controller.repo.get_total_subjects()
        current = self.controller.repo.get_current_cycle_position()
        percent = min((current / total) * 100 if total > 0 else 0, 100.0)

        self.progress_var.set(percent)
        self.progress_percent_label.config(text=f"{int(percent)}%")
        self.root.title(f"ENGENHARIA - Engenharia de Software | {int(percent)}% Concluído")

        try:
            info = self.controller.repo.get_progresso_bloco_atual()
            self.lbl_date.config(
                text=f"📅 {date.today().strftime('%d/%m/%Y')} • 📚 {info['bloco']} ({info['atual']}/{info['total']})"
            )
        except Exception:
            pass

        if not data:
            self.txt_subject.config(state="normal")
            self.txt_subject.delete("1.0", tk.END)
            self.txt_subject.insert("1.0", "🎉 CICLO COMPLETO CONCLUÍDO!\nPARABÉNS PELO ESFORÇO!")
            self.txt_subject.config(state="disabled")
            self.lbl_status.config(text="✓ Você completou todas as matérias do ciclo atual!")
            return

        name = data['name']
        self.txt_subject.config(state="normal")
        self.txt_subject.delete("1.0", tk.END)
        self.txt_subject.insert("1.0", name)
        self.txt_subject.config(state="disabled")
        self.lbl_progress.config(text=f"Ciclos Completos: {data['cycles']}")

        bg_color    = BACKGROUND_MAIN
        status_text = "Modo: Estudo Teórico e Prático"

        if "[REV" in name or "[ANKI]" in name:
            bg_color, status_text = REVIEW_COLOR,   "⚡ MODO REVISÃO ATIVO - Foco em consolidação e memorização"
        elif "[SIM" in name:
            bg_color, status_text = SIMULADO_COLOR, "🔥 MODO SIMULADO - Condições reais de prova, sem consultas"
        elif "[RED]" in name:
            bg_color, status_text = REDACAO_COLOR,  "✍️ MODO REDAÇÃO - Estrutura, argumentação e desenvolvimento textual"
        elif "[PROJ]" in name or "[PRAT]" in name:
            bg_color, status_text = CODING_COLOR,   "💻 MODO PRÁTICO - Implementação e desenvolvimento de código"

        self.main_frame.config(bg=bg_color)
        self.lbl_status.config(text=status_text, bg=bg_color)
        self.lbl_date.config(bg=bg_color)
        self.lbl_progress.config(bg=bg_color)
        self.progress_percent_label.config(bg=bg_color)

        for widget in self.main_frame.winfo_children():
            if isinstance(widget, (tk.Label, tk.Frame)) and widget not in (
                self.lbl_date, self.lbl_status, self.lbl_progress, self.progress_percent_label
            ):
                try:
                    widget.config(bg=bg_color)
                except Exception:
                    pass

        self.btn_skip.config(state="normal", bg="#F39C12" if data['cycles'] == 0 else "#E74C3C")

        if not self.timer_running:
            self.lbl_timer.config(text="00:00:00")
            self.time_elapsed = 0
            self.btn_finish.config(state="disabled")

    # ── Janelas auxiliares ─────────────────────────────────────────────────
    def _show_stats_window(self):
        JanelaStatsDetalhado(self.root, self.controller.get_report_data(), self._format_duration)

    def _show_daily_stats(self):
        JanelaStatsDiario(self.root, self.controller.get_daily_summary(), self._format_duration)

    def _show_difficulties(self):
        JanelaDificuldades(self.root, self.controller).show()

    def _add_difficulty(self):
        if not self.controller.current_subject_data:
            messagebox.showwarning("Atenção", "Nenhuma matéria ativa no momento.", parent=self.root)
            return
        JanelaAdicionarDificuldade(self.root, self.controller.current_subject_data['name'],
                                   self.controller.save_difficulty)

    def _show_decision_dialog(self, subject_name):
        JanelaDecisao(
            self.root, subject_name,
            callback_next=lambda: (self.controller.finish_subject_and_advance(),
                                   self._refresh_view(),
                                   self.btn_action.config(text="⏱ INICIAR ESTUDOS", bg=ENGENHARIA_GREEN)),
            callback_continue=lambda: (self.controller.continue_same_subject(),
                                       self._refresh_view(),
                                       self.btn_action.config(text="➕ CICLO EXTRA", bg=ENGENHARIA_LIGHT_BLUE)),
        )


# ── Entry point ────────────────────────────────────────────────────────────────
def main():
    try:
        root = tk.Tk()
        StudyApp(root)
        root.mainloop()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Erro fatal: {e}", file=sys.stderr)
        messagebox.showerror("Erro Fatal", f"A aplicação encontrou um erro:\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
