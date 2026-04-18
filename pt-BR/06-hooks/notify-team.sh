#!/bin/bash
# i18n-source: 06-hooks/notify-team.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Envia notificações em eventos
# Hook: PostToolUse (matcher: Bash) — executa após comandos bash; filtra por git push na lógica do script
# Nota: O Claude Code não tem um evento nativo PostPush. Para disparar no git push, verifique a string
# do comando bash por "git push" usando um matcher ou lógica condicional dentro deste script.

REPO_NAME=$(basename $(git rev-parse --show-toplevel 2>/dev/null) 2>/dev/null)
COMMIT_MSG=$(git log -1 --pretty=%B 2>/dev/null)
AUTHOR=$(git log -1 --pretty=%an 2>/dev/null)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

echo "📢 Enviando notificação para a equipe..."

# Exemplo de webhook do Slack (substitua pela URL do seu webhook)
SLACK_WEBHOOK="${SLACK_WEBHOOK_URL:-}"

if [ -n "$SLACK_WEBHOOK" ]; then
  curl -X POST "$SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"text\": \"Novo push em *$REPO_NAME*\",
      \"attachments\": [{
        \"color\": \"good\",
        \"fields\": [
          {\"title\": \"Branch\", \"value\": \"$BRANCH\", \"short\": true},
          {\"title\": \"Autor\", \"value\": \"$AUTHOR\", \"short\": true},
          {\"title\": \"Commit\", \"value\": \"$COMMIT_MSG\"}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ Notificação do Slack enviada"
fi

# Exemplo de webhook do Discord (substitua pela URL do seu webhook)
DISCORD_WEBHOOK="${DISCORD_WEBHOOK_URL:-}"

if [ -n "$DISCORD_WEBHOOK" ]; then
  curl -X POST "$DISCORD_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"content\": \"**Novo push em $REPO_NAME**\",
      \"embeds\": [{
        \"title\": \"$COMMIT_MSG\",
        \"color\": 3066993,
        \"fields\": [
          {\"name\": \"Branch\", \"value\": \"$BRANCH\", \"inline\": true},
          {\"name\": \"Autor\", \"value\": \"$AUTHOR\", \"inline\": true}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ Notificação do Discord enviada"
fi

# Exemplo de notificação por e-mail
EMAIL_TO="${TEAM_EMAIL:-}"

if [ -n "$EMAIL_TO" ]; then
  echo "Novo push em $REPO_NAME por $AUTHOR" | \
    mail -s "Git Push: $BRANCH" "$EMAIL_TO"

  echo "✅ Notificação por e-mail enviada"
fi

exit 0
