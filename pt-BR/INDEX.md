<!-- i18n-source: INDEX.md -->
<!-- i18n-source-sha: 9c224ff -->
<!-- i18n-date: 2026-04-14 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Examples - Índice Completo

Este documento reúne um índice completo de todos os arquivos de exemplo organizados por tipo de recurso.

## Estatísticas Resumidas

- **Total de arquivos**: 100+ arquivos
- **Categorias**: 10 categorias de funcionalidades
- **Plugins**: 3 plugins completos
- **Skills**: 6 skills completas
- **Hooks**: 8 exemplos de hooks
- **Pronto para uso**: Todos os exemplos

---

## 01. Slash Commands (10 arquivos)

Atalhos acionados pelo usuário para fluxos de trabalho comuns.

| Arquivo | Descrição | Caso de uso |
|------|-------------|----------|
| `optimize.md` | Analisador de otimização de código | Encontrar problemas de performance |
| `pr.md` | Preparação de pull request | Automação do fluxo de PR |
| `generate-api-docs.md` | Gerador de documentação de API | Criar docs de API |
| `commit.md` | Assistente de mensagem de commit | Commits padronizados |
| `setup-ci-cd.md` | Configuração de pipeline CI/CD | Automação DevOps |
| `push-all.md` | Enviar todas as mudanças | Fluxo rápido de push |
| `unit-test-expand.md` | Expandir cobertura de testes unitários | Automação de testes |
| `doc-refactor.md` | Refatoração de documentação | Melhorias de documentação |
| `pr-slash-command.png` | Exemplo em screenshot | Referência visual |
| `README.md` | Documentação | Guia de configuração e uso |

**Caminho de instalação**: `.claude/commands/`

**Uso**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Memory (6 arquivos)

Contexto persistente e padrões do projeto.

| Arquivo | Descrição | Escopo | Localização |
|------|------|---------|-------------|
| `project-CLAUDE.md` | Padrões do time e do projeto | Projeto inteiro | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | Regras específicas da API | Diretório | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Preferências pessoais | Usuário | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Screenshot: memória salva | - | Referência visual |
| `memory-ask-claude.png` | Screenshot: perguntar ao Claude | - | Referência visual |
| `README.md` | Documentação | - | Referência |

**Instalação**: Copie para o local apropriado

**Uso**: Carregado automaticamente pelo Claude

---

## 03. Skills (28 arquivos)

Capacidades auto-invocadas com scripts e templates.

### Skill Code Review (5 arquivos)

```text
code-review/
├── SKILL.md                          # Definição da skill
├── scripts/
│   ├── analyze-metrics.py            # Analisador de métricas de código
│   └── compare-complexity.py         # Comparação de complexidade
└── templates/
    ├── review-checklist.md           # Checklist de revisão
    └── finding-template.md           # Template de achados
```

**Objetivo**: Revisão de código abrangente com análise de segurança, performance e qualidade

**Auto-invocada**: Ao revisar código

---

### Skill Brand Voice (4 arquivos)

```text
brand-voice/
├── SKILL.md                          # Definição da skill
├── templates/
│   ├── email-template.txt            # Formato de e-mail
│   └── social-post-template.txt      # Formato de post social
└── tone-examples.md                  # Exemplos de mensagens
```

**Objetivo**: Manter consistência de voz da marca na comunicação

**Auto-invocada**: Ao criar texto de marketing

---

### Skill Documentation Generator (2 arquivos)

```text
doc-generator/
├── SKILL.md                          # Definição da skill
└── generate-docs.py                  # Extrator de documentação em Python
```

**Objetivo**: Gerar documentação de API a partir do código-fonte

**Auto-invocada**: Ao criar ou atualizar documentação de API

---

### Skill Refactor (5 arquivos)

```text
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

**Objetivo**: Refatoração sistemática com análise de complexidade

**Auto-invocada**: Ao refatorar código

---

### Skill Claude MD (1 arquivo)

```text
claude-md/
└── SKILL.md                          # Definição da skill
```

**Objetivo**: Gerenciar e otimizar arquivos `CLAUDE.md`

---

### Skill Blog Draft (3 arquivos)

```text
blog-draft/
├── SKILL.md                          # Definição da skill
└── templates/
    ├── draft-template.md             # Template de rascunho de blog
    └── outline-template.md           # Template de estrutura de blog
```

**Objetivo**: Criar rascunhos de posts com estrutura consistente

**Além disso**: `README.md` - visão geral das skills e guia de uso

**Caminho de instalação**: `~/.claude/skills/` ou `.claude/skills/`

---

## 04. Subagents (9 arquivos)

Assistentes de IA especializados com capacidades personalizadas.

| Arquivo | Descrição | Ferramentas | Caso de uso |
|------|------|-------------|----------|
| `code-reviewer.md` | Análise de qualidade de código | read, grep, diff, lint_runner | Revisões completas |
| `test-engineer.md` | Análise de cobertura de testes | read, write, bash, grep | Automação de testes |
| `documentation-writer.md` | Criação de documentação | read, write, grep | Geração de docs |
| `secure-reviewer.md` | Revisão de segurança (somente leitura) | read, grep | Auditorias de segurança |
| `implementation-agent.md` | Implementação completa | read, write, bash, grep, edit, glob | Desenvolvimento de funcionalidades |
| `debugger.md` | Especialista em depuração | read, bash, grep | Investigação de bugs |
| `data-scientist.md` | Especialista em análise de dados | read, write, bash | Fluxos de dados |
| `clean-code-reviewer.md` | Padrões de Clean Code | read, grep | Qualidade de código |
| `README.md` | Documentação | - | Guia de configuração e uso |

**Caminho de instalação**: `.claude/agents/`

**Uso**: Delegação automática pelo agente principal

---

## 05. MCP Protocol (5 arquivos)

Integrações com ferramentas externas e APIs.

| Arquivo | Descrição | Integra com | Caso de uso |
|------|------|-------------|----------|
| `github-mcp.json` | Integração com GitHub | GitHub API | Gestão de PR/issues |
| `database-mcp.json` | Consultas a banco | PostgreSQL/MySQL | Consultas de dados |
| `filesystem-mcp.json` | Operações de arquivo | Sistema de arquivos local | Gerenciamento de arquivos |
| `multi-mcp.json` | Vários servidores | GitHub + DB + Slack | Integração completa |
| `README.md` | Documentação | - | Guia de configuração e uso |

**Caminho de instalação**: `.mcp.json` (escopo do projeto) ou `~/.claude.json` (escopo do usuário)

**Uso**: `/mcp__github__list_prs`, etc.

---

## 06. Hooks (9 arquivos)

Scripts de automação orientados a eventos executados automaticamente.

| Arquivo | Descrição | Evento | Caso de uso |
|------|------|-------|----------|
| `format-code.sh` | Autoformatação de código | PreToolUse:Write | Formatação |
| `pre-commit.sh` | Executa testes antes do commit | PreToolUse:Bash | Automação de testes |
| `security-scan.sh` | Varredura de segurança | PostToolUse:Write | Verificações de segurança |
| `log-bash.sh` | Log de comandos bash | PostToolUse:Bash | Registro de comandos |
| `validate-prompt.sh` | Validação de prompts | PreToolUse | Validação de entrada |
| `notify-team.sh` | Envio de notificações | Notification | Comunicação com a equipe |
| `context-tracker.py` | Uso do contexto da sessão | PostToolUse | Monitoramento de contexto |
| `context-tracker-tiktoken.py` | Rastreamento por tokens | PostToolUse | Contagem precisa de tokens |
| `README.md` | Documentação | - | Guia de configuração e uso |

**Caminho de instalação**: Configure em `~/.claude/settings.json`

**Uso**: Configurado em settings, executado automaticamente

---

## 07. Plugins (3 plugins completos, 40 arquivos)

Conjuntos empacotados de funcionalidades.

### PR Review Plugin (10 arquivos)

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Manifesto do plugin
├── commands/
│   ├── review-pr.md                  # Revisão completa
│   ├── check-security.md             # Verificação de segurança
│   └── check-tests.md                # Verificação de cobertura de testes
├── agents/
│   ├── security-reviewer.md          # Especialista em segurança
│   ├── test-checker.md               # Especialista em testes
│   └── performance-analyzer.md       # Especialista em performance
├── mcp/
│   └── github-config.json            # Integração com GitHub
├── hooks/
│   └── pre-review.js                 # Validação pré-revisão
└── README.md                         # Documentação do plugin
```

**Recursos**: análise de segurança, cobertura de testes, impacto de performance

**Comandos**: `/review-pr`, `/check-security`, `/check-tests`

**Instalação**: `/plugin install pr-review`

---

### DevOps Automation Plugin (15 arquivos)

```text
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Manifesto do plugin
├── commands/
│   ├── deploy.md                     # Deploy
│   ├── rollback.md                   # Rollback
│   ├── status.md                     # Status do sistema
│   └── incident.md                   # Resposta a incidentes
├── agents/
│   ├── deployment-specialist.md      # Especialista em deploy
│   ├── incident-commander.md         # Coordenador de incidentes
│   └── alert-analyzer.md             # Analisador de alertas
├── mcp/
│   └── kubernetes-config.json        # Integração com Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # Verificações pré-deploy
│   └── post-deploy.js                # Tarefas pós-deploy
├── scripts/
│   ├── deploy.sh                     # Automação de deploy
│   ├── rollback.sh                   # Automação de rollback
│   └── health-check.sh               # Health checks
└── README.md                         # Documentação do plugin
```

**Recursos**: deploy em Kubernetes, rollback, monitoramento, resposta a incidentes

**Comandos**: `/deploy`, `/rollback`, `/status`, `/incident`

**Instalação**: `/plugin install devops-automation`

---

### Documentation Plugin (14 arquivos)

```text
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
│   └── github-docs-config.json       # Integração com GitHub
├── templates/
│   ├── api-endpoint.md               # Template de endpoint de API
│   ├── function-docs.md              # Template de documentação de função
│   └── adr-template.md               # Template de ADR
└── README.md                         # Documentação do plugin
```

**Recursos**: docs de API, geração de README, sincronização e validação

**Comandos**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Instalação**: `/plugin install documentation`

**Além disso**: `README.md` - visão geral dos plugins e guia de uso

---

## 08. Checkpoints and Rewind (2 arquivos)

Salva o estado da conversa e permite explorar abordagens alternativas.

**Conceitos principais**:
- **Checkpoint**: snapshot do estado da conversa
- **Rewind**: voltar ao checkpoint anterior
- **Branch Point**: explorar múltiplas abordagens

**Uso**:
```
# Checkpoints são criados automaticamente a cada prompt do usuário
# Para voltar, pressione Esc duas vezes ou use:
/rewind
# Depois escolha: Restore code and conversation, Restore conversation,
# Restore code, Summarize from here, ou Never mind
```

**Casos de uso**:
- Testar implementações diferentes
- Recuperar-se de erros
- Experimentar com segurança
- Comparar soluções
- Fazer A/B testing

---

## 09. Advanced Features (3 arquivos)

Capacidades avançadas para fluxos de trabalho complexos.

| Arquivo | Descrição | Recursos |
|------|-------------|----------|
| `README.md` | Guia completo | Documentação de todos os recursos avançados |
| `config-examples.json` | Exemplos de configuração | 10+ configurações por caso de uso |
| `planning-mode-examples.md` | Exemplos de planejamento | REST API, migração de banco, refatoração |
| Scheduled Tasks | Tarefas recorrentes com `/loop` e ferramentas cron | Fluxos recorrentes automatizados |
| Chrome Integration | Automação de navegador via Chromium headless | Testes web e scraping |
| Remote Control (expanded) | Métodos de conexão, segurança, tabela comparativa | Gestão remota de sessões |
| Keyboard Customization | Keybindings personalizados, suporte a chord, contextos | Atalhos personalizados |
| Desktop App (expanded) | Conectores, launch.json, recursos corporativos | Integração com desktop |

---

## 10. CLI Usage (1 arquivo)

Padrões de uso e referência da interface de linha de comando.

| Arquivo | Descrição | Conteúdo |
|------|-------------|----------|
| `README.md` | Documentação do CLI | Flags, opções e padrões de uso |

**Recursos principais do CLI**:
- `claude` - inicia sessão interativa
- `claude -p "prompt"` - modo headless/não interativo
- `claude web` - abre sessão web
- `claude --model` - seleciona o modelo (Sonnet 4.6, Opus 4.6)
- `claude --permission-mode` - define o modo de permissão
- `claude --remote` - habilita controle remoto via WebSocket

---

## Arquivos de Documentação (13 arquivos)

| Arquivo | Local | Descrição |
|------|----------|-------------|
| `README.md` | `/` | Visão geral principal dos exemplos |
| `INDEX.md` | `/` | Este índice completo |
| `QUICK_REFERENCE.md` | `/` | Cartão de referência rápida |
| `README.md` | `/01-slash-commands/` | Guia de slash commands |
| `README.md` | `/02-memory/` | Guia de memória |
| `README.md` | `/03-skills/` | Guia de skills |
| `README.md` | `/04-subagents/` | Guia de subagentes |
| `README.md` | `/05-mcp/` | Guia de MCP |
| `README.md` | `/06-hooks/` | Guia de hooks |
| `README.md` | `/07-plugins/` | Guia de plugins |
| `README.md` | `/08-checkpoints/` | Guia de checkpoints |
| `README.md` | `/09-advanced-features/` | Guia de recursos avançados |
| `README.md` | `/10-cli/` | Guia de CLI |

---

## Árvore Completa de Arquivos

```text
claude-howto/
├── README.md                                    # Visão geral principal
├── INDEX.md                                     # Este arquivo
├── QUICK_REFERENCE.md                           # Cartão de referência rápida
├── claude_concepts_guide.md                     # Guia original
│
├── 01-slash-commands/                           # Slash Commands
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
├── 02-memory/                                   # Memory
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
```

---

## Recursos Adicionais

- [Documentação oficial do Claude Code](https://code.claude.com/docs/en/overview)
- [Especificação MCP](https://modelcontextprotocol.io)
- [Mapa de aprendizado](LEARNING-ROADMAP.md)
- [README principal](README.md)

---
