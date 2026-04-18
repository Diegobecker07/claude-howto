#!/usr/bin/env node
// i18n-source: 07-plugins/pr-review/hooks/pre-review.js
// i18n-source-sha: d4369ce
// i18n-date: 2026-04-16

/**
 * Hook pré-revisão
 * Executado antes de iniciar a revisão de PR para garantir que os pré-requisitos sejam atendidos
 */

async function preReview() {
  console.log('Executando verificações pré-revisão...');

  // Verifica se é um repositório git
  const { execSync } = require('child_process');
  try {
    execSync('git rev-parse --git-dir', { stdio: 'pipe' });
  } catch (error) {
    console.error('❌ Não é um repositório git');
    process.exit(1);
  }

  // Verifica alterações não commitadas
  try {
    const status = execSync('git status --porcelain', { encoding: 'utf-8' });
    if (status.trim()) {
      console.warn('⚠️  Aviso: Alterações não commitadas detectadas');
    }
  } catch (error) {
    console.error('❌ Falha ao verificar o status do git');
    process.exit(1);
  }

  console.log('✅ Verificações pré-revisão concluídas');
}

preReview().catch(error => {
  console.error('Hook pré-revisão falhou:', error);
  process.exit(1);
});
