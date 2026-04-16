<!-- i18n-source: claude_concepts_guide.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Guia Completo dos Conceitos do Claude

Um guia de referência abrangente cobrindo Slash Commands, Subagentes, Memória, Protocolo MCP e Skills de Agentes com tabelas, diagramas e exemplos práticos.

---

## Índice

1. [Slash Commands](#slash-commands)
2. [Subagentes](#subagentes)
3. [Memória](#memória)
4. [Protocolo MCP](#protocolo-mcp)
5. [Skills de Agentes](#skills-de-agentes)
6. [Plugins](#plugins-do-claude-code)
7. [Hooks](#hooks)
8. [Checkpoints e Rewind](#checkpoints-e-rewind)
9. [Recursos Avançados](#recursos-avançados)
10. [Comparação e Integração](#comparação--integração)

---

## Slash Commands

### Visão Geral

Slash commands são atalhos invocados pelo usuário, armazenados como arquivos Markdown que o Claude Code pode executar. Eles permitem que equipes padronizem prompts e workflows usados com frequência.

### Arquitetura

```mermaid
graph TD
    A["User Input: /command-name"] -->|Triggers| B["Search .claude/commands/"]
    B -->|Finds| C["command-name.md"]
    C -->|Loads| D["Markdown Content"]
    D -->|Executes| E["Claude Processes Prompt"]
    E -->|Returns| F["Result in Context"]
```

### Estrutura de Arquivos

```mermaid
graph LR
    A["Project Root"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### Tabela de Organização de Comandos

| Localização | Escopo | Disponibilidade | Caso de Uso | Rastreado pelo Git |
|-------------|--------|-----------------|-------------|-------------------|
| `.claude/commands/` | Específico do projeto | Membros da equipe | Workflows da equipe, padrões compartilhados | ✅ Sim |
| `~/.claude/commands/` | Pessoal | Usuário individual | Atalhos pessoais em todos os projetos | ❌ Não |
| Subdiretórios | Com namespace | Baseado no pai | Organizar por categoria | ✅ Sim |

### Recursos e Capacidades

| Recurso | Exemplo | Suportado |
|---------|---------|-----------|
| Execução de scripts shell | `bash scripts/deploy.sh` | ✅ Sim |
| Referências de arquivo | `@path/to/file.js` | ✅ Sim |
| Integração Bash | `$(git log --oneline)` | ✅ Sim |
| Argumentos | `/pr --verbose` | ✅ Sim |
| Comandos MCP | `/mcp__github__list_prs` | ✅ Sim |

### Exemplos Práticos

#### Exemplo 1: Comando de Otimização de Código

**Arquivo:** `.claude/commands/optimize.md`

```markdown
---
name: Code Optimization
description: Analyze code for performance issues and suggest optimizations
tags: performance, analysis
---

# Code Optimization

Review the provided code for the following issues in order of priority:

1. **Performance bottlenecks** - identify O(n²) operations, inefficient loops
2. **Memory leaks** - find unreleased resources, circular references
3. **Algorithm improvements** - suggest better algorithms or data structures
4. **Caching opportunities** - identify repeated computations
5. **Concurrency issues** - find race conditions or threading problems

Format your response with:
- Issue severity (Critical/High/Medium/Low)
- Location in code
- Explanation
- Recommended fix with code example
```

**Uso:**
```bash
# Usuário digita no Claude Code
/optimize

# Claude carrega o prompt e aguarda a entrada do código
```

#### Exemplo 2: Comando Auxiliar de Pull Request

**Arquivo:** `.claude/commands/pr.md`

```markdown
---
name: Prepare Pull Request
description: Clean up code, stage changes, and prepare a pull request
tags: git, workflow
---

# Pull Request Preparation Checklist

Before creating a PR, execute these steps:

1. Run linting: `prettier --write .`
2. Run tests: `npm test`
3. Review git diff: `git diff HEAD`
4. Stage changes: `git add .`
5. Create commit message following conventional commits:
   - `fix:` for bug fixes
   - `feat:` for new features
   - `docs:` for documentation
   - `refactor:` for code restructuring
   - `test:` for test additions
   - `chore:` for maintenance

6. Generate PR summary including:
   - What changed
   - Why it changed
   - Testing performed
   - Potential impacts
```

**Uso:**
```bash
/pr

# Claude executa a checklist e prepara o PR
```

#### Exemplo 3: Gerador de Documentação Hierárquico

**Arquivo:** `.claude/commands/docs/generate-api-docs.md`

```markdown
---
name: Generate API Documentation
description: Create comprehensive API documentation from source code
tags: documentation, api
---

# API Documentation Generator

Generate API documentation by:

1. Scanning all files in `/src/api/`
2. Extracting function signatures and JSDoc comments
3. Organizing by endpoint/module
4. Creating markdown with examples
5. Including request/response schemas
6. Adding error documentation

Output format:
- Markdown file in `/docs/api.md`
- Include curl examples for all endpoints
- Add TypeScript types
```

### Diagrama do Ciclo de Vida do Comando

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant FS as File System
    participant CLI as Shell/Bash

    User->>Claude: Types /optimize
    Claude->>FS: Searches .claude/commands/
    FS-->>Claude: Returns optimize.md
    Claude->>Claude: Loads Markdown content
    Claude->>User: Displays prompt context
    User->>Claude: Provides code to analyze
    Claude->>CLI: (May execute scripts)
    CLI-->>Claude: Results
    Claude->>User: Returns analysis
```

### Boas Práticas

| ✅ Faça | ❌ Não faça |
|---------|------------|
| Use nomes claros e orientados a ações | Crie comandos para tarefas únicas |
| Documente palavras-gatilho na descrição | Construa lógica complexa em comandos |
| Mantenha comandos focados em uma única tarefa | Crie comandos redundantes |
| Controle de versão dos comandos do projeto | Codifique informações sensíveis |
| Organize em subdiretórios | Crie listas longas de comandos |
| Use prompts simples e legíveis | Use palavras abreviadas ou crípticas |

---

## Subagentes

### Visão Geral

Subagentes são assistentes de IA especializados com janelas de contexto isoladas e prompts de sistema personalizados. Eles permitem a execução delegada de tarefas enquanto mantêm uma separação clara de responsabilidades.

### Diagrama de Arquitetura

```mermaid
graph TB
    User["👤 User"]
    Main["🎯 Main Agent<br/>(Coordinator)"]
    Reviewer["🔍 Code Reviewer<br/>Subagent"]
    Tester["✅ Test Engineer<br/>Subagent"]
    Docs["📝 Documentation<br/>Subagent"]

    User -->|asks| Main
    Main -->|delegates| Reviewer
    Main -->|delegates| Tester
    Main -->|delegates| Docs
    Reviewer -->|returns result| Main
    Tester -->|returns result| Main
    Docs -->|returns result| Main
    Main -->|synthesizes| User
```

### Ciclo de Vida do Subagente

```mermaid
sequenceDiagram
    participant User
    participant MainAgent as Main Agent
    participant CodeReviewer as Code Reviewer<br/>Subagent
    participant Context as Separate<br/>Context Window

    User->>MainAgent: "Build new auth feature"
    MainAgent->>MainAgent: Analyze task
    MainAgent->>CodeReviewer: "Review this code"
    CodeReviewer->>Context: Initialize clean context
    Context->>CodeReviewer: Load reviewer instructions
    CodeReviewer->>CodeReviewer: Perform review
    CodeReviewer-->>MainAgent: Return findings
    MainAgent->>MainAgent: Incorporate results
    MainAgent-->>User: Provide synthesis
```

### Tabela de Configuração do Subagente

| Configuração | Tipo | Propósito | Exemplo |
|-------------|------|-----------|---------|
| `name` | String | Identificador do agente | `code-reviewer` |
| `description` | String | Propósito e termos de ativação | `Comprehensive code quality analysis` |
| `tools` | Lista/String | Capacidades permitidas | `read, grep, diff, lint_runner` |
| `system_prompt` | Markdown | Instruções comportamentais | Diretrizes personalizadas |

### Hierarquia de Acesso a Ferramentas

```mermaid
graph TD
    A["Subagent Configuration"] -->|Option 1| B["Inherit All Tools<br/>from Main Thread"]
    A -->|Option 2| C["Specify Individual Tools"]
    B -->|Includes| B1["File Operations"]
    B -->|Includes| B2["Shell Commands"]
    B -->|Includes| B3["MCP Tools"]
    C -->|Explicit List| C1["read, grep, diff"]
    C -->|Explicit List| C2["Bash(npm:*), Bash(test:*)"]
```

### Exemplos Práticos

#### Exemplo 1: Configuração Completa de Subagente

**Arquivo:** `.claude/agents/code-reviewer.md`

```yaml
---
name: code-reviewer
description: Comprehensive code quality and maintainability analysis
tools: read, grep, diff, lint_runner
---

# Code Reviewer Agent

You are an expert code reviewer specializing in:
- Performance optimization
- Security vulnerabilities
- Code maintainability
- Testing coverage
- Design patterns

## Review Priorities (in order)

1. **Security Issues** - Authentication, authorization, data exposure
2. **Performance Problems** - O(n²) operations, memory leaks, inefficient queries
3. **Code Quality** - Readability, naming, documentation
4. **Test Coverage** - Missing tests, edge cases
5. **Design Patterns** - SOLID principles, architecture

## Review Output Format

For each issue:
- **Severity**: Critical / High / Medium / Low
- **Category**: Security / Performance / Quality / Testing / Design
- **Location**: File path and line number
- **Issue Description**: What's wrong and why
- **Suggested Fix**: Code example
- **Impact**: How this affects the system

## Example Review

### Issue: N+1 Query Problem
- **Severity**: High
- **Category**: Performance
- **Location**: src/user-service.ts:45
- **Issue**: Loop executes database query in each iteration
- **Fix**: Use JOIN or batch query
```

**Arquivo:** `.claude/agents/test-engineer.md`

```yaml
---
name: test-engineer
description: Test strategy, coverage analysis, and automated testing
tools: read, write, bash, grep
---

# Test Engineer Agent

You are expert at:
- Writing comprehensive test suites
- Ensuring high code coverage (>80%)
- Testing edge cases and error scenarios
- Performance benchmarking
- Integration testing

## Testing Strategy

1. **Unit Tests** - Individual functions/methods
2. **Integration Tests** - Component interactions
3. **End-to-End Tests** - Complete workflows
4. **Edge Cases** - Boundary conditions
5. **Error Scenarios** - Failure handling

## Test Output Requirements

- Use Jest for JavaScript/TypeScript
- Include setup/teardown for each test
- Mock external dependencies
- Document test purpose
- Include performance assertions when relevant

## Coverage Requirements

- Minimum 80% code coverage
- 100% for critical paths
- Report missing coverage areas
```

**Arquivo:** `.claude/agents/documentation-writer.md`

```yaml
---
name: documentation-writer
description: Technical documentation, API docs, and user guides
tools: read, write, grep
---

# Documentation Writer Agent

You create:
- API documentation with examples
- User guides and tutorials
- Architecture documentation
- Changelog entries
- Code comment improvements

## Documentation Standards

1. **Clarity** - Use simple, clear language
2. **Examples** - Include practical code examples
3. **Completeness** - Cover all parameters and returns
4. **Structure** - Use consistent formatting
5. **Accuracy** - Verify against actual code

## Documentation Sections

### For APIs
- Description
- Parameters (with types)
- Returns (with types)
- Throws (possible errors)
- Examples (curl, JavaScript, Python)
- Related endpoints

### For Features
- Overview
- Prerequisites
- Step-by-step instructions
- Expected outcomes
- Troubleshooting
- Related topics
```

#### Exemplo 2: Delegação de Subagente em Ação

```markdown
# Cenário: Construindo um Recurso de Pagamento

## Requisição do Usuário
"Construir um recurso seguro de processamento de pagamentos integrado com Stripe"

## Fluxo do Agente Principal

1. **Fase de Planejamento**
   - Entende os requisitos
   - Determina as tarefas necessárias
   - Planeja a arquitetura

2. **Delega para o Subagente Revisor de Código**
   - Tarefa: "Revisar a implementação de processamento de pagamentos para segurança"
   - Contexto: Autenticação, chaves de API, manipulação de tokens
   - Revisa por: Injeção SQL, exposição de chaves, HTTPS obrigatório

3. **Delega para o Subagente Engenheiro de Testes**
   - Tarefa: "Criar testes abrangentes para fluxos de pagamento"
   - Contexto: Cenários de sucesso, falhas, casos extremos
   - Cria testes para: Pagamentos válidos, cartões recusados, falhas de rede, webhooks

4. **Delega para o Subagente Escritor de Documentação**
   - Tarefa: "Documentar os endpoints da API de pagamento"
   - Contexto: Schemas de requisição/resposta
   - Produz: Docs de API com exemplos cURL, códigos de erro

5. **Síntese**
   - Agente principal coleta todas as saídas
   - Integra os resultados
   - Retorna a solução completa ao usuário
```

#### Exemplo 3: Escopo de Permissões de Ferramentas

**Configuração Restritiva - Limitada a Comandos Específicos**

```yaml
---
name: secure-reviewer
description: Security-focused code review with minimal permissions
tools: read, grep
---

# Secure Code Reviewer

Reviews code for security vulnerabilities only.

This agent:
- ✅ Reads files to analyze
- ✅ Searches for patterns
- ❌ Cannot execute code
- ❌ Cannot modify files
- ❌ Cannot run tests

This ensures the reviewer doesn't accidentally break anything.
```

**Configuração Ampliada - Todas as Ferramentas para Implementação**

```yaml
---
name: implementation-agent
description: Full implementation capabilities for feature development
tools: read, write, bash, grep, edit, glob
---

# Implementation Agent

Builds features from specifications.

This agent:
- ✅ Reads specifications
- ✅ Writes new code files
- ✅ Runs build commands
- ✅ Searches codebase
- ✅ Edits existing files
- ✅ Finds files matching patterns

Full capabilities for independent feature development.
```

### Gerenciamento de Contexto do Subagente

```mermaid
graph TB
    A["Main Agent Context<br/>50,000 tokens"]
    B["Subagent 1 Context<br/>20,000 tokens"]
    C["Subagent 2 Context<br/>20,000 tokens"]
    D["Subagent 3 Context<br/>20,000 tokens"]

    A -->|Clean slate| B
    A -->|Clean slate| C
    A -->|Clean slate| D

    B -->|Results only| A
    C -->|Results only| A
    D -->|Results only| A

    style A fill:#e1f5ff
    style B fill:#fff9c4
    style C fill:#fff9c4
    style D fill:#fff9c4
```

### Quando Usar Subagentes

| Cenário | Usar Subagente | Por quê |
|---------|---------------|---------|
| Recurso complexo com muitos passos | ✅ Sim | Separar responsabilidades, evitar poluição de contexto |
| Revisão de código rápida | ❌ Não | Overhead desnecessário |
| Execução paralela de tarefas | ✅ Sim | Cada subagente tem seu próprio contexto |
| Especialização necessária | ✅ Sim | Prompts de sistema personalizados |
| Análise de longa duração | ✅ Sim | Evita o esgotamento do contexto principal |
| Tarefa única | ❌ Não | Adiciona latência desnecessariamente |

### Equipes de Agentes

Equipes de Agentes coordenam múltiplos agentes trabalhando em tarefas relacionadas. Em vez de delegar para um subagente por vez, as Equipes de Agentes permitem que o agente principal orquestre um grupo de agentes que colaboram, compartilham resultados intermediários e trabalham em direção a um objetivo comum. Isso é útil para tarefas de grande escala, como o desenvolvimento de recursos full-stack, onde um agente de frontend, um agente de backend e um agente de testes trabalham em paralelo.

---

## Memória

### Visão Geral

A memória permite que o Claude retenha contexto entre sessões e conversas. Ela existe em duas formas: síntese automática no claude.ai, e CLAUDE.md baseado em sistema de arquivos no Claude Code.

### Arquitetura de Memória

```mermaid
graph TB
    A["Claude Session"]
    B["User Input"]
    C["Memory System"]
    D["Memory Storage"]

    B -->|User provides info| C
    C -->|Synthesizes every 24h| D
    D -->|Loads automatically| A
    A -->|Uses context| C
```

### Hierarquia de Memória no Claude Code (7 Camadas)

O Claude Code carrega memória de 7 camadas, listadas da maior para a menor prioridade:

```mermaid
graph TD
    A["1. Managed Policy<br/>Enterprise admin policies"] --> B["2. Project Memory<br/>./CLAUDE.md"]
    B --> C["3. Project Rules<br/>.claude/rules/*.md"]
    C --> D["4. User Memory<br/>~/.claude/CLAUDE.md"]
    D --> E["5. User Rules<br/>~/.claude/rules/*.md"]
    E --> F["6. Local Memory<br/>.claude/local/CLAUDE.md"]
    F --> G["7. Auto Memory<br/>Automatically captured preferences"]

    style A fill:#fce4ec,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#e1f5fe,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
    style G fill:#fff3e0,stroke:#333,color:#333
```

### Tabela de Locais de Memória

| Camada | Localização | Escopo | Prioridade | Compartilhado | Ideal Para |
|--------|-------------|--------|-----------|---------------|------------|
| 1. Managed Policy | Admin empresarial | Organização | Mais alta | Todos os usuários da org | Políticas de conformidade e segurança |
| 2. Project | `./CLAUDE.md` | Projeto | Alta | Equipe (Git) | Padrões da equipe, arquitetura |
| 3. Project Rules | `.claude/rules/*.md` | Projeto | Alta | Equipe (Git) | Convenções modulares do projeto |
| 4. User | `~/.claude/CLAUDE.md` | Pessoal | Média | Individual | Preferências pessoais |
| 5. User Rules | `~/.claude/rules/*.md` | Pessoal | Média | Individual | Módulos de regras pessoais |
| 6. Local | `.claude/local/CLAUDE.md` | Local | Baixa | Não compartilhado | Configurações específicas da máquina |
| 7. Auto Memory | Automático | Sessão | Mais baixa | Individual | Preferências aprendidas, padrões |

### Auto Memory

A Auto Memory captura automaticamente preferências e padrões do usuário observados durante as sessões. O Claude aprende com suas interações e lembra:

- Preferências de estilo de codificação
- Correções comuns que você faz
- Escolhas de frameworks e ferramentas
- Preferências de estilo de comunicação

A Auto Memory funciona em segundo plano e não requer configuração manual.

### Ciclo de Vida da Atualização de Memória

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Editor as File System
    participant Memory as CLAUDE.md

    User->>Claude: "Remember: use async/await"
    Claude->>User: "Which memory file?"
    User->>Claude: "Project memory"
    Claude->>Editor: Open ~/.claude/settings.json
    Claude->>Memory: Write to ./CLAUDE.md
    Memory-->>Claude: File saved
    Claude->>Claude: Load updated memory
    Claude-->>User: "Memory saved!"
```

### Exemplos Práticos

#### Exemplo 1: Estrutura de Memória do Projeto

**Arquivo:** `./CLAUDE.md`

```markdown
# Project Configuration

## Project Overview
- **Name**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **Team Size**: 5 developers
- **Deadline**: Q4 2025

## Architecture
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Development Standards

### Code Style
- Use Prettier for formatting
- Use ESLint with airbnb config
- Maximum line length: 100 characters
- Use 2-space indentation

### Naming Conventions
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- Branch names: `feature/description` or `fix/description`
- Commit messages: Follow conventional commits
- PR required before merge
- All CI/CD checks must pass
- Minimum 1 approval required

### Testing Requirements
- Minimum 80% code coverage
- All critical paths must have tests
- Use Jest for unit tests
- Use Cypress for E2E tests
- Test filenames: `*.test.ts` or `*.spec.ts`

### API Standards
- RESTful endpoints only
- JSON request/response
- Use HTTP status codes correctly
- Version API endpoints: `/api/v1/`
- Document all endpoints with examples

### Database
- Use migrations for schema changes
- Never hardcode credentials
- Use connection pooling
- Enable query logging in development
- Regular backups required

### Deployment
- Docker-based deployment
- Kubernetes orchestration
- Blue-green deployment strategy
- Automatic rollback on failure
- Database migrations run before deploy

## Common Commands

| Command | Purpose |
|---------|---------|
| `npm run dev` | Start development server |
| `npm test` | Run test suite |
| `npm run lint` | Check code style |
| `npm run build` | Build for production |
| `npm run migrate` | Run database migrations |

## Team Contacts
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Known Issues & Workarounds
- PostgreSQL connection pooling limited to 20 during peak hours
- Workaround: Implement query queuing
- Safari 14 compatibility issues with async generators
- Workaround: Use Babel transpiler

## Related Projects
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`
```

#### Exemplo 2: Memória Específica de Diretório

**Arquivo:** `./src/api/CLAUDE.md`

~~~~markdown
# API Module Standards

This file overrides root CLAUDE.md for everything in /src/api/

## API-Specific Standards

### Request Validation
- Use Zod for schema validation
- Always validate input
- Return 400 with validation errors
- Include field-level error details

### Authentication
- All endpoints require JWT token
- Token in Authorization header
- Token expires after 24 hours
- Implement refresh token mechanism

### Response Format

All responses must follow this structure:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

### Error responses:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Pagination
- Use cursor-based pagination (not offset)
- Include `hasMore` boolean
- Limit max page size to 100
- Default page size: 20

### Rate Limiting
- 1000 requests per hour for authenticated users
- 100 requests per hour for public endpoints
- Return 429 when exceeded
- Include retry-after header

### Caching
- Use Redis for session caching
- Cache duration: 5 minutes default
- Invalidate on write operations
- Tag cache keys with resource type
~~~~

#### Exemplo 3: Memória Pessoal

**Arquivo:** `~/.claude/CLAUDE.md`

~~~~markdown
# My Development Preferences

## About Me
- **Experience Level**: 8 years full-stack development
- **Preferred Languages**: TypeScript, Python
- **Communication Style**: Direct, with examples
- **Learning Style**: Visual diagrams with code

## Code Preferences

### Error Handling
I prefer explicit error handling with try-catch blocks and meaningful error messages.
Avoid generic errors. Always log errors for debugging.

### Comments
Use comments for WHY, not WHAT. Code should be self-documenting.
Comments should explain business logic or non-obvious decisions.

### Testing
I prefer TDD (test-driven development).
Write tests first, then implementation.
Focus on behavior, not implementation details.

### Architecture
I prefer modular, loosely-coupled design.
Use dependency injection for testability.
Separate concerns (Controllers, Services, Repositories).

## Debugging Preferences
- Use console.log with prefix: `[DEBUG]`
- Include context: function name, relevant variables
- Use stack traces when available
- Always include timestamps in logs

## Communication
- Explain complex concepts with diagrams
- Show concrete examples before explaining theory
- Include before/after code snippets
- Summarize key points at the end

## Project Organization
I organize my projects as:
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Tooling
- **IDE**: VS Code with vim keybindings
- **Terminal**: Zsh with Oh-My-Zsh
- **Format**: Prettier (100 char line length)
- **Linter**: ESLint with airbnb config
- **Test Framework**: Jest with React Testing Library
~~~~

#### Exemplo 4: Atualização de Memória Durante a Sessão

**Interação na Sessão:**

```markdown
User: Remember that I prefer using React hooks instead of class components
     for all new components.

Claude: I'm adding that to your memory. Which memory file should this go in?
        1. Project memory (./CLAUDE.md)
        2. Personal memory (~/.claude/CLAUDE.md)

User: Project memory

Claude: ✅ Memory saved!

Added to ./CLAUDE.md:
---

### Component Development
- Use functional components with React Hooks
- Prefer hooks over class components
- Custom hooks for reusable logic
- Use useCallback for event handlers
- Use useMemo for expensive computations
```

### Memória no Claude Web/Desktop

#### Linha do Tempo da Síntese de Memória

```mermaid
graph LR
    A["Day 1: User<br/>Conversations"] -->|24 hours| B["Day 2: Memory<br/>Synthesis"]
    B -->|Automatic| C["Memory Updated<br/>Summarized"]
    C -->|Loaded in| D["Day 2-N:<br/>New Conversations"]
    D -->|Add to| E["Memory"]
    E -->|24 hours later| F["Memory Refreshed"]
```

**Exemplo de Resumo de Memória:**

```markdown
## Claude's Memory of User

### Professional Background
- Senior full-stack developer with 8 years experience
- Focus on TypeScript/Node.js backends and React frontends
- Active open source contributor
- Interested in AI and machine learning

### Project Context
- Currently building e-commerce platform
- Tech stack: Node.js, PostgreSQL, React 18, Docker
- Working with team of 5 developers
- Using CI/CD and blue-green deployments

### Communication Preferences
- Prefers direct, concise explanations
- Likes visual diagrams and examples
- Appreciates code snippets
- Explains business logic in comments

### Current Goals
- Improve API performance
- Increase test coverage to 90%
- Implement caching strategy
- Document architecture
```

### Comparação de Recursos de Memória

| Recurso | Claude Web/Desktop | Claude Code (CLAUDE.md) |
|---------|-------------------|------------------------|
| Auto-síntese | ✅ A cada 24h | ❌ Manual |
| Entre projetos | ✅ Compartilhado | ❌ Específico do projeto |
| Acesso da equipe | ✅ Projetos compartilhados | ✅ Rastreado pelo Git |
| Pesquisável | ✅ Integrado | ✅ Via `/memory` |
| Editável | ✅ No chat | ✅ Edição direta do arquivo |
| Importar/Exportar | ✅ Sim | ✅ Copiar/colar |
| Persistente | ✅ 24h+ | ✅ Indefinido |

---

## Protocolo MCP

### Visão Geral

MCP (Model Context Protocol) é uma forma padronizada para o Claude acessar ferramentas externas, APIs e fontes de dados em tempo real. Ao contrário da Memória, o MCP fornece acesso ao vivo a dados em constante mudança.

### Arquitetura MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A
```

### Ecossistema MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]
```

### Processo de Configuração do MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

### Tabela de Servidores MCP Disponíveis

| Servidor MCP | Propósito | Ferramentas Comuns | Autenticação | Tempo Real |
|-------------|-----------|-------------------|--------------|-----------|
| **Filesystem** | Operações de arquivo | read, write, delete | Permissões do SO | ✅ Sim |
| **GitHub** | Gerenciamento de repositório | list_prs, create_issue, push | OAuth | ✅ Sim |
| **Slack** | Comunicação da equipe | send_message, list_channels | Token | ✅ Sim |
| **Database** | Consultas SQL | query, insert, update | Credenciais | ✅ Sim |
| **Google Docs** | Acesso a documentos | read, write, share | OAuth | ✅ Sim |
| **Asana** | Gerenciamento de projetos | create_task, update_status | API Key | ✅ Sim |
| **Stripe** | Dados de pagamento | list_charges, create_invoice | API Key | ✅ Sim |
| **Memory** | Memória persistente | store, retrieve, delete | Local | ❌ Não |

### Exemplos Práticos

#### Exemplo 1: Configuração do GitHub MCP

**Arquivo:** `.mcp.json` (escopo do projeto) ou `~/.claude.json` (escopo do usuário)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Ferramentas MCP do GitHub Disponíveis:**

~~~~markdown
# GitHub MCP Tools

## Pull Request Management
- `list_prs` - List all PRs in repository
- `get_pr` - Get PR details including diff
- `create_pr` - Create new PR
- `update_pr` - Update PR description/title
- `merge_pr` - Merge PR to main branch
- `review_pr` - Add review comments

Example request:
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

## Issue Management
- `list_issues` - List all issues
- `get_issue` - Get issue details
- `create_issue` - Create new issue
- `close_issue` - Close issue
- `add_comment` - Add comment to issue

## Repository Information
- `get_repo_info` - Repository details
- `list_files` - File tree structure
- `get_file_content` - Read file contents
- `search_code` - Search across codebase

## Commit Operations
- `list_commits` - Commit history
- `get_commit` - Specific commit details
- `create_commit` - Create new commit
~~~~

#### Exemplo 2: Configuração do Database MCP

**Configuração:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**Exemplo de Uso:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

#### Exemplo 3: Workflow Multi-MCP

**Cenário: Geração de Relatório Diário**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

#### Exemplo 4: Operações do Filesystem MCP

**Configuração:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**Operações Disponíveis:**

| Operação | Comando | Propósito |
|----------|---------|-----------|
| Listar arquivos | `ls ~/projects` | Mostrar conteúdo do diretório |
| Ler arquivo | `cat src/main.ts` | Ler conteúdo do arquivo |
| Escrever arquivo | `create docs/api.md` | Criar novo arquivo |
| Editar arquivo | `edit src/app.ts` | Modificar arquivo |
| Buscar | `grep "async function"` | Buscar em arquivos |
| Excluir | `rm old-file.js` | Excluir arquivo |

### MCP vs Memória: Matriz de Decisão

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style B fill:#e1f5ff
    style D fill:#fff9c4
```

### Padrão de Requisição/Resposta

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

---

## Skills de Agentes

### Visão Geral

Skills de Agentes são capacidades reutilizáveis, invocadas pelo modelo, empacotadas como pastas contendo instruções, scripts e recursos. O Claude detecta e usa automaticamente as skills relevantes.

### Arquitetura de Skill

```mermaid
graph TB
    A["Skill Directory"]
    B["SKILL.md"]
    C["YAML Metadata"]
    D["Instructions"]
    E["Scripts"]
    F["Templates"]

    A --> B
    B --> C
    B --> D
    E --> A
    F --> A
```

### Processo de Carregamento de Skill

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude
    participant System as System
    participant Skill as Skill

    User->>Claude: "Create Excel report"
    Claude->>System: Scan available skills
    System->>System: Load skill metadata
    Claude->>Claude: Match user request to skills
    Claude->>Skill: Load xlsx skill SKILL.md
    Skill-->>Claude: Return instructions + tools
    Claude->>Claude: Execute skill
    Claude->>User: Generate Excel file
```

### Tabela de Tipos e Locais de Skills

| Tipo | Localização | Escopo | Compartilhado | Sincronização | Ideal Para |
|------|-------------|--------|---------------|--------------|------------|
| Pré-construída | Integrada | Global | Todos os usuários | Automática | Criação de documentos |
| Pessoal | `~/.claude/skills/` | Individual | Não | Manual | Automação pessoal |
| Projeto | `.claude/skills/` | Equipe | Sim | Git | Padrões da equipe |
| Plugin | Via instalação de plugin | Variado | Depende | Automática | Recursos integrados |

### Skills Pré-construídas

```mermaid
graph TB
    A["Pre-built Skills"]
    B["PowerPoint (pptx)"]
    C["Excel (xlsx)"]
    D["Word (docx)"]
    E["PDF"]

    A --> B
    A --> C
    A --> D
    A --> E

    B --> B1["Create presentations"]
    B --> B2["Edit slides"]
    C --> C1["Create spreadsheets"]
    C --> C2["Analyze data"]
    D --> D1["Create documents"]
    D --> D2["Format text"]
    E --> E1["Generate PDFs"]
    E --> E2["Fill forms"]
```

### Skills Integradas

O Claude Code agora inclui 5 skills integradas disponíveis de imediato:

| Skill | Comando | Propósito |
|-------|---------|-----------|
| **Simplify** | `/simplify` | Simplificar código ou explicações complexas |
| **Batch** | `/batch` | Executar operações em múltiplos arquivos ou itens |
| **Debug** | `/debug` | Depuração sistemática de problemas com análise de causa raiz |
| **Loop** | `/loop` | Agendar tarefas recorrentes em um timer |
| **Claude API** | `/claude-api` | Interagir diretamente com a API da Anthropic |

Essas skills integradas estão sempre disponíveis e não requerem instalação ou configuração.

### Exemplos Práticos

#### Exemplo 1: Skill Personalizada de Revisão de Código

**Estrutura de Diretório:**

```
~/.claude/skills/code-review/
├── SKILL.md
├── templates/
│   ├── review-checklist.md
│   └── finding-template.md
└── scripts/
    ├── analyze-metrics.py
    └── compare-complexity.py
```

**Arquivo:** `~/.claude/skills/code-review/SKILL.md`

```yaml
---
name: Code Review Specialist
description: Comprehensive code review with security, performance, and quality analysis
version: "1.0.0"
tags:
  - code-review
  - quality
  - security
when_to_use: When users ask to review code, analyze code quality, or evaluate pull requests
effort: high
shell: bash
---

# Code Review Skill

This skill provides comprehensive code review capabilities focusing on:

1. **Security Analysis**
   - Authentication/authorization issues
   - Data exposure risks
   - Injection vulnerabilities
   - Cryptographic weaknesses
   - Sensitive data logging

2. **Performance Review**
   - Algorithm efficiency (Big O analysis)
   - Memory optimization
   - Database query optimization
   - Caching opportunities
   - Concurrency issues

3. **Code Quality**
   - SOLID principles
   - Design patterns
   - Naming conventions
   - Documentation
   - Test coverage

4. **Maintainability**
   - Code readability
   - Function size (should be < 50 lines)
   - Cyclomatic complexity
   - Dependency management
   - Type safety

## Review Template

For each piece of code reviewed, provide:

### Summary
- Overall quality assessment (1-5)
- Key findings count
- Recommended priority areas

### Critical Issues (if any)
- **Issue**: Clear description
- **Location**: File and line number
- **Impact**: Why this matters
- **Severity**: Critical/High/Medium
- **Fix**: Code example

### Findings by Category

#### Security (if issues found)
List security vulnerabilities with examples

#### Performance (if issues found)
List performance problems with complexity analysis

#### Quality (if issues found)
List code quality issues with refactoring suggestions

#### Maintainability (if issues found)
List maintainability problems with improvements
```
## Python Script: analyze-metrics.py

```python
#!/usr/bin/env python3
import re
import sys

def analyze_code_metrics(code):
    """Analyze code for common metrics."""

    # Count functions
    functions = len(re.findall(r'^def\s+\w+', code, re.MULTILINE))

    # Count classes
    classes = len(re.findall(r'^class\s+\w+', code, re.MULTILINE))

    # Average line length
    lines = code.split('\n')
    avg_length = sum(len(l) for l in lines) / len(lines) if lines else 0

    # Estimate complexity
    complexity = len(re.findall(r'\b(if|elif|else|for|while|and|or)\b', code))

    return {
        'functions': functions,
        'classes': classes,
        'avg_line_length': avg_length,
        'complexity_score': complexity
    }

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        code = f.read()
    metrics = analyze_code_metrics(code)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
```

## Python Script: compare-complexity.py

```python
#!/usr/bin/env python3
"""
Compare cyclomatic complexity of code before and after changes.
Helps identify if refactoring actually simplifies code structure.
"""

import re
import sys
from typing import Dict, Tuple

class ComplexityAnalyzer:
    """Analyze code complexity metrics."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calculate cyclomatic complexity using McCabe's method.
        Count decision points: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Base complexity

        # Count decision points
        decision_patterns = [
            r'\bif\b',
            r'\belif\b',
            r'\bfor\b',
            r'\bwhile\b',
            r'\bexcept\b',
            r'\band\b(?!$)',
            r'\bor\b(?!$)'
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        Calculate cognitive complexity - how hard is it to understand?
        Based on nesting depth and control flow.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Track nesting depth
            if re.search(r'^\s*(if|for|while|def|class|try)\b', line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r'^\s*(elif|else|except|finally)\b', line):
                cognitive += nesting_depth

            # Reduce nesting when unindenting
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Maintainability Index ranges from 0-100.
        > 85: Excellent
        > 65: Good
        > 50: Fair
        < 50: Poor
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Simplified MI calculation
        mi = 171 - 5.2 * (cyclomatic / lines) - 0.23 * (cognitive) - 16.2 * (lines / 1000)

        return max(0, min(100, mi))

    def get_complexity_report(self) -> Dict:
        """Generate comprehensive complexity report."""
        return {
            'cyclomatic_complexity': self.calculate_cyclomatic_complexity(),
            'cognitive_complexity': self.calculate_cognitive_complexity(),
            'maintainability_index': round(self.calculate_maintainability_index(), 2),
            'lines_of_code': len(self.lines),
            'avg_line_length': round(sum(len(l) for l in self.lines) / len(self.lines), 2) if self.lines else 0
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compare complexity metrics between two code versions."""

    with open(before_file, 'r') as f:
        before_code = f.read()

    with open(after_file, 'r') as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("CODE COMPLEXITY COMPARISON")
    print("=" * 60)

    print("\nBEFORE:")
    print(f"  Cyclomatic Complexity:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {before_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {before_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {before_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {before_metrics['avg_line_length']}")

    print("\nAFTER:")
    print(f"  Cyclomatic Complexity:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Cognitive Complexity:     {after_metrics['cognitive_complexity']}")
    print(f"  Maintainability Index:    {after_metrics['maintainability_index']}")
    print(f"  Lines of Code:            {after_metrics['lines_of_code']}")
    print(f"  Avg Line Length:          {after_metrics['avg_line_length']}")

    print("\nCHANGES:")
    cyclomatic_change = after_metrics['cyclomatic_complexity'] - before_metrics['cyclomatic_complexity']
    cognitive_change = after_metrics['cognitive_complexity'] - before_metrics['cognitive_complexity']
    mi_change = after_metrics['maintainability_index'] - before_metrics['maintainability_index']
    loc_change = after_metrics['lines_of_code'] - before_metrics['lines_of_code']

    print(f"  Cyclomatic Complexity:    {cyclomatic_change:+d}")
    print(f"  Cognitive Complexity:     {cognitive_change:+d}")
    print(f"  Maintainability Index:    {mi_change:+.2f}")
    print(f"  Lines of Code:            {loc_change:+d}")

    print("\nASSESSMENT:")
    if mi_change > 0:
        print("  ✅ Code is MORE maintainable")
    elif mi_change < 0:
        print("  ⚠️  Code is LESS maintainable")
    else:
        print("  ➡️  Maintainability unchanged")

    if cyclomatic_change < 0:
        print("  ✅ Complexity DECREASED")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexity INCREASED")
    else:
        print("  ➡️  Complexity unchanged")

    print("=" * 60)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare-complexity.py <before_file> <after_file>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
```

## Template: review-checklist.md

```markdown
# Code Review Checklist

## Security Checklist
- [ ] No hardcoded credentials or secrets
- [ ] Input validation on all user inputs
- [ ] SQL injection prevention (parameterized queries)
- [ ] CSRF protection on state-changing operations
- [ ] XSS prevention with proper escaping
- [ ] Authentication checks on protected endpoints
- [ ] Authorization checks on resources
- [ ] Secure password hashing (bcrypt, argon2)
- [ ] No sensitive data in logs
- [ ] HTTPS enforced

## Performance Checklist
- [ ] No N+1 queries
- [ ] Appropriate use of indexes
- [ ] Caching implemented where beneficial
- [ ] No blocking operations on main thread
- [ ] Async/await used correctly
- [ ] Large datasets paginated
- [ ] Database connections pooled
- [ ] Regular expressions optimized
- [ ] No unnecessary object creation
- [ ] Memory leaks prevented

## Quality Checklist
- [ ] Functions < 50 lines
- [ ] Clear variable naming
- [ ] No duplicate code
- [ ] Proper error handling
- [ ] Comments explain WHY, not WHAT
- [ ] No console.logs in production
- [ ] Type checking (TypeScript/JSDoc)
- [ ] SOLID principles followed
- [ ] Design patterns applied correctly
- [ ] Self-documenting code

## Testing Checklist
- [ ] Unit tests written
- [ ] Edge cases covered
- [ ] Error scenarios tested
- [ ] Integration tests present
- [ ] Coverage > 80%
- [ ] No flaky tests
- [ ] Mock external dependencies
- [ ] Clear test names
```

## Template: finding-template.md

~~~~markdown
# Code Review Finding Template

Use this template when documenting each issue found during code review.

---

## Issue: [TITLE]

### Severity
- [ ] Critical (blocks deployment)
- [ ] High (should fix before merge)
- [ ] Medium (should fix soon)
- [ ] Low (nice to have)

### Category
- [ ] Security
- [ ] Performance
- [ ] Code Quality
- [ ] Maintainability
- [ ] Testing
- [ ] Design Pattern
- [ ] Documentation

### Location
**File:** `src/components/UserCard.tsx`

**Lines:** 45-52

**Function/Method:** `renderUserDetails()`

### Issue Description

**What:** Describe what the issue is.

**Why it matters:** Explain the impact and why this needs to be fixed.

**Current behavior:** Show the problematic code or behavior.

**Expected behavior:** Describe what should happen instead.

### Code Example

#### Current (Problematic)

```typescript
// Shows the N+1 query problem
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query per user!
  renderUserPosts(posts);
});
```

#### Suggested Fix

```typescript
// Optimized with JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Impact Analysis

| Aspect | Impact | Severity |
|--------|--------|----------|
| Performance | 100+ queries for 20 users | High |
| User Experience | Slow page load | High |
| Scalability | Breaks at scale | Critical |
| Maintainability | Hard to debug | Medium |

### Related Issues

- Similar issue in `AdminUserList.tsx` line 120
- Related PR: #456
- Related issue: #789

### Additional Resources

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### Reviewer Notes

- This is a common pattern in this codebase
- Consider adding this to the code style guide
- Might be worth creating a helper function

### Author Response (for feedback)

*To be filled by the code author:*

- [ ] Fix implemented in commit: `abc123`
- [ ] Fix status: Complete / In Progress / Needs Discussion
- [ ] Questions or concerns: (describe)

---

## Finding Statistics (for Reviewer)

When reviewing multiple findings, track:

- **Total Issues Found:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**Recommendation:** ✅ Approve / ⚠️ Request Changes / 🔄 Needs Discussion

**Overall Code Quality:** 1-5 stars
~~~~

## Exemplo de Uso

~~~~markdown
User: Review this React component code

Claude: I'll conduct a comprehensive code review using my Code Review Skill.

[Loads SKILL.md]
[Analyzes code against checklist]
[Runs Python metrics script]
[Applies templates]

## Code Review Results

### Summary
Quality Score: 3.5/5
Key Findings: 7 items
Priority Areas: Performance optimization, error handling

### Critical Issues: 1

**Issue**: N+1 Query Problem
**Location**: UserComponent.tsx, lines 45-52
**Impact**: Renders 100+ database queries for list of 20 users
**Severity**: High
**Fix**:
```javascript
// Before: N+1 queries
const users = fetchUsers();
users.forEach(user => fetchUserPosts(user.id)); // 20+ queries

// After: Single query with JOIN
const users = fetchUsersWithPosts(); // 1 query
```

### Performance Findings
- Missing pagination on large lists
- Recommendation: Use React.memo() for items
- Database query: Could be optimized with index

### Quality Findings
- Function in line 20 is 127 lines (max: 50)
- Missing error boundary
- Props should have TypeScript types
~~~~

#### Exemplo 2: Skill de Voz da Marca

**Estrutura de Diretório:**

```
.claude/skills/brand-voice/
├── SKILL.md
├── brand-guidelines.md
├── tone-examples.md
└── templates/
    ├── email-template.txt
    ├── social-post-template.txt
    └── blog-post-template.md
```

**Arquivo:** `.claude/skills/brand-voice/SKILL.md`

```yaml
---
name: Brand Voice Consistency
description: Ensure all communication matches brand voice and tone guidelines
tags:
  - brand
  - writing
  - consistency
when_to_use: When creating marketing copy, customer communications, or public-facing content
---

# Brand Voice Skill

## Overview
This skill ensures all communications maintain consistent brand voice, tone, and messaging.

## Brand Identity

### Mission
Help teams automate their development workflows with AI

### Values
- **Simplicity**: Make complex things simple
- **Reliability**: Rock-solid execution
- **Empowerment**: Enable human creativity

### Tone of Voice
- **Friendly but professional** - approachable without being casual
- **Clear and concise** - avoid jargon, explain technical concepts simply
- **Confident** - we know what we're doing
- **Empathetic** - understand user needs and pain points

## Writing Guidelines

### Do's ✅
- Use "you" when addressing readers
- Use active voice: "Claude generates reports" not "Reports are generated by Claude"
- Start with value proposition
- Use concrete examples
- Keep sentences under 20 words
- Use lists for clarity
- Include calls-to-action

### Don'ts ❌
- Don't use corporate jargon
- Don't patronize or oversimplify
- Don't use "we believe" or "we think"
- Don't use ALL CAPS except for emphasis
- Don't create walls of text
- Don't assume technical knowledge

## Vocabulary

### ✅ Preferred Terms
- Claude (not "the Claude AI")
- Code generation (not "auto-coding")
- Agent (not "bot")
- Streamline (not "revolutionize")
- Integrate (not "synergize")

### ❌ Avoid Terms
- "Cutting-edge" (overused)
- "Game-changer" (vague)
- "Leverage" (corporate-speak)
- "Utilize" (use "use")
- "Paradigm shift" (unclear)
```
## Examples

### ✅ Good Example
"Claude automates your code review process. Instead of manually checking each PR, Claude reviews security, performance, and quality—saving your team hours every week."

Why it works: Clear value, specific benefits, action-oriented

### ❌ Bad Example
"Claude leverages cutting-edge AI to provide comprehensive software development solutions."

Why it doesn't work: Vague, corporate jargon, no specific value

## Template: Email

```
Subject: [Clear, benefit-driven subject]

Hi [Name],

[Opening: What's the value for them]

[Body: How it works / What they'll get]

[Specific example or benefit]

[Call to action: Clear next step]

Best regards,
[Name]
```

## Template: Social Media

```
[Hook: Grab attention in first line]
[2-3 lines: Value or interesting fact]
[Call to action: Link, question, or engagement]
[Emoji: 1-2 max for visual interest]
```

## File: tone-examples.md
```
Exciting announcement:
"Save 8 hours per week on code reviews. Claude reviews your PRs automatically."

Empathetic support:
"We know deployments can be stressful. Claude handles testing so you don't have to worry."

Confident product feature:
"Claude doesn't just suggest code. It understands your architecture and maintains consistency."

Educational blog post:
"Let's explore how agents improve code review workflows. Here's what we learned..."
```

#### Exemplo 3: Skill de Gerador de Documentação

**Arquivo:** `.claude/skills/doc-generator/SKILL.md`

~~~~yaml
---
name: API Documentation Generator
description: Generate comprehensive, accurate API documentation from source code
version: "1.0.0"
tags:
  - documentation
  - api
  - automation
when_to_use: When creating or updating API documentation
---

# API Documentation Generator Skill

## Generates

- OpenAPI/Swagger specifications
- API endpoint documentation
- SDK usage examples
- Integration guides
- Error code references
- Authentication guides

## Documentation Structure

### For Each Endpoint

```markdown
## GET /api/v1/users/:id

### Description
Brief explanation of what this endpoint does

### Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| id | string | Yes | User ID |

### Response

**200 Success**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Not Found**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### Examples

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```

## Python Script: generate-docs.py

```python
#!/usr/bin/env python3
import ast
import json
from typing import Dict, List

class APIDocExtractor(ast.NodeVisitor):
    """Extract API documentation from Python source code."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extract function documentation."""
        if node.name.startswith('get_') or node.name.startswith('post_'):
            doc = ast.get_docstring(node)
            endpoint = {
                'name': node.name,
                'docstring': doc,
                'params': [arg.arg for arg in node.args.args],
                'returns': self._extract_return_type(node)
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extract return type from function annotation."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"

def generate_markdown_docs(endpoints: List[Dict]) -> str:
    """Generate markdown documentation from endpoints."""
    docs = "# API Documentation\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parameters**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Returns**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs

if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
~~~~
### Descoberta e Invocação de Skills

```mermaid
graph TD
    A["User Request"] --> B["Claude Analyzes"]
    B -->|Scans| C["Available Skills"]
    C -->|Metadata check| D["Skill Description Match?"]
    D -->|Yes| E["Load SKILL.md"]
    D -->|No| F["Try next skill"]
    F -->|More skills?| D
    F -->|No more| G["Use general knowledge"]
    E --> H["Extract Instructions"]
    H --> I["Execute Skill"]
    I --> J["Return Results"]
```

### Skills vs Outros Recursos

```mermaid
graph TB
    A["Extending Claude"]
    B["Slash Commands"]
    C["Subagents"]
    D["Memory"]
    E["MCP"]
    F["Skills"]

    A --> B
    A --> C
    A --> D
    A --> E
    A --> F

    B -->|User-invoked| G["Quick shortcuts"]
    C -->|Auto-delegated| H["Isolated contexts"]
    D -->|Persistent| I["Cross-session context"]
    E -->|Real-time| J["External data access"]
    F -->|Auto-invoked| K["Autonomous execution"]
```

---

## Plugins do Claude Code

### Visão Geral

Plugins do Claude Code são coleções empacotadas de personalizações (slash commands, subagentes, servidores MCP e hooks) que se instalam com um único comando. Eles representam o mecanismo de extensão de mais alto nível — combinando múltiplos recursos em pacotes coesos e compartilháveis.

### Arquitetura

```mermaid
graph TB
    A["Plugin"]
    B["Slash Commands"]
    C["Subagents"]
    D["MCP Servers"]
    E["Hooks"]
    F["Configuration"]

    A -->|bundles| B
    A -->|bundles| C
    A -->|bundles| D
    A -->|bundles| E
    A -->|bundles| F
```

### Processo de Carregamento de Plugin

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as Plugin Marketplace
    participant Install as Installation
    participant SlashCmds as Slash Commands
    participant Subagents
    participant MCPServers as MCP Servers
    participant Hooks
    participant Tools as Configured Tools

    User->>Claude: /plugin install pr-review
    Claude->>Plugin: Download plugin manifest
    Plugin-->>Claude: Return plugin definition
    Claude->>Install: Extract components
    Install->>SlashCmds: Configure
    Install->>Subagents: Configure
    Install->>MCPServers: Configure
    Install->>Hooks: Configure
    SlashCmds-->>Tools: Ready to use
    Subagents-->>Tools: Ready to use
    MCPServers-->>Tools: Ready to use
    Hooks-->>Tools: Ready to use
    Tools-->>Claude: Plugin installed ✅
```

### Tipos e Distribuição de Plugins

| Tipo | Escopo | Compartilhado | Autoridade | Exemplos |
|------|--------|---------------|-----------|----------|
| Oficial | Global | Todos os usuários | Anthropic | PR Review, Security Guidance |
| Comunitário | Público | Todos os usuários | Comunidade | DevOps, Data Science |
| Organizacional | Interno | Membros da equipe | Empresa | Padrões internos, ferramentas |
| Pessoal | Individual | Usuário único | Desenvolvedor | Workflows personalizados |

### Estrutura da Definição do Plugin

```yaml
---
name: plugin-name
version: "1.0.0"
description: "What this plugin does"
author: "Your Name"
license: MIT

# Plugin metadata
tags:
  - category
  - use-case

# Requirements
requires:
  - claude-code: ">=1.0.0"

# Components bundled
components:
  - type: commands
    path: commands/
  - type: agents
    path: agents/
  - type: mcp
    path: mcp/
  - type: hooks
    path: hooks/

# Configuration
config:
  auto_load: true
  enabled_by_default: true
---
```

### Estrutura do Plugin

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/
│   ├── skill-1.md
│   └── skill-2.md
├── hooks/
│   └── hooks.json
├── .mcp.json
├── .lsp.json
├── settings.json
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### Exemplos Práticos

#### Exemplo 1: Plugin de Revisão de PR

**Arquivo:** `.claude-plugin/plugin.json`

```json
{
  "name": "pr-review",
  "version": "1.0.0",
  "description": "Complete PR review workflow with security, testing, and docs",
  "author": {
    "name": "Anthropic"
  },
  "license": "MIT"
}
```

**Arquivo:** `commands/review-pr.md`

```markdown
---
name: Review PR
description: Start comprehensive PR review with security and testing checks
---

# PR Review

This command initiates a complete pull request review including:

1. Security analysis
2. Test coverage verification
3. Documentation updates
4. Code quality checks
5. Performance impact assessment
```

**Arquivo:** `agents/security-reviewer.md`

```yaml
---
name: security-reviewer
description: Security-focused code review
tools: read, grep, diff
---

# Security Reviewer

Specializes in finding security vulnerabilities:
- Authentication/authorization issues
- Data exposure
- Injection attacks
- Secure configuration
```

**Instalação:**

```bash
/plugin install pr-review

# Result:
# ✅ 3 slash commands installed
# ✅ 3 subagents configured
# ✅ 2 MCP servers connected
# ✅ 4 hooks registered
# ✅ Ready to use!
```

#### Exemplo 2: Plugin DevOps

**Componentes:**

```
devops-automation/
├── commands/
│   ├── deploy.md
│   ├── rollback.md
│   ├── status.md
│   └── incident.md
├── agents/
│   ├── deployment-specialist.md
│   ├── incident-commander.md
│   └── alert-analyzer.md
├── mcp/
│   ├── github-config.json
│   ├── kubernetes-config.json
│   └── prometheus-config.json
├── hooks/
│   ├── pre-deploy.js
│   ├── post-deploy.js
│   └── on-error.js
└── scripts/
    ├── deploy.sh
    ├── rollback.sh
    └── health-check.sh
```

#### Exemplo 3: Plugin de Documentação

**Componentes Empacotados:**

```
documentation/
├── commands/
│   ├── generate-api-docs.md
│   ├── generate-readme.md
│   ├── sync-docs.md
│   └── validate-docs.md
├── agents/
│   ├── api-documenter.md
│   ├── code-commentator.md
│   └── example-generator.md
├── mcp/
│   ├── github-docs-config.json
│   └── slack-announce-config.json
└── templates/
    ├── api-endpoint.md
    ├── function-docs.md
    └── adr-template.md
```

### Marketplace de Plugins

```mermaid
graph TB
    A["Plugin Marketplace"]
    B["Official<br/>Anthropic"]
    C["Community<br/>Marketplace"]
    D["Enterprise<br/>Registry"]

    A --> B
    A --> C
    A --> D

    B -->|Categories| B1["Development"]
    B -->|Categories| B2["DevOps"]
    B -->|Categories| B3["Documentation"]

    C -->|Search| C1["DevOps Automation"]
    C -->|Search| C2["Mobile Dev"]
    C -->|Search| C3["Data Science"]

    D -->|Internal| D1["Company Standards"]
    D -->|Internal| D2["Legacy Systems"]
    D -->|Internal| D3["Compliance"]
```

### Instalação e Ciclo de Vida do Plugin

```mermaid
graph LR
    A["Discover"] -->|Browse| B["Marketplace"]
    B -->|Select| C["Plugin Page"]
    C -->|View| D["Components"]
    D -->|Install| E["/plugin install"]
    E -->|Extract| F["Configure"]
    F -->|Activate| G["Use"]
    G -->|Check| H["Update"]
    H -->|Available| G
    G -->|Done| I["Disable"]
    I -->|Later| J["Enable"]
    J -->|Back| G
```

### Comparação de Recursos de Plugins

| Recurso | Slash Command | Skill | Subagente | Plugin |
|---------|---------------|-------|-----------|--------|
| **Instalação** | Cópia manual | Cópia manual | Config manual | Um comando |
| **Tempo de Setup** | 5 minutos | 10 minutos | 15 minutos | 2 minutos |
| **Empacotamento** | Arquivo único | Arquivo único | Arquivo único | Múltiplos |
| **Versionamento** | Manual | Manual | Manual | Automático |
| **Compartilhamento** | Copiar arquivo | Copiar arquivo | Copiar arquivo | ID de instalação |
| **Atualizações** | Manual | Manual | Manual | Disponível automaticamente |
| **Dependências** | Nenhuma | Nenhuma | Nenhuma | Pode incluir |
| **Marketplace** | Não | Não | Não | Sim |
| **Distribuição** | Repositório | Repositório | Repositório | Marketplace |

### Casos de Uso de Plugins

| Caso de Uso | Recomendação | Por quê |
|-------------|--------------|---------|
| **Integração de Equipe** | ✅ Use Plugin | Setup instantâneo, todas as configurações |
| **Setup de Framework** | ✅ Use Plugin | Agrupa comandos específicos do framework |
| **Padrões Empresariais** | ✅ Use Plugin | Distribuição central, controle de versão |
| **Automação Rápida de Tarefas** | ❌ Use Command | Complexidade excessiva |
| **Especialização em Domínio Único** | ❌ Use Skill | Muito pesado, use skill em vez disso |
| **Análise Especializada** | ❌ Use Subagente | Crie manualmente ou use skill |
| **Acesso a Dados ao Vivo** | ❌ Use MCP | Independente, não agrupar |

### Quando Criar um Plugin

```mermaid
graph TD
    A["Should I create a plugin?"]
    A -->|Need multiple components| B{"Multiple commands<br/>or subagents<br/>or MCPs?"}
    B -->|Yes| C["✅ Create Plugin"]
    B -->|No| D["Use Individual Feature"]
    A -->|Team workflow| E{"Share with<br/>team?"}
    E -->|Yes| C
    E -->|No| F["Keep as Local Setup"]
    A -->|Complex setup| G{"Needs auto<br/>configuration?"}
    G -->|Yes| C
    G -->|No| D
```

### Publicando um Plugin

**Passos para publicar:**

1. Criar estrutura do plugin com todos os componentes
2. Escrever o manifest `.claude-plugin/plugin.json`
3. Criar `README.md` com documentação
4. Testar localmente com `/plugin install ./my-plugin`
5. Enviar para o marketplace de plugins
6. Ser revisado e aprovado
7. Publicado no marketplace
8. Usuários podem instalar com um comando

**Exemplo de envio:**

~~~~markdown
# PR Review Plugin

## Description
Complete PR review workflow with security, testing, and documentation checks.

## What's Included
- 3 slash commands for different review types
- 3 specialized subagents
- GitHub and CodeQL MCP integration
- Automated security scanning hooks

## Installation
```bash
/plugin install pr-review
```

## Features
✅ Security analysis
✅ Test coverage checking
✅ Documentation verification
✅ Code quality assessment
✅ Performance impact analysis

## Usage
```bash
/review-pr
/check-security
/check-tests
```

## Requirements
- Claude Code 1.0+
- GitHub access
- CodeQL (optional)
~~~~

### Plugin vs Configuração Manual

**Setup Manual (2+ horas):**
- Instalar slash commands um por um
- Criar subagentes individualmente
- Configurar MCPs separadamente
- Configurar hooks manualmente
- Documentar tudo
- Compartilhar com a equipe (torcer para que configurem corretamente)

**Com Plugin (2 minutos):**
```bash
/plugin install pr-review
# ✅ Everything installed and configured
# ✅ Ready to use immediately
# ✅ Team can reproduce exact setup
```

---

## Comparação e Integração

### Matriz de Comparação de Recursos

| Recurso | Invocação | Persistência | Escopo | Caso de Uso |
|---------|-----------|-------------|--------|------------|
| **Slash Commands** | Manual (`/cmd`) | Apenas sessão | Comando único | Atalhos rápidos |
| **Subagentes** | Auto-delegado | Contexto isolado | Tarefa especializada | Distribuição de tarefas |
| **Memória** | Carregado automaticamente | Entre sessões | Contexto usuário/equipe | Aprendizado de longo prazo |
| **Protocolo MCP** | Auto-consultado | Externo em tempo real | Acesso a dados ao vivo | Informações dinâmicas |
| **Skills** | Auto-invocado | Baseado em sistema de arquivos | Especialização reutilizável | Workflows automatizados |

### Linha do Tempo de Interação

```mermaid
graph LR
    A["Session Start"] -->|Load| B["Memory (CLAUDE.md)"]
    B -->|Discover| C["Available Skills"]
    C -->|Register| D["Slash Commands"]
    D -->|Connect| E["MCP Servers"]
    E -->|Ready| F["User Interaction"]

    F -->|Type /cmd| G["Slash Command"]
    F -->|Request| H["Skill Auto-Invoke"]
    F -->|Query| I["MCP Data"]
    F -->|Complex task| J["Delegate to Subagent"]

    G -->|Uses| B
    H -->|Uses| B
    I -->|Uses| B
    J -->|Uses| B
```

### Exemplo Prático de Integração: Automação de Suporte ao Cliente

#### Arquitetura

```mermaid
graph TB
    User["Customer Email"] -->|Receives| Router["Support Router"]

    Router -->|Analyze| Memory["Memory<br/>Customer history"]
    Router -->|Lookup| MCP1["MCP: Customer DB<br/>Previous tickets"]
    Router -->|Check| MCP2["MCP: Slack<br/>Team status"]

    Router -->|Route Complex| Sub1["Subagent: Tech Support<br/>Context: Technical issues"]
    Router -->|Route Simple| Sub2["Subagent: Billing<br/>Context: Payment issues"]
    Router -->|Route Urgent| Sub3["Subagent: Escalation<br/>Context: Priority handling"]

    Sub1 -->|Format| Skill1["Skill: Response Generator<br/>Brand voice maintained"]
    Sub2 -->|Format| Skill2["Skill: Response Generator"]
    Sub3 -->|Format| Skill3["Skill: Response Generator"]

    Skill1 -->|Generate| Output["Formatted Response"]
    Skill2 -->|Generate| Output
    Skill3 -->|Generate| Output

    Output -->|Post| MCP3["MCP: Slack<br/>Notify team"]
    Output -->|Send| Reply["Customer Reply"]
```

#### Fluxo de Requisição

```markdown
## Customer Support Request Flow

### 1. Incoming Email
"I'm getting error 500 when trying to upload files. This is blocking my workflow!"

### 2. Memory Lookup
- Loads CLAUDE.md with support standards
- Checks customer history: VIP customer, 3rd incident this month

### 3. MCP Queries
- GitHub MCP: List open issues (finds related bug report)
- Database MCP: Check system status (no outages reported)
- Slack MCP: Check if engineering is aware

### 4. Skill Detection & Loading
- Request matches "Technical Support" skill
- Loads support response template from Skill

### 5. Subagent Delegation
- Routes to Tech Support Subagent
- Provides context: customer history, error details, known issues
- Subagent has full access to: read, bash, grep tools

### 6. Subagent Processing
Tech Support Subagent:
- Searches codebase for 500 error in file upload
- Finds recent change in commit 8f4a2c
- Creates workaround documentation

### 7. Skill Execution
Response Generator Skill:
- Uses Brand Voice guidelines
- Formats response with empathy
- Includes workaround steps
- Links to related documentation

### 8. MCP Output
- Posts update to #support Slack channel
- Tags engineering team
- Updates ticket in Jira MCP

### 9. Response
Customer receives:
- Empathetic acknowledgment
- Explanation of cause
- Immediate workaround
- Timeline for permanent fix
- Link to related issues
```

### Orquestração Completa de Recursos

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Memory as Memory<br/>CLAUDE.md
    participant MCP as MCP Servers
    participant Skills as Skills
    participant SubAgent as Subagents

    User->>Claude: Request: "Build auth system"
    Claude->>Memory: Load project standards
    Memory-->>Claude: Auth standards, team practices
    Claude->>MCP: Query GitHub for similar implementations
    MCP-->>Claude: Code examples, best practices
    Claude->>Skills: Detect matching Skills
    Skills-->>Claude: Security Review Skill + Testing Skill
    Claude->>SubAgent: Delegate implementation
    SubAgent->>SubAgent: Build feature
    Claude->>Skills: Apply Security Review Skill
    Skills-->>Claude: Security checklist results
    Claude->>SubAgent: Delegate testing
    SubAgent-->>Claude: Test results
    Claude->>User: Complete system delivered
```

### Quando Usar Cada Recurso

```mermaid
graph TD
    A["New Task"] --> B{Type of Task?}

    B -->|Repeated workflow| C["Slash Command"]
    B -->|Need real-time data| D["MCP Protocol"]
    B -->|Remember for next time| E["Memory"]
    B -->|Specialized subtask| F["Subagent"]
    B -->|Domain-specific work| G["Skill"]

    C --> C1["✅ Team shortcut"]
    D --> D1["✅ Live API access"]
    E --> E1["✅ Persistent context"]
    F --> F1["✅ Parallel execution"]
    G --> G1["✅ Auto-invoked expertise"]
```

### Árvore de Decisão de Seleção

```mermaid
graph TD
    Start["Need to extend Claude?"]

    Start -->|Quick repeated task| A{"Manual or Auto?"}
    A -->|Manual| B["Slash Command"]
    A -->|Auto| C["Skill"]

    Start -->|Need external data| D{"Real-time?"}
    D -->|Yes| E["MCP Protocol"]
    D -->|No/Cross-session| F["Memory"]

    Start -->|Complex project| G{"Multiple roles?"}
    G -->|Yes| H["Subagents"]
    G -->|No| I["Skills + Memory"]

    Start -->|Long-term context| J["Memory"]
    Start -->|Team workflow| K["Slash Command +<br/>Memory"]
    Start -->|Full automation| L["Skills +<br/>Subagents +<br/>MCP"]
```

---

## Tabela Resumo

| Aspecto | Slash Commands | Subagentes | Memória | MCP | Skills | Plugins |
|---------|---|---|---|---|---|---|
| **Dificuldade de Setup** | Fácil | Médio | Fácil | Médio | Médio | Fácil |
| **Curva de Aprendizado** | Baixa | Média | Baixa | Média | Média | Baixa |
| **Benefício para a Equipe** | Alto | Alto | Médio | Alto | Alto | Muito Alto |
| **Nível de Automação** | Baixo | Alto | Médio | Alto | Alto | Muito Alto |
| **Gerenciamento de Contexto** | Sessão única | Isolado | Persistente | Tempo real | Persistente | Todos os recursos |
| **Carga de Manutenção** | Baixa | Média | Baixa | Média | Média | Baixa |
| **Escalabilidade** | Boa | Excelente | Boa | Excelente | Excelente | Excelente |
| **Compartilhamento** | Regular | Regular | Bom | Bom | Bom | Excelente |
| **Versionamento** | Manual | Manual | Manual | Manual | Manual | Automático |
| **Instalação** | Cópia manual | Config manual | N/A | Config manual | Cópia manual | Um comando |

---

## Guia de Início Rápido

### Semana 1: Comece Simples
- Crie 2-3 slash commands para tarefas comuns
- Ative a Memória nas Configurações
- Documente os padrões da equipe no CLAUDE.md

### Semana 2: Adicione Acesso em Tempo Real
- Configure 1 MCP (GitHub ou Banco de Dados)
- Use `/mcp` para configurar
- Consulte dados ao vivo nos seus workflows

### Semana 3: Distribua o Trabalho
- Crie o primeiro Subagente para um papel específico
- Use o comando `/agents`
- Teste a delegação com uma tarefa simples

### Semana 4: Automatize Tudo
- Crie a primeira Skill para automação repetida
- Use o marketplace de Skills ou construa uma personalizada
- Combine todos os recursos para um workflow completo

### Continuamente
- Revise e atualize a Memória mensalmente
- Adicione novas Skills conforme padrões emergem
- Otimize consultas MCP
- Refine prompts de Subagentes

---

## Hooks

### Visão Geral

Hooks são comandos shell orientados a eventos que executam automaticamente em resposta a eventos do Claude Code. Eles permitem automação, validação e workflows personalizados sem intervenção manual.

### Eventos de Hook

O Claude Code suporta **25 eventos de hook** em quatro tipos de hook (command, http, prompt, agent):

| Evento de Hook | Gatilho | Casos de Uso |
|---------------|---------|-------------|
| **SessionStart** | Sessão inicia/retoma/limpa/compacta | Configuração de ambiente, inicialização |
| **InstructionsLoaded** | CLAUDE.md ou arquivo de regras carregado | Validação, transformação, aumento |
| **UserPromptSubmit** | Usuário envia prompt | Validação de entrada, filtragem de prompt |
| **PreToolUse** | Antes de qualquer ferramenta executar | Validação, portões de aprovação, logging |
| **PermissionRequest** | Diálogo de permissão exibido | Fluxos de aprovação/negação automática |
| **PostToolUse** | Após ferramenta ter sucesso | Auto-formatação, notificações, limpeza |
| **PostToolUseFailure** | Execução de ferramenta falha | Tratamento de erros, logging |
| **Notification** | Notificação enviada | Alertas, integrações externas |
| **SubagentStart** | Subagente criado | Injeção de contexto, inicialização |
| **SubagentStop** | Subagente termina | Validação de resultado, logging |
| **Stop** | Claude termina de responder | Geração de resumo, tarefas de limpeza |
| **StopFailure** | Erro de API encerra turno | Recuperação de erros, logging |
| **TeammateIdle** | Membro da equipe de agentes ocioso | Distribuição de trabalho, coordenação |
| **TaskCompleted** | Tarefa marcada como completa | Processamento pós-tarefa |
| **TaskCreated** | Tarefa criada via TaskCreate | Rastreamento de tarefas, logging |
| **ConfigChange** | Arquivo de configuração muda | Validação, propagação |
| **CwdChanged** | Diretório de trabalho muda | Configuração específica de diretório |
| **FileChanged** | Arquivo monitorado muda | Monitoramento de arquivo, gatilhos de rebuild |
| **PreCompact** | Antes da compactação de contexto | Preservação de estado |
| **PostCompact** | Após compactação completar | Ações pós-compactação |
| **WorktreeCreate** | Worktree sendo criado | Configuração de ambiente, instalação de dependências |
| **WorktreeRemove** | Worktree sendo removido | Limpeza, desalocação de recursos |
| **Elicitation** | Servidor MCP solicita entrada do usuário | Validação de entrada |
| **ElicitationResult** | Usuário responde à elicitação | Processamento de resposta |
| **SessionEnd** | Sessão termina | Limpeza, logging final |

### Hooks Comuns

Hooks são configurados em `~/.claude/settings.json` (nível de usuário) ou `.claude/settings.json` (nível de projeto):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write $CLAUDE_FILE_PATH"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "eslint $CLAUDE_FILE_PATH"
          }
        ]
      }
    ]
  }
}
```

### Variáveis de Ambiente do Hook

- `$CLAUDE_FILE_PATH` — Caminho para o arquivo sendo editado/escrito
- `$CLAUDE_TOOL_NAME` — Nome da ferramenta sendo usada
- `$CLAUDE_SESSION_ID` — Identificador da sessão atual
- `$CLAUDE_PROJECT_DIR` — Caminho do diretório do projeto

### Boas Práticas

✅ **Faça:**
- Mantenha hooks rápidos (< 1 segundo)
- Use hooks para validação e automação
- Trate erros graciosamente
- Use caminhos absolutos

❌ **Não faça:**
- Hooks interativos
- Hooks para tarefas de longa duração
- Credenciais codificadas diretamente

**Veja**: [06-hooks/](06-hooks/) para exemplos detalhados

---

## Checkpoints e Rewind

### Visão Geral

Checkpoints permitem que você salve o estado da conversa e retroceda a pontos anteriores, possibilitando experimentação segura e exploração de múltiplas abordagens.

### Conceitos-Chave

| Conceito | Descrição |
|----------|-----------|
| **Checkpoint** | Snapshot do estado da conversa incluindo mensagens, arquivos e contexto |
| **Rewind** | Retornar a um checkpoint anterior, descartando mudanças subsequentes |
| **Branch Point** | Checkpoint a partir do qual múltiplas abordagens são exploradas |

### Acessando Checkpoints

Checkpoints são criados automaticamente a cada prompt do usuário. Para retroceder:

```bash
# Pressione Esc duas vezes para abrir o navegador de checkpoints
Esc + Esc

# Ou use o comando /rewind
/rewind
```

Ao selecionar um checkpoint, você escolhe entre cinco opções:
1. **Restore code and conversation** — Reverter ambos para aquele ponto
2. **Restore conversation** — Retroceder mensagens, manter o código atual
3. **Restore code** — Reverter arquivos, manter a conversa
4. **Summarize from here** — Compactar conversa em um resumo
5. **Never mind** — Cancelar

### Casos de Uso

| Cenário | Workflow |
|---------|----------|
| **Explorando Abordagens** | Salvar → Tentar A → Salvar → Retroceder → Tentar B → Comparar |
| **Refatoração Segura** | Salvar → Refatorar → Testar → Se falhar: Retroceder |
| **Testes A/B** | Salvar → Design A → Salvar → Retroceder → Design B → Comparar |
| **Recuperação de Erros** | Notar problema → Retroceder ao último estado bom |

### Configuração

```json
{
  "autoCheckpoint": true
}
```

**Veja**: [08-checkpoints/](08-checkpoints/) para exemplos detalhados

---

## Recursos Avançados

### Modo de Planejamento

Crie planos de implementação detalhados antes de codificar.

**Ativação:**
```bash
/plan Implement user authentication system
```

**Benefícios:**
- Roteiro claro com estimativas de tempo
- Avaliação de riscos
- Decomposição sistemática de tarefas
- Oportunidade de revisão e modificação

### Raciocínio Estendido

Raciocínio profundo para problemas complexos.

**Ativação:**
- Alternar com `Alt+T` (ou `Option+T` no macOS) durante uma sessão
- Definir a variável de ambiente `MAX_THINKING_TOKENS` para controle programático

```bash
# Enable extended thinking via environment variable
export MAX_THINKING_TOKENS=50000
claude -p "Should we use microservices or monolith?"
```

**Benefícios:**
- Análise minuciosa de trade-offs
- Melhores decisões arquiteturais
- Consideração de casos extremos
- Avaliação sistemática

### Tarefas em Segundo Plano

Execute operações longas sem bloquear a conversa.

**Uso:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### Modos de Permissão

Controle o que o Claude pode fazer.

| Modo | Descrição | Caso de Uso |
|------|-----------|-------------|
| **default** | Permissões padrão com prompts para ações sensíveis | Desenvolvimento geral |
| **acceptEdits** | Aceitar automaticamente edições de arquivo sem confirmação | Workflows de edição confiáveis |
| **plan** | Apenas análise e planejamento, sem modificações de arquivo | Revisão de código, planejamento de arquitetura |
| **auto** | Aprovar automaticamente ações seguras, perguntar apenas para arriscadas | Autonomia equilibrada com segurança |
| **dontAsk** | Executar todas as ações sem prompts de confirmação | Usuários experientes, automação |
| **bypassPermissions** | Acesso total irrestrito, sem verificações de segurança | Pipelines CI/CD, scripts confiáveis |

**Uso:**
```bash
claude --permission-mode plan          # Read-only analysis
claude --permission-mode acceptEdits   # Auto-accept edits
claude --permission-mode auto          # Auto-approve safe actions
claude --permission-mode dontAsk       # No confirmation prompts
```

### Modo Headless (Modo Print)

Execute o Claude Code sem entrada interativa para automação e CI/CD usando a flag `-p` (print).

**Uso:**
```bash
# Run specific task
claude -p "Run all tests"

# Pipe input for analysis
cat error.log | claude -p "explain this error"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR changes and report issues"

# JSON output for scripting
claude -p --output-format json "list all functions in src/"
```

### Tarefas Agendadas

Execute tarefas em um agendamento recorrente usando o comando `/loop`.

**Uso:**
```bash
/loop every 30m "Run tests and report failures"
/loop every 2h "Check for dependency updates"
/loop every 1d "Generate daily summary of code changes"
```

As tarefas agendadas são executadas em segundo plano e reportam os resultados quando concluídas. São úteis para monitoramento contínuo, verificações periódicas e workflows de manutenção automatizada.

### Integração com Chrome

O Claude Code pode se integrar ao navegador Chrome para tarefas de automação web. Isso permite capacidades como navegar em páginas web, preencher formulários, tirar screenshots e extrair dados de websites diretamente no seu workflow de desenvolvimento.

### Gerenciamento de Sessões

Gerencie múltiplas sessões de trabalho.

**Comandos:**
```bash
/resume                # Resume a previous conversation
/rename "Feature"      # Name the current session
/fork                  # Fork into a new session
claude -c              # Continue most recent conversation
claude -r "Feature"    # Resume session by name/ID
```

### Recursos Interativos

**Atalhos de Teclado:**
- `Ctrl + R` — Buscar no histórico de comandos
- `Tab` — Autocompletar
- `↑ / ↓` — Histórico de comandos
- `Ctrl + L` — Limpar tela

**Entrada de Múltiplas Linhas:**
```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

### Configuração

Exemplo de configuração completa:

```json
{
  "planning": {
    "autoEnter": true,
    "requireApproval": true
  },
  "extendedThinking": {
    "enabled": true,
    "showThinkingProcess": true
  },
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5
  },
  "permissions": {
    "mode": "default"
  }
}
```

**Veja**: [09-advanced-features/](09-advanced-features/) para guia abrangente

---

## Recursos

- [Documentação do Claude Code](https://code.claude.com/docs/en/overview)
- [Documentação da Anthropic](https://docs.anthropic.com)
- [Servidores MCP no GitHub](https://github.com/modelcontextprotocol/servers)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)

---

*Última atualização: 11 de abril de 2026*
*Para Claude Haiku 4.5, Sonnet 4.6 e Opus 4.6*
*Inclui agora: Hooks, Checkpoints, Modo de Planejamento, Raciocínio Estendido, Tarefas em Segundo Plano, Modos de Permissão (6 modos), Modo Headless, Gerenciamento de Sessões, Auto Memory, Equipes de Agentes, Tarefas Agendadas, Integração Chrome, Canais, Ditado por Voz e Skills Integradas*

---
**Última Atualização**: 11 de abril de 2026
**Versão do Claude Code**: 2.1.101
**Fontes**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/memory
