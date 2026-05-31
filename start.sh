#!/bin/bash

# garante que o script roda no diretório do projeto
cd "$(dirname "$0")"

# ativa o virtualenv
source .venv/bin/activate

# executa o app
python main.py
