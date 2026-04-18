<!-- i18n-source: CATALOG.md -->
<!-- i18n-source-sha: 2deba3a -->
<!-- i18n-date: 2026-04-16 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Catálogo de Funcionalidades do Claude Code

> Guia de referência rápida para todas as funcionalidades do Claude Code: comandos, agentes, skills, plugins e hooks.

**Navegação**: [Slash Commands](#slash-commands) | [Modos de permissão](#modos-de-permissão) | [Subagents](#subagents) | [Skills](#skills) | [Plugins](#plugins) | [Servidores MCP](#servidores-mcp) | [Hooks](#hooks) | [Memory](#arquivos-de-memory) | [Novos recursos](#novos-recursos-abril-de-2026)

---

## Resumo

| Funcionalidade | Nativo | Exemplos | Total | Referência |
|----------------|--------|----------|-------|------------|
| **Slash Commands** | 60+ | 8 | 68+ | [01-slash-commands/](01-slash-commands/) |
| **Subagents** | 6 | 11 | 17 | [04-subagents/](04-subagents/) |
| **Skills** | 5 embutidas | 4 | 9 | [03-skills/](03-skills/) |
| **Plugins** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **Servidores MCP** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **Hooks** | 25 eventos | 8 | 8 | [06-hooks/](06-hooks/) |
| **Memory** | 7 tipos | 3 | 3 | [02-memory/](02-memory/) |
| **Total** | **99** | **45** | **119** | |

---

## Slash Commands

Comandos são atalhos iniciados pelo usuário para executar ações específicas.

### Comandos nativos

| Comando | Descrição | Quando usar |
|---------|-----------|-------------|
| `/help` | Exibir informações de ajuda | Começar, conhecer comandos |
| `/btw` | Pergunta paralela sem adicionar ao contexto | Dúvidas rápidas fora do fluxo |
| `/chrome` | Configurar integração com o Chrome | Automação de navegador |
| `/clear` | Limpar histórico da conversa | Começar do zero, reduzir contexto |
| `/diff` | Visualizador interativo de diff | Revisar mudanças |
| `/config` | Ver/editar configuração | Personalizar comportamento |
| `/status` | Exibir status da sessão | Verificar estado atual |
| `/agents` | Listar agentes disponíveis | Ver opções de delegação |
| `/skills` | Listar skills disponíveis | Ver capacidades autoinvocadas |
| `/hooks` | Listar hooks configurados | Depurar automação |
| `/insights` | Analisar padrões da sessão | Otimização da sessão |
| `/install-slack-app` | Instalar app do Claude no Slack | Integração com Slack |
| `/keybindings` | Personalizar atalhos de teclado | Customização de teclas |
| `/mcp` | Listar servidores MCP | Verificar integrações externas |
| `/memory` | Ver arquivos de Memory carregados | Depurar carregamento de contexto |
| `/mobile` | Gerar QR code para mobile | Acesso mobile |
| `/passes` | Ver passes de uso | Informações de assinatura |
| `/plugin` | Gerenciar plugins | Instalar/remover extensões |
| `/plan` | Entrar em modo de planejamento | Implementações complexas |
| `/proactive` | Alias para `/loop` | Igual a `/loop` |
| `/recap` | Exibir recapitulação da sessão ao retornar | Voltar a uma sessão e obter contexto do que foi feito |
| `/rewind` | Retroceder até um checkpoint | Desfazer mudanças, explorar alternativas |
| `/checkpoint` | Gerenciar checkpoints | Salvar/restaurar estados |
| `/cost` | Exibir custos de tokens | Monitorar gastos |
| `/context` | Exibir uso da janela de contexto | Gerenciar tamanho da conversa |
| `/export` | Exportar conversa | Salvar para referência |
| `/extra-usage` | Configurar limites extras de uso | Gestão de rate limit |
| `/feedback` | Enviar feedback ou bug report | Reportar problemas |
| `/login` | Autenticar com a Anthropic | Acessar recursos |
| `/logout` | Sair | Trocar de conta |
| `/sandbox` | Alternar modo sandbox | Execução segura de comandos |
| `/doctor` | Rodar diagnóstico | Solucionar problemas |
| `/reload-plugins` | Recarregar plugins instalados | Gestão de plugins |
| `/release-notes` | Exibir notas de versão | Ver novos recursos |
| `/remote-control` | Habilitar controle remoto | Acesso remoto |
| `/permissions` | Gerenciar permissões | Controlar acesso |
| `/session` | Gerenciar sessões | Fluxos multisessão |
| `/rename` | Renomear sessão atual | Organizar sessões |
| `/resume` | Retomar sessão anterior | Continuar o trabalho |
| `/todo` | Ver/gerenciar lista de tarefas | Acompanhar tarefas |
| `/tui` | Alternar modo TUI (text user interface) em tela cheia | Renderização sem flicker em fullscreen/tmux |
| `/tasks` | Ver tarefas em background | Monitorar operações assíncronas |
| `/copy` | Copiar última resposta para a área de transferência | Compartilhar saída rapidamente |
| `/teleport` | Transferir sessão para outra máquina | Continuar o trabalho remotamente |
| `/desktop` | Abrir app Claude Desktop | Mudar para a interface desktop |
| `/theme` | Trocar tema de cores | Personalizar aparência |
| `/usage` | Exibir estatísticas de uso da API | Monitorar cota e custos |
| `/focus` | Alternar modo foco (saída sem distrações) | Reduzir ruído visual em tarefas longas |
| `/fork` | Fazer fork da conversa atual | Explorar alternativas |
| `/stats` | Exibir estatísticas da sessão | Revisar métricas da sessão |
| `/statusline` | Configurar status line | Personalizar exibição de status |
| `/stickers` | Ver stickers da sessão | Recompensas divertidas |
| `/fast` | Alternar modo de saída rápida | Acelerar respostas |
| `/terminal-setup` | Configurar integração com o terminal | Configurar recursos de terminal |
| `/undo` | Alias para `/rewind` | Igual a `/rewind` |
| `/upgrade` | Verificar atualizações | Gestão de versão |
| `/team-onboarding` | Gerar guia de ramp-up da equipe a partir do uso atual do Claude Code no projeto | Onboarding de novos colegas (v2.1.101) |
| `/ultraplan` | Delegar tarefa de planejamento para uma sessão web do Claude Code em modo plano | Planejamento pesado offload (Research Preview, v2.1.91+) |
| `/ultrareview` | Rodar revisão multi-agente de código na nuvem sobre as mudanças atuais | Revisão profunda pré-merge por múltiplos agentes (v2.1.112) |
| `/less-permission-prompts` | Escanear transcrições e propor allowlist priorizada para ferramentas comuns de só-leitura | Reduzir prompts repetidos de permissão no projeto (v2.1.112) |

### Comandos personalizados (exemplos)

| Comando | Descrição | Quando usar | Escopo | Instalação |
|---------|-----------|-------------|--------|------------|
| `/optimize` | Analisar código para otimização | Melhorias de performance | Projeto | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | Preparar pull request | Antes de enviar PRs | Projeto | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | Gerar documentação de API | Documentar APIs | Projeto | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | Criar commit git com contexto | Commitar mudanças | Usuário | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | Stage, commit e push | Deploy rápido | Usuário | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | Reestruturar documentação | Melhorar docs | Projeto | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | Configurar pipeline CI/CD | Projetos novos | Projeto | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | Expandir cobertura de testes | Melhorar testes | Projeto | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **Escopo**: `Usuário` = fluxos pessoais (`~/.claude/commands/`), `Projeto` = compartilhado com a equipe (`.claude/commands/`)

**Referência**: [01-slash-commands/](01-slash-commands/) | [Documentação oficial](https://code.claude.com/docs/en/interactive-mode)

**Instalação rápida (todos os comandos personalizados)**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## Modos de permissão

O Claude Code oferece 6 modos de permissão que controlam como o uso de ferramentas é autorizado.

| Modo | Descrição | Quando usar |
|------|-----------|-------------|
| `default` | Pedir confirmação para cada uso de ferramenta | Uso interativo padrão |
| `acceptEdits` | Aceitar edições de arquivo automaticamente, perguntar nas demais | Fluxos de edição confiáveis |
| `plan` | Apenas ferramentas somente leitura, sem escritas | Planejamento e exploração |
| `auto` | Aceitar todas as ferramentas sem perguntar | Operação totalmente autônoma (Research Preview) |
| `bypassPermissions` | Pular todas as checagens de permissão | CI/CD, ambientes headless |
| `dontAsk` | Pular ferramentas que exigiriam permissão | Scripts não interativos |

> **Nota**: o modo `auto` é um Research Preview (março de 2026). Use `bypassPermissions` apenas em ambientes confiáveis e isolados (sandbox).

**Referência**: [Documentação oficial](https://code.claude.com/docs/en/permissions)

---

## Subagents

Assistentes de IA especializados com contextos isolados para tarefas específicas.

### Subagents nativos

| Agente | Descrição | Ferramentas | Modelo | Quando usar |
|--------|-----------|-------------|--------|-------------|
| **general-purpose** | Tarefas multi-etapas, pesquisa | Todas as ferramentas | Herda o modelo | Pesquisa complexa, tarefas multi-arquivo |
| **Plan** | Planejamento de implementação | Read, Glob, Grep, Bash | Herda o modelo | Arquitetura, planejamento |
| **Explore** | Exploração de código | Read, Glob, Grep | Haiku 4.5 | Buscas rápidas, compreensão de código |
| **Bash** | Execução de comandos | Bash | Herda o modelo | Operações git, tarefas de terminal |
| **statusline-setup** | Configuração da status line | Bash, Read, Write | Sonnet 4.6 | Configurar exibição da status line |
| **Claude Code Guide** | Ajuda e documentação | Read, Glob, Grep | Haiku 4.5 | Obter ajuda, aprender recursos |

### Campos de configuração de Subagent

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `name` | string | Identificador do agente |
| `description` | string | O que o agente faz |
| `model` | string | Sobrescrita de modelo (ex.: `haiku-4.5`) |
| `tools` | array | Lista de ferramentas permitidas |
| `effort` | string | Nível de esforço de raciocínio (`low`, `medium`, `high`) |
| `initialPrompt` | string | System prompt injetado ao iniciar o agente |
| `disallowedTools` | array | Ferramentas explicitamente negadas a este agente |

### Subagents personalizados (exemplos)

| Agente | Descrição | Quando usar | Escopo | Instalação |
|--------|-----------|-------------|--------|------------|
| `code-reviewer` | Qualidade abrangente de código | Sessões de revisão de código | Projeto | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | Projeto de arquitetura de features | Planejamento de novas features | Projeto | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | Análise profunda do código | Entender features existentes | Projeto | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | Revisão baseada em Clean Code | Revisão de manutenibilidade | Projeto | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | Estratégia e cobertura de testes | Planejamento de testes | Projeto | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | Documentação técnica | Docs de API, guias | Projeto | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | Revisão focada em segurança | Auditorias de segurança | Projeto | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | Implementação completa de features | Desenvolvimento de features | Projeto | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | Análise de causa raiz | Investigação de bugs | Usuário | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | Consultas SQL, análise de dados | Tarefas de dados | Usuário | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | Profiling e tuning de performance | Investigação de gargalos | Projeto | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **Escopo**: `Usuário` = pessoal (`~/.claude/agents/`), `Projeto` = compartilhado com a equipe (`.claude/agents/`)

**Referência**: [04-subagents/](04-subagents/) | [Documentação oficial](https://code.claude.com/docs/en/sub-agents)

**Instalação rápida (todos os agentes personalizados)**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## Skills

Capacidades autoinvocadas com instruções, scripts e templates.

### Skills de exemplo

| Skill | Descrição | Quando autoinvocada | Escopo | Instalação |
|-------|-----------|---------------------|--------|------------|
| `code-review` | Revisão abrangente de código | "Revisar este código", "Verificar qualidade" | Projeto | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | Verificador de consistência de voz de marca | Escrever copy de marketing | Projeto | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | Gerador de documentação de API | "Gerar docs", "Documentar API" | Projeto | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | Refatoração sistemática de código (Martin Fowler) | "Refatorar isso", "Limpar o código" | Usuário | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **Escopo**: `Usuário` = pessoal (`~/.claude/skills/`), `Projeto` = compartilhado com a equipe (`.claude/skills/`)

### Estrutura da skill

```
~/.claude/skills/skill-name/
├── SKILL.md          # Definição e instruções da skill
├── scripts/          # Scripts auxiliares
└── templates/        # Templates de saída
```

### Campos de frontmatter da skill

Skills suportam frontmatter YAML em `SKILL.md` para configuração:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `name` | string | Nome de exibição da skill |
| `description` | string | O que a skill faz |
| `autoInvoke` | array | Frases-gatilho para autoinvocação |
| `effort` | string | Nível de esforço de raciocínio (`low`, `medium`, `high`) |
| `shell` | string | Shell para executar scripts (`bash`, `zsh`, `sh`) |

**Referência**: [03-skills/](03-skills/) | [Documentação oficial](https://code.claude.com/docs/en/skills)

**Instalação rápida (todas as skills)**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### Skills embutidas

| Skill | Descrição | Quando autoinvocada |
|-------|-----------|---------------------|
| `/simplify` | Revisar código por qualidade | Depois de escrever código |
| `/batch` | Rodar prompts em múltiplos arquivos | Operações em lote |
| `/debug` | Depurar testes/erros falhando | Sessões de debug |
| `/loop` | Rodar prompts em intervalo | Tarefas recorrentes |
| `/claude-api` | Construir apps com a API do Claude | Desenvolvimento com API |

---

## Plugins

Coleções agrupadas de comandos, agentes, servidores MCP e hooks.

### Plugins de exemplo

| Plugin | Descrição | Componentes | Quando usar | Escopo | Instalação |
|--------|-----------|-------------|-------------|--------|------------|
| `pr-review` | Fluxo de revisão de PR | 3 comandos, 3 agentes, MCP do GitHub | Revisões de código | Projeto | `/plugin install pr-review` |
| `devops-automation` | Deployment e monitoramento | 4 comandos, 3 agentes, MCP do K8s | Tarefas de DevOps | Projeto | `/plugin install devops-automation` |
| `documentation` | Suíte de geração de documentação | 4 comandos, 3 agentes, templates | Documentação | Projeto | `/plugin install documentation` |

> **Escopo**: `Projeto` = compartilhado com a equipe, `Usuário` = fluxos pessoais

### Estrutura do plugin

```
.claude-plugin/
├── plugin.json       # Arquivo de manifesto
├── commands/         # Slash Commands
├── agents/           # Subagents
├── skills/           # Skills
├── mcp/              # Configurações MCP
├── hooks/            # Scripts de hook
└── scripts/          # Scripts utilitários
```

**Referência**: [07-plugins/](07-plugins/) | [Documentação oficial](https://code.claude.com/docs/en/plugins)

**Comandos de gerenciamento de plugins**:
```bash
/plugin list              # Listar plugins instalados
/plugin install <name>    # Instalar plugin
/plugin remove <name>     # Remover plugin
/plugin update <name>     # Atualizar plugin
```

---

## Servidores MCP

Servidores Model Context Protocol para acesso a ferramentas e APIs externas.

### Servidores MCP comuns

| Servidor | Descrição | Quando usar | Escopo | Instalação |
|----------|-----------|-------------|--------|------------|
| **GitHub** | Gestão de PR, issues, código | Fluxos com GitHub | Projeto | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | Consultas SQL, acesso a dados | Operações em banco | Projeto | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | Operações avançadas de arquivo | Tarefas complexas de arquivo | Usuário | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | Comunicação com a equipe | Notificações, atualizações | Projeto | Configurar nos settings |
| **Google Docs** | Acesso a documentos | Edição/revisão de docs | Projeto | Configurar nos settings |
| **Asana** | Gerenciamento de projetos | Acompanhamento de tarefas | Projeto | Configurar nos settings |
| **Stripe** | Dados de pagamento | Análise financeira | Projeto | Configurar nos settings |
| **Memory** | Memory persistente | Recuperação entre sessões | Usuário | Configurar nos settings |
| **Context7** | Documentação de bibliotecas | Consulta de docs atualizadas | Nativo | Nativo |

> **Escopo**: `Projeto` = equipe (`.mcp.json`), `Usuário` = pessoal (`~/.claude.json`), `Nativo` = pré-instalado

### Exemplo de configuração MCP

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Referência**: [05-mcp/](05-mcp/) | [Documentação do protocolo MCP](https://modelcontextprotocol.io)

**Instalação rápida (MCP do GitHub)**:
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## Hooks

Automação orientada a eventos que executa comandos shell em eventos do Claude Code.

### Eventos de hook

| Evento | Descrição | Quando é disparado | Casos de uso |
|--------|-----------|--------------------|--------------|
| `SessionStart` | Sessão começa/é retomada | Inicialização da sessão | Tarefas de setup |
| `InstructionsLoaded` | Instruções carregadas | CLAUDE.md ou arquivo de regras carregado | Tratamento customizado de instruções |
| `UserPromptSubmit` | Antes do processamento do prompt | Usuário envia mensagem | Validação de entrada |
| `PreToolUse` | Antes da execução da ferramenta | Antes de qualquer ferramenta rodar | Validação, logging |
| `PermissionRequest` | Caixa de permissão exibida | Antes de ações sensíveis | Fluxos de aprovação personalizados |
| `PostToolUse` | Depois que a ferramenta tem sucesso | Depois de qualquer ferramenta concluir | Formatação, notificações |
| `PostToolUseFailure` | Execução da ferramenta falha | Após erro em ferramenta | Tratamento de erro, logging |
| `Notification` | Notificação enviada | Claude envia notificação | Alertas externos |
| `SubagentStart` | Subagent é criado | Tarefa de Subagent inicia | Inicializar contexto do Subagent |
| `SubagentStop` | Subagent termina | Tarefa de Subagent conclui | Encadear ações |
| `Stop` | Claude termina de responder | Resposta concluída | Cleanup, relatórios |
| `StopFailure` | Erro de API encerra o turno | Erro de API ocorre | Recuperação de erro, logging |
| `TeammateIdle` | Agente parceiro ocioso | Coordenação de equipe de agentes | Distribuir trabalho |
| `TaskCompleted` | Tarefa marcada como concluída | Tarefa finalizada | Processamento pós-tarefa |
| `TaskCreated` | Tarefa criada via TaskCreate | Nova tarefa criada | Rastreamento, logging de tarefas |
| `ConfigChange` | Configuração atualizada | Settings modificados | Reagir a mudanças de config |
| `CwdChanged` | Diretório de trabalho muda | Diretório alterado | Setup específico por diretório |
| `FileChanged` | Arquivo monitorado muda | Arquivo modificado | Monitoramento de arquivos, rebuild |
| `PreCompact` | Antes da operação de compact | Compressão de contexto | Preservação de estado |
| `PostCompact` | Após a compactação concluir | Compactação concluída | Ações pós-compact |
| `WorktreeCreate` | Worktree sendo criada | Git worktree criada | Setup do ambiente da worktree |
| `WorktreeRemove` | Worktree sendo removida | Git worktree removida | Cleanup de recursos da worktree |
| `Elicitation` | Servidor MCP pede entrada | Elicitation MCP | Validação de entrada |
| `ElicitationResult` | Usuário responde à elicitation | Usuário responde | Processamento da resposta |
| `SessionEnd` | Sessão termina | Encerramento da sessão | Cleanup, salvar estado |

### Hooks de exemplo

| Hook | Descrição | Evento | Escopo | Instalação |
|------|-----------|--------|--------|------------|
| `validate-bash.py` | Validação de comandos | PreToolUse:Bash | Projeto | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | Varredura de segurança | PostToolUse:Write | Projeto | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | Autoformatação | PostToolUse:Write | Usuário | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | Validação de prompt | UserPromptSubmit | Projeto | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Rastreio de uso de tokens | Stop | Usuário | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | Validação pré-commit | PreToolUse:Bash | Projeto | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | Log de comandos | PostToolUse:Bash | Usuário | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | Varredura de vulnerabilidades em mudanças de manifesto | PostToolUse:Write | Projeto | `cp 06-hooks/dependency-check.sh .claude/hooks/` |

> **Escopo**: `Projeto` = equipe (`.claude/settings.json`), `Usuário` = pessoal (`~/.claude/settings.json`)

### Configuração de hooks

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**Referência**: [06-hooks/](06-hooks/) | [Documentação oficial](https://code.claude.com/docs/en/hooks)

**Instalação rápida (todos os hooks)**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## Arquivos de Memory

Contexto persistente carregado automaticamente entre sessões.

### Tipos de Memory

| Tipo | Local | Escopo | Quando usar |
|------|-------|--------|-------------|
| **Managed Policy** | Políticas gerenciadas pela organização | Organização | Aplicar padrões em toda a organização |
| **Project** | `./CLAUDE.md` | Projeto (equipe) | Padrões de equipe, contexto do projeto |
| **Project Rules** | `.claude/rules/` | Projeto (equipe) | Regras modulares do projeto |
| **User** | `~/.claude/CLAUDE.md` | Usuário (pessoal) | Preferências pessoais |
| **User Rules** | `~/.claude/rules/` | Usuário (pessoal) | Regras pessoais modulares |
| **Local** | `./CLAUDE.local.md` | Local (ignorado pelo git) | Sobrescritas específicas da máquina (não aparece nas docs oficiais em março de 2026; pode ser legado) |
| **Auto Memory** | Automático | Sessão | Insights e correções capturados automaticamente |

> **Escopo**: `Organização` = gerenciado por admins, `Projeto` = compartilhado com a equipe via git, `Usuário` = preferências pessoais, `Local` = não commitado, `Sessão` = auto-gerenciado

**Referência**: [02-memory/](02-memory/) | [Documentação oficial](https://code.claude.com/docs/en/memory)

**Instalação rápida**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## Novos recursos (abril de 2026)

| Recurso | Descrição | Como usar |
|---------|-----------|-----------|
| **/focus** | Alternar modo foco para saída sem distrações (v2.1.110) | Rode `/focus` para reduzir o ruído visual em tarefas longas |
| **/proactive** | Alias para `/loop` — mesmo comportamento de tarefas recorrentes (v2.1.105) | Use `/proactive` de forma intercambiável com `/loop` |
| **/recap** | Mostrar uma recapitulação da sessão ao retornar a uma sessão existente (v2.1.108) | Rode `/recap` após um período ausente para obter contexto do que foi feito |
| **/tui** | Alternar modo TUI (text user interface) em tela cheia para renderização sem flicker (v2.1.110) | Use `/tui` em terminais fullscreen ou tmux |
| **/undo** | Alias para `/rewind` — retorna ao checkpoint anterior (v2.1.108) | Use `/undo` de forma intercambiável com `/rewind` |
| **Ferramenta Monitor** | Observar o stream de stdout de um comando em background e reagir a eventos em vez de ficar fazendo polling (v2.1.98+) | Use a ferramenta Monitor via [Funcionalidades avançadas](09-advanced-features/) |
| **/team-onboarding** | Gerar automaticamente um guia de ramp-up a partir da configuração do Claude Code no projeto (v2.1.101) | Rode `/team-onboarding` no seu projeto |
| **Ultraplan auto-create** | Ambiente cloud criado automaticamente na primeira invocação de `/ultraplan` — sem setup manual (v2.1.101) | Use `/ultraplan <prompt>` |
| **Controle remoto** | Controlar sessões do Claude Code remotamente via API | Use a API de controle remoto para enviar prompts e receber respostas programaticamente |
| **Sessões web** | Rodar o Claude Code em ambiente baseado em navegador | Acesse via `claude web` ou pelo Anthropic Console |
| **App Desktop** | Aplicação desktop nativa do Claude Code | Use `/desktop` ou baixe pelo site da Anthropic |
| **Agent Teams** | Coordenar múltiplos agentes trabalhando em tarefas relacionadas | Configure agentes parceiros que colaboram e compartilham contexto |
| **Lista de tarefas** | Gestão e monitoramento de tarefas em background | Use `/tasks` para ver e gerenciar operações em background |
| **Sugestões de prompt** | Sugestões de comandos cientes de contexto | Sugestões aparecem automaticamente com base no contexto |
| **Git worktrees** | Worktrees git isoladas para desenvolvimento paralelo | Use comandos de worktree para trabalho paralelo seguro |
| **Sandboxing** | Ambientes de execução isolados por segurança | Use `/sandbox` para alternar; roda comandos em ambientes restritos |
| **OAuth em MCP** | Autenticação OAuth para servidores MCP | Configure credenciais OAuth nos settings do servidor MCP para acesso seguro |
| **Busca de ferramentas MCP** | Buscar e descobrir ferramentas MCP dinamicamente | Use a busca para encontrar ferramentas disponíveis entre servidores conectados |
| **Tarefas agendadas** | Tarefas recorrentes com `/loop` e ferramentas cron | Use `/loop 5m /command` ou a ferramenta CronCreate |
| **Integração Chrome** | Automação de navegador com Chromium headless | Use a flag `--chrome` ou o comando `/chrome` |
| **Personalização de teclado** | Customizar keybindings, incluindo suporte a chord | Use `/keybindings` ou edite `~/.claude/keybindings.json` |
| **Auto Mode** | Operação totalmente autônoma sem prompts de permissão (Research Preview) | Use `--mode auto` ou `/permissions auto`; março de 2026 |
| **Canais** | Comunicação multicanal (Telegram, Slack etc.) (Research Preview) | Configure plugins de canais; março de 2026 |
| **Ditado de voz** | Entrada por voz para prompts | Use o ícone de microfone ou o keybinding de voz |
| **Tipo de hook Agent** | Hooks que invocam um Subagent em vez de rodar um comando shell | Defina `"type": "agent"` na configuração do hook |
| **Tipo de hook Prompt** | Hooks que injetam texto de prompt na conversa | Defina `"type": "prompt"` na configuração do hook |
| **MCP Elicitation** | Servidores MCP podem pedir entrada do usuário durante a execução de ferramentas | Trate via eventos `Elicitation` e `ElicitationResult` |
| **Suporte a LSP em plugins** | Integração com Language Server Protocol via plugins | Configure servidores LSP em `plugin.json` para recursos do editor |
| **Managed Drop-ins** | Configurações drop-in gerenciadas pela organização (v2.1.83) | Configurado por admins via managed policies; aplicado automaticamente a todos os usuários |

---

## Matriz de referência rápida

### Guia de seleção de funcionalidades

| Necessidade | Recurso recomendado | Por quê |
|-------------|---------------------|---------|
| Atalho rápido | Slash Command | Manual, imediato |
| Contexto persistente | Memory | Carregado automaticamente |
| Automação complexa | Skill | Autoinvocada |
| Tarefa especializada | Subagent | Contexto isolado |
| Dados externos | Servidor MCP | Acesso em tempo real |
| Automação por evento | Hook | Disparado por evento |
| Solução completa | Plugin | Pacote tudo-em-um |

### Prioridade de instalação

| Prioridade | Recurso | Comando |
|------------|---------|---------|
| 1. Essencial | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. Uso diário | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. Qualidade | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. Automação | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. Externo | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. Avançado | Skills | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. Completo | Plugins | `/plugin install pr-review` |

---

## Instalação completa em um comando

Instale todos os exemplos deste repositório:

```bash
# Criar diretórios
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# Instalar todas as features
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## Recursos adicionais

- [Documentação oficial do Claude Code](https://code.claude.com/docs/en/overview)
- [Especificação do protocolo MCP](https://modelcontextprotocol.io)
- [Roteiro de aprendizado](LEARNING-ROADMAP.md)
- [README principal](README.md)

---

**Última atualização**: 16 de abril de 2026
**Versão do Claude Code**: 2.1.112
**Fontes**:
- https://docs.anthropic.com/en/docs/claude-code
- https://www.anthropic.com/news/claude-opus-4-7
- https://support.claude.com/en/articles/12138966-release-notes
**Modelos Compatíveis**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
