#!/bin/bash
# i18n-source: 06-hooks/security-scan.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Varredura de segurança ao escrever arquivo
# Hook: PostToolUse:Write
#
# Verifica arquivos em busca de segredos codificados no código, chaves de API e credenciais.
# Emite um aviso não-bloqueante via additionalContext quando problemas são encontrados.
#
# Compatível com: macOS, Linux, Windows (Git Bash)

# Lê entrada JSON do stdin (protocolo de hooks do Claude Code)
INPUT=$(cat)

# Extrai file_path usando sed (compatível com todas as plataformas incluindo Windows Git Bash)
# Evita grep -P (não disponível no Windows Git Bash) e dependência de python3
FILE_PATH=$(echo "$INPUT" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# Ignora arquivos binários, diretórios vendor e artefatos de build
case "$FILE_PATH" in
  *.png|*.jpg|*.jpeg|*.gif|*.svg|*.ico|*.woff|*.woff2|*.ttf|*.eot) exit 0 ;;
  */node_modules/*|*/.git/*|*/dist/*|*/build/*) exit 0 ;;
esac

ISSUES=""

# Verifica senhas codificadas no código
# Trata formatos JSON ("password": "value") e de código (password = 'value')
# Usa \\n como separador — é um escape JSON válido e passa com segurança pelo printf
if grep -qiE '"password"[[:space:]]*:[[:space:]]*"[^"]+"' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- AVISO: Possível senha codificada no código detectada\\n"
elif grep -qiE '(password|passwd|pwd)[[:space:]]*=[[:space:]]*'"'"'[^'"'"']+'"'"'' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- AVISO: Possível senha codificada no código detectada\\n"
fi

# Verifica chaves de API codificadas no código
if grep -qiE '"(api[_-]?key|apikey|access[_-]?token)"[[:space:]]*:[[:space:]]*"[^"]+"' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- AVISO: Possível chave de API codificada no código detectada\\n"
fi

# Verifica segredos e tokens codificados no código
if grep -qiE '(secret|token)[[:space:]]*=[[:space:]]*['"'"'"][^'"'"'"]+['"'"'"]' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- AVISO: Possível segredo ou token codificado no código detectado\\n"
fi

# Verifica chaves privadas
if grep -q "BEGIN.*PRIVATE KEY" "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- AVISO: Chave privada detectada\\n"
fi

# Verifica chaves AWS
if grep -qE "AKIA[0-9A-Z]{16}" "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- AVISO: Chave de acesso AWS detectada\\n"
fi

# Verifica com semgrep se disponível (stdout suprimido para evitar mistura com saída JSON)
if command -v semgrep &> /dev/null; then
  semgrep --config=auto "$FILE_PATH" --quiet >/dev/null 2>/dev/null
fi

# Verifica com trufflehog se disponível (stdout suprimido para evitar mistura com saída JSON)
if command -v trufflehog &> /dev/null; then
  trufflehog filesystem "$FILE_PATH" --only-verified --quiet >/dev/null 2>/dev/null
fi

# Se problemas forem encontrados, emite como additionalContext (aviso não-bloqueante)
# Usa o formato hookSpecificOutput exigido pelo protocolo PostToolUse do Claude Code
if [ -n "$ISSUES" ]; then
  # Escapa o caminho do arquivo para JSON (barra invertida e aspas duplas)
  # ISSUES já usa \\n como separador (escape JSON válido) — apenas escapa aspas duplas
  SAFE_PATH=$(printf '%s' "$FILE_PATH" | sed 's/\\/\\\\/g; s/"/\\"/g')
  SAFE_ISSUES=$(printf '%s' "$ISSUES" | sed 's/"/\\"/g')
  printf '{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "Varredura de segurança encontrou problemas em %s:\\n%sRevise e use variáveis de ambiente em vez disso."}}' "$SAFE_PATH" "$SAFE_ISSUES"
fi

exit 0
