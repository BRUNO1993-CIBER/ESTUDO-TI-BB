# 📚 Sistema de Estudos — Engenharia de Software

> Aplicativo desktop desenvolvido em Python para organizar, cronometrar e acompanhar os estudos de **Engenharia de Software**.

---

## ✨ Funcionalidades

| Módulo | Descrição |
|---|---|
| ⏱ **Timer de Ciclos** | Cronômetro por sessão de estudo com registro automático |
| 📊 **Progresso do Ciclo** | Barra de progresso sobre todas as matérias |
| 📝 **Registro de Dificuldades** | Anote pontos de atenção por matéria durante o estudo |
| 🎯 **Painel de Dificuldades** | Visualize todos os pontos registrados organizados por matéria |
| 📈 **Estatísticas Diárias** | Resumo de tempo e ciclos por dia |
| 📊 **Relatório Detalhado** | Histórico completo de todas as sessões |
| 📚 **Fontes de Estudo** | Biblioteca de links e materiais organizados por tópico |
| 🙏 **Janela de Oração** | Momento de foco espiritual antes de estudar |
| 🕊️ **Protocolo de Descanso** | Rotina de descompressão entre ciclos de estudo |

---

## 🖥️ Interface

- Janela principal maximizada com design limpo e profissional
- Paleta de cores adaptada ao modo de estudo (revisão, simulado, redação, prático)
- Todas as janelas auxiliares abertas em tela cheia

---

## 🗂️ Estrutura do Projeto

```
ESTUDO-TI/
│
├── main.py              # Entry point — inicia o app
├── config.py            # Caminhos e constantes globais
├── start.sh             # Script de inicialização (Linux)
├── requirements.txt
│
├── core/                # Lógica de negócio
│   ├── backend.py       # Repositório SQLite (acesso a dados)
│   ├── ciclo_estudo.py  # Lista de matérias
│   └── agrupar_materias.py
│
├── ui/                  # Janelas da interface
│   ├── janela_dificuldades.py
│   ├── janela_adicionar_dificuldade.py
│   ├── janela_decisao.py
│   ├── janela_stats_diario.py
│   ├── janela_stats_detalhado.py
│   ├── fontes_estudo.py
│   ├── janela_oracao.py
│   └── janela_descanso.py
│
├── assets/              # Ícones e arquivos estáticos
│   └── estudos.png
│
└── data/                # Banco de dados e backups (local)
    ├── eng_software.db
    └── backups/
```

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.10+
- Tkinter (já incluso no Python padrão)
- Linux (testado no Linux Mint) ou Windows

### Instalação

```bash
git clone https://github.com/BRUNO1993-CIBER/ESTUDO-TI-BB.git
cd ESTUDO-TI-BB
```

### Executar

**Linux:**
```bash
chmod +x start.sh
./start.sh
```

**Direto pelo Python:**
```bash
python main.py
```

---

## 🎯 Fluxo de Estudo

```
1. Abra o app → matéria atual carrega automaticamente
2. Clique em INICIAR ESTUDOS → timer começa
3. Estude com foco total
4. Pause quando precisar → registre dificuldades se houver
5. Clique em FINALIZAR CICLO → registre questões feitas (opcional)
6. Repita até 4 ciclos → app avança para próxima matéria automaticamente
```

---

## 🤖 Prompts de IA

Os arquivos `prompts/prompt_aula.py` e `prompts/prompt_questoes.py` estão em branco por padrão. O usuário deve preencher com seus próprios prompts.

---

## 🗄️ Banco de Dados

O progresso é salvo localmente em `data/eng_software.db` (SQLite).

---

## 👨‍💻 Autor

Desenvolvido por **Bruno Machado** para estudo e domínio de Engenharia de Software.

---

## 📄 Licença

Este projeto é de uso pessoal e educacional.
