<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: 2deba3a -->
<!-- i18n-date: 2026-04-16 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Exemplos do Claude Code — Cartão de Referência Rápida

## 🚀 Comandos rápidos de instalação

### Comandos slash
```bash
# Instalar todos
cp 01-slash-commands/*.md .claude/commands/

# Instalar específico
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

# Skills de projeto
cp -r 03-skills/code-review .claude/skills/
```

### Subagentes
```bash
# Instalar todos
cp 04-subagents/*.md .claude/agents/

# Instalar específico
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# Definir credenciais
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Instalar configuração (escopo de projeto)
cp 05-mcp/github-mcp.json .mcp.json

# Ou escopo de usuário: adicionar em ~/.claude.json
```

### Hooks
```bash
# Instalar hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configurar nos settings (~/.claude/settings.json)
```

### Plugins
```bash
# Instalar a partir dos exemplos (se publicados)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# Checkpoints são criados automaticamente a cada prompt do usuário
# Para voltar, pressione Esc duas vezes ou use:
/rewind

# Depois escolha: Restaurar código e conversa, Restaurar conversa,
# Restaurar código, Resumir a partir daqui, ou Cancelar
```

### Funcionalidades avançadas
```bash
# Configurar nos settings (.claude/settings.json)
# Veja 09-advanced-features/config-examples.json

# Modo de planejamento
/plan Task description

# Modos de permissão (use a flag --permission-mode)
# default        - Pede aprovação em ações arriscadas
# acceptEdits    - Aceita edições de arquivo automaticamente, pergunta nas demais
# plan           - Análise somente leitura, sem modificações
# dontAsk        - Aceita todas as ações exceto as arriscadas
# auto           - Classificador em background decide permissões automaticamente
# bypassPermissions - Aceita todas as ações (requer --dangerously-skip-permissions)

# Gerenciamento de sessões
/resume                # Retomar conversa anterior
/rename "name"         # Dar nome à sessão atual
/fork                  # Fazer fork da sessão atual
claude -c              # Continuar a conversa mais recente
claude -r "session"    # Retomar sessão por nome/ID
```

---

## 📋 Cheat sheet de funcionalidades

| Funcionalidade | Caminho de instalação | Uso |
|----------------|------------------------|-----|
| **Comandos slash (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Memória** | `./CLAUDE.md` | Carregada automaticamente |
| **Skills** | `.claude/skills/*/SKILL.md` | Autoinvocadas |
| **Subagentes** | `.claude/agents/*.md` | Delegados automaticamente |
| **MCP** | `.mcp.json` (projeto) ou `~/.claude.json` (usuário) | `/mcp__server__action` |
| **Hooks (25 eventos)** | `~/.claude/hooks/*.sh` | Disparados por evento (4 tipos) |
| **Plugins** | Via `/plugin install` | Agrupam tudo |
| **Checkpoints** | Nativo | `Esc+Esc` ou `/rewind` |
| **Modo de planejamento** | Nativo | `/plan <task>` |
| **Modos de permissão (6)** | Nativo | `--allowedTools`, `--permission-mode` |
| **Sessões** | Nativo | `/session <command>` |
| **Tarefas em background** | Nativo | Execute em background |
| **Controle remoto** | Nativo | API WebSocket |
| **Sessões web** | Nativo | `claude web` |
| **Git worktrees** | Nativo | `/worktree` |
| **Auto memory** | Nativo | Salva automaticamente no CLAUDE.md |
| **Lista de tarefas** | Nativo | `/task list` |
| **Skills embutidas (5)** | Nativo | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 Casos de uso comuns

### Code review
```bash
# Método 1: comando slash
cp 01-slash-commands/optimize.md .claude/commands/
# Uso: /optimize

# Método 2: subagente
cp 04-subagents/code-reviewer.md .claude/agents/
# Uso: delegado automaticamente

# Método 3: skill
cp -r 03-skills/code-review ~/.claude/skills/
# Uso: autoinvocada

# Método 4: plugin (melhor)
/plugin install pr-review
# Uso: /review-pr
```

### Documentação
```bash
# Comando slash
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

### Padrões de equipe
```bash
# Memória do projeto
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Edite para a sua equipe
vim CLAUDE.md
```

### Automação e hooks
```bash
# Instalar hooks (25 eventos, 4 tipos: command, http, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Exemplos:
# - Testes pré-commit: pre-commit.sh
# - Autoformatação de código: format-code.sh
# - Varredura de segurança: security-scan.sh

# Auto Mode para fluxos totalmente autônomos
claude --enable-auto-mode -p "Refactor and test the auth module"
# Ou alterne modos interativamente com Shift+Tab
```

### Refatoração segura
```bash
# Checkpoints são criados automaticamente antes de cada prompt
# Experimente a refatoração
# Se funcionar: siga em frente
# Se falhar: pressione Esc+Esc ou use /rewind para voltar
```

### Implementação complexa
```bash
# Use o modo de planejamento
/plan Implement user authentication system

# Claude cria um plano detalhado
# Revise e aprove
# Claude implementa de forma sistemática
```

### Integração CI/CD
```bash
# Rodar em modo headless (não interativo)
claude -p "Run all tests and generate report"

# Com modo de permissão para CI
claude -p "Run tests" --permission-mode dontAsk

# Com Auto Mode para tarefas de CI totalmente autônomas
claude --enable-auto-mode -p "Run tests and fix failures"

# Com hooks para automação
# Veja 09-advanced-features/README.md
```

### Aprendizado e experimentação
```bash
# Use o modo plan para análise segura
claude --permission-mode plan

# Experimente com segurança — checkpoints são criados automaticamente
# Se precisar voltar: pressione Esc+Esc ou use /rewind
```

### Agent Teams
```bash
# Habilitar agent teams
export CLAUDE_AGENT_TEAMS=1

# Ou no settings.json
{ "agentTeams": { "enabled": true } }

# Comece com: "Implement feature X using a team approach"
```

### Tarefas agendadas
```bash
# Rodar um comando a cada 5 minutos
/loop 5m /check-status

# Lembrete único
/loop 30m "remind me to check the deploy"
```

---

## 📁 Referência de localização de arquivos

```
Seu projeto/
├── .claude/
│   ├── commands/              # Comandos slash ficam aqui
│   ├── agents/                # Subagentes ficam aqui
│   ├── skills/                # Skills do projeto ficam aqui
│   └── settings.json          # Settings do projeto (hooks etc.)
├── .mcp.json                  # Configuração MCP (escopo de projeto)
├── CLAUDE.md                  # Memória do projeto
└── src/
    └── api/
        └── CLAUDE.md          # Memória específica de diretório

Home do usuário/
├── .claude/
│   ├── commands/              # Comandos pessoais
│   ├── agents/                # Agentes pessoais
│   ├── skills/                # Skills pessoais
│   ├── hooks/                 # Scripts de hook
│   ├── settings.json          # Settings do usuário
│   ├── managed-settings.d/    # Settings gerenciados (empresa/organização)
│   └── CLAUDE.md              # Memória pessoal
└── .claude.json               # Config MCP pessoal (escopo de usuário)
```

---

## 🔍 Encontrando exemplos

### Por categoria
- **Comandos slash**: `01-slash-commands/`
- **Memória**: `02-memory/`
- **Skills**: `03-skills/`
- **Subagentes**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Hooks**: `06-hooks/`
- **Plugins**: `07-plugins/`
- **Checkpoints**: `08-checkpoints/`
- **Funcionalidades avançadas**: `09-advanced-features/`
- **CLI**: `10-cli/`

### Por caso de uso
- **Performance**: `01-slash-commands/optimize.md`
- **Segurança**: `04-subagents/secure-reviewer.md`
- **Testes**: `04-subagents/test-engineer.md`
- **Docs**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### Por complexidade
- **Simples**: comandos slash
- **Médio**: subagentes, memória
- **Avançado**: skills, hooks
- **Completo**: plugins

---

## 🎓 Trilha de aprendizado

### Dia 1
```bash
# Ler a visão geral
cat README.md

# Instalar um comando
cp 01-slash-commands/optimize.md .claude/commands/

# Experimentar
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

# Experimentar comandos MCP
/mcp__github__list_prs
```

### Semana 2
```bash
# Instalar skill
cp -r 03-skills/code-review ~/.claude/skills/

# Deixe a autoinvocação agir
# Basta dizer: "Review this code for issues"
```

### Semana 3+
```bash
# Instalar plugin completo
/plugin install pr-review

# Usar as funcionalidades agrupadas
/review-pr
/check-security
/check-tests
```

---

## Novos recursos (março de 2026)

| Recurso | Descrição | Uso |
|---------|-----------|-----|
| **Auto Mode** | Operação totalmente autônoma com classificador em background | Flag `--enable-auto-mode`, `Shift+Tab` para alternar modos |
| **Canais** | Integração com Discord e Telegram | Flag `--channels`, bots Discord/Telegram |
| **Ditado de voz** | Falar comandos e contexto para o Claude | Comando `/voice` |
| **Hooks (26 eventos)** | Sistema de hooks ampliado com 4 tipos | Tipos command, http, prompt, agent |
| **MCP Elicitation** | Servidores MCP podem pedir entrada do usuário em tempo de execução | Prompt automático quando o servidor precisa de esclarecimento |
| **Plugin LSP** | Suporte a Language Server Protocol para plugins | `userConfig`, variável `${CLAUDE_PLUGIN_DATA}` |
| **Controle remoto** | Controlar o Claude Code via API WebSocket | `claude --remote` para integrações externas |
| **Sessões web** | Interface do Claude Code baseada em navegador | `claude web` para iniciar |
| **App Desktop** | Aplicação desktop nativa | Baixar em claude.ai/download |
| **Lista de tarefas** | Gerenciar tarefas em background | `/task list`, `/task status <id>` |
| **Auto Memory** | Salvamento automático de memória a partir das conversas | O Claude salva contexto-chave em CLAUDE.md |
| **Git worktrees** | Workspaces isolados para desenvolvimento paralelo | `/worktree` para criar workspace isolado |
| **Seleção de modelo** | Alternar entre Sonnet 4.6 e Opus 4.6 | `/model` ou flag `--model` |
| **Agent Teams** | Coordenar múltiplos agentes em tarefas | Ative com a variável `CLAUDE_AGENT_TEAMS=1` |
| **Tarefas agendadas** | Tarefas recorrentes com `/loop` | `/loop 5m /command` ou ferramenta CronCreate |
| **Integração Chrome** | Automação de navegador | Flag `--chrome` ou comando `/chrome` |
| **Personalização de teclado** | Keybindings customizados | Comando `/keybindings` |

---

## Dicas e truques

### Personalização
- Comece com os exemplos como estão
- Modifique conforme suas necessidades
- Teste antes de compartilhar com a equipe
- Versione suas configurações

### Boas práticas
- Use memória para padrões de equipe
- Use plugins para fluxos completos
- Use subagentes para tarefas complexas
- Use comandos slash para tarefas rápidas

### Troubleshooting
```bash
# Verificar locais dos arquivos
ls -la .claude/commands/
ls -la .claude/agents/

# Conferir sintaxe YAML
head -20 .claude/agents/code-reviewer.md

# Testar conexão MCP
echo $GITHUB_TOKEN
```

---

## 📊 Matriz de funcionalidades

| Necessidade | Use isto | Exemplo |
|-------------|----------|---------|
| Atalho rápido | Comando slash (55+) | `01-slash-commands/optimize.md` |
| Padrões de equipe | Memória | `02-memory/project-CLAUDE.md` |
| Fluxo automático | Skill | `03-skills/code-review/` |
| Tarefa especializada | Subagente | `04-subagents/code-reviewer.md` |
| Dados externos | MCP (+ Elicitation) | `05-mcp/github-mcp.json` |
| Automação por evento | Hook (26 eventos, 4 tipos) | `06-hooks/pre-commit.sh` |
| Solução completa | Plugin (+ suporte a LSP) | `07-plugins/pr-review/` |
| Experimentação segura | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| Totalmente autônomo | Auto Mode | `--enable-auto-mode` ou `Shift+Tab` |
| Integrações de chat | Canais | `--channels` (Discord, Telegram) |
| Pipeline CI/CD | CLI | `10-cli/README.md` |

---

## 🔗 Links rápidos

- **Guia principal**: `README.md`
- **Índice completo**: `INDEX.md`
- **Resumo**: `EXAMPLES_SUMMARY.md`
- **Guia original**: `claude_concepts_guide.md`

---

## 📞 Perguntas frequentes

**P: Qual devo usar?**
R: Comece com comandos slash e adicione recursos conforme a necessidade.

**P: Posso combinar funcionalidades?**
R: Sim! Elas funcionam juntas. Memória + comandos + MCP = poder.

**P: Como compartilho com a equipe?**
R: Commite o diretório `.claude/` no git.

**P: E quanto a segredos?**
R: Use variáveis de ambiente, nunca deixe valores fixos no código.

**P: Posso modificar os exemplos?**
R: Com certeza! Eles são templates para você personalizar.

---

## ✅ Checklist

Checklist para começar:

- [ ] Leia `README.md`
- [ ] Instale 1 comando slash
- [ ] Experimente o comando
- [ ] Crie o `CLAUDE.md` do projeto
- [ ] Instale 1 subagente
- [ ] Configure 1 integração MCP
- [ ] Instale 1 skill
- [ ] Experimente um plugin completo
- [ ] Personalize para suas necessidades
- [ ] Compartilhe com a equipe

---

**Início rápido**: `cat README.md`

**Índice completo**: `cat INDEX.md`

**Este cartão**: mantenha à mão para referência rápida!

---
**Última atualização**: 11 de abril de 2026
**Versão do Claude Code**: 2.1.101
**Fontes**:
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/cli-reference
