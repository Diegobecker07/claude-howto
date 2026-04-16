<!-- i18n-source: 03-skills/refactor/SKILL.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: code-refactor
description: Refatoração sistemática de código baseada na metodologia de Martin Fowler. Usar quando usuários pedem para refatorar código, melhorar estrutura de código, reduzir dívida técnica, limpar código legado, eliminar code smells ou melhorar manutenibilidade. Esta skill guia através de uma abordagem em fases com pesquisa, planejamento e implementação incremental segura.
---

# Skill de Refatoração de Código

Uma abordagem sistemática para refatoração de código baseada em *Refactoring: Improving the Design of Existing Code* (2ª Edição) de Martin Fowler. Esta skill enfatiza mudanças seguras e incrementais respaldadas por testes.

> "Refatoração é o processo de alterar um sistema de software de tal forma que não muda o comportamento externo do código, mas melhora sua estrutura interna." — Martin Fowler

## Princípios Fundamentais

1. **Preservação de Comportamento**: O comportamento externo deve permanecer inalterado
2. **Pequenos Passos**: Fazer mudanças minúsculas e testáveis
3. **Orientado a Testes**: Os testes são a rede de segurança
4. **Contínuo**: Refatoração é contínua, não um evento único
5. **Colaborativo**: Aprovação do usuário necessária em cada fase

## Visão Geral do Fluxo de Trabalho

```
Fase 1: Pesquisa e Análise
    ↓
Fase 2: Avaliação de Cobertura de Testes
    ↓
Fase 3: Identificação de Code Smells
    ↓
Fase 4: Criação do Plano de Refatoração
    ↓
Fase 5: Implementação Incremental
    ↓
Fase 6: Revisão e Iteração
```

---

## Fase 1: Pesquisa e Análise

### Objetivos
- Entender a estrutura e propósito do código-fonte
- Identificar o escopo da refatoração
- Coletar contexto sobre requisitos de negócio

### Perguntas a Fazer ao Usuário
Antes de começar, esclareça:

1. **Escopo**: Quais arquivos/módulos/funções precisam ser refatorados?
2. **Objetivos**: Quais problemas você está tentando resolver? (legibilidade, desempenho, manutenibilidade)
3. **Restrições**: Há áreas que NÃO devem ser alteradas?
4. **Pressão de prazo**: Isso está bloqueando outro trabalho?
5. **Status dos testes**: Existem testes? Estão passando?

### Ações
- [ ] Ler e entender o código-alvo
- [ ] Identificar dependências e integrações
- [ ] Documentar a arquitetura atual
- [ ] Anotar marcadores de dívida técnica existentes (TODOs, FIXMEs)

### Saída
Apresente os resultados ao usuário:
- Resumo da estrutura do código
- Áreas problemáticas identificadas
- Recomendações iniciais
- **Solicite aprovação para prosseguir**

---

## Fase 2: Avaliação de Cobertura de Testes

### Por que os Testes Importam
> "Refatoração sem testes é como dirigir sem cinto de segurança." — Martin Fowler

Os testes são o **habilitador-chave** de refatoração segura. Sem eles, você arrisca introduzir bugs.

### Passos de Avaliação

1. **Verificar testes existentes**
   ```bash
   # Procurar por arquivos de teste
   find . -name "*test*" -o -name "*spec*" | head -20
   ```

2. **Executar os testes existentes**
   ```bash
   # JavaScript/TypeScript
   npm test

   # Python
   pytest -v

   # Java
   mvn test
   ```

3. **Verificar cobertura (se disponível)**
   ```bash
   # JavaScript
   npm run test:coverage

   # Python
   pytest --cov=.
   ```

### Ponto de Decisão: Perguntar ao Usuário

**Se os testes existem e passam:**
- Prossiga para a Fase 3

**Se os testes estão faltando ou incompletos:**
Apresente opções:
1. Escrever testes primeiro (recomendado)
2. Adicionar testes incrementalmente durante a refatoração
3. Prosseguir sem testes (arriscado — requer reconhecimento do usuário)

**Se os testes estão falhando:**
- PARE. Corrija os testes que falham antes de refatorar
- Pergunte ao usuário: Devemos corrigir os testes primeiro?

### Diretrizes para Escrita de Testes (se necessário)

Para cada função sendo refatorada, garanta que os testes cubram:
- Caminho feliz (operação normal)
- Casos extremos (entradas vazias, nulas, limites)
- Cenários de erro (entradas inválidas, exceções)

Use o ciclo "vermelho-verde-refatorar":
1. Escreva o teste que falha (vermelho)
2. Faça-o passar (verde)
3. Refatore

---

## Fase 3: Identificação de Code Smells

### O que São Code Smells?
Sintomas de problemas mais profundos no código. Não são bugs, mas indicadores de que o código pode ser melhorado.

### Code Smells Comuns a Verificar

Veja [references/code-smells.md](references/code-smells.md) para o catálogo completo.

#### Referência Rápida

| Smell | Sinais | Impacto |
|-------|--------|---------|
| **Método Longo** | Métodos > 30-50 linhas | Difícil de entender, testar, manter |
| **Código Duplicado** | Mesma lógica em vários lugares | Correções necessárias em múltiplos lugares |
| **Classe Grande** | Classe com muitas responsabilidades | Viola Responsabilidade Única |
| **Inveja de Recurso** | Método usa mais dados de outra classe | Encapsulamento ruim |
| **Obsessão por Primitivos** | Uso excessivo de primitivos em vez de objetos | Conceitos de domínio ausentes |
| **Lista Longa de Parâmetros** | Métodos com 4+ parâmetros | Difícil de chamar corretamente |
| **Aglomerados de Dados** | Mesmos itens de dados aparecendo juntos | Abstração ausente |
| **Instruções Switch** | Cadeias complexas de switch/if-else | Difícil de estender |
| **Generalidade Especulativa** | Código "por precaução" | Complexidade desnecessária |
| **Código Morto** | Código não utilizado | Confusão, carga de manutenção |

### Passos de Análise

1. **Análise Automatizada** (se scripts disponíveis)
   ```bash
   python scripts/detect-smells.py <arquivo>
   ```

2. **Revisão Manual**
   - Percorra o código sistematicamente
   - Anote cada smell com localização e severidade
   - Categorize por impacto (Crítico/Alto/Médio/Baixo)

3. **Priorização**
   Foque em smells que:
   - Bloqueiam o desenvolvimento atual
   - Causam bugs ou confusão
   - Afetam os caminhos de código mais alterados

### Saída: Relatório de Smells

Apresente ao usuário:
- Lista de smells identificados com localizações
- Avaliação de severidade para cada um
- Ordem de prioridade recomendada
- **Solicite aprovação nas prioridades**

---

## Fase 4: Criação do Plano de Refatoração

### Selecionando Refatorações

Para cada smell, selecione uma refatoração apropriada do catálogo.

Veja [references/refactoring-catalog.md](references/refactoring-catalog.md) para a lista completa.

#### Mapeamento Smell → Refatoração

| Code Smell | Refatoração(ões) Recomendada(s) |
|------------|----------------------------------|
| Método Longo | Extrair Método, Substituir Temporária por Query |
| Código Duplicado | Extrair Método, Subir Método, Formar Template Method |
| Classe Grande | Extrair Classe, Extrair Subclasse |
| Inveja de Recurso | Mover Método, Mover Campo |
| Obsessão por Primitivos | Substituir Primitivo por Objeto, Substituir Tipo por Classe |
| Lista Longa de Parâmetros | Introduzir Objeto de Parâmetro, Preservar Objeto Inteiro |
| Aglomerados de Dados | Extrair Classe, Introduzir Objeto de Parâmetro |
| Instruções Switch | Substituir Condicional por Polimorfismo |
| Generalidade Especulativa | Recolher Hierarquia, Internalizar Classe, Remover Código Morto |
| Código Morto | Remover Código Morto |

### Estrutura do Plano

Use o template em [templates/refactoring-plan.md](templates/refactoring-plan.md).

Para cada refatoração:
1. **Alvo**: Qual código será alterado
2. **Smell**: Qual problema está sendo abordado
3. **Refatoração**: Qual técnica aplicar
4. **Passos**: Micro-passos detalhados
5. **Riscos**: O que pode dar errado
6. **Rollback**: Como desfazer se necessário

### Abordagem em Fases

**CRÍTICO**: Introduza a refatoração gradualmente em fases.

**Fase A: Vitórias Rápidas** (Baixo risco, alto valor)
- Renomear variáveis para clareza
- Extrair código duplicado óbvio
- Remover código morto

**Fase B: Melhorias Estruturais** (Risco médio)
- Extrair métodos de funções longas
- Introduzir objetos de parâmetro
- Mover métodos para classes apropriadas

**Fase C: Mudanças Arquiteturais** (Risco maior)
- Substituir condicionais por polimorfismo
- Extrair classes
- Introduzir padrões de projeto

### Ponto de Decisão: Apresentar Plano ao Usuário

Antes da implementação:
- Mostre o plano completo de refatoração
- Explique cada fase e seus riscos
- Obtenha aprovação explícita para cada fase
- **Pergunte**: "Devo prosseguir com a Fase A?"

---

## Fase 5: Implementação Incremental

### A Regra de Ouro
> "Mudança → Teste → Verde? → Commit → Próximo passo"

### Ritmo de Implementação

Para cada passo de refatoração:

1. **Pré-verificação**
   - Testes estão passando (verde)
   - Código compila

2. **Faça UMA pequena mudança**
   - Siga as mecânicas do catálogo
   - Mantenha as mudanças mínimas

3. **Verifique**
   - Execute os testes imediatamente
   - Verifique erros de compilação

4. **Se os testes passam (verde)**
   - Commit com mensagem descritiva
   - Passe para o próximo passo

5. **Se os testes falham (vermelho)**
   - PARE imediatamente
   - Desfaça a mudança
   - Analise o que deu errado
   - Pergunte ao usuário se não estiver claro

### Estratégia de Commits

Cada commit deve ser:
- **Atômico**: Uma mudança lógica
- **Reversível**: Fácil de reverter
- **Descritivo**: Mensagem de commit clara

Exemplos de mensagens de commit:
```
refactor: Extrair calculateTotal() de processOrder()
refactor: Renomear 'x' para 'customerCount' por clareza
refactor: Remover método validateOldFormat() não utilizado
```

### Relatório de Progresso

Após cada sub-fase, reporte ao usuário:
- Mudanças feitas
- Testes ainda passando?
- Algum problema encontrado
- **Pergunte**: "Continuar com o próximo lote?"

---

## Fase 6: Revisão e Iteração

### Checklist Pós-Refatoração

- [ ] Todos os testes passando
- [ ] Sem novos avisos/erros
- [ ] Código compila com sucesso
- [ ] Comportamento inalterado (verificação manual)
- [ ] Documentação atualizada se necessário
- [ ] Histórico de commits está limpo

### Comparação de Métricas

Execute análise de complexidade antes e depois:
```bash
python scripts/analyze-complexity.py <arquivo>
```

Apresente melhorias:
- Mudança nas linhas de código
- Mudança na complexidade ciclomática
- Mudança no índice de manutenibilidade

### Revisão do Usuário

Apresente os resultados finais:
- Resumo de todas as mudanças
- Comparação antes/depois do código
- Melhorias de métricas
- Dívida técnica restante
- **Pergunte**: "Você está satisfeito com essas mudanças?"

### Próximos Passos

Discuta com o usuário:
- Outros smells a abordar?
- Agendar refatoração de acompanhamento?
- Aplicar mudanças similares em outros lugares?

---

## Diretrizes Importantes

### Quando PARAR e Perguntar

Sempre pause e consulte o usuário quando:
- Não tiver certeza sobre lógica de negócio
- A mudança pode afetar APIs externas
- A cobertura de testes é inadequada
- Uma decisão arquitetural significativa é necessária
- O nível de risco aumenta
- Você encontra complexidade inesperada

### Regras de Segurança

1. **Nunca refatore sem testes** (a menos que o usuário reconheça explicitamente o risco)
2. **Nunca faça grandes mudanças** — divida em passos minúsculos
3. **Nunca pule a execução dos testes** após cada mudança
4. **Nunca continue se os testes falham** — corrija ou faça rollback primeiro
5. **Nunca assuma** — na dúvida, pergunte

### O que NÃO Fazer

- Não combine refatoração com adição de funcionalidades
- Não refatore durante emergências de produção
- Não refatore código que você não entende
- Não engenheirice demais — mantenha simples
- Não refatore tudo de uma vez

---

## Exemplo de Início Rápido

### Cenário: Método Longo com Duplicação

**Antes:**
```javascript
function processOrder(order) {
  // 150 linhas de código com:
  // - Lógica de validação duplicada
  // - Cálculos inline
  // - Responsabilidades misturadas
}
```

**Passos de Refatoração:**

1. **Garanta que existem testes** para processOrder()
2. **Extraia** a validação para validateOrder()
3. **Teste** — deve passar
4. **Extraia** o cálculo para calculateOrderTotal()
5. **Teste** — deve passar
6. **Extraia** a notificação para notifyCustomer()
7. **Teste** — deve passar
8. **Revise** — processOrder() agora orquestra 3 funções claras

**Depois:**
```javascript
function processOrder(order) {
  validateOrder(order);
  const total = calculateOrderTotal(order);
  notifyCustomer(order, total);
  return { order, total };
}
```

---

## Referências

- [Catálogo de Code Smells](references/code-smells.md) - Lista completa de code smells
- [Catálogo de Refatorações](references/refactoring-catalog.md) - Técnicas de refatoração
- [Template de Plano de Refatoração](templates/refactoring-plan.md) - Template de planejamento

## Scripts

- `scripts/analyze-complexity.py` - Analisar métricas de complexidade do código
- `scripts/detect-smells.py` - Detecção automatizada de smells

## Histórico de Versões

- v1.0.0 (2025-01-15): Lançamento inicial com metodologia Fowler, abordagem em fases, pontos de consulta ao usuário
