<!-- i18n-source: 07-plugins/pr-review/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin PR Review

Fluxo completo de revisão de PR com verificações de segurança, testes e documentação.

## Funcionalidades

✅ Análise de segurança
✅ Verificação de cobertura de testes
✅ Verificação de documentação
✅ Avaliação de qualidade de código
✅ Análise de impacto de desempenho

## Instalação

```bash
/plugin install pr-review
```

## O Que Está Incluído

### Slash Commands
- `/review-pr` - Revisão abrangente de PR
- `/check-security` - Revisão focada em segurança
- `/check-tests` - Análise de cobertura de testes

### Subagentes
- `security-reviewer` - Detecção de vulnerabilidades de segurança
- `test-checker` - Análise de cobertura de testes
- `performance-analyzer` - Avaliação de impacto de desempenho

### Servidores MCP
- Integração com GitHub para dados de PR

### Hooks
- `pre-review.js` - Validação pré-revisão

## Uso

### Revisão Básica de PR
```
/review-pr
```

### Somente Verificação de Segurança
```
/check-security
```

### Verificação de Cobertura de Testes
```
/check-tests
```

## Requisitos

- Claude Code 1.0+
- Acesso ao GitHub
- Repositório Git

## Configuração

Configure seu token do GitHub:
```bash
export GITHUB_TOKEN="seu_github_token"
```

## Exemplo de Fluxo de Trabalho

```
Usuário: /review-pr

Claude:
1. Executa hook pré-revisão (valida repositório git)
2. Busca dados do PR via GitHub MCP
3. Delega revisão de segurança para o subagente security-reviewer
4. Delega testes para o subagente test-checker
5. Delega desempenho para o subagente performance-analyzer
6. Sintetiza todos os achados
7. Fornece relatório de revisão abrangente

Resultado:
✅ Segurança: Nenhum problema crítico encontrado
⚠️  Testes: Cobertura é 65%, recomenda-se 80%+
✅ Desempenho: Sem impacto significativo
📝 Recomendações: Adicionar testes para casos extremos
```
