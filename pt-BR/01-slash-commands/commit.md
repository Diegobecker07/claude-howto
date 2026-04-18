<!-- i18n-source: 01-slash-commands/commit.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: Criar um commit git com contexto
---

## Contexto

- Status git atual: !`git status`
- Diff git atual: !`git diff HEAD`
- Branch atual: !`git branch --show-current`
- Commits recentes: !`git log --oneline -10`

## Sua tarefa

Com base nas alterações acima, crie um único commit git.

Se uma mensagem foi fornecida via argumentos, use-a: $ARGUMENTS

Caso contrário, analise as alterações e crie uma mensagem de commit adequada seguindo o formato conventional commits:
- `feat:` para novos recursos
- `fix:` para correções de bugs
- `docs:` para mudanças em documentação
- `refactor:` para refatoração de código
- `test:` para adição de testes
- `chore:` para tarefas de manutenção

---
**Última Atualização**: 9 de abril de 2026
