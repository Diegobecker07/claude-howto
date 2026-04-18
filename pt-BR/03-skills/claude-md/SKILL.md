<!-- i18n-source: 03-skills/claude-md/SKILL.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: claude-md
description: Criar ou atualizar arquivos CLAUDE.md seguindo boas práticas para integração ideal de agentes de IA
---

## Entrada do Usuário

```text
$ARGUMENTS
```

Você **DEVE** considerar a entrada do usuário antes de prosseguir (se não estiver vazia). O usuário pode especificar:
- `create` - Criar novo CLAUDE.md do zero
- `update` - Melhorar CLAUDE.md existente
- `audit` - Analisar e relatar sobre a qualidade do CLAUDE.md atual
- Um caminho específico para criar/atualizar (ex: `src/api/CLAUDE.md` para instruções específicas de diretório)

## Princípios Fundamentais

**LLMs são sem estado**: CLAUDE.md é o único arquivo incluído automaticamente em cada conversa. Ele serve como o documento principal de integração de agentes de IA ao seu código-fonte.

### As Regras de Ouro

1. **Menos é Mais**: LLMs de ponta conseguem seguir ~150-200 instruções. O prompt de sistema do Claude Code já usa ~50. Mantenha seu CLAUDE.md focado e conciso.

2. **Aplicabilidade Universal**: Inclua apenas informações relevantes para TODAS as sessões. Instruções específicas de tarefas pertencem a arquivos separados.

3. **Não Use Claude como Linter**: Diretrizes de estilo inchão o contexto e degradam o seguimento de instruções. Use ferramentas determinísticas (prettier, eslint, etc.) em vez disso.

4. **Nunca Gere Automaticamente**: CLAUDE.md é o ponto de maior alavancagem do conjunto de IA. Crie-o manualmente com consideração cuidadosa.

## Fluxo de Execução

### 1. Análise do Projeto

Primeiro, analise o estado atual do projeto:

1. Verifique arquivos CLAUDE.md existentes:
   - Nível raiz: `./CLAUDE.md` ou `.claude/CLAUDE.md`
   - Específico de diretório: `**/CLAUDE.md`
   - Config global do usuário: `~/.claude/CLAUDE.md`

2. Identifique a estrutura do projeto:
   - Stack tecnológica (linguagens, frameworks)
   - Tipo de projeto (monorepo, app único, biblioteca)
   - Ferramentas de desenvolvimento (gerenciador de pacotes, sistema de build, executor de testes)

3. Revise a documentação existente:
   - README.md
   - CONTRIBUTING.md
   - package.json, pyproject.toml, Cargo.toml, etc.

### 2. Estratégia de Conteúdo (O QUÊ, POR QUÊ, COMO)

Estruture o CLAUDE.md em torno de três dimensões:

#### O QUÊ - Tecnologia e Estrutura
- Visão geral da stack tecnológica
- Organização do projeto (especialmente importante para monorepos)
- Diretórios-chave e seus propósitos

#### POR QUÊ - Propósito e Contexto
- O que o projeto faz
- Por que certas decisões arquiteturais foram tomadas
- Para que cada componente principal é responsável

#### COMO - Fluxo de Trabalho e Convenções
- Fluxo de trabalho de desenvolvimento (bun vs node, pip vs uv, etc.)
- Procedimentos e comandos de teste
- Métodos de verificação e build
- "Armadilhas" críticas ou requisitos não óbvios

### 3. Estratégia de Divulgação Progressiva

Para projetos maiores, recomende criar uma pasta `agent_docs/`:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

No CLAUDE.md, referencie esses arquivos com instruções como:
```markdown
Para instruções detalhadas de build, consulte `agent_docs/building_the_project.md`
```

**Importante**: Use referências `arquivo:linha` em vez de trechos de código para evitar contexto desatualizado.

### 4. Restrições de Qualidade

Ao criar ou atualizar CLAUDE.md:

1. **Tamanho-Alvo**: Menos de 300 linhas (idealmente menos de 100)
2. **Sem Regras de Estilo**: Remova quaisquer instruções de lint/formatação
3. **Sem Instruções Específicas de Tarefa**: Mova para arquivos separados
4. **Sem Trechos de Código**: Use referências de arquivo em vez disso
5. **Sem Informação Redundante**: Não repita o que está em package.json ou README

### 5. Seções Essenciais

Um CLAUDE.md bem estruturado deve incluir:

```markdown
# Nome do Projeto

Descrição breve em uma linha.

## Stack Tecnológica
- Linguagem principal e versão
- Frameworks/bibliotecas-chave
- Banco de dados/armazenamento (se houver)

## Estrutura do Projeto
[Apenas para monorepos ou estruturas complexas]
- `apps/` - Pontos de entrada das aplicações
- `packages/` - Bibliotecas compartilhadas

## Comandos de Desenvolvimento
- Instalar: `comando`
- Testar: `comando`
- Build: `comando`

## Convenções Críticas
[Apenas convenções não óbvias e de alto impacto]
- Convenção 1 com breve explicação
- Convenção 2 com breve explicação

## Problemas Conhecidos / Armadilhas
[Coisas que consistentemente confundem os desenvolvedores]
- Problema 1
- Problema 2
```

### 6. Anti-Padrões a Evitar

**NÃO inclua:**
- Diretrizes de estilo de código (use linters)
- Documentação sobre como usar Claude
- Explicações longas de padrões óbvios
- Exemplos de código copiados e colados
- Boas práticas genéricas ("escreva código limpo")
- Instruções para tarefas específicas
- Conteúdo gerado automaticamente
- Listas extensas de TODOs

### 7. Checklist de Validação

Antes de finalizar, verifique:

- [ ] Menos de 300 linhas (preferencialmente menos de 100)
- [ ] Cada linha se aplica a TODAS as sessões
- [ ] Sem regras de estilo/formatação
- [ ] Sem trechos de código (use referências de arquivo)
- [ ] Comandos verificados para funcionar
- [ ] Divulgação progressiva usada para projetos complexos
- [ ] Armadilhas críticas documentadas
- [ ] Sem redundância com README.md

## Formato de Saída

### Para `create` ou padrão:

1. Analise o projeto
2. Escreva um rascunho de CLAUDE.md seguindo a estrutura acima
3. Apresente o rascunho para revisão
4. Escreva no local apropriado após aprovação

### Para `update`:

1. Leia o CLAUDE.md existente
2. Audite em relação às boas práticas
3. Identifique:
   - Conteúdo a remover (regras de estilo, trechos de código, específico de tarefa)
   - Conteúdo a condensar
   - Informações essenciais faltando
4. Apresente as alterações para revisão
5. Aplique as alterações após aprovação

### Para `audit`:

1. Leia o CLAUDE.md existente
2. Gere um relatório com:
   - Contagem de linhas atual vs. alvo
   - Percentual de conteúdo universalmente aplicável
   - Lista de anti-padrões encontrados
   - Recomendações de melhoria
3. NÃO modifique o arquivo, apenas reporte

## Tratamento de AGENTS.md

Se o usuário solicitar criação/atualização de AGENTS.md:

AGENTS.md é usado para definir comportamentos especializados de agentes. Ao contrário do CLAUDE.md (que é para contexto do projeto), AGENTS.md define:
- Papéis e capacidades de agentes personalizados
- Instruções e restrições específicas de agentes
- Definições de fluxo de trabalho para cenários multi-agente

Aplique princípios similares:
- Mantenha focado e conciso
- Use divulgação progressiva
- Referencie documentos externos em vez de incorporar conteúdo

## Notas

- Sempre verifique se os comandos funcionam antes de incluí-los
- Na dúvida, deixe de fora — menos é mais
- O lembrete do sistema diz ao Claude que CLAUDE.md "pode ou não ser relevante" — quanto mais ruído, mais ele é ignorado
- Monorepos se beneficiam mais da estrutura clara O QUÊ/POR QUÊ/COMO
- Arquivos CLAUDE.md específicos de diretório devem ser ainda mais focados
