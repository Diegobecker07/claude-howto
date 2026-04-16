#!/bin/bash
# i18n-source: 06-hooks/pre-tool-check.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Verificação de segurança pré-ferramenta para comandos Bash
# Hook: PreToolUse (matcher: Bash)
#
# Este hook é executado antes de cada execução da ferramenta Bash e bloqueia ou avisa sobre
# comandos shell potencialmente destrutivos ou de alto risco.
#
# Configuração:
#   cp 06-hooks/pre-tool-check.sh ~/.claude/hooks/
#   chmod +x ~/.claude/hooks/pre-tool-check.sh
#
# Configure em ~/.claude/settings.json:
#   {
#     "hooks": {
#       "PreToolUse": [
#         {
#           "matcher": "Bash",
#           "hooks": [
#             {
#               "type": "command",
#               "command": "~/.claude/hooks/pre-tool-check.sh"
#             }
#           ]
#         }
#       ]
#     }
#   }
#
# Entrada: JSON via stdin com o formato:
#   { "tool_name": "Bash", "tool_input": { "command": "..." } }
#
# Convenção de saída (conforme o protocolo de hooks do Claude Code):
#   - exit 0 → permitir. stdout pode conter JSON (hookSpecificOutput); stderr
#     é descartado silenciosamente, portanto avisos impressos em stderr NÃO são visíveis.
#     Para observabilidade em comandos permitidos, grave em um arquivo de log de auditoria.
#   - exit 2 → bloquear. stderr é devolvido ao Claude como o motivo do bloqueio.
#     Qualquer echo explicando *por que* um comando foi bloqueado DEVE ser redirecionado para
#     stderr com `>&2`, caso contrário o Claude Code reporta "No stderr output".
#
# Log de auditoria: cada invocação é registrada em
#   $CLAUDE_PROJECT_DIR/.claude/hooks/audit.log
# com a decisão (BLOCK/WARN/ALLOW), para que você possa observar correspondências do
# nível WARN mesmo que sua saída stderr seja descartada pelo Claude Code.

# Lê a entrada JSON completa do stdin
INPUT=$(cat)

# Extrai o comando usando sed portátil (compatível com macOS e Linux)
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

# Usa a entrada bruta como fallback se a extração falhar
if [ -z "$COMMAND" ]; then
  COMMAND="$INPUT"
fi

# ── Log de auditoria ─────────────────────────────────────────────────────────
# Registra cada invocação com a decisão final. Esta é a única maneira confiável
# de observar o nível WARN, pois o Claude Code descarta silenciosamente o stderr no
# exit 0. Usa $(pwd) como fallback quando o hook é invocado fora do Claude Code
# (ex.: para testes locais).
LOG_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}/.claude/hooks"
LOG_FILE="$LOG_DIR/audit.log"
mkdir -p "$LOG_DIR" 2>/dev/null
log_decision() {
  echo "$(date -u +%FT%TZ) [$1] $COMMAND" >> "$LOG_FILE"
}

# ── Padrões bloqueados ────────────────────────────────────────────────────────
# Estes comandos são bloqueados incondicionalmente pois são quase sempre
# destrutivos e raramente intencionais em um contexto automatizado.

BLOCKED_PATTERNS=(
  # Âncora `rm -rf /` para que `/` deva ser seguido por espaço em branco ou fim de linha,
  # caso contrário a correspondência de substring sinalizaria falsamente ex.: `rm -rf /tmp/foo`.
  "rm -rf /([[:space:]]|$)"
  "rm -rf \*"
  "dd if=/dev/zero"
  "dd if=/dev/random"
  ":\(\)\{:\|:&\};:"  # Fork bomb (metacaracteres regex escapados)
  "mkfs\."           # Formato de sistema de arquivos
  "format c:"        # Formato de disco Windows
)

for pattern in "${BLOCKED_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    log_decision "BLOCK:$pattern"
    # Estes echos DEVEM ir para stderr — o Claude Code apresenta o stderr como o
    # motivo do bloqueio no exit 2. Escrever no stdout mostraria "No stderr output".
    echo "❌ Bloqueado: Comando potencialmente destrutivo detectado: $pattern" >&2
    echo "   Comando: $COMMAND" >&2
    exit 2
  fi
done

# ── Padrões de aviso ──────────────────────────────────────────────────────────
# Estes padrões são arriscados mas podem ser intencionais. Registra um aviso e permite.

WARNING_PATTERNS=(
  "rm -rf"
  "git push --force"
  "git reset --hard"
  "git clean -f"
  "chmod -R 777"
  "sudo rm"
  "DROP TABLE"
  "DROP DATABASE"
  "truncate"
)

MATCHED_WARNINGS=""
for pattern in "${WARNING_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qi "$pattern"; then
    MATCHED_WARNINGS="${MATCHED_WARNINGS:+$MATCHED_WARNINGS,}$pattern"
    # Espelha o aviso no stderr para humanos que executam o hook manualmente.
    # O Claude Code descarta isso no exit 0 — o log de auditoria é o registro
    # confiável (veja entradas WARN).
    echo "⚠️  Aviso: Operação de alto risco detectada: $pattern" >&2
  fi
done

if [ -n "$MATCHED_WARNINGS" ]; then
  log_decision "WARN:$MATCHED_WARNINGS"
  echo "   Comando: $COMMAND" >&2
  echo "   Prosseguindo — revise os avisos acima antes de continuar." >&2
else
  log_decision "ALLOW"
fi

# ── Permitir ──────────────────────────────────────────────────────────────────
exit 0
