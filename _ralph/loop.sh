#!/usr/bin/env bash
# Ralph loop — reinvoca o agente Claude até o BACKLOG.md zerar.
# Cada iteração: lê PROMPT.md, executa UMA tarefa [ ] do BACKLOG.md, marca [x].
#
# Uso:
#   ./loop.sh           # roda até acabar o backlog (ou MAX_ITERS)
#   MAX_ITERS=3 ./loop.sh
#
# Requisitos: Claude Code CLI (`claude`) instalado e autenticado.
# Rode a partir da RAIZ do projeto:  bash _ralph/loop.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PROMPT_FILE="_ralph/PROMPT.md"
BACKLOG_FILE="_ralph/BACKLOG.md"
MAX_ITERS="${MAX_ITERS:-12}"

i=0
while :; do
  i=$((i+1))
  if [ "$i" -gt "$MAX_ITERS" ]; then
    echo "==> Limite de $MAX_ITERS iterações atingido. Parando."
    break
  fi

  # Para se não houver mais tarefas pendentes "[ ]"
  if ! grep -q '^\#\#\s*\[ \]' "$BACKLOG_FILE"; then
    echo "==> BACKLOG vazio. Tudo concluído em $((i-1)) iterações."
    break
  fi

  echo "================ Iteração $i ================"
  # -p: modo não-interativo; passa o PROMPT padrão via stdin.
  # --dangerously-skip-permissions: necessário p/ rodar sem prompts no loop.
  cat "$PROMPT_FILE" | claude -p --dangerously-skip-permissions

  echo "---- fim da iteração $i ----"
  sleep 2
done
