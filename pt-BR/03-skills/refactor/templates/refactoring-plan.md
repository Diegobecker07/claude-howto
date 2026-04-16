<!-- i18n-source: 03-skills/refactor/templates/refactoring-plan.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Template de Plano de Refatoração

Use este template para documentar e acompanhar seu esforço de refatoração.

---

## Informações do Projeto

| Campo | Valor |
|-------|-------|
| **Projeto/Módulo** | [Nome do projeto] |
| **Arquivos Alvo** | [Lista de arquivos a refatorar] |
| **Data de Criação** | [Data] |
| **Autor** | [Nome] |
| **Status** | Rascunho / Em Revisão / Aprovado / Em Andamento / Concluído |

---

## Resumo Executivo

### Objetivos
- [ ] [Objetivo principal: ex., Melhorar legibilidade do processamento de pagamentos]
- [ ] [Objetivo secundário: ex., Reduzir duplicação de código]
- [ ] [Objetivo terciário: ex., Melhorar testabilidade]

### Restrições
- [ ] [Restrição 1: ex., Não pode alterar a API pública]
- [ ] [Restrição 2: ex., Deve manter compatibilidade retroativa]
- [ ] [Restrição 3: ex., Sem mudanças no schema do banco de dados]

### Nível de Risco
- [ ] Baixo — Mudanças menores, código bem testado
- [ ] Médio — Mudanças moderadas, algum risco
- [ ] Alto — Mudanças significativas, atenção cuidadosa necessária

---

## Checklist Pré-Refatoração

### Avaliação de Cobertura de Testes

| Métrica | Atual | Alvo | Status |
|---------|-------|------|--------|
| Cobertura de Testes Unitários | __%  | ≥80% | |
| Testes de Integração | Sim/Não | Sim | |
| Todos os Testes Passando | Sim/Não | Sim | |

### Necessário Antes de Começar
- [ ] Todos os testes passando
- [ ] Código revisado e compreendido
- [ ] Backup/controle de versão em vigor
- [ ] Aprovação do usuário obtida

---

## Code Smells Identificados

### Resumo

| # | Smell | Localização | Severidade | Prioridade |
|---|-------|-------------|------------|------------|
| 1 | [ex., Método Longo] | [arquivo:linha] | Alto | P1 |
| 2 | [ex., Código Duplicado] | [arquivo:linha] | Médio | P2 |
| 3 | [ex., Inveja de Recurso] | [arquivo:linha] | Baixo | P3 |

### Análise Detalhada

#### Smell #1: [Nome]

**Localização**: `caminho/para/arquivo.js:45-120`

**Descrição**: [Descrição detalhada do problema]

**Impacto**:
- [Impacto 1]
- [Impacto 2]

**Solução Proposta**: [Visão geral de como corrigir]

---

## Fases de Refatoração

### Fase A: Vitórias Rápidas (Baixo Risco)

**Objetivo**: Melhorias simples com valor imediato

**Mudanças Estimadas**: [X arquivos, Y métodos]

**Aprovação do Usuário Necessária**: Sim / Não

| # | Tarefa | Arquivo | Refatoração | Status |
|---|--------|---------|-------------|--------|
| A1 | Renomear variável `x` para `userCount` | utils.js:15 | Renomear Variável | [ ] |
| A2 | Remover `oldHandler()` não utilizado | api.js:89 | Remover Código Morto | [ ] |
| A3 | Extrair validação duplicada | form.js:23,67 | Extrair Método | [ ] |

**Plano de Rollback**: Reverter commits A1-A3

---

### Fase B: Melhorias Estruturais (Risco Médio)

**Objetivo**: Melhorar organização e clareza do código

**Mudanças Estimadas**: [X arquivos, Y métodos]

**Aprovação do Usuário Necessária**: Sim

**Dependências**: Fase A deve estar completa

| # | Tarefa | Arquivo | Refatoração | Status |
|---|--------|---------|-------------|--------|
| B1 | Extrair `calculatePrice()` de método longo | order.js:45 | Extrair Método | [ ] |
| B2 | Introduzir objeto de parâmetro `OrderDetails` | order.js:12 | Introduzir Objeto de Parâmetro | [ ] |
| B3 | Mover `formatAddress()` para classe Address | customer.js:78 | Mover Método | [ ] |

**Plano de Rollback**: Reverter para o commit pós-Fase-A

---

### Fase C: Mudanças Arquiteturais (Risco Maior)

**Objetivo**: Abordar problemas estruturais mais profundos

**Mudanças Estimadas**: [X arquivos, Y métodos]

**Aprovação do Usuário Necessária**: Sim

**Dependências**: Fases A e B devem estar completas

| # | Tarefa | Arquivo | Refatoração | Status |
|---|--------|---------|-------------|--------|
| C1 | Substituir switch de preços por polimorfismo | pricing.js:30 | Substituir Condicional por Polimorfismo | [ ] |
| C2 | Extrair classe `NotificationService` | user.js:100 | Extrair Classe | [ ] |

**Plano de Rollback**: Reverter para o commit pós-Fase-B

---

## Passos Detalhados de Refatoração

### Tarefa [ID]: [Nome da Tarefa]

**Smell Abordado**: [Nome do smell]

**Técnica de Refatoração**: [Nome da técnica]

**Nível de Risco**: Baixo / Médio / Alto

#### Contexto

**Antes** (Estado Atual):
```javascript
// Cole o código atual aqui
```

**Depois** (Estado Esperado):
```javascript
// Cole o código esperado aqui
```

#### Mecânica Passo a Passo

1. [ ] **Passo 1**: [Descrição]
   - Teste: Execute os testes após este passo
   - Esperado: Todos os testes passam

2. [ ] **Passo 2**: [Descrição]
   - Teste: Execute os testes após este passo
   - Esperado: Todos os testes passam

3. [ ] **Passo 3**: [Descrição]
   - Teste: Execute os testes após este passo
   - Esperado: Todos os testes passam

#### Verificação

- [ ] Todos os testes passando
- [ ] Comportamento inalterado
- [ ] Código compila
- [ ] Sem novos avisos

#### Mensagem de Commit
```
refactor: [Descreva a refatoração]
```

---

## Acompanhamento de Progresso

### Status das Fases

| Fase | Status | Iniciado | Concluído | Testes Passando |
|------|--------|----------|-----------|-----------------|
| A | Não Iniciado / Em Andamento / Concluído | | | |
| B | Não Iniciado / Em Andamento / Concluído | | | |
| C | Não Iniciado / Em Andamento / Concluído | | | |

### Problemas Encontrados

| # | Problema | Resolução | Status |
|---|----------|-----------|--------|
| 1 | [Descrição] | [Como foi resolvido] | Aberto / Resolvido |

---

## Comparação de Métricas

### Antes da Refatoração

| Métrica | Arquivo 1 | Arquivo 2 | Total |
|---------|-----------|-----------|-------|
| Linhas de Código | | | |
| Complexidade Ciclomática | | | |
| Índice de Manutenibilidade | | | |
| Número de Métodos | | | |
| Comprimento Médio de Método | | | |

### Depois da Refatoração

| Métrica | Arquivo 1 | Arquivo 2 | Total | Mudança |
|---------|-----------|-----------|-------|---------|
| Linhas de Código | | | | |
| Complexidade Ciclomática | | | | |
| Índice de Manutenibilidade | | | | |
| Número de Métodos | | | | |
| Comprimento Médio de Método | | | | |

---

## Checklist Pós-Refatoração

- [ ] Todos os testes passando
- [ ] Sem novos avisos ou erros
- [ ] Código compila com sucesso
- [ ] Verificação manual concluída
- [ ] Documentação atualizada (se necessário)
- [ ] Código revisado
- [ ] Métricas melhoradas
- [ ] Aprovação do usuário obtida

---

## Lições Aprendidas

### O que Funcionou Bem
- [Item 1]
- [Item 2]

### O que Pode Ser Melhorado
- [Item 1]
- [Item 2]

### Recomendações para o Futuro
- [Item 1]
- [Item 2]

---

## Aprovações

| Papel | Nome | Data | Assinatura |
|-------|------|------|------------|
| Autor do Plano | | | |
| Tech Lead | | | |
| Product Owner | | | |

---

## Apêndice

### A. Documentação Relacionada
- [Link para documentação relevante]

### B. Materiais de Referência
- [Link para catálogo de code smells]
- [Link para catálogo de refatorações]

### C. Ferramentas Utilizadas
- [Framework de testes]
- [Ferramentas de lint]
- [Ferramentas de análise de complexidade]
