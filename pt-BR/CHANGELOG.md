<!-- i18n-source: CHANGELOG.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# Changelog

## v2.3.0 — 2026-04-07

### Funcionalidades

- build e publicação de artefatos EPUB por idioma (90e9c30) @Thiên Toán
- adicionar hook pre-tool-check.sh ausente em 06-hooks (b511ed1) @JiayuWang
- adicionar traduções para Chinês no diretório zh/ (89e89d4) @Luong NGUYEN
- Adicionar subagente performance-optimizer e hook dependency-check (f53d080) @qk

### Correções de Bugs

- Compatibilidade com Windows Git Bash + protocolo JSON stdin (2cbb10c) @Luong NGUYEN
- corrigir documentação de configuração autoCheckpoint em 08-checkpoints (749c79f) @JiayuWang
- incorporar imagens SVG em vez de substituir por placeholders (1b16709) @Thiên Toán
- renderização de code fence aninhado no README de memória (ce24423) @Zhaoshan Duan
- aplicar correções de revisão perdidas por squash merge (34259ca) @Luong NGUYEN
- tornar scripts de hook compatíveis com Windows Git Bash e usar protocolo JSON stdin (107153d) @binyu li

### Documentação

- sincronizar todos os tutoriais com os docs mais recentes do Claude Code (Abril 2026) (72d3b01) @Luong NGUYEN
- adicionar link do idioma Chinês ao seletor de idioma (6cbaa4d) @Luong NGUYEN
- adicionar seletor de idioma entre Inglês e Vietnamita (100c45e) @Luong NGUYEN
- adicionar badge GitHub #1 Trending (0ca8c37) @Luong NGUYEN
- Apresentar cc-context-stats para monitoramento de zona de contexto (d41b335) @Luong NGUYEN
- Apresentar coleção luongnv89/skills e gerenciador de skills luongnv89/asm (7e3c0b6) @Luong NGUYEN
- Atualizar estatísticas do README para refletir métricas atuais do GitHub (5.900+ estrelas, 690+ forks) (5001525) @Luong NGUYEN
- Atualizar estatísticas do README para refletir métricas atuais do GitHub (3.900+ estrelas, 460+ forks) (9cb92d6) @Luong NGUYEN

### Refatoração

- substituir dependência HTTP Kroki por renderização local mmdc (e76bbe4) @Luong NGUYEN
- mover verificações de qualidade para pré-commit, CI como 2ª passagem (6d1e0ae) @Luong NGUYEN
- restringir baseline de permissões do modo auto (2790fb2) @Luong NGUYEN
- Substituir hook auto-adapt por script de configuração única de permissões (995a5d6) @Luong NGUYEN

### Outros

- gates de qualidade shift-left — adicionar mypy ao pré-commit, corrigir falhas de CI (699fb39) @Luong NGUYEN
- Adicionar Localização para Vietnamita (Tiếng Việt) (a70777e) @Thiên Toán

**Changelog Completo**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — 2026-03-26

### Documentação

- Sincronizar todos os tutoriais e referências com Claude Code v2.1.84 (f78c094) @luongnv89
  - Atualizar slash commands para 55+ built-in + 5 skills em pacote, marcar 3 como depreciados
  - Expandir eventos de hook de 18 para 25, adicionar tipo de hook `agent` (agora 4 tipos)
  - Adicionar Modo Auto, Canais, Ditado por Voz em recursos avançados
  - Adicionar campos `effort`, `shell` no frontmatter de skill; campos `initialPrompt`, `disallowedTools` em agente
  - Adicionar transporte MCP WebSocket, elicitação, limite de ferramenta de 2KB
  - Adicionar suporte LSP de plugin, `userConfig`, `${CLAUDE_PLUGIN_DATA}`
  - Atualizar todos os docs de referência (CATALOG, QUICK_REFERENCE, LEARNING-ROADMAP, INDEX)
- Reescrever README como guia estruturado de landing page (32a0776) @luongnv89

### Correções de Bugs

- Adicionar palavras ausentes ao cSpell e seções do README para conformidade com CI (93f9d51) @luongnv89
- Adicionar `Sandboxing` ao dicionário cSpell (b80ce6f) @luongnv89

**Changelog Completo**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Correções de Bugs

- Remover link morto do marketplace que falha nas verificações de link do CI (3fdf0d6) @luongnv89
- Adicionar `sandboxed` e `pycache` ao dicionário cSpell (dc64618) @luongnv89

**Changelog Completo**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### Funcionalidades

- Adicionar caminho de aprendizado adaptativo com skills de autoavaliação e quiz de lição (1ef46cd) @luongnv89
  - `/self-assessment` — quiz interativo de proficiência em 10 áreas de recursos com caminho de aprendizado personalizado
  - `/lesson-quiz [lesson]` — verificação de conhecimento por lição com 8-10 perguntas direcionadas

### Correções de Bugs

- Atualizar URLs quebradas, depreciações e referências desatualizadas (8fe4520) @luongnv89
- Corrigir links quebrados em recursos e skill de autoavaliação (7a05863) @luongnv89
- Usar fences com til para blocos de código aninhados no guia de conceitos (5f82719) @VikalpP
- Adicionar palavras ausentes ao dicionário cSpell (8df7572) @luongnv89

### Documentação

- QA Fase 5 — corrigir consistência, URLs e terminologia nos docs (00bbe4c) @luongnv89
- Concluir Fases 3-4 — nova cobertura de recursos e atualizações de docs de referência (132de29) @luongnv89
- Adicionar runtime MCPorter à seção de context bloat do MCP (ef52705) @luongnv89
- Adicionar comandos, recursos e configurações ausentes em 6 guias (4bc8f15) @luongnv89
- Adicionar guia de estilo baseado nas convenções existentes do repositório (84141d0) @luongnv89
- Adicionar linha de autoavaliação à tabela de comparação de guias (8fe0c96) @luongnv89
- Adicionar VikalpP à lista de colaboradores pelo PR #7 (d5b4350) @luongnv89
- Adicionar referências às skills de autoavaliação e lesson-quiz ao README e roadmap (d5a6106) @luongnv89

### Novos Colaboradores

- @VikalpP fez sua primeira contribuição no #7

**Changelog Completo**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### Funcionalidades

- Sincronizar toda a documentação com os recursos do Claude Code de Fevereiro de 2026 (487c96d)
  - Atualizar 26 arquivos em todos os 10 diretórios de tutoriais e 7 documentos de referência
  - Adicionar documentação para **Auto Memory** — aprendizados persistentes por projeto
  - Adicionar documentação para **Remote Control**, **Web Sessions** e **Desktop App**
  - Adicionar documentação para **Agent Teams** (colaboração multi-agente experimental)
  - Adicionar documentação para **MCP OAuth 2.0**, **Tool Search** e **Claude.ai Connectors**
  - Adicionar documentação para **Persistent Memory** e **Worktree Isolation** para subagentes
  - Adicionar documentação para **Background Subagents**, **Task List**, **Prompt Suggestions**
  - Adicionar documentação para **Sandboxing** e **Managed Settings** (Enterprise)
  - Adicionar documentação para **HTTP Hooks** e 7 novos eventos de hook
  - Adicionar documentação para **Plugin Settings**, **LSP Servers** e atualizações do Marketplace
  - Adicionar documentação para a opção de retrocesso **Summarize from Checkpoint**
  - Documentar 17 novos slash commands (`/fork`, `/desktop`, `/teleport`, `/tasks`, `/fast`, etc.)
  - Documentar novos flags CLI (`--worktree`, `--from-pr`, `--remote`, `--teleport`, `--teammate-mode`, etc.)
  - Documentar novas variáveis de ambiente para auto memory, níveis de esforço, equipes de agentes e mais

### Design

- Redesenhar logo para marca de compasso-colchete com paleta mínima (20779db)

### Correções de Bugs / Correções

- Atualizar nomes de modelos: Sonnet 4.5 → **Sonnet 4.6**, Opus 4.5 → **Opus 4.6**
- Corrigir nomes de modos de permissão: substituir "Unrestricted/Confirm/Read-only" fictícios pelo `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions` reais
- Corrigir eventos de hook: remover `PreCommit`/`PostCommit`/`PrePush` fictícios, adicionar eventos reais (`SubagentStart`, `WorktreeCreate`, `ConfigChange`, etc.)
- Corrigir sintaxe CLI: substituir `claude-code --headless` por `claude -p` (modo print)
- Corrigir comandos de checkpoint: substituir `/checkpoint save/list/rewind/diff` fictícios pela interface real `Esc+Esc` / `/rewind`
- Corrigir gerenciamento de sessão: substituir `/session list/new/switch/save` fictícios pelo `/resume`/`/rename`/`/fork` reais
- Corrigir formato do manifesto de plugin: migrar `plugin.yaml` → `.claude-plugin/plugin.json`
- Corrigir caminhos de config MCP: `~/.claude/mcp.json` → `.mcp.json` (projeto) / `~/.claude.json` (usuário)
- Corrigir URLs de documentação: `docs.claude.com` → `docs.anthropic.com`; remover `plugins.claude.com` fictício
- Remover campos de configuração fictícios em múltiplos arquivos
- Atualizar todas as datas "Last Updated" para Fevereiro de 2026

**Changelog Completo**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
