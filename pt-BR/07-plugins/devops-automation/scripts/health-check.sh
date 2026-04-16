#!/bin/bash
# i18n-source: 07-plugins/devops-automation/scripts/health-check.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16

echo "🏥 Verificação de Saúde do Sistema"
echo "===================="

ENV=${1:-production}

# Verifica API
echo -n "API: "
if curl -sf http://api.$ENV.example.com/health > /dev/null; then
  echo "✅ Saudável"
else
  echo "❌ Com problemas"
fi

# Verifica Banco de Dados
echo -n "Banco de Dados: "
if pg_isready -h db.$ENV.example.com > /dev/null 2>&1; then
  echo "✅ Saudável"
else
  echo "❌ Com problemas"
fi

# Verifica Pods
echo -n "Pods Kubernetes: "
PODS_READY=$(kubectl get pods -n $ENV --no-headers | grep "Running" | wc -l)
PODS_TOTAL=$(kubectl get pods -n $ENV --no-headers | wc -l)
echo "$PODS_READY/$PODS_TOTAL prontos"

echo "===================="
