<!-- i18n-source: 01-slash-commands/setup-ci-cd.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: Setup CI/CD Pipeline
description: Implementar hooks de pre-commit e GitHub Actions para garantia de qualidade
tags: ci-cd, devops, automation
---

# Configurar Pipeline CI/CD

Implementar gates de qualidade DevOps abrangentes adaptados ao tipo de projeto:

1. **Analisar o projeto**: Detectar linguagem(ns), framework, sistema de build e ferramentas existentes
2. **Configurar hooks de pre-commit** com ferramentas específicas da linguagem:
   - Formatação: Prettier/Black/gofmt/rustfmt/etc.
   - Linting: ESLint/Ruff/golangci-lint/Clippy/etc.
   - Segurança: Bandit/gosec/cargo-audit/npm audit/etc.
   - Verificação de tipos: TypeScript/mypy/flow (se aplicável)
   - Testes: Executar suítes de testes relevantes
3. **Criar workflows do GitHub Actions** (.github/workflows/):
   - Espelhar verificações de pre-commit em push/PR
   - Matriz de múltiplas versões/plataformas (se aplicável)
   - Verificação de build e teste
   - Etapas de implantação (se necessário)
4. **Verificar pipeline**: Testar localmente, criar PR de teste, confirmar que todas as verificações passam

Use ferramentas gratuitas/open-source. Respeite configurações existentes. Mantenha execução rápida.

---
**Última Atualização**: 9 de abril de 2026
