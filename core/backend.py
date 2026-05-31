
import sqlite3
from datetime import date, datetime
from typing import Optional
import os
import shutil

from .ciclo_estudo import STUDY_CYCLE
from .agrupar_materias import agrupar_materias_por_bloco
from config import DB_PATH, BACKUP_DIR

DB_NAME = DB_PATH

class StudyRepository:
    def __init__(self, db_name: str = DB_NAME):
        self.db_name = db_name
        self._backup_db()
        self._init_db()
        self._migrate_db()
        self._migrate_difficulties()
        
        self.blocos = agrupar_materias_por_bloco()
        self.ordem_blocos = ["BD", "ES", "REQ", "ARQ", "LANG", "QUAL", "SEG", "CLOUD", "PROD", "INFRA", "GOV"]

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _backup_db(self):
        if os.path.exists(self.db_name):

            backup_dir = BACKUP_DIR
            os.makedirs(backup_dir, exist_ok=True)

            filename = os.path.basename(self.db_name)

            backup_name = os.path.join(
                backup_dir,
                f"{filename}.{date.today().isoformat()}.backup"
            )

            try:
                shutil.copy2(self.db_name, backup_name)
            except Exception:
                pass

    def _init_db(self):
        with self._get_connection() as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                study_date TEXT NOT NULL,
                subject_name TEXT NOT NULL,
                cycles_completed INTEGER DEFAULT 0,
                total_seconds INTEGER DEFAULT 0,
                status TEXT DEFAULT 'IN_PROGRESS' 
            );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS cycle_control (
                id INTEGER PRIMARY KEY,
                current_block_index INTEGER DEFAULT 0
            );
            """)
            conn.execute("""
            CREATE TABLE IF NOT EXISTS block_indices (
                block_name TEXT PRIMARY KEY,
                current_subject_index INTEGER DEFAULT 0
            );
            """)
            
            cursor = conn.cursor()
            cursor.execute("SELECT count(*) FROM cycle_control")
            if cursor.fetchone()[0] == 0:
                conn.execute("INSERT INTO cycle_control (id, current_block_index) VALUES (1, 0)")
            
            blocos_lista = ["BD", "ES", "REQ", "ARQ", "LANG", "QUAL", "SEG", "CLOUD", "PROD", "INFRA", "GOV"]
            for bloco in blocos_lista:
                cursor.execute("SELECT count(*) FROM block_indices WHERE block_name = ?", (bloco,))
                if cursor.fetchone()[0] == 0:
                    conn.execute("INSERT INTO block_indices (block_name, current_subject_index) VALUES (?, 0)", (bloco,))
            
            conn.commit()

    def _migrate_db(self):
        cols = [
            ("questions_done", "INTEGER DEFAULT 0"),
            ("questions_correct", "INTEGER DEFAULT 0")
        ]
        with self._get_connection() as conn:
            cursor = conn.cursor()
            for col_name, col_type in cols:
                try:
                    cursor.execute(f"ALTER TABLE study_sessions ADD COLUMN {col_name} {col_type}")
                except Exception:
                    pass

    def _migrate_difficulties(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("ALTER TABLE study_sessions ADD COLUMN difficulties TEXT DEFAULT ''")
            except Exception:
                pass

    def get_subject_total_time(self, subject_name: str) -> int:
        """Retorna o tempo total acumulado de TODOS os dias para uma matéria específica"""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT SUM(total_seconds) FROM study_sessions WHERE subject_name = ?", 
                (subject_name,)
            )
            result = cursor.fetchone()
            return result[0] if result and result[0] else 0

    def get_subject_total_cycles(self, subject_name: str) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT SUM(cycles_completed) FROM study_sessions WHERE subject_name = ?",
                (subject_name,)
            )
            result = cursor.fetchone()
            return result[0] if result and result[0] else 0

    def get_next_subject_from_cycle(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT current_block_index FROM cycle_control WHERE id = 1")
            bloco_idx = cursor.fetchone()[0]
            bloco_nome = self.ordem_blocos[bloco_idx]
            
            cursor.execute("SELECT current_subject_index FROM block_indices WHERE block_name = ?", (bloco_nome,))
            materia_idx = cursor.fetchone()[0]
            
            materias_do_bloco = self.blocos[bloco_nome]
            
            if materia_idx >= len(materias_do_bloco):
                materia_idx = 0
                conn.execute("UPDATE block_indices SET current_subject_index = 0 WHERE block_name = ?", (bloco_nome,))
                conn.commit()
            
            return materias_do_bloco[materia_idx]

    def advance_cycle(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT current_block_index FROM cycle_control WHERE id = 1")
            bloco_idx = cursor.fetchone()[0]
            
            bloco_idx += 1
            
            if bloco_idx >= len(self.ordem_blocos):
                bloco_idx = 0
                
                for bloco_nome in self.ordem_blocos:
                    cursor.execute("SELECT current_subject_index FROM block_indices WHERE block_name = ?", (bloco_nome,))
                    materia_idx = cursor.fetchone()[0]
                    
                    materia_idx += 1
                    
                    if materia_idx >= len(self.blocos[bloco_nome]):
                        materia_idx = 0
                    
                    conn.execute("UPDATE block_indices SET current_subject_index = ? WHERE block_name = ?", 
                            (materia_idx, bloco_nome))
            
            conn.execute("UPDATE cycle_control SET current_block_index = ? WHERE id = 1", (bloco_idx,))
            conn.commit()

    def ensure_daily_plan_exists(self):

        today = date.today().isoformat()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id FROM study_sessions 
                WHERE status != 'FINISHED' AND study_date = ?
                ORDER BY id DESC LIMIT 1
            """, (today,))
            row = cursor.fetchone()
            
            if not row:
                next_subject = self.get_next_subject_from_cycle()
                cursor.execute("""
                    INSERT INTO study_sessions (study_date, subject_name, status)
                    VALUES (?, ?, 'IN_PROGRESS')
                """, (today, next_subject))
                conn.commit()

    def get_current_subject(self) -> Optional[dict]:
        self.ensure_daily_plan_exists()
        today = date.today().isoformat()
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, subject_name, cycles_completed, status 
                FROM study_sessions 
                WHERE status != 'FINISHED' AND study_date = ?
                ORDER BY id DESC
                LIMIT 1
            """, (today,))
            row = cursor.fetchone()
            
            if row:
                return {
                    "id": row[0],
                    "name": row[1],
                    "cycles": row[2],
                    "status": row[3]
                }
            return None

    def record_cycle(self, row_id: int, duration: int, q_done: int = 0, q_correct: int = 0):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT cycles_completed FROM study_sessions WHERE id = ?", (row_id,))
            res = cursor.fetchone()
            
            if res:
                new_cycles = res[0] + 1
                cursor.execute("""
                    UPDATE study_sessions 
                    SET cycles_completed = ?, 
                        total_seconds = total_seconds + ?,
                        questions_done = questions_done + ?,
                        questions_correct = questions_correct + ?
                    WHERE id = ?
                """, (new_cycles, duration, q_done, q_correct, row_id))
                conn.commit()

    def mark_as_finished(self, row_id: int):
        with self._get_connection() as conn:
            conn.execute("UPDATE study_sessions SET status = 'FINISHED' WHERE id = ?", (row_id,))
            conn.commit()
        self.advance_cycle()

    def get_session_total_time(self, session_id: int) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT total_seconds FROM study_sessions WHERE id = ?", (session_id,))
            result = cursor.fetchone()
            return result[0] if result else 0

    def save_difficulty(self, session_id: int, difficulty_text: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT difficulties FROM study_sessions WHERE id = ?", (session_id,))
            result = cursor.fetchone()
            
            if result:
                existing = result[0] or ""
                timestamp = datetime.now().strftime("%H:%M")
                if existing:
                    new_text = f"{existing}\n[{timestamp}] {difficulty_text}"
                else:
                    new_text = f"[{timestamp}] {difficulty_text}"
                
                cursor.execute("""
                    UPDATE study_sessions 
                    SET difficulties = ?
                    WHERE id = ?
                """, (new_text, session_id))
                conn.commit()

    def get_difficulties_by_subject(self):
        sql = """
            SELECT subject_name, GROUP_CONCAT(difficulties, '\n---\n') as all_difficulties
            FROM study_sessions
            WHERE difficulties IS NOT NULL AND difficulties != ''
            GROUP BY subject_name
            ORDER BY subject_name
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()

    def get_all_stats(self):
        sql = """
            SELECT 
                subject_name as Materia,
                COUNT(*) as Total_Sessoes,
                SUM(cycles_completed) as Total_Ciclos,
                SUM(total_seconds) as Total_Segundos,
                SUM(questions_done) as Total_Questoes,
                SUM(questions_correct) as Total_Acertos,
                CASE 
                    WHEN SUM(questions_done) > 0 
                    THEN ROUND((SUM(questions_correct) * 100.0 / SUM(questions_done)), 1)
                    ELSE 0 
                END as Percentual_Acerto
            FROM study_sessions
            GROUP BY subject_name
            ORDER BY subject_name
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    
    def get_daily_summary(self):
        sql = """
            SELECT 
                study_date,
                COUNT(*) as total_sessions,
                SUM(cycles_completed) as total_cycles,
                SUM(total_seconds) as total_seconds,
                SUM(questions_done) as total_questions,
                SUM(questions_correct) as total_correct
            FROM study_sessions
            GROUP BY study_date
            ORDER BY study_date DESC
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
    
    def get_total_subjects(self):
        return len(STUDY_CYCLE)
        
    def get_current_cycle_position(self):
            """
            Retorna a quantidade exata de itens do STUDY_CYCLE atual 
            que já foram finalizados (avançados) no banco de dados.
            """
            with self._get_connection() as conn:
                cursor = conn.cursor()
                # Pega todas as matérias que você já apertou em 'AVANÇAR' ou 'FINALIZAR'
                cursor.execute("""
                    SELECT DISTINCT subject_name
                    FROM study_sessions
                    WHERE status = 'FINISHED'
                """)
                materias_finalizadas_db = [row[0] for row in cursor.fetchall()]

            # Agora ele cruza os dados: só conta se a matéria terminada ESTIVER no seu STUDY_CYCLE atual
            progresso_real = 0
            for materia in STUDY_CYCLE:
                if materia in materias_finalizadas_db:
                    progresso_real += 1
                    
            return progresso_real

    def get_progresso_bloco_atual(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT current_block_index FROM cycle_control WHERE id = 1")
            bloco_idx = cursor.fetchone()[0]
            bloco_nome = self.ordem_blocos[bloco_idx]
            
            cursor.execute("SELECT current_subject_index FROM block_indices WHERE block_name = ?", (bloco_nome,))
            materia_idx = cursor.fetchone()[0]
            
            total_no_bloco = len(self.blocos[bloco_nome])
            
            return {
                "bloco": bloco_nome,
                "sigla": bloco_nome,
                "atual": materia_idx + 1,
                "total": total_no_bloco,
                "percentual": int((materia_idx / total_no_bloco) * 100) if total_no_bloco > 0 else 0
            }
