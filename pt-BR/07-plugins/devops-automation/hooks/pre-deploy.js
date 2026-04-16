#!/usr/bin/env node
// i18n-source: 07-plugins/devops-automation/hooks/pre-deploy.js
// i18n-source-sha: d4369ce
// i18n-date: 2026-04-16

/**
 * Hook pré-deploy
 * Valida o ambiente e pré-requisitos antes do deploy
 */

async function preDeploy() {
  console.log('Executando verificações pré-deploy...');

  const { execSync } = require('child_process');

  // Verifica se kubectl está instalado
  try {
    execSync('which kubectl', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ kubectl não encontrado. Instale o Kubernetes CLI.');
    process.exit(1);
  }

  // Verifica se está conectado ao cluster
  try {
    execSync('kubectl cluster-info', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ Não conectado ao cluster Kubernetes');
    process.exit(1);
  }

  console.log('✅ Verificações pré-deploy concluídas');
}

preDeploy().catch(error => {
  console.error('Hook pré-deploy falhou:', error);
  process.exit(1);
});
