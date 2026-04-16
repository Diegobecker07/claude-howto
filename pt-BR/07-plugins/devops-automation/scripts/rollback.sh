#!/bin/bash
# i18n-source: 07-plugins/devops-automation/scripts/rollback.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
set -e

echo "⏪ Iniciando rollback..."

ENV=${1:-staging}
echo "📦 Ambiente alvo: $ENV"

# Obtém o deploy anterior
PREVIOUS=$(kubectl rollout history deployment/app -n $ENV | tail -2 | head -1 | awk '{print $1}')
echo "🔄 Revertendo para a revisão: $PREVIOUS"

# Executa o rollback
kubectl rollout undo deployment/app -n $ENV

# Aguarda o rollback
echo "⏳ Aguardando a conclusão do rollback..."
kubectl rollout status deployment/app -n $ENV

# Verificação de saúde
echo "🏥 Executando verificações de saúde..."
sleep 5
curl -f http://api.$ENV.example.com/health

echo "✅ Rollback concluído!"
