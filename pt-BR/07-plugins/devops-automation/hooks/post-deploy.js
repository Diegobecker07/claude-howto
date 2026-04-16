#!/usr/bin/env node
// i18n-source: 07-plugins/devops-automation/hooks/post-deploy.js
// i18n-source-sha: d4369ce
// i18n-date: 2026-04-16

/**
 * Hook pós-deploy
 * Executado após a conclusão do deploy
 */

async function postDeploy() {
  console.log('Executando tarefas pós-deploy...');

  const { execSync } = require('child_process');

  // Aguarda os pods ficarem prontos
  console.log('Aguardando os pods ficarem prontos...');
  try {
    execSync('kubectl wait --for=condition=ready pod -l app=myapp --timeout=300s', {
      stdio: 'inherit'
    });
  } catch (error) {
    console.error('❌ Os pods não ficaram prontos');
    process.exit(1);
  }

  // Executa smoke tests
  console.log('Executando smoke tests...');
  // Adicione seus comandos de smoke test aqui

  console.log('✅ Tarefas pós-deploy concluídas');
}

postDeploy().catch(error => {
  console.error('Hook pós-deploy falhou:', error);
  process.exit(1);
});
