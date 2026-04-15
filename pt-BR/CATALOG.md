<!-- i18n-source: CATALOG.md -->
<!-- i18n-source-sha: 9c224ff -->
<!-- i18n-date: 2026-04-14 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Catálogo de Funcionalidades do Claude Code

> Guia rápido de todas as funcionalidades do Claude Code: comandos, agentes, skills, plugins e hooks.

**Navegação**: [Commands](#slash-commands) | [Permission Modes](#permission-modes) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [MCP Servers](#mcp-servers) | [Hooks](#hooks) | [Memory](#memory-files) | [New Features](#new-features-april-2026)

---

## Resumo

| Funcionalidade | Nativo | Exemplos | Total | Referência |
|---------|----------|----------|-------|-----------|
| **Slash Commands** | 55+ | 8 | 63+ | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | 6 | 11 | 17 | [04-subagents/](04-subagents/) |
| **Skills** | 5 incluídas | 4 | 9 | [03-skills/](03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP Servers** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **Hooks** | 25 eventos | 8 | 8 | [06-hooks/](06-hooks/) |
| **Memory** | 7 tipos | 3 | 3 | [02-memory/](02-memory/) |
| **Total** | **99** | **45** | **119** | |

---

## Slash Commands

Comandos são atalhos acionados pelo usuário para executar ações específicas.

### Built-in Commands

| Command | Description | When to Use |
|---------|-------------|-------------|
| `/help` | Mostrar ajuda | Começar, aprender comandos |
| `/btw` | Pergunta lateral sem adicionar ao contexto | Questões rápidas e pontuais |
| `/chrome` | Configurar integração com Chrome | Automação de navegador |
| `/clear` | Limpar histórico da conversa | Começar do zero |
| `/diff` | Visualizador interativo de diff | Revisar mudanças |
| `/config` | Ver/editar configuração | Personalizar comportamento |
| `/status` | Mostrar status da sessão | Ver estado atual |
| `/agents` | Listar agentes disponíveis | Ver opções de delegação |
| `/skills` | Listar skills disponíveis | Ver auto-invocações |
| `/hooks` | Listar hooks configurados | Depurar automação |
| `/insights` | Analisar padrões da sessão | Otimização de sessão |
| `/install-slack-app` | Instalar app Slack do Claude | Integração com Slack |
| `/keybindings` | Personalizar atalhos de teclado | Personalização |
| `/mcp` | Listar servidores MCP | Ver integrações externas |
| `/memory` | Ver arquivos de memória carregados | Depurar contexto |
| `/mobile` | Gerar QR code para mobile | Acesso móvel |
| `/passes` | Ver uso de passes | Informação de assinatura |
| `/plugin` | Gerenciar plugins | Instalar/remover extensões |
| `/plan` | Entrar no modo de planejamento | Implementações complexas |
| `/rewind` | Voltar ao checkpoint | Desfazer mudanças |
| `/checkpoint` | Gerenciar checkpoints | Salvar/restaurar estados |
| `/cost` | Mostrar custo em tokens | Monitorar gastos |
| `/context` | Mostrar uso da janela de contexto | Gerenciar comprimento da conversa |
| `/export` | Exportar conversa | Salvar referência |
| `/extra-usage` | Configurar limites extras | Gerenciar rate limit |
| `/feedback` | Enviar feedback ou bug | Reportar problemas |
| `/login` | Autenticar com Anthropic | Acessar recursos |
| `/logout` | Sair da conta | Trocar de conta |
| `/sandbox` | Alternar modo sandbox | Execução segura |
| `/doctor` | Rodar diagnósticos | Resolver problemas |
| `/reload-plugins` | Recarregar plugins | Gerenciar plugins |
| `/release-notes` | Mostrar notas de versão | Ver novidades |
| `/remote-control` | Habilitar controle remoto | Acesso remoto |
| `/permissions` | Gerenciar permissões | Controlar acesso |
| `/session` | Gerenciar sessões | Fluxos multi-sessão |
| `/rename` | Renomear sessão atual | Organizar sessões |
| `/resume` | Retomar sessão anterior | Continuar trabalho |
| `/todo` | Ver/gerenciar lista de tarefas | Acompanhar tarefas |
| `/tasks` | Ver tarefas em background | Monitorar operações assíncronas |
| `/copy` | Copiar última resposta | Compartilhar rápido |
| `/teleport` | Transferir sessão para outro computador | Continuar remotamente |
| `/desktop` | Abrir app desktop do Claude | Trocar para interface desktop |
| `/theme` | Trocar tema de cor | Personalizar aparência |
| `/usage` | Mostrar estatísticas de uso | Monitorar cota e custos |
| `/fork` | Fazer fork da conversa atual | Explorar alternativas |
| `/stats` | Mostrar estatísticas da sessão | Revisar métricas |
| `/statusline` | Configurar a linha de status | Personalizar exibição |
| `/stickers` | Ver stickers da sessão | Recompensas divertidas |
| `/fast` | Alternar modo rápido | Acelerar respostas |
| `/terminal-setup` | Configurar integração com terminal | Ajuste do terminal |
| `/upgrade` | Verificar atualizações | Gerenciar versão |

### Custom Commands (Examples)

| Command | Description | When to Use | Scope | Installation |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | Analisar código para otimização | Melhorar performance | Project | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Preparar pull request | Antes de abrir PRs | Project | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | Gerar documentação de API | Documentar APIs | Project | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | Criar commit com contexto | Fazer commits | User | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | Stage, commit e push | Deploy rápido | User | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | Reestruturar documentação | Melhorar docs | Project | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | Configurar pipeline CI/CD | Novos projetos | Project | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | Expandir cobertura de testes | Melhorar testes | Project | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Escopo**: `User` = fluxos pessoais (`~/.claude/commands/`), `Project` = compartilhado pelo time (`.claude/commands/`)

**Referência**: [01-slash-commands/](01-slash-commands/) | [Official Docs](https://code.claude.com/docs/en/interactive-mode)

**Instalação rápida (todos os comandos customizados)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Permission Modes

O Claude Code suporta 6 modos de permissão que controlam a autorização de uso de ferramentas.

| Mode | Description | When to Use |
|------|-------------|-------------|
| `default` | Solicita aprovação para cada tool call | Uso interativo padrão |
| `acceptEdits` | Aceita edições automaticamente, pede para outras ações | Fluxos de edição confiáveis |
| `plan` | Apenas leitura, sem escrita | Planejamento e exploração |
| `auto` | Aceita tudo sem perguntar | Operação totalmente autônoma (Research Preview) |
| `bypassPermissions` | Ignora todas as verificações | CI/CD, ambientes headless |
| `dontAsk` | Ignora ferramentas que exigiriam permissão | Scripting não interativo |

> **Nota**: `auto` é um recurso de Research Preview (março de 2026). Use `bypassPermissions` apenas em ambientes confiáveis e isolados.

**Referência**: [Official Docs](https://code.claude.com/docs/en/permissions)

---

## Subagents

Assistentes especializados com contextos isolados para tarefas específicas.

### Built-in Subagents

| Agent | Description | Tools | Model | When to Use |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | Tarefas multi-etapas, pesquisa | Todas as ferramentas | Herda o modelo | Pesquisas complexas, tarefas com múltiplos arquivos |
| **Plan** | Planejamento de implementação | Read, Glob, Grep, Bash | Herda o modelo | Design de arquitetura, planejamento |
| **Explore** | Exploração da base de código | Read, Glob, Grep | Haiku 4.5 | Buscas rápidas, entender código |
| **Bash** | Execução de comandos | Bash | Herda o modelo | Git, tarefas de terminal |
| **statusline-setup** | Configuração da barra de status | Bash, Read, Write | Sonnet 4.6 | Configurar a exibição da barra |
| **Claude Code Guide** | Ajuda e documentação | Read, Glob, Grep | Haiku 4.5 | Aprender recursos, obter ajuda |

### Custom Subagents (Examples)

| Agent | Description | When to Use | Scope | Installation |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | Revisão completa de qualidade | Sessões de code review | Project | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `clean-code-reviewer` | Revisão por princípios de Clean Code | Manutenibilidade | Project | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | Estratégia e cobertura de testes | Planejamento de testes | Project | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | Documentação técnica | Docs de API e guias | Project | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | Revisão focada em segurança | Auditorias de segurança | Project | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | Implementação completa de features | Desenvolvimento | Project | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | Análise de causa raiz | Investigação de bugs | User | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL e análise de dados | Dados e métricas | User | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | Profiling e tuning | Gargalos de performance | Project | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **Escopo**: `User` = pessoal (`~/.claude/agents/`), `Project` = compartilhado (`.claude/agents/`)

**Referência**: [04-subagents/](04-subagents/) | [Official Docs](https://code.claude.com/docs/en/sub-agents)

**Instalação rápida (todos os agentes customizados)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

Capacidades auto-invocadas com instruções, scripts e templates.

### Example Skills

| Skill | Description | When Auto-Invoked | Scope | Installation |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | Revisão de código abrangente | "Review this code", "Check quality" | Project | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | Verificador de consistência da marca | Texto de marketing | Project | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | Gerador de documentação de API | "Generate docs", "Document API" | Project | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | Refatoração sistemática (Martin Fowler) | "Refactor this", "Clean up code" | User | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **Escopo**: `User` = pessoal (`~/.claude/skills/`), `Project` = compartilhado (`.claude/skills/`)

### Bundled Skills

| Skill | Description | When Auto-Invoked |
|-------|-------------|-------------------|
| `/simplify` | Revisar código por qualidade | Depois de escrever código |
| `/batch` | Executar prompts em múltiplos arquivos | Operações em lote |
| `/debug` | Depurar testes/erros que falharam | Sessões de debug |
| `/loop` | Executar prompts em intervalo | Tarefas recorrentes |
| `/claude-api` | Criar apps com a API do Claude | Desenvolvimento com API |

---

## Plugins

Conjuntos completos de comandos, agentes, servidores MCP e hooks.

### Example Plugins

| Plugin | Description | Components | When to Use | Scope | Installation |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | Fluxo de revisão de PR | 3 commands, 3 agents, GitHub MCP | Code reviews | Project | `/plugin install pr-review` |
| `devops-automation` | Deploy e monitoramento | 4 commands, 3 agents, K8s MCP | Tarefas DevOps | Project | `/plugin install devops-automation` |
| `documentation` | Suite de geração de docs | 4 commands, 3 agents, templates | Documentação | Project | `/plugin install documentation` |

> **Escopo**: `Project` = compartilhado pela equipe, `User` = fluxos pessoais

---

## MCP Servers

Servidores Model Context Protocol para acesso externo a ferramentas e APIs.

### Common MCP Servers

| Server | Description | When to Use | Scope | Installation |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | Gestão de PRs, issues e código | Fluxos GitHub | Project | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | Consultas SQL e acesso a dados | Operações de banco | Project | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | Operações avançadas de arquivos | Tarefas complexas de arquivos | User | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | Comunicação da equipe | Notificações, atualizações | Project | Configure em settings |
| **Google Docs** | Acesso a documentos | Edição e revisão | Project | Configure em settings |
| **Asana** | Gestão de projetos | Acompanhamento de tarefas | Project | Configure em settings |
| **Stripe** | Dados de pagamento | Análise financeira | Project | Configure em settings |
| **Memory** | Memória persistente | Recuperação entre sessões | User | Configure em settings |
| **Context7** | Documentação de bibliotecas | Consulta de docs atualizadas | Built-in | Integrado |

> **Escopo**: `Project` = time (`.mcp.json`), `User` = pessoal (`~/.claude.json`), `Built-in` = pré-instalado

---

## Hooks

Automação orientada a eventos que executa comandos shell em eventos do Claude Code.

### Hook Events

| Event | Description | When Triggered | Use Cases |
|-------|-------------|----------------|-----------|
| `SessionStart` | Sessão começa/retoma | Inicialização | Setup |
| `InstructionsLoaded` | Instruções carregadas | CLAUDE.md ou rules | Tratamento de instruções |
| `UserPromptSubmit` | Antes de processar o prompt | Usuário envia mensagem | Validação de entrada |
| `PreToolUse` | Antes da execução da ferramenta | Antes de qualquer tool | Validação, logging |
| `PermissionRequest` | Diálogo de permissão exibido | Antes de ações sensíveis | Fluxos de aprovação |
| `PostToolUse` | Depois que a ferramenta funciona | Após conclusão | Formatação, notificações |
| `PostToolUseFailure` | Ferramenta falha | Após erro | Tratamento, logging |
| `Notification` | Notificação enviada | Claude notifica | Alertas externos |
| `SubagentStart` | Subagente iniciado | Início de tarefa | Inicializar contexto |
| `SubagentStop` | Subagente finaliza | Tarefa concluída | Encadear ações |
| `Stop` | Claude termina de responder | Resposta concluída | Limpeza, relatório |
| `StopFailure` | Erro de API encerra a resposta | Erro de API | Recuperação |
| `TeammateIdle` | Agente de equipe ocioso | Coordenação | Distribuição de trabalho |
| `TaskCompleted` | Tarefa marcada como concluída | Tarefa feita | Pós-processamento |
| `TaskCreated` | Tarefa criada via TaskCreate | Nova tarefa | Rastreamento, logging |
| `ConfigChange` | Configuração atualizada | Settings alterado | Reagir a mudanças |
| `CwdChanged` | Diretório de trabalho muda | Mudança de pasta | Setup específico por diretório |
| `FileChanged` | Arquivo observado muda | Arquivo modificado | Monitoramento, rebuild |
| `PreCompact` | Antes da compactação | Compressão de contexto | Preservação de estado |
| `PostCompact` | Depois da compactação | Compactação concluída | Ações pós-compactação |
| `WorktreeCreate` | Worktree sendo criado | Git worktree criado | Preparar ambiente |
| `WorktreeRemove` | Worktree sendo removido | Git worktree removido | Limpeza |
| `Elicitation` | Servidor MCP pede entrada | Elicitação MCP | Validação de entrada |
| `ElicitationResult` | Usuário responde à elicitação | Resposta recebida | Processamento |
| `SessionEnd` | Sessão termina | Encerramento | Limpeza, salvar estado |

---

## Memory Files

Contexto persistente carregado automaticamente entre sessões.

### Memory Types

| Type | Location | Scope | When to Use |
|------|----------|-------|-------------|
| **Managed Policy** | Políticas gerenciadas pela organização | Organization | Aplicar padrões globais |
| **Project** | `./CLAUDE.md` | Project (team) | Padrões do time, contexto do projeto |
| **Project Rules** | `.claude/rules/` | Project (team) | Regras modulares do projeto |
| **User** | `~/.claude/CLAUDE.md` | User (personal) | Preferências pessoais |
| **User Rules** | `~/.claude/rules/` | User (personal) | Regras modulares pessoais |
| **Local** | `./CLAUDE.local.md` | Local (git-ignored) | Overrides específicos da máquina |
| **Auto Memory** | Automatic | Session | Insights e correções capturadas automaticamente |

> **Escopo**: `Organization` = gerenciado por admins, `Project` = compartilhado no git, `User` = preferências pessoais, `Local` = não commitado, `Session` = gerenciado automaticamente

---

## New Features (April 2026)

| Feature | Description | How to Use |
|---------|-------------|------------|
| **Monitor Tool** | Observa o stdout de um comando em background e reage a eventos em vez de fazer polling (v2.1.98+) | Use a ferramenta Monitor em [Advanced Features](09-advanced-features/) |
| **/team-onboarding** | Gera automaticamente um guia de ramp-up a partir da configuração do projeto | Execute `/team-onboarding` no projeto |
| **Ultraplan auto-create** | Ambiente cloud criado automaticamente no primeiro uso de `/ultraplan` | Use `/ultraplan <prompt>` |
| **Remote Control** | Controle sessões do Claude Code remotamente via API | Use a API de controle remoto para enviar prompts e receber respostas |
| **Web Sessions** | Execute o Claude Code em ambiente baseado em navegador | Acesse via `claude web` ou pelo Anthropic Console |
| **Desktop App** | Aplicativo desktop nativo do Claude Code | Use `/desktop` ou baixe no site da Anthropic |
| **Agent Teams** | Coordene múltiplos agentes em tarefas relacionadas | Configure agentes de equipe que colaboram e compartilham contexto |
| **Task List** | Gestão e monitoramento de tarefas em background | Use `/tasks` para ver e gerenciar operações |
| **Prompt Suggestions** | Sugestões de comando com base no contexto | Surgem automaticamente conforme o contexto |
| **Git Worktrees** | Worktrees isolados para desenvolvimento paralelo | Use comandos de worktree para branches paralelas |
| **Sandboxing** | Ambientes isolados para segurança | Use `/sandbox` para alternar; comandos rodam em ambiente restrito |
| **MCP OAuth** | Autenticação OAuth para servidores MCP | Configure credenciais OAuth nas settings do MCP |
| **MCP Tool Search** | Pesquisar e descobrir ferramentas MCP dinamicamente | Use tool search para achar ferramentas conectadas |
| **Scheduled Tasks** | Tarefas recorrentes com `/loop` e cron tools | Use `/loop 5m /command` ou CronCreate |
| **Chrome Integration** | Automação de navegador com Chromium headless | Use a flag `--chrome` ou o comando `/chrome` |
| **Keyboard Customization** | Personalizar keybindings com suporte a chord | Use `/keybindings` ou edite `~/.claude/keybindings.json` |
| **Auto Mode** | Operação totalmente autônoma sem prompts de permissão | Use `--mode auto` ou `/permissions auto` |
| **Channels** | Comunicação multicanal (Telegram, Slack etc.) | Configure plugins de canais |
| **Voice Dictation** | Entrada por voz para prompts | Use o ícone de microfone ou keybinding de voz |
| **Agent Hook Type** | Hooks que sobem um subagente em vez de rodar shell | Defina `"type": "agent"` na configuração |
| **Prompt Hook Type** | Hooks que injetam texto de prompt na conversa | Defina `"type": "prompt"` |
| **MCP Elicitation** | Servidores MCP podem pedir entrada do usuário durante a execução | Trate com `Elicitation` e `ElicitationResult` |
| **Plugin LSP Support** | Integração de Language Server Protocol via plugins | Configure servidores LSP em `plugin.json` |
| **Managed Drop-ins** | Configurações drop-in gerenciadas pela organização | Aplicadas automaticamente por políticas |

---

## Matriz Rápida de Referência

### Guia de Seleção de Funcionalidade

| Need | Recommended Feature | Why |
|------|---------------------|-----|
| Atalho rápido | Slash Command | Manual, imediato |
| Contexto persistente | Memory | Carregado automaticamente |
| Automação complexa | Skill | Auto-invocada |
| Tarefa especializada | Subagent | Contexto isolado |
| Dados externos | MCP Server | Acesso em tempo real |
| Automação por evento | Hook | Disparado por evento |
| Solução completa | Plugin | Pacote tudo-em-um |

### Prioridade de Instalação

| Priority | Feature | Command |
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
# Create directories
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Install all features
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
- [Roteiro de Aprendizado](LEARNING-ROADMAP.md)
- [README principal](README.md)

---
