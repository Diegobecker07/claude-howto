<!-- i18n-source: INDEX.md -->
<!-- i18n-source-sha: 2deba3a -->
<!-- i18n-date: 2026-04-16 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Exemplos do Claude Code — Índice Completo

Este documento fornece um índice completo de todos os arquivos de exemplo organizados por tipo de funcionalidade.

## Estatísticas gerais

- **Total de arquivos**: 100+ arquivos
- **Categorias**: 10 categorias de funcionalidades
- **Plugins**: 3 plugins completos
- **Skills**: 6 skills completas
- **Hooks**: 8 hooks de exemplo
- **Prontos para uso**: todos os exemplos

---

## 01. Comandos slash (10 arquivos)

Atalhos iniciados pelo usuário para fluxos comuns.

| Arquivo | Descrição | Caso de uso |
|---------|-----------|-------------|
| `optimize.md` | Analisador de otimização de código | Encontrar problemas de performance |
| `pr.md` | Preparação de pull request | Automação do fluxo de PR |
| `generate-api-docs.md` | Gerador de documentação de API | Gerar docs de API |
| `commit.md` | Auxiliar de mensagem de commit | Commits padronizados |
| `setup-ci-cd.md` | Configuração de pipeline CI/CD | Automação DevOps |
| `push-all.md` | Push de todas as alterações | Fluxo rápido de push |
| `unit-test-expand.md` | Expandir cobertura de testes unitários | Automação de testes |
| `doc-refactor.md` | Refatoração de documentação | Melhorias de docs |
| `pr-slash-command.png` | Captura de tela de exemplo | Referência visual |
| `README.md` | Documentação | Guia de instalação e uso |

**Caminho de instalação**: `.claude/commands/`

**Uso**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Memória (6 arquivos)

Contexto persistente e padrões do projeto.

| Arquivo | Descrição | Escopo | Local |
|---------|-----------|--------|-------|
| `project-CLAUDE.md` | Padrões de projeto da equipe | Projeto inteiro | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | Regras específicas de API | Diretório | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Preferências pessoais | Usuário | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Captura: memória salva | - | Referência visual |
| `memory-ask-claude.png` | Captura: perguntando ao Claude | - | Referência visual |
| `README.md` | Documentação | - | Referência |

**Instalação**: copiar para o local apropriado

**Uso**: carregado automaticamente pelo Claude

---

## 03. Skills (28 arquivos)

Capacidades autoinvocadas com scripts e templates.

### Skill de Code Review (5 arquivos)
```
code-review/
├── SKILL.md                          # Definição da skill
├── scripts/
│   ├── analyze-metrics.py            # Analisador de métricas de código
│   └── compare-complexity.py         # Comparação de complexidade
└── templates/
    ├── review-checklist.md           # Checklist de revisão
    └── finding-template.md           # Documentação de achados
```

**Objetivo**: revisão abrangente de código com análise de segurança, performance e qualidade

**Autoinvocada**: ao revisar código

---

### Skill de Brand Voice (4 arquivos)
```
brand-voice/
├── SKILL.md                          # Definição da skill
├── templates/
│   ├── email-template.txt            # Formato de e-mail
│   └── social-post-template.txt      # Formato de post em redes sociais
└── tone-examples.md                  # Exemplos de mensagens
```

**Objetivo**: garantir voz de marca consistente nas comunicações

**Autoinvocada**: ao criar materiais de marketing

---

### Skill de Documentation Generator (2 arquivos)
```
doc-generator/
├── SKILL.md                          # Definição da skill
└── generate-docs.py                  # Extrator de docs em Python
```

**Objetivo**: gerar documentação de API abrangente a partir do código-fonte

**Autoinvocada**: ao criar/atualizar documentação de API

---

### Skill de Refactor (5 arquivos)
```
refactor/
├── SKILL.md                          # Definição da skill
├── scripts/
│   ├── analyze-complexity.py         # Analisador de complexidade
│   └── detect-smells.py              # Detector de code smells
├── references/
│   ├── code-smells.md                # Catálogo de code smells
│   └── refactoring-catalog.md        # Padrões de refatoração
└── templates/
    └── refactoring-plan.md           # Template de plano de refatoração
```

**Objetivo**: refatoração sistemática de código com análise de complexidade

**Autoinvocada**: ao refatorar código

---

### Skill Claude MD (1 arquivo)
```
claude-md/
└── SKILL.md                          # Definição da skill
```

**Objetivo**: gerenciar e otimizar arquivos CLAUDE.md

---

### Skill de Blog Draft (3 arquivos)
```
blog-draft/
├── SKILL.md                          # Definição da skill
└── templates/
    ├── draft-template.md             # Template de rascunho de blog
    └── outline-template.md           # Template de roteiro de blog
```

**Objetivo**: redigir posts de blog com estrutura consistente

**Mais**: `README.md` — visão geral e guia de uso das skills

**Caminho de instalação**: `~/.claude/skills/` ou `.claude/skills/`

---

## 04. Subagentes (9 arquivos)

Assistentes de IA especializados com capacidades personalizadas.

| Arquivo | Descrição | Ferramentas | Caso de uso |
|---------|-----------|-------------|-------------|
| `code-reviewer.md` | Análise de qualidade de código | read, grep, diff, lint_runner | Revisões abrangentes |
| `test-engineer.md` | Análise de cobertura de testes | read, write, bash, grep | Automação de testes |
| `documentation-writer.md` | Criação de documentação | read, write, grep | Geração de docs |
| `secure-reviewer.md` | Revisão de segurança (somente leitura) | read, grep | Auditorias de segurança |
| `implementation-agent.md` | Implementação completa | read, write, bash, grep, edit, glob | Desenvolvimento de features |
| `debugger.md` | Especialista em depuração | read, bash, grep | Investigação de bugs |
| `data-scientist.md` | Especialista em análise de dados | read, write, bash | Fluxos de dados |
| `clean-code-reviewer.md` | Padrões de clean code | read, grep | Qualidade de código |
| `README.md` | Documentação | - | Guia de instalação e uso |

**Caminho de instalação**: `.claude/agents/`

**Uso**: delegado automaticamente pelo agente principal

---

## 05. Protocolo MCP (5 arquivos)

Integrações com ferramentas externas e APIs.

| Arquivo | Descrição | Integra com | Caso de uso |
|---------|-----------|-------------|-------------|
| `github-mcp.json` | Integração GitHub | GitHub API | Gestão de PRs/issues |
| `database-mcp.json` | Consultas a banco de dados | PostgreSQL/MySQL | Consultas ao vivo |
| `filesystem-mcp.json` | Operações de arquivo | Sistema de arquivos local | Gerenciamento de arquivos |
| `multi-mcp.json` | Múltiplos servidores | GitHub + BD + Slack | Integração completa |
| `README.md` | Documentação | - | Guia de instalação e uso |

**Caminho de instalação**: `.mcp.json` (escopo de projeto) ou `~/.claude.json` (escopo de usuário)

**Uso**: `/mcp__github__list_prs`, etc.

---

## 06. Hooks (9 arquivos)

Scripts de automação acionados por eventos, executados automaticamente.

| Arquivo | Descrição | Evento | Caso de uso |
|---------|-----------|--------|-------------|
| `format-code.sh` | Autoformatação de código | PreToolUse:Write | Formatação de código |
| `pre-commit.sh` | Rodar testes antes do commit | PreToolUse:Bash | Automação de testes |
| `security-scan.sh` | Varredura de segurança | PostToolUse:Write | Checagens de segurança |
| `log-bash.sh` | Logar comandos bash | PostToolUse:Bash | Log de comandos |
| `validate-prompt.sh` | Validar prompts | PreToolUse | Validação de entrada |
| `notify-team.sh` | Enviar notificações | Notification | Notificações de equipe |
| `context-tracker.py` | Rastrear uso da janela de contexto | PostToolUse | Monitoramento de contexto |
| `context-tracker-tiktoken.py` | Rastreio baseado em tokens | PostToolUse | Contagem precisa de tokens |
| `README.md` | Documentação | - | Guia de instalação e uso |

**Caminho de instalação**: configurar em `~/.claude/settings.json`

**Uso**: configurados nos settings, executados automaticamente

**Tipos de hooks** (4 tipos, 25 eventos):
- Tool Hooks: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Session Hooks: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Task Hooks: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Lifecycle Hooks: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Plugins (3 plugins completos, 40 arquivos)

Coleções agrupadas de funcionalidades.

### Plugin PR Review (10 arquivos)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Manifesto do plugin
├── commands/
│   ├── review-pr.md                  # Revisão abrangente
│   ├── check-security.md             # Verificação de segurança
│   └── check-tests.md                # Verificação de cobertura de testes
├── agents/
│   ├── security-reviewer.md          # Especialista em segurança
│   ├── test-checker.md               # Especialista em testes
│   └── performance-analyzer.md       # Especialista em performance
├── mcp/
│   └── github-config.json            # Integração GitHub
├── hooks/
│   └── pre-review.js                 # Validação pré-revisão
└── README.md                         # Documentação do plugin
```

**Funcionalidades**: análise de segurança, cobertura de testes, impacto em performance

**Comandos**: `/review-pr`, `/check-security`, `/check-tests`

**Instalação**: `/plugin install pr-review`

---

### Plugin DevOps Automation (15 arquivos)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Manifesto do plugin
├── commands/
│   ├── deploy.md                     # Deployment
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # Status do sistema
│   └── incident.md                   # Resposta a incidentes
├── agents/
│   ├── deployment-specialist.md      # Especialista em deployment
│   ├── incident-commander.md         # Coordenador de incidentes
│   └── alert-analyzer.md             # Analista de alertas
├── mcp/
│   └── kubernetes-config.json        # Integração Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # Checagens pré-deployment
│   └── post-deploy.js                # Tarefas pós-deployment
├── scripts/
│   ├── deploy.sh                     # Automação de deployment
│   ├── rollback.sh                   # Automação de rollback
│   └── health-check.sh               # Checagens de saúde
└── README.md                         # Documentação do plugin
```

**Funcionalidades**: deployment Kubernetes, rollback, monitoramento, resposta a incidentes

**Comandos**: `/deploy`, `/rollback`, `/status`, `/incident`

**Instalação**: `/plugin install devops-automation`

---

### Plugin Documentation (14 arquivos)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Manifesto do plugin
├── commands/
│   ├── generate-api-docs.md          # Geração de docs de API
│   ├── generate-readme.md            # Criação de README
│   ├── sync-docs.md                  # Sincronização de docs
│   └── validate-docs.md              # Validação de docs
├── agents/
│   ├── api-documenter.md             # Especialista em docs de API
│   ├── code-commentator.md           # Especialista em comentários de código
│   └── example-generator.md          # Criador de exemplos
├── mcp/
│   └── github-docs-config.json       # Integração GitHub
├── templates/
│   ├── api-endpoint.md               # Template de endpoint de API
│   ├── function-docs.md              # Template de doc de função
│   └── adr-template.md               # Template de ADR
└── README.md                         # Documentação do plugin
```

**Funcionalidades**: docs de API, geração de README, sync de docs, validação

**Comandos**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Instalação**: `/plugin install documentation`

**Mais**: `README.md` — visão geral e guia de uso dos plugins

---

## 08. Checkpoints e Rewind (2 arquivos)

Salve o estado da conversa e explore abordagens alternativas.

| Arquivo | Descrição | Conteúdo |
|---------|-----------|----------|
| `README.md` | Documentação | Guia abrangente de checkpoints |
| `checkpoint-examples.md` | Exemplos reais | Migração de banco, otimização de performance, iteração de UI, depuração |
| | | |

**Conceitos-chave**:
- **Checkpoint**: snapshot do estado da conversa
- **Rewind**: retornar a um checkpoint anterior
- **Branch Point**: explorar múltiplas abordagens

**Uso**:
```
# Checkpoints são criados automaticamente a cada prompt do usuário
# Para voltar, pressione Esc duas vezes ou use:
/rewind
# Então escolha: Restaurar código e conversa, Restaurar conversa,
# Restaurar código, Resumir a partir daqui, ou Cancelar
```

**Casos de uso**:
- Testar implementações diferentes
- Recuperar-se de erros
- Experimentação segura
- Comparar soluções
- Testes A/B

---

## 09. Funcionalidades avançadas (3 arquivos)

Capacidades avançadas para fluxos complexos.

| Arquivo | Descrição | Recursos |
|---------|-----------|----------|
| `README.md` | Guia completo | Documentação de todas as funcionalidades avançadas |
| `config-examples.json` | Exemplos de configuração | 10+ configurações específicas por caso de uso |
| `planning-mode-examples.md` | Exemplos de planejamento | REST API, migração de banco, refatoração |
| Tarefas agendadas | Tarefas recorrentes com `/loop` e ferramentas cron | Fluxos recorrentes automatizados |
| Integração Chrome | Automação de navegador via Chromium headless | Testes web e scraping |
| Controle remoto (expandido) | Métodos de conexão, segurança, tabela comparativa | Gerenciamento de sessões remotas |
| Personalização de teclado | Keybindings customizados, suporte a chord, contextos | Atalhos personalizados |
| App Desktop (expandido) | Conectores, launch.json, recursos enterprise | Integração desktop |
| | | |

**Funcionalidades avançadas cobertas**:

### Modo de planejamento (Planning Mode)
- Criar planos de implementação detalhados
- Estimativas de tempo e avaliação de risco
- Decomposição sistemática de tarefas

### Pensamento estendido (Extended Thinking)
- Raciocínio profundo para problemas complexos
- Análise de decisões arquiteturais
- Avaliação de trade-offs

### Tarefas em background
- Operações longas sem bloquear
- Fluxos de desenvolvimento em paralelo
- Gerenciamento e monitoramento de tarefas

### Modos de permissão
- **default**: pedir aprovação em ações arriscadas
- **acceptEdits**: aceitar edições de arquivo automaticamente, perguntar nas demais
- **plan**: análise somente leitura, sem modificações
- **auto**: aprovar automaticamente ações seguras, perguntar nas arriscadas
- **dontAsk**: aceitar todas as ações exceto as arriscadas
- **bypassPermissions**: aceitar tudo (requer `--dangerously-skip-permissions`)

### Modo headless (`claude -p`)
- Integração CI/CD
- Execução automática de tarefas
- Processamento em lote

### Gerenciamento de sessões
- Múltiplas sessões de trabalho
- Troca e salvamento de sessões
- Persistência de sessões

### Recursos interativos
- Atalhos de teclado
- Histórico de comandos
- Autocompletar com tab
- Entrada multilinha

### Configuração
- Gerenciamento abrangente de settings
- Configurações por ambiente
- Personalização por projeto

### Tarefas agendadas
- Tarefas recorrentes com o comando `/loop`
- Ferramentas cron: CronCreate, CronList, CronDelete
- Fluxos recorrentes automatizados

### Integração Chrome
- Automação de navegador via Chromium headless
- Capacidades de testes web e scraping
- Interação com páginas e extração de dados

### Controle remoto (expandido)
- Métodos e protocolos de conexão
- Considerações de segurança e boas práticas
- Tabela comparativa de opções de acesso remoto

### Personalização de teclado
- Configuração de keybindings personalizados
- Suporte a chord para atalhos com múltiplas teclas
- Ativação contextual de keybindings

### App Desktop (expandido)
- Conectores para integração com IDE
- Configuração do `launch.json`
- Recursos e implantação enterprise

---

## 10. Uso da CLI (1 arquivo)

Padrões de uso e referência da interface de linha de comando.

| Arquivo | Descrição | Conteúdo |
|---------|-----------|----------|
| `README.md` | Documentação da CLI | Flags, opções e padrões de uso |

**Recursos-chave da CLI**:
- `claude` — iniciar sessão interativa
- `claude -p "prompt"` — modo headless / não interativo
- `claude web` — abrir sessão web
- `claude --model` — selecionar modelo (Sonnet 4.6, Opus 4.7)
- `claude --permission-mode` — definir modo de permissão
- `claude --remote` — habilitar controle remoto via WebSocket

---

## Arquivos de documentação (13 arquivos)

| Arquivo | Local | Descrição |
|---------|-------|-----------|
| `README.md` | `/` | Visão geral dos exemplos |
| `INDEX.md` | `/` | Este índice completo |
| `QUICK_REFERENCE.md` | `/` | Cartão de referência rápida |
| `README.md` | `/01-slash-commands/` | Guia de comandos slash |
| `README.md` | `/02-memory/` | Guia de memória |
| `README.md` | `/03-skills/` | Guia de skills |
| `README.md` | `/04-subagents/` | Guia de subagentes |
| `README.md` | `/05-mcp/` | Guia de MCP |
| `README.md` | `/06-hooks/` | Guia de hooks |
| `README.md` | `/07-plugins/` | Guia de plugins |
| `README.md` | `/08-checkpoints/` | Guia de checkpoints |
| `README.md` | `/09-advanced-features/` | Guia de funcionalidades avançadas |
| `README.md` | `/10-cli/` | Guia da CLI |

---

## Árvore de arquivos completa

```
claude-howto/
├── README.md                                    # Visão geral
├── INDEX.md                                     # Este arquivo
├── QUICK_REFERENCE.md                           # Cartão de referência rápida
├── claude_concepts_guide.md                     # Guia original
│
├── 01-slash-commands/                           # Comandos slash
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # Memória
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Skills
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # Subagentes
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # Protocolo MCP
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Hooks
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # Plugins
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # Checkpoints
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Funcionalidades avançadas
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # Uso da CLI
    └── README.md
```

---

## Início rápido por caso de uso

### Qualidade de código e revisões
```bash
# Instalar comando slash
cp 01-slash-commands/optimize.md .claude/commands/

# Instalar subagente
cp 04-subagents/code-reviewer.md .claude/agents/

# Instalar skill
cp -r 03-skills/code-review ~/.claude/skills/

# Ou instalar plugin completo
/plugin install pr-review
```

### DevOps e deployment
```bash
# Instalar plugin (inclui tudo)
/plugin install devops-automation
```

### Documentação
```bash
# Instalar comando slash
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Instalar subagente
cp 04-subagents/documentation-writer.md .claude/agents/

# Instalar skill
cp -r 03-skills/doc-generator ~/.claude/skills/

# Ou instalar plugin completo
/plugin install documentation
```

### Padrões de equipe
```bash
# Configurar memória do projeto
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Editar para refletir os padrões da sua equipe
```

### Integrações externas
```bash
# Definir variáveis de ambiente
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Instalar configuração MCP (escopo de projeto)
cp 05-mcp/multi-mcp.json .mcp.json
```

### Automação e validação
```bash
# Instalar hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Configurar hooks nos settings (~/.claude/settings.json)
# Veja 06-hooks/README.md
```

### Experimentação segura
```bash
# Checkpoints são criados automaticamente a cada prompt do usuário
# Para retroceder: pressione Esc+Esc ou use /rewind
# Depois escolha o que restaurar no menu de rewind

# Veja 08-checkpoints/README.md para exemplos
```

### Fluxos avançados
```bash
# Configurar recursos avançados
# Veja 09-advanced-features/config-examples.json

# Usar modo de planejamento
/plan Implement feature X

# Usar modos de permissão
claude --permission-mode plan          # Para revisão de código (somente leitura)
claude --permission-mode acceptEdits   # Aceitar edições automaticamente
claude --permission-mode auto          # Aprovar ações seguras automaticamente

# Executar em modo headless para CI/CD
claude -p "Run tests and report results"

# Executar tarefas em background
Run tests in background

# Veja 09-advanced-features/README.md para o guia completo
```

---

## Matriz de cobertura de funcionalidades

| Categoria | Comandos | Agentes | MCP | Hooks | Scripts | Templates | Docs | Imagens | Total |
|-----------|----------|---------|-----|-------|---------|-----------|------|---------|-------|
| **01 Comandos slash** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Memória** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Skills** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Subagentes** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Hooks** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Plugins** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Checkpoints** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Avançadas** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## Trilha de aprendizado

### Iniciante (Semana 1)
1. ✅ Leia `README.md`
2. ✅ Instale 1–2 comandos slash
3. ✅ Crie arquivo de memória do projeto
4. ✅ Experimente comandos básicos

### Intermediário (Semana 2–3)
1. ✅ Configure o MCP do GitHub
2. ✅ Instale um subagente
3. ✅ Experimente delegar tarefas
4. ✅ Instale uma skill

### Avançado (Semana 4+)
1. ✅ Instale um plugin completo
2. ✅ Crie comandos slash personalizados
3. ✅ Crie um subagente personalizado
4. ✅ Crie uma skill personalizada
5. ✅ Construa seu próprio plugin

### Especialista (Semana 5+)
1. ✅ Configure hooks para automação
2. ✅ Use checkpoints para experimentação
3. ✅ Configure o modo de planejamento
4. ✅ Use modos de permissão com eficácia
5. ✅ Configure o modo headless para CI/CD
6. ✅ Domine o gerenciamento de sessões

---

## Busca por palavra-chave

### Performance
- `01-slash-commands/optimize.md` — análise de performance
- `04-subagents/code-reviewer.md` — revisão de performance
- `03-skills/code-review/` — métricas de performance
- `07-plugins/pr-review/agents/performance-analyzer.md` — especialista em performance

### Segurança
- `04-subagents/secure-reviewer.md` — revisão de segurança
- `03-skills/code-review/` — análise de segurança
- `07-plugins/pr-review/` — checagens de segurança

### Testes
- `04-subagents/test-engineer.md` — engenheiro de testes
- `07-plugins/pr-review/commands/check-tests.md` — cobertura de testes

### Documentação
- `01-slash-commands/generate-api-docs.md` — comando de docs de API
- `04-subagents/documentation-writer.md` — agente redator de docs
- `03-skills/doc-generator/` — skill de geração de docs
- `07-plugins/documentation/` — plugin completo de documentação

### Deployment
- `07-plugins/devops-automation/` — solução completa de DevOps

### Automação
- `06-hooks/` — automação orientada a eventos
- `06-hooks/pre-commit.sh` — automação pré-commit
- `06-hooks/format-code.sh` — autoformatação
- `09-advanced-features/` — modo headless para CI/CD

### Validação
- `06-hooks/security-scan.sh` — validação de segurança
- `06-hooks/validate-prompt.sh` — validação de prompt

### Experimentação
- `08-checkpoints/` — experimentação segura com rewind
- `08-checkpoints/checkpoint-examples.md` — exemplos reais

### Planejamento
- `09-advanced-features/planning-mode-examples.md` — exemplos de modo de planejamento
- `09-advanced-features/README.md` — pensamento estendido

### Configuração
- `09-advanced-features/config-examples.json` — exemplos de configuração

---

## Notas

- Todos os exemplos estão prontos para uso
- Modifique conforme suas necessidades específicas
- Os exemplos seguem as boas práticas do Claude Code
- Cada categoria tem seu próprio README com instruções detalhadas
- Os scripts incluem tratamento adequado de erros
- Os templates são personalizáveis

---

## Como contribuir

Quer adicionar mais exemplos? Siga a estrutura:
1. Crie o subdiretório apropriado
2. Inclua um `README.md` com instruções de uso
3. Siga as convenções de nomenclatura
4. Teste cuidadosamente
5. Atualize este índice

---

**Última atualização**: 16 de abril de 2026
**Versão do Claude Code**: 2.1.112
**Fontes**:
- https://docs.anthropic.com/en/docs/claude-code
- https://www.anthropic.com/news/claude-opus-4-7
- https://support.claude.com/en/articles/12138966-release-notes
**Modelos Compatíveis**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
**Total de exemplos**: 100+ arquivos
**Categorias**: 10 funcionalidades
**Hooks**: 8 scripts de automação
**Exemplos de configuração**: 10+ cenários
**Prontos para uso**: todos os exemplos
