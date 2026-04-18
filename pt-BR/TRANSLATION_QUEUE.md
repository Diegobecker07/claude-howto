<!-- i18n-source: uk/TRANSLATION_QUEUE.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# Fila de Tradução em Português do Brasil

**Status geral:** ✅ concluído (100% — paridade com uk/)

**Objetivo:** organizar a tradução pt-BR por prioridade, mantendo a estrutura do guia clara para os demais workers.

## Prioridade 1 - Núcleo

| Arquivo | Status | Observação |
|---------|--------|------------|
| README.md | ✅ concluído | Tradução completa do README principal |
| INDEX.md | ✅ concluído | Linha a linha a partir do SHA 2deba3a |
| CATALOG.md | ✅ concluído | Linha a linha a partir do SHA 2deba3a |
| QUICK_REFERENCE.md | ✅ concluído | Linha a linha a partir do SHA 2deba3a |
| LEARNING-ROADMAP.md | ✅ concluído | Todos os níveis cobertos |

## Prioridade 2 - Módulos principais

| Pasta | Status | Observação |
|-------|--------|------------|
| 01-slash-commands/ | ✅ concluído | README + exemplos traduzidos |
| 02-memory/ | ✅ concluído | README + templates traduzidos |
| 03-skills/ | ✅ concluído | README + skills + catálogo de refatoração |
| 04-subagents/ | ✅ concluído | README + agentes traduzidos |
| 05-mcp/ | ✅ concluído | README + configs MCP (técnico: copiado verbatim) |
| 06-hooks/ | ✅ concluído | README + hooks (comentários/echos traduzidos) |
| 07-plugins/ | ✅ concluído | README + plugins (devops, documentation, pr-review) |
| 08-checkpoints/ | ✅ concluído | README + exemplos traduzidos |
| 09-advanced-features/ | ✅ concluído | README + exemplos traduzidos |
| 10-cli/ | ✅ concluído | README traduzido |

## Prioridade 3 - Exemplos e material de apoio

| Área | Status | Observação |
|------|--------|------------|
| Arquivos de suporte raiz | ✅ concluído | CLAUDE.md, CHANGELOG.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md, STYLE_GUIDE.md, clean-code-rules.md, RELEASE_NOTES.md, LICENSE (copiado) |
| resources.md | ✅ concluído | Recursos e guia de workflow |
| claude_concepts_guide.md | ✅ concluído | Guia completo de conceitos (84KB) |
| docs/ | ✅ concluído | ROADMAP-20260401.md + TASKS-20260401.md |
| prompts/ | ✅ concluído | remotion-video.md |
| resources/ | ✅ concluído | DESIGN-SYSTEM.md + QUICK-START.md + README.md |
| scripts/ | ✅ concluído | README.md (scripts Python/configs: copiados verbatim) |

## Observações operacionais

- Cada arquivo em `pt-BR/` começa com os metadados `i18n-*`
- O glossário em `TRANSLATION_NOTES.md` é a fonte de verdade para terminologia
- Diagramas Mermaid: preservados verbatim (rótulos técnicos em inglês)
- Código/comandos/URLs: preservados verbatim
- Configs JSON técnicos: copiados verbatim sem tradução
- Scripts Python/Shell: docstrings, comentários e mensagens de usuário traduzidos; código preservado
- Hooks JavaScript: comentários JSDoc e mensagens console.log/error traduzidos
- Nomes de comandos (frontmatter `name`): preservados como identificadores técnicos
- Descrições de comandos/agentes (frontmatter `description`): traduzidas
