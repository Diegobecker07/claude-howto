<!-- i18n-source: 05-mcp/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

Esta pasta contém documentação abrangente e exemplos para configurações e uso de servidores MCP com o Claude Code.

## Visão geral

MCP (Model Context Protocol) é uma forma padronizada de o Claude acessar ferramentas externas, APIs e fontes de dados em tempo real. Ao contrário da Memory, o MCP fornece acesso ao vivo a dados em constante mudança.

Características principais:
- Acesso em tempo real a serviços externos
- Sincronização de dados ao vivo
- Arquitetura extensível
- Autenticação segura
- Interações baseadas em ferramentas

## Arquitetura MCP

```mermaid
graph TB
    A["Claude"]
    B["Servidor MCP"]
    C["Serviço Externo"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## Ecossistema MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Servidor MCP<br/>Filesystem"]
    A -->|MCP| C["Servidor MCP<br/>GitHub"]
    A -->|MCP| D["Servidor MCP<br/>Database"]
    A -->|MCP| E["Servidor MCP<br/>Slack"]
    A -->|MCP| F["Servidor MCP<br/>Google Docs"]

    B -->|File I/O| G["Arquivos locais"]
    C -->|API| H["Repos GitHub"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Workspace Slack"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## Métodos de instalação MCP

O Claude Code suporta múltiplos protocolos de transporte para conexões com servidores MCP:

### Transporte HTTP (recomendado)

```bash
# Conexão HTTP básica
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP com header de autenticação
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer seu-token"
```

### Transporte Stdio (local)

Para servidores MCP em execução local:

```bash
# Servidor Node.js local
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# Com variáveis de ambiente
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### Transporte SSE (descontinuado)

O transporte Server-Sent Events está descontinuado em favor do `http`, mas ainda é suportado:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Nota para Windows

No Windows nativo (não WSL), use `cmd /c` para comandos npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### Autenticação OAuth 2.0

O Claude Code suporta OAuth 2.0 para servidores MCP que o exigem. Ao conectar a um servidor habilitado com OAuth, o Claude Code cuida de todo o fluxo de autenticação:

```bash
# Conectar a um servidor MCP habilitado com OAuth (fluxo interativo)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Pré-configurar credenciais OAuth para configuração não interativa
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "seu-client-id" \
  --client-secret "seu-client-secret" \
  --callback-port 8080
```

| Recurso | Descrição |
|---------|-----------|
| **OAuth interativo** | Use `/mcp` para acionar o fluxo OAuth baseado em navegador |
| **Clientes OAuth pré-configurados** | Clientes OAuth integrados para serviços comuns como Notion, Stripe e outros (v2.1.30+) |
| **Credenciais pré-configuradas** | Flags `--client-id`, `--client-secret`, `--callback-port` para configuração automatizada |
| **Armazenamento de tokens** | Tokens são armazenados com segurança no keychain do sistema |
| **Step-up auth** | Suporta autenticação step-up para operações privilegiadas |
| **Cache de descoberta** | Metadados de descoberta OAuth são cacheados para reconexões mais rápidas |
| **Substituição de metadados** | `oauth.authServerMetadataUrl` em `.mcp.json` para substituir a descoberta padrão de metadados OAuth |

#### Substituindo a descoberta de metadados OAuth

Se seu servidor MCP retorna erros no endpoint padrão de metadados OAuth (`/.well-known/oauth-authorization-server`) mas expõe um endpoint OIDC funcional, você pode dizer ao Claude Code para buscar metadados OAuth de uma URL específica. Defina `authServerMetadataUrl` no objeto `oauth` da configuração do servidor:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

A URL deve usar `https://`. Esta opção requer Claude Code v2.1.64 ou posterior.

### Conectores MCP do Claude.ai

Servidores MCP configurados na sua conta Claude.ai estão automaticamente disponíveis no Claude Code. Isso significa que quaisquer conexões MCP configuradas pela interface web do Claude.ai estarão acessíveis sem configuração adicional.

Os conectores MCP do Claude.ai também estão disponíveis no modo `--print` (v2.1.83+), habilitando uso não interativo e com scripts.

Para desabilitar os servidores MCP do Claude.ai no Claude Code, defina a variável de ambiente `ENABLE_CLAUDEAI_MCP_SERVERS` como `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Nota:** Este recurso está disponível apenas para usuários logados com contas Claude.ai.

## Processo de configuração MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as Serviço Externo

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP conectado!
```

## Busca de ferramentas MCP

Quando as descrições de ferramentas MCP excedem 10% da janela de contexto, o Claude Code habilita automaticamente a busca de ferramentas para selecionar eficientemente as ferramentas certas sem sobrecarregar o contexto do modelo.

| Configuração | Valor | Descrição |
|-------------|-------|-----------|
| `ENABLE_TOOL_SEARCH` | `auto` (padrão) | Habilita automaticamente quando descrições excedem 10% do contexto |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Habilita automaticamente em um limite personalizado de `N` ferramentas |
| `ENABLE_TOOL_SEARCH` | `true` | Sempre habilitado independentemente da contagem de ferramentas |
| `ENABLE_TOOL_SEARCH` | `false` | Desabilitado; todas as descrições de ferramentas enviadas completas |

> **Nota:** A busca de ferramentas requer Sonnet 4 ou posterior, ou Opus 4 ou posterior. Modelos Haiku não são suportados para busca de ferramentas.

## Atualizações dinâmicas de ferramentas

O Claude Code suporta notificações `list_changed` do MCP. Quando um servidor MCP adiciona, remove ou modifica dinamicamente suas ferramentas disponíveis, o Claude Code recebe a atualização e ajusta sua lista de ferramentas automaticamente — sem necessidade de reconexão ou reinicialização.

## Apps MCP

MCP Apps é a primeira extensão oficial do MCP, habilitando chamadas de ferramentas MCP para retornar componentes de UI interativos que são renderizados diretamente na interface de chat. Em vez de respostas em texto simples, servidores MCP podem entregar dashboards ricos, formulários, visualizações de dados e workflows de múltiplas etapas — todos exibidos inline sem sair da conversa.

## Elicitação MCP

Servidores MCP podem solicitar entrada estruturada do usuário via diálogos interativos (v2.1.49+). Isso permite que um servidor MCP peça informações adicionais no meio do workflow — por exemplo, solicitando uma confirmação, selecionando de uma lista de opções ou preenchendo campos obrigatórios — adicionando interatividade às interações com servidores MCP.

## Limite de descrição e instrução de ferramenta

A partir da v2.1.84, o Claude Code impõe um **limite de 2 KB** nas descrições e instruções de ferramentas por servidor MCP. Isso impede que servidores individuais consumam contexto excessivo com definições de ferramentas excessivamente detalhadas, reduzindo o inchaço de contexto e mantendo as interações eficientes.

## Prompts MCP como Slash Commands

Servidores MCP podem expor prompts que aparecem como Slash Commands no Claude Code. Os prompts são acessíveis usando a convenção de nomenclatura:

```
/mcp__<servidor>__<prompt>
```

Por exemplo, se um servidor chamado `github` expõe um prompt chamado `review`, você pode invocá-lo como `/mcp__github__review`.

## Deduplicação de servidores

Quando o mesmo servidor MCP é definido em múltiplos escopos (local, projeto, usuário), a configuração local tem precedência. Isso permite substituir configurações MCP de nível de projeto ou usuário com personalizações locais sem conflitos.

## Recursos MCP via @ menções

Você pode referenciar recursos MCP diretamente nos seus prompts usando a sintaxe de @ menção:

```
@nome-do-servidor:protocolo://recurso/caminho
```

Por exemplo, para referenciar um recurso de banco de dados específico:

```
@database:postgres://mydb/users
```

Isso permite que o Claude busque e inclua o conteúdo do recurso MCP inline como parte do contexto da conversa.

## Escopos MCP

As configurações MCP podem ser armazenadas em diferentes escopos com diferentes níveis de compartilhamento:

| Escopo | Localização | Descrição | Compartilhado com | Requer aprovação |
|--------|-------------|-----------|-------------------|-----------------|
| **Local** (padrão) | `~/.claude.json` (sob o caminho do projeto) | Privado para o usuário atual, apenas projeto atual (era chamado de `project` em versões antigas) | Apenas você | Não |
| **Projeto** | `.mcp.json` | Commitado no repositório git | Membros da equipe | Sim (primeiro uso) |
| **Usuário** | `~/.claude.json` | Disponível em todos os projetos (era chamado de `global` em versões antigas) | Apenas você | Não |

### Usando o escopo de projeto

Armazene configurações MCP específicas do projeto em `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

Membros da equipe verão um prompt de aprovação no primeiro uso de MCPs de projeto.

## Gerenciamento de configuração MCP

### Adicionando servidores MCP

```bash
# Adicionar servidor baseado em HTTP
claude mcp add --transport http github https://api.github.com/mcp

# Adicionar servidor stdio local
claude mcp add --transport stdio database -- npx @company/db-server

# Listar todos os servidores MCP
claude mcp list

# Obter detalhes de um servidor específico
claude mcp get github

# Remover um servidor MCP
claude mcp remove github

# Redefinir escolhas de aprovação específicas do projeto
claude mcp reset-project-choices

# Importar do Claude Desktop
claude mcp add-from-claude-desktop
```

## Tabela de servidores MCP disponíveis

| Servidor MCP | Finalidade | Ferramentas comuns | Auth | Tempo real |
|-------------|-----------|-------------------|------|-----------|
| **Filesystem** | Operações de arquivo | read, write, delete | Permissões do SO | ✅ Sim |
| **GitHub** | Gerenciamento de repositório | list_prs, create_issue, push | OAuth | ✅ Sim |
| **Slack** | Comunicação em equipe | send_message, list_channels | Token | ✅ Sim |
| **Database** | Queries SQL | query, insert, update | Credenciais | ✅ Sim |
| **Google Docs** | Acesso a documentos | read, write, share | OAuth | ✅ Sim |
| **Asana** | Gerenciamento de projetos | create_task, update_status | Chave de API | ✅ Sim |
| **Stripe** | Dados de pagamento | list_charges, create_invoice | Chave de API | ✅ Sim |
| **Memory** | Memory persistente | store, retrieve, delete | Local | ❌ Não |

## Exemplos práticos

### Exemplo 1: Configuração do GitHub MCP

**Arquivo:** `.mcp.json` (raiz do projeto)

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

**Ferramentas GitHub MCP disponíveis:**

#### Gerenciamento de pull requests
- `list_prs` — listar todos os PRs no repositório
- `get_pr` — obter detalhes do PR incluindo diff
- `create_pr` — criar novo PR
- `update_pr` — atualizar descrição/título do PR
- `merge_pr` — fazer merge do PR na branch main
- `review_pr` — adicionar comentários de revisão

**Exemplo de solicitação:**
```
/mcp__github__get_pr 456

# Retorna:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Gerenciamento de issues
- `list_issues` — listar todas as issues
- `get_issue` — obter detalhes da issue
- `create_issue` — criar nova issue
- `close_issue` — fechar issue
- `add_comment` — adicionar comentário à issue

#### Informações do repositório
- `get_repo_info` — detalhes do repositório
- `list_files` — estrutura de árvore de arquivos
- `get_file_content` — ler conteúdo de arquivo
- `search_code` — buscar em todo o código

#### Operações de commit
- `list_commits` — histórico de commits
- `get_commit` — detalhes de um commit específico
- `create_commit` — criar novo commit

**Configuração**:
```bash
export GITHUB_TOKEN="seu_github_token"
# Ou use o CLI para adicionar diretamente:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Expansão de variáveis de ambiente na configuração

As configurações MCP suportam expansão de variáveis de ambiente com padrões de fallback. A sintaxe `${VAR}` e `${VAR:-default}` funciona nos seguintes campos: `command`, `args`, `env`, `url` e `headers`.

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-valor-padrao}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

As variáveis são expandidas em tempo de execução:
- `${VAR}` — usa a variável de ambiente, erro se não definida
- `${VAR:-default}` — usa a variável de ambiente, cai no padrão se não definida

### Exemplo 2: Configuração do Database MCP

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

**Exemplo de uso:**

```markdown
Usuário: Busque todos os usuários com mais de 10 pedidos

Claude: Vou consultar seu banco de dados para encontrar essa informação.

# Usando a ferramenta MCP de banco de dados:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Resultados:
- Alice: 15 pedidos
- Bob: 12 pedidos
- Charlie: 11 pedidos
```

**Configuração**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Ou use o CLI para adicionar diretamente:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### Exemplo 3: Workflow com múltiplos MCPs

**Cenário: Geração de relatório diário**

```markdown
# Workflow de relatório diário usando múltiplos MCPs

## Configuração
1. GitHub MCP — buscar métricas de PRs
2. Database MCP — consultar dados de vendas
3. Slack MCP — postar relatório
4. Filesystem MCP — salvar relatório

## Workflow

### Passo 1: Buscar dados do GitHub
/mcp__github__list_prs completed:true last:7days

Saída:
- Total de PRs: 42
- Tempo médio de merge: 2,3 horas
- Tempo de resposta de revisão: 1,1 horas

### Passo 2: Consultar banco de dados
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Saída:
- Vendas: 247
- Receita: R$ 12.450

### Passo 3: Gerar relatório
Combinar dados em relatório HTML

### Passo 4: Salvar no Filesystem
Escrever report.html em /reports/

### Passo 5: Postar no Slack
Enviar resumo para o canal #daily-reports

Saída final:
✅ Relatório gerado e postado
📊 47 PRs mergeados esta semana
💰 R$ 12.450 em vendas diárias
```

**Configuração**:
```bash
export GITHUB_TOKEN="seu_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="seu_slack_token"
# Adicione cada servidor MCP via CLI ou configure em .mcp.json
```

### Exemplo 4: Operações do Filesystem MCP

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

**Operações disponíveis:**

| Operação | Comando | Finalidade |
|----------|---------|-----------|
| Listar arquivos | `ls ~/projects` | Mostrar conteúdo do diretório |
| Ler arquivo | `cat src/main.ts` | Ler conteúdo do arquivo |
| Escrever arquivo | `create docs/api.md` | Criar novo arquivo |
| Editar arquivo | `edit src/app.ts` | Modificar arquivo |
| Buscar | `grep "async function"` | Buscar em arquivos |
| Deletar | `rm old-file.js` | Deletar arquivo |

**Configuração**:
```bash
# Use o CLI para adicionar diretamente:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## Matriz de decisão: MCP vs Memory

```mermaid
graph TD
    A["Precisa de dados externos?"]
    A -->|Não| B["Use Memory"]
    A -->|Sim| C["Os dados mudam com frequência?"]
    C -->|Não/Raramente| B
    C -->|Sim/Frequentemente| D["Use MCP"]

    B -->|Armazena| E["Preferências<br/>Contexto<br/>Histórico"]
    D -->|Acessa| F["APIs ao vivo<br/>Bancos de dados<br/>Serviços"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## Padrão de requisição/resposta

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as Servidor MCP
    participant DB as Banco de dados

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Acesso em tempo real<br/>Sem cache
```

## Variáveis de ambiente

Armazene credenciais sensíveis em variáveis de ambiente:

```bash
# ~/.bashrc ou ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Em seguida, referencie-as na configuração MCP:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude como servidor MCP (`claude mcp serve`)

O próprio Claude Code pode atuar como servidor MCP para outras aplicações. Isso permite que ferramentas externas, editores e sistemas de automação aproveitem as capacidades do Claude por meio do protocolo MCP padrão.

```bash
# Iniciar o Claude Code como servidor MCP em stdio
claude mcp serve
```

Outras aplicações podem então se conectar a este servidor como fariam com qualquer servidor MCP baseado em stdio. Por exemplo, para adicionar o Claude Code como servidor MCP em outra instância do Claude Code:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

Isso é útil para construir workflows multi-agente onde uma instância do Claude orquestra outra.

## Configuração gerenciada de MCP (Enterprise)

Para implantações enterprise, administradores de TI podem impor políticas de servidor MCP por meio do arquivo de configuração `managed-mcp.json`. Este arquivo fornece controle exclusivo sobre quais servidores MCP são permitidos ou bloqueados em toda a organização.

**Localização:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Recursos:**
- `allowedMcpServers` — lista de permissão de servidores autorizados
- `deniedMcpServers` — lista de bloqueio de servidores proibidos
- Suporta correspondência por nome de servidor, comando e padrões de URL
- Políticas MCP de toda a organização aplicadas antes da configuração do usuário
- Previne conexões não autorizadas com servidores

**Exemplo de configuração:**

```json
{
  "allowedMcpServers": [
    {
      "serverName": "github",
      "serverUrl": "https://api.github.com/mcp"
    },
    {
      "serverName": "company-internal",
      "serverCommand": "company-mcp-server"
    }
  ],
  "deniedMcpServers": [
    {
      "serverName": "untrusted-*"
    },
    {
      "serverUrl": "http://*"
    }
  ]
}
```

> **Nota:** Quando tanto `allowedMcpServers` quanto `deniedMcpServers` correspondem a um servidor, a regra de negação tem precedência.

## Servidores MCP fornecidos por plugins

Plugins podem incluir seus próprios servidores MCP, tornando-os disponíveis automaticamente quando o plugin é instalado. Servidores MCP fornecidos por plugins podem ser definidos de duas formas:

1. **`.mcp.json` standalone** — coloque um arquivo `.mcp.json` no diretório raiz do plugin
2. **Inline em `plugin.json`** — defina servidores MCP diretamente no manifesto do plugin

Use a variável `${CLAUDE_PLUGIN_ROOT}` para referenciar caminhos relativos ao diretório de instalação do plugin:

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## MCP com escopo de Subagent

Servidores MCP podem ser definidos inline no frontmatter do agente usando a chave `mcpServers:`, limitando-os a um Subagent específico em vez de todo o projeto. Isso é útil quando um agente precisa de acesso a um servidor MCP específico que outros agentes no workflow não precisam.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

Você é um agente com acesso a my-tool para operações especializadas.
```

Servidores MCP com escopo de Subagent estão disponíveis apenas dentro do contexto de execução daquele agente e não são compartilhados com o agente pai ou irmãos.

## Limites de saída MCP

O Claude Code impõe limites na saída de ferramentas MCP para prevenir transbordamento de contexto:

| Limite | Limite | Comportamento |
|--------|--------|--------------|
| **Aviso** | 10.000 tokens | Um aviso é exibido indicando que a saída é grande |
| **Máximo padrão** | 25.000 tokens | A saída é truncada além deste limite |
| **Persistência em disco** | 50.000 caracteres | Resultados de ferramentas acima de 50K chars são persistidos em disco |

O limite máximo de saída é configurável via variável de ambiente `MAX_MCP_OUTPUT_TOKENS`:

```bash
# Aumentar o máximo para 50.000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Resolvendo inchaço de contexto com execução de código

Conforme a adoção do MCP escala, conectar-se a dezenas de servidores com centenas ou milhares de ferramentas cria um desafio significativo: **inchaço de contexto**. Este é indiscutivelmente o maior problema com MCP em escala, e a equipe de engenharia da Anthropic propôs uma solução elegante — usar execução de código em vez de chamadas diretas de ferramentas.

> **Fonte**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — Blog de Engenharia da Anthropic

### O problema: duas fontes de desperdício de tokens

**1. Definições de ferramentas sobrecarregam a janela de contexto**

A maioria dos clientes MCP carrega todas as definições de ferramentas antecipadamente. Quando conectado a milhares de ferramentas, o modelo deve processar centenas de milhares de tokens antes mesmo de ler a solicitação do usuário.

**2. Resultados intermediários consomem tokens adicionais**

Cada resultado intermediário de ferramenta passa pelo contexto do modelo. Considere transferir uma transcrição de reunião do Google Drive para o Salesforce — a transcrição completa flui pelo contexto **duas vezes**: uma ao lê-la e outra ao escrevê-la no destino. Uma transcrição de reunião de 2 horas pode significar 50.000+ tokens extras.

```mermaid
graph LR
    A["Modelo"] -->|"Tool Call: getDocument"| B["Servidor MCP"]
    B -->|"Transcrição completa (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(reenvia transcrição completa)"| B
    B -->|"Confirmação"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### A solução: ferramentas MCP como APIs de código

Em vez de passar definições de ferramentas e resultados pela janela de contexto, o agente **escreve código** que chama ferramentas MCP como APIs. O código roda em um ambiente de execução em sandbox, e apenas o resultado final retorna ao modelo.

```mermaid
graph LR
    A["Modelo"] -->|"Escreve código"| B["Ambiente de<br/>Execução de Código"]
    B -->|"Chama ferramentas diretamente"| C["Servidores MCP"]
    C -->|"Dados ficam no<br/>ambiente de execução"| B
    B -->|"Apenas resultado final<br/>(tokens mínimos)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### Como funciona

As ferramentas MCP são apresentadas como uma árvore de arquivos de funções tipadas:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

Cada arquivo de ferramenta contém um wrapper tipado:

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

O agente então escreve código para orquestrar as ferramentas:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Os dados fluem diretamente entre ferramentas — nunca pelo modelo
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**Resultado: o uso de tokens cai de ~150.000 para ~2.000 — uma redução de 98,7%.**

### Principais benefícios

| Benefício | Descrição |
|-----------|-----------|
| **Divulgação progressiva** | O agente navega pelo sistema de arquivos para carregar apenas as definições de ferramentas necessárias, em vez de todas antecipadamente |
| **Resultados eficientes em contexto** | Os dados são filtrados/transformados no ambiente de execução antes de retornar ao modelo |
| **Controle de fluxo poderoso** | Loops, condicionais e tratamento de erros rodam no código sem round-trips pelo modelo |
| **Preservação de privacidade** | Dados intermediários (PII, registros sensíveis) ficam no ambiente de execução; nunca entram no contexto do modelo |
| **Persistência de estado** | Agentes podem salvar resultados intermediários em arquivos e construir funções de skill reutilizáveis |

#### Exemplo: filtrando grandes conjuntos de dados

```typescript
// Sem execução de código — todas as 10.000 linhas fluem pelo contexto
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> retorna 10.000 linhas no contexto

// Com execução de código — filtrar no ambiente de execução
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Encontrado ${pendingOrders.length} pedidos pendentes`);
console.log(pendingOrders.slice(0, 5)); // Apenas 5 linhas chegam ao modelo
```

#### Exemplo: loop sem round-tripping

```typescript
// Aguardar notificação de deploy — roda inteiramente em código
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Notificação de deploy recebida');
```

### Compensações a considerar

A execução de código introduz sua própria complexidade. Executar código gerado por agentes requer:

- Um **ambiente de execução em sandbox seguro** com limites de recursos apropriados
- **Monitoramento e logging** do código executado
- **Overhead de infraestrutura** adicional em comparação com chamadas diretas de ferramentas

Os benefícios — custos reduzidos de tokens, menor latência, melhor composição de ferramentas — devem ser ponderados contra esses custos de implementação. Para agentes com apenas alguns servidores MCP, chamadas diretas de ferramentas podem ser mais simples. Para agentes em escala (dezenas de servidores, centenas de ferramentas), a execução de código é uma melhoria significativa.

### MCPorter: um runtime para composição de ferramentas MCP

[MCPorter](https://github.com/steipete/mcporter) é um runtime TypeScript e toolkit CLI que torna prático chamar servidores MCP sem boilerplate — e ajuda a reduzir o inchaço de contexto por meio de exposição seletiva de ferramentas e wrappers tipados.

**O que resolve:** em vez de carregar todas as definições de ferramentas de todos os servidores MCP antecipadamente, o MCPorter permite descobrir, inspecionar e chamar ferramentas específicas sob demanda — mantendo seu contexto enxuto.

**Recursos principais:**

| Recurso | Descrição |
|---------|-----------|
| **Descoberta zero-config** | Descobre automaticamente servidores MCP do Cursor, Claude, Codex ou configs locais |
| **Clientes de ferramenta tipados** | `mcporter emit-ts` gera interfaces `.d.ts` e wrappers prontos para uso |
| **API composável** | `createServerProxy()` expõe ferramentas como métodos camelCase com helpers `.text()`, `.json()`, `.markdown()` |
| **Geração de CLI** | `mcporter generate-cli` converte qualquer servidor MCP em uma CLI standalone com filtragem `--include-tools` / `--exclude-tools` |
| **Ocultação de parâmetros** | Parâmetros opcionais ficam ocultos por padrão, reduzindo a verbosidade do esquema |

**Instalação:**

```bash
npx mcporter list          # Sem instalação necessária — descubra servidores instantaneamente
pnpm add mcporter          # Adicionar a um projeto
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**Exemplo — compondo ferramentas em TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Os dados fluem entre ferramentas sem passar pelo contexto do modelo
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Exemplo — chamada de ferramenta via CLI:**

```bash
# Chamar uma ferramenta específica diretamente
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# Listar servidores e ferramentas disponíveis
npx mcporter list
```

O MCPorter complementa a abordagem de execução de código descrita acima, fornecendo a infraestrutura de runtime para chamar ferramentas MCP como APIs tipadas — facilitando manter os dados intermediários fora do contexto do modelo.

## Melhores práticas

### Considerações de segurança

#### O que fazer ✅
- Use variáveis de ambiente para todas as credenciais
- Rotacione tokens e chaves de API regularmente (mensalmente recomendado)
- Use tokens somente leitura quando possível
- Limite o escopo de acesso do servidor MCP ao mínimo necessário
- Monitore o uso e logs de acesso do servidor MCP
- Use OAuth para serviços externos quando disponível
- Implemente rate limiting em requisições MCP
- Teste conexões MCP antes do uso em produção
- Documente todas as conexões MCP ativas
- Mantenha os pacotes de servidor MCP atualizados

#### O que não fazer ❌
- Não codifique credenciais diretamente nos arquivos de configuração
- Não commite tokens ou segredos no git
- Não compartilhe tokens em chats de equipe ou e-mails
- Não use tokens pessoais para projetos de equipe
- Não conceda permissões desnecessárias
- Não ignore erros de autenticação
- Não exponha endpoints MCP publicamente
- Não execute servidores MCP com privilégios de root/admin
- Não cache dados sensíveis em logs
- Não desabilite mecanismos de autenticação

### Melhores práticas de configuração

1. **Controle de versão**: mantenha `.mcp.json` no git mas use variáveis de ambiente para segredos
2. **Menor privilégio**: conceda permissões mínimas necessárias para cada servidor MCP
3. **Isolamento**: execute diferentes servidores MCP em processos separados quando possível
4. **Monitoramento**: registre todas as requisições e erros MCP para trilhas de auditoria
5. **Testes**: teste todas as configurações MCP antes de fazer deploy em produção

### Dicas de performance

- Cache dados acessados frequentemente no nível da aplicação
- Use queries MCP específicas para reduzir transferência de dados
- Monitore tempos de resposta para operações MCP
- Considere rate limiting para APIs externas
- Use batching ao realizar múltiplas operações

## Instruções de instalação

### Pré-requisitos
- Node.js e npm instalados
- CLI do Claude Code instalada
- Tokens/credenciais de API para serviços externos

### Configuração passo a passo

1. **Adicione seu primeiro servidor MCP** usando o CLI (exemplo: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   Ou crie um arquivo `.mcp.json` na raiz do projeto:
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

2. **Defina variáveis de ambiente:**
```bash
export GITHUB_TOKEN="seu_token_de_acesso_pessoal_github"
```

3. **Teste a conexão:**
```bash
claude /mcp
```

4. **Use ferramentas MCP:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Título" "Descrição"
```

### Instalação para serviços específicos

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP:**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP:**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## Solução de problemas

### Servidor MCP não encontrado
```bash
# Verifique se o servidor MCP está instalado
npm list -g @modelcontextprotocol/server-github

# Instale se estiver faltando
npm install -g @modelcontextprotocol/server-github
```

### Autenticação falhou
```bash
# Verifique se a variável de ambiente está definida
echo $GITHUB_TOKEN

# Reexporte se necessário
export GITHUB_TOKEN="seu_token"

# Verifique se o token tem as permissões corretas
# Verifique os escopos do token GitHub em: https://github.com/settings/tokens
```

### Timeout de conexão
- Verifique a conectividade de rede: `ping api.github.com`
- Verifique se o endpoint da API está acessível
- Verifique os limites de rate na API
- Tente aumentar o timeout na configuração
- Verifique problemas de firewall ou proxy

### Servidor MCP trava
- Verifique os logs do servidor MCP: `~/.claude/logs/`
- Verifique se todas as variáveis de ambiente estão definidas
- Garanta as permissões de arquivo corretas
- Tente reinstalar o pacote do servidor MCP
- Verifique processos conflitantes na mesma porta

## Conceitos relacionados

### Memory vs MCP
- **Memory**: armazena dados persistentes e imutáveis (preferências, contexto, histórico)
- **MCP**: acessa dados ao vivo e em constante mudança (APIs, bancos de dados, serviços em tempo real)

### Quando usar cada um
- **Use Memory** para: preferências do usuário, histórico de conversa, contexto aprendido
- **Use MCP** para: issues atuais do GitHub, queries ao banco de dados ao vivo, dados em tempo real

### Integração com outros recursos do Claude
- Combine MCP com Memory para contexto rico
- Use ferramentas MCP em prompts para melhor raciocínio
- Aproveite múltiplos MCPs para workflows complexos

## Recursos adicionais

- [Documentação oficial do MCP](https://code.claude.com/docs/en/mcp)
- [Especificação do Protocolo MCP](https://modelcontextprotocol.io/specification)
- [Repositório GitHub do MCP](https://github.com/modelcontextprotocol/servers)
- [Servidores MCP disponíveis](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — runtime TypeScript e CLI para chamar servidores MCP sem boilerplate
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — blog de engenharia da Anthropic sobre como resolver o inchaço de contexto
- [Referência CLI do Claude Code](https://code.claude.com/docs/en/cli-reference)
- [Documentação da API Claude](https://docs.anthropic.com)

---
**Última atualização**: 16 de abril de 2026
**Versão do Claude Code**: 2.1.112
**Fontes**:
- https://docs.anthropic.com/en/docs/claude-code/mcp
- https://www.anthropic.com/news/claude-opus-4-7
- https://support.claude.com/en/articles/12138966-release-notes
**Modelos compatíveis**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
