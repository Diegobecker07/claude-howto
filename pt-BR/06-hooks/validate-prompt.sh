#!/bin/bash
# i18n-source: 06-hooks/validate-prompt.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Valida prompts do usuário
# Hook: UserPromptSubmit
#
# Lê o prompt do usuário a partir do JSON no stdin e bloqueia operações perigosas.
#
# Compatível com: macOS, Linux, Windows (Git Bash)

# Lê entrada JSON do stdin (protocolo de hooks do Claude Code)
INPUT=$(cat)

# Extrai o texto do prompt da entrada JSON
# O Claude Code envia UserPromptSubmit com o campo "user_prompt" (fallback para "prompt")
PROMPT=$(echo "$INPUT" | sed -n 's/.*"user_prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
if [ -z "$PROMPT" ]; then
  PROMPT=$(echo "$INPUT" | sed -n 's/.*"prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
fi

if [ -z "$PROMPT" ]; then
  exit 0
fi

# Verifica operações perigosas
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "delete database"
  "drop database"
  "format disk"
  "dd if="
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$PROMPT" | grep -qi "$pattern"; then
    printf '{"decision": "block", "reason": "Operação perigosa detectada: %s"}' "$pattern"
    exit 0
  fi
done

# Verifica deploys em produção
if echo "$PROMPT" | grep -qiE "(deploy|push).*production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo '{"decision": "block", "reason": "Deploy em produção requer aprovação. Crie o arquivo .deployment-approved para prosseguir."}'
    exit 0
  fi
fi

# Verifica contexto necessário em certas operações
if echo "$PROMPT" | grep -qi "refactor"; then
  if [ ! -d "tests" ] && [ ! -d "test" ]; then
    printf '{"additionalContext": "Aviso: Refatorar sem testes pode ser arriscado. Considere escrever testes primeiro."}'
  fi
fi

exit 0
