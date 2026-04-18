#!/bin/bash
# i18n-source: 07-plugins/devops-automation/scripts/deploy.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
set -e

echo "🚀 Iniciando deploy..."

# Carrega o ambiente
ENV=${1:-staging}
echo "📦 Ambiente alvo: $ENV"

# Verificações pré-deploy
echo "✓ Executando verificações pré-deploy..."
npm run lint
npm test

# Build
echo "🔨 Construindo a aplicação..."
npm run build

# Deploy
echo "🚢 Fazendo deploy em $ENV..."
kubectl apply -f k8s/$ENV/

# Verificação de saúde
echo "🏥 Executando verificações de saúde..."
sleep 10
curl -f http://api.$ENV.example.com/health

echo "✅ Deploy concluído!"
