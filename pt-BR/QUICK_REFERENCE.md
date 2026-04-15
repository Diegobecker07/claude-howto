<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: 9c224ff -->
<!-- i18n-date: 2026-04-14 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - Cartão de Referência Rápida

## 🚀 Comandos Rápidos de Instalação

### Slashes

```bash
# Instalar todos
cp 01-slash-commands/*.md .claude/commands/

# Instalar um específico
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memória

```bash
# Memória do projeto
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Memória pessoal
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills

```bash
# Skills pessoais
cp -r 03-skills/code-review ~/.claude/skills/

# Skills do projeto
cp -r 03-skills/code-review .claude/skills/
```

### Subagentes

```bash
# Instalar todos
cp 04-subagents/*.md .claude/agents/

# Instalar um específico
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP

```bash
# Definir credenciais
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Instalar a configuração (escopo do projeto)
cp 05-mcp/github-mcp.json .mcp.json

# Ou no escopo do usuário: adicionar em ~/.claude.json
```

### Hooks

```bash
# Instalar hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configurar em settings (~/.claude/settings.json)
```

### Plugins

```bash
# Instalar a partir dos exemplos (se estiverem publicados)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints

```bash
# Checkpoints são criados automaticamente a cada prompt do usuário
# Para voltar, pressione Esc duas vezes ou use:
/rewind

# Depois escolha: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, ou Never mind
```

### Recursos Avançados

```bash
# Configurar em settings (.claude/settings.json)
# Veja 09-advanced-features/config-examples.json

# Modo de planejamento
/plan Task description

# Modos de permissão (use a flag --permission-mode)
# default        - pede aprovação para ações arriscadas
# acceptEdits    - aceita edições automaticamente, pede para as demais
# plan           - análise somente leitura, sem modificações
# dontAsk        - aceita tudo, exceto ações arriscadas
# auto           - o classificador de fundo decide permissões automaticamente
# bypassPermissions - aceita tudo (requer --dangerously-skip-permissions)

# Gerenciamento de sessão
/resume                # Retomar uma conversa anterior
/rename "name"         # Dar nome à sessão atual
/fork                  # Criar uma ramificação da sessão
claude -c              # Continuar a conversa mais recente
claude -r "session"    # Retomar sessão por nome/ID
```

---

## 📋 Resumo das Funcionalidades

| Funcionalidade | Caminho de Instalação | Uso |
|---------|------------------|-------------|
| **Slash Commands (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Memória** | `./CLAUDE.md` | Carregamento automático |
| **Skills** | `.claude/skills/*/SKILL.md` | Auto-invocadas |
| **Subagentes** | `.claude/agents/*.md` | Delegação automática |
| **MCP** | `.mcp.json` (projeto) ou `~/.claude.json` (usuário) | `/mcp__server__action` |
| **Hooks (25 eventos)** | `~/.claude/hooks/*.sh` | Disparados por evento (4 tipos) |
| **Plugins** | Via `/plugin install` | Pacote completo |
| **Checkpoints** | Integrado | `Esc+Esc` ou `/rewind` |
| **Modo de Planejamento** | Integrado | `/plan <task>` |
| **Modos de Permissão (6)** | Integrado | `--allowedTools`, `--permission-mode` |
| **Sessões** | Integrado | `/session <command>` |
| **Tarefas em Segundo Plano** | Integrado | Executar em background |
| **Controle Remoto** | Integrado | API via WebSocket |
| **Sessões Web** | Integrado | `claude web` |
| **Git Worktrees** | Integrado | `/worktree` |
| **Auto Memory** | Integrado | Auto-salva em CLAUDE.md |
| **Lista de Tarefas** | Integrado | `/task list` |
| **Skills Integradas (5)** | Integrado | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 Casos de Uso Comuns

### Revisão de Código
```bash
# Método 1: Slash command
cp 01-slash-commands/optimize.md .claude/commands/
# Uso: /optimize

# Método 2: Subagente
cp 04-subagents/code-reviewer.md .claude/agents/
# Uso: Delegação automática

# Método 3: Skill
cp -r 03-skills/code-review ~/.claude/skills/
# Uso: Auto-invocada

# Método 4: Plugin (melhor opção)
/plugin install pr-review
# Uso: /review-pr
```

### Documentação
```bash
# Slash command
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Subagente
cp 04-subagents/documentation-writer.md .claude/agents/

# Skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Plugin (solução completa)
/plugin install documentation
```

### DevOps
```bash
# Plugin completo
/plugin install devops-automation

# Comandos: /deploy, /rollback, /status, /incident
```

### Padrões da Equipe
```bash
# Memória do projeto
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Edite conforme a sua equipe
vim CLAUDE.md
```

### Automação e Hooks
```bash
# Instalar hooks (25 eventos, 4 tipos: command, http, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Exemplos:
# - Testes antes do commit: pre-commit.sh
# - Autoformatação de código: format-code.sh
# - Verificação de segurança: security-scan.sh

# Auto Mode para fluxos totalmente autônomos
claude --enable-auto-mode -p "Refactor and test the auth module"
# Ou alterne modos com Shift+Tab
```

### Refatoração Segura
```bash
# Checkpoints são criados automaticamente antes de cada prompt
# Tente refatorar
# Se funcionar: continue
# Se falhar: pressione Esc+Esc ou use /rewind para voltar
```

### Implementação Complexa
```bash
# Use o modo de planejamento
/plan Implement user authentication system

# Claude cria um plano detalhado
# Revise e aprove
# Claude implementa de forma sistemática
```

### Integração CI/CD
```bash
# Execute em modo headless (não interativo)
claude -p "Run all tests and generate report"

# Com modo de permissão para CI
claude -p "Run tests" --permission-mode dontAsk

# Com Auto Mode para CI totalmente autônomo
claude --enable-auto-mode -p "Run tests and fix failures"

# Com hooks para automação
# Veja 09-advanced-features/README.md
```

### Experimentação e Aprendizado
```bash
# Use o modo de planejamento para análise segura
claude --permission-mode plan

# Experimente com segurança - checkpoints são criados automaticamente
# Se precisar voltar: pressione Esc+Esc ou use /rewind
```

### Times de Agentes
```bash
# Ativar times de agentes
export CLAUDE_AGENT_TEAMS=1

# Ou em settings.json
{ "agentTeams": { "enabled": true } }

# Comece com: "Implement feature X using a team approach"
```

### Tarefas Agendadas
```bash
# Executar um comando a cada 5 minutos
/loop 5m /check-status

# Lembrete único
/loop 30m "remind me to check the deploy"
```

---

## 📁 Referência de Localização dos Arquivos

```
Seu Projeto/
├── .claude/
│   ├── commands/              # Slash commands vão aqui
│   ├── agents/                # Subagentes vão aqui
│   ├── skills/                # Skills do projeto vão aqui
│   └── settings.json          # Configurações do projeto (hooks etc.)
├── .mcp.json                  # Configuração MCP (escopo do projeto)
├── CLAUDE.md                  # Memória do projeto
└── src/
    └── api/
        └── CLAUDE.md          # Memória específica do diretório

Home do Usuário/
├── .claude/
│   ├── commands/              # Comandos pessoais
│   ├── agents/                # Agentes pessoais
│   ├── skills/                # Skills pessoais
│   ├── hooks/                 # Scripts de hooks
│   ├── settings.json          # Configurações do usuário
│   ├── managed-settings.d/    # Configurações gerenciadas (empresa/org)
│   └── CLAUDE.md              # Memória pessoal
└── .claude.json               # Configuração MCP pessoal (escopo do usuário)
```

---

## 🔍 Encontrando Exemplos

### Por Categoria
- **Slash Commands**: `01-slash-commands/`
- **Memory**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagents**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Advanced Features**: `09-advanced-features/`
- **CLI**: `10-cli/`

### Por Caso de Uso
- **Performance**: `01-slash-commands/optimize.md`
- **Segurança**: `04-subagents/secure-reviewer.md`
- **Testes**: `04-subagents/test-engineer.md`
- **Docs**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### Por Complexidade
- **Simples**: Slash commands
- **Médio**: Subagentes, memória
- **Avançado**: Skills, hooks
- **Completo**: Plugins

---

## 🎓 Caminho de Aprendizado

### Dia 1
```bash
# Ler a visão geral
cat README.md

# Instalar um comando
cp 01-slash-commands/optimize.md .claude/commands/

# Testar
/optimize
```

### Dias 2-3
```bash
# Configurar memória
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Instalar subagente
cp 04-subagents/code-reviewer.md .claude/agents/
```

### Dias 4-5
```bash
# Configurar MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# Testar comandos MCP
/mcp__github__list_prs
```

### Semana 2
```bash
# Instalar skill
cp -r 03-skills/code-review ~/.claude/skills/

# Deixe a auto-invocação agir
# Basta dizer: "Review this code for issues"
```

### Semana 3+
```bash
# Instalar plugin completo
/plugin install pr-review

# Usar recursos integrados
/review-pr
/check-security
/check-tests
```

---

## Novas Funcionalidades (Março de 2026)

| Funcionalidade | Descrição | Uso |
|---------|-------------|-------|
| **Auto Mode** | Operação totalmente autônoma com classificador em segundo plano | `--enable-auto-mode`, `Shift+Tab` para alternar modos |
| **Channels** | Integração com Discord e Telegram | `--channels`, bots do Discord/Telegram |
| **Voice Dictation** | Falar comandos e contexto para o Claude | comando `/voice` |
| **Hooks (26 eventos)** | Sistema expandido de hooks com 4 tipos | tipos command, http, prompt, agent |
| **MCP Elicitation** | MCP servers podem pedir entrada do usuário em tempo de execução | prompt automático quando o servidor precisar de esclarecimento |
| **Plugin LSP** | Suporte a Language Server Protocol para plugins | `userConfig`, variável `${CLAUDE_PLUGIN_DATA}` |
| **Remote Control** | Controlar sessões do Claude Code via WebSocket API | `claude --remote` para integrações externas |
| **Web Sessions** | Interface baseada em navegador para o Claude Code | `claude web` para abrir |
| **Desktop App** | Aplicativo desktop nativo | Use `/desktop` ou baixe no site da Anthropic |
| **Task List** | Gerenciar e monitorar tarefas em segundo plano | `/task list`, `/task status <id>` |
| **Auto Memory** | Salvamento automático de memória a partir das conversas | o Claude salva contexto importante em CLAUDE.md |
| **Git Worktrees** | Ambientes isolados para desenvolvimento paralelo | `/worktree` para criar workspaces isolados |
| **Model Selection** | Alternar entre Sonnet 4.6 e Opus 4.6 | `/model` ou flag `--model` |
| **Agent Teams** | Coordenar vários agentes em tarefas relacionadas | configure agentes colaborativos com contexto compartilhado |
| **Scheduled Tasks** | Tarefas recorrentes com `/loop` | `/loop 5m /command` ou CronCreate |
| **Chrome Integration** | Automação de navegador com Chromium sem interface | flag `--chrome` ou comando `/chrome` |
| **Keyboard Customization** | Personalização de atalhos | comando `/keybindings` |

---

## Matriz Rápida de Referência

### Guia de Seleção de Funcionalidade

| Necessidade | Funcionalidade Recomendada | Motivo |
|------|---------------------|-----|
| Atalho rápido | Slash Command | Manual e imediato |
| Contexto persistente | Memory | Carregado automaticamente |
| Automação complexa | Skill | Auto-invocada |
| Tarefa especializada | Subagent | Contexto isolado |
| Dados externos | MCP Server | Acesso em tempo real |
| Automação por evento | Hook | Disparo por evento |
| Solução completa | Plugin | Pacote tudo-em-um |

### Prioridade de Instalação

| Prioridade | Funcionalidade | Comando |
|----------|---------|---------|
| 1. Essencial | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Uso diário | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. Qualidade | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. Automação | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. Externo | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. Avançado | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. Completo | Plugins | `/plugin install pr-review` |

---

## Instalação Completa em Um Comando

Instale todos os exemplos deste repositório:

```bash
# Criar diretórios
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Instalar tudo
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Recursos Adicionais

- [Documentação oficial do Claude Code](https://code.claude.com/docs/en/overview)
- [Especificação do Protocolo MCP](https://modelcontextprotocol.io)
- [Mapa de aprendizado](LEARNING-ROADMAP.md)
- [README principal](README.md)

---
