#!/bin/bash
# i18n-source: 06-hooks/log-bash.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Registra todos os comandos bash
# Hook: PostToolUse:Bash
#
# Lê o comando executado a partir do JSON no stdin e o registra em um arquivo.
#
# Compatível com: macOS, Linux, Windows (Git Bash)

# Lê entrada JSON do stdin (protocolo de hooks do Claude Code)
INPUT=$(cat)

# Extrai o comando bash de tool_input
# Nota: sed [^"]* para na primeira aspa escapada do JSON; para comandos com strings
# entre aspas duplas, apenas a parte até o primeiro \" será capturada — esta é uma
# limitação conhecida da análise JSON com sed e é aceitável para fins de log.
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$COMMAND" ]; then
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# Cria o diretório de log se não existir
mkdir -p "$(dirname "$LOGFILE")"

# Registra o comando
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

exit 0
