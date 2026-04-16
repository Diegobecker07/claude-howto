<!-- i18n-source: 03-skills/code-review/SKILL.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: code-review-specialist
description: Revisão de código abrangente com análise de segurança, desempenho e qualidade. Usar quando usuários pedem para revisar código, analisar qualidade de código, avaliar pull requests, ou mencionam revisão de código, análise de segurança ou otimização de desempenho.
---

# Skill de Revisão de Código

Esta skill fornece capacidades abrangentes de revisão de código com foco em:

1. **Análise de Segurança**
   - Problemas de autenticação/autorização
   - Riscos de exposição de dados
   - Vulnerabilidades de injeção
   - Fraquezas criptográficas
   - Log de dados sensíveis

2. **Revisão de Desempenho**
   - Eficiência de algoritmos (análise Big O)
   - Otimização de memória
   - Otimização de queries de banco de dados
   - Oportunidades de cache
   - Problemas de concorrência

3. **Qualidade de Código**
   - Princípios SOLID
   - Padrões de projeto
   - Convenções de nomenclatura
   - Documentação
   - Cobertura de testes

4. **Manutenibilidade**
   - Legibilidade do código
   - Tamanho de funções (deve ser < 50 linhas)
   - Complexidade ciclomática
   - Gerenciamento de dependências
   - Segurança de tipos

## Template de Revisão

Para cada trecho de código revisado, forneça:

### Resumo
- Avaliação geral de qualidade (1-5)
- Contagem de achados-chave
- Áreas de prioridade recomendadas

### Problemas Críticos (se houver)
- **Problema**: Descrição clara
- **Localização**: Arquivo e número de linha
- **Impacto**: Por que isso importa
- **Severidade**: Crítico/Alto/Médio
- **Correção**: Exemplo de código

### Achados por Categoria

#### Segurança (se houver problemas)
Liste vulnerabilidades de segurança com exemplos

#### Desempenho (se houver problemas)
Liste problemas de desempenho com análise de complexidade

#### Qualidade (se houver problemas)
Liste problemas de qualidade de código com sugestões de refatoração

#### Manutenibilidade (se houver problemas)
Liste problemas de manutenibilidade com melhorias

## Histórico de Versões

- v1.0.0 (2024-12-10): Lançamento inicial com análise de segurança, desempenho, qualidade e manutenibilidade
