#!/bin/bash
# i18n-source: 06-hooks/format-code.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Formata código automaticamente após a escrita
# Hook: PostToolUse:Write
#
# Lê o caminho do arquivo alvo a partir do JSON no stdin e executa o formatador
# adequado no arquivo após o Claude escrevê-lo.
#
# Compatível com: macOS, Linux, Windows (Git Bash)

# Lê entrada JSON do stdin (protocolo de hooks do Claude Code)
INPUT=$(cat)

# Extrai file_path usando sed (compatível com todas as plataformas)
FILE_PATH=$(echo "$INPUT" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# Detecta o tipo de arquivo e formata adequadamente
case "$FILE_PATH" in
  *.js|*.jsx|*.ts|*.tsx)
    if command -v prettier &> /dev/null; then
      prettier --write "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.py)
    if command -v black &> /dev/null; then
      black "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.go)
    if command -v gofmt &> /dev/null; then
      gofmt -w "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.rs)
    if command -v rustfmt &> /dev/null; then
      rustfmt "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.java)
    if command -v google-java-format &> /dev/null; then
      google-java-format -i "$FILE_PATH" 2>/dev/null
    fi
    ;;
esac

exit 0
