<!-- i18n-source: uk/TRANSLATION_QUEUE.md -->
<!-- i18n-source-sha: 8438a03 -->
<!-- i18n-date: 2026-04-14 -->

# Fila de Tradução em Português do Brasil

**Status geral:** em preparação

**Objetivo:** organizar a tradução pt-BR por prioridade, mantendo a estrutura do guia clara para os demais workers.

## Prioridade 1 - Núcleo

| Arquivo | Status | Observação |
|---------|--------|------------|
| README.md | pendente | Porta de entrada da tradução |
| INDEX.md | pendente | Índice principal do guia |
| CATALOG.md | pendente | Catálogo de recursos |
| QUICK_REFERENCE.md | pendente | Referência rápida |
| LEARNING-ROADMAP.md | pendente | Roteiro de aprendizado |

## Prioridade 2 - Módulos principais

| Pasta | Status | Observação |
|-------|--------|------------|
| 01-slash-commands/ | pendente | Comandos slash |
| 02-memory/ | pendente | Memória e contexto |
| 03-skills/ | pendente | Skills reutilizáveis |
| 04-subagents/ | pendente | Agentes especializados |
| 05-mcp/ | pendente | Configurações MCP |
| 06-hooks/ | pendente | Hooks e automação |
| 07-plugins/ | pendente | Pacotes de plugin |
| 08-checkpoints/ | pendente | Checkpoints |
| 09-advanced-features/ | pendente | Recursos avançados |
| 10-cli/ | pendente | Referência da CLI |

## Prioridade 3 - Exemplos e material de apoio

| Área | Status | Observação |
|------|--------|------------|
| Exemplos de comandos | pendente | Traduzir só a explicação, nunca o comando |
| Templates e modelos | pendente | Manter trechos reutilizáveis alinhados ao glossário |
| Arquivos de suporte | pendente | Rever antes de copiar para `pt-BR/` |

## Observações operacionais

- Cada arquivo novo em `pt-BR/` deve começar com os metadados `i18n-*`
- O glossário em `TRANSLATION_NOTES.md` é a fonte de verdade para terminologia
- Se um worker precisar de contexto adicional, ele deve atualizar esta fila em vez de espalhar notas em arquivos soltos
