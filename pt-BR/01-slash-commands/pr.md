<!-- i18n-source: 01-slash-commands/pr.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
description: Limpar código, preparar alterações e criar um pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Checklist de Preparação de Pull Request

Antes de criar um PR, execute estas etapas:

1. Executar linting: `prettier --write .`
2. Executar testes: `npm test`
3. Revisar git diff: `git diff HEAD`
4. Preparar alterações: `git add .`
5. Criar mensagem de commit seguindo conventional commits:
   - `fix:` para correções de bugs
   - `feat:` para novos recursos
   - `docs:` para documentação
   - `refactor:` para reestruturação de código
   - `test:` para adições de teste
   - `chore:` para manutenção

6. Gerar resumo do PR incluindo:
   - O que mudou
   - Por que mudou
   - Testes realizados
   - Impactos potenciais

---
**Última Atualização**: 9 de abril de 2026
