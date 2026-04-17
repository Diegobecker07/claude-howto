<!-- i18n-source: 06-hooks/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks são scripts automatizados que executam em resposta a eventos específicos durante as sessões do Claude Code. Eles permitem automação, validação, gerenciamento de permissões e fluxos de trabalho personalizados.

## Visão Geral

Hooks são ações automatizadas (comandos shell, webhooks HTTP, prompts de LLM ou avaliações de subagentes) que executam automaticamente quando eventos específicos ocorrem no Claude Code. Eles recebem entrada JSON e comunicam resultados via códigos de saída e saída JSON.

**Funcionalidades principais:**
- Automação orientada a eventos
- Entrada/saída baseada em JSON
- Suporte para tipos de hook: command, prompt, http e agent
- Correspondência de padrões para hooks específicos de ferramentas

## Configuração

Hooks são configurados em arquivos de configurações com uma estrutura específica:

- `~/.claude/settings.json` - Configurações do usuário (todos os projetos)
- `.claude/settings.json` - Configurações do projeto (compartilháveis, versionadas)
- `.claude/settings.local.json` - Configurações locais do projeto (não versionadas)
- Política gerenciada - Configurações em nível de organização
- Plugin `hooks/hooks.json` - Hooks com escopo de plugin
- Frontmatter de Skill/Agent - Hooks com tempo de vida do componente

### Estrutura Básica de Configuração

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "seu-comando-aqui",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**Campos principais:**

| Campo | Descrição | Exemplo |
|-------|-----------|---------|
| `matcher` | Padrão para corresponder nomes de ferramenta (sensível a maiúsculas) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Array de definições de hook | `[{ "type": "command", ... }]` |
| `type` | Tipo de hook: `"command"` (bash), `"prompt"` (LLM), `"http"` (webhook) ou `"agent"` (subagente) | `"command"` |
| `command` | Comando shell a executar | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Timeout opcional em segundos (padrão 60) | `30` |
| `once` | Se `true`, executa o hook apenas uma vez por sessão | `true` |

### Padrões de Matcher

| Padrão | Descrição | Exemplo |
|--------|-----------|---------|
| String exata | Corresponde ferramenta específica | `"Write"` |
| Padrão regex | Corresponde múltiplas ferramentas | `"Edit\|Write"` |
| Coringa | Corresponde todas as ferramentas | `"*"` ou `""` |
| Ferramentas MCP | Padrão de servidor e ferramenta | `"mcp__memory__.*"` |

**Valores do matcher InstructionsLoaded:**

| Valor do Matcher | Descrição |
|------------------|-----------|
| `session_start` | Instruções carregadas na inicialização da sessão |
| `nested_traversal` | Instruções carregadas durante travessia de diretório aninhado |
| `path_glob_match` | Instruções carregadas via correspondência de padrão glob de caminho |

## Tipos de Hook

O Claude Code suporta quatro tipos de hook:

### Hooks de Comando

O tipo de hook padrão. Executa um comando shell e se comunica via JSON stdin/stdout e códigos de saída.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### Hooks HTTP

> Adicionado na v2.1.63.

Endpoints de webhook remoto que recebem a mesma entrada JSON que os hooks de comando. Hooks HTTP fazem POST de JSON na URL e recebem uma resposta JSON. Hooks HTTP são roteados pelo sandbox quando o modo sandbox está ativado. A interpolação de variáveis de ambiente em URLs requer uma lista explícita `allowedEnvVars` por segurança.

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://meu-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**Propriedades principais:**
- `"type": "http"` -- identifica como hook HTTP
- `"url"` -- a URL do endpoint de webhook
- Roteado pelo sandbox quando sandbox está ativado
- Requer lista explícita `allowedEnvVars` para qualquer interpolação de variável de ambiente na URL

### Hooks de Prompt

Prompts avaliados por LLM onde o conteúdo do hook é um prompt que o Claude avalia. Usado principalmente com eventos `Stop` e `SubagentStop` para verificação inteligente de conclusão de tarefas.

```json
{
  "type": "prompt",
  "prompt": "Avalie se o Claude completou todas as tarefas solicitadas.",
  "timeout": 30
}
```

O LLM avalia o prompt e retorna uma decisão estruturada (veja [Hooks Baseados em Prompt](#hooks-baseados-em-prompt) para detalhes).

### Hooks de Agente

Hooks de verificação baseados em subagente que criam um agente dedicado para avaliar condições ou realizar verificações complexas. Ao contrário dos hooks de prompt (avaliação LLM de turno único), hooks de agente podem usar ferramentas e realizar raciocínio em múltiplas etapas.

```json
{
  "type": "agent",
  "prompt": "Verifique se as alterações de código seguem as diretrizes de arquitetura. Confira os documentos de design relevantes e compare.",
  "timeout": 120
}
```

**Propriedades principais:**
- `"type": "agent"` -- identifica como hook de agente
- `"prompt"` -- a descrição da tarefa para o subagente
- O agente pode usar ferramentas (Read, Grep, Bash, etc.) para realizar sua avaliação
- Retorna uma decisão estruturada semelhante aos hooks de prompt

## Eventos de Hook

O Claude Code suporta **26 eventos de hook**:

| Evento | Quando Disparado | Entrada do Matcher | Pode Bloquear | Uso Comum |
|--------|------------------|--------------------|---------------|-----------|
| **SessionStart** | Sessão começa/retoma/limpa/compacta | startup/resume/clear/compact | Não | Configuração de ambiente |
| **InstructionsLoaded** | Após carregar CLAUDE.md ou arquivo de regras | (nenhum) | Não | Modificar/filtrar instruções |
| **UserPromptSubmit** | Usuário envia prompt | (nenhum) | Sim | Validar prompts |
| **PreToolUse** | Antes da execução da ferramenta | Nome da ferramenta | Sim (allow/deny/ask) | Validar, modificar entradas |
| **PermissionRequest** | Diálogo de permissão exibido | Nome da ferramenta | Sim | Aprovar/negar automaticamente |
| **PermissionDenied** | Usuário nega prompt de permissão | Nome da ferramenta | Não | Log, análise, aplicação de política |
| **PostToolUse** | Após ferramenta ter sucesso | Nome da ferramenta | Não | Adicionar contexto, feedback |
| **PostToolUseFailure** | Execução da ferramenta falha | Nome da ferramenta | Não | Tratamento de erros, log |
| **Notification** | Notificação enviada | Tipo de notificação | Não | Notificações personalizadas |
| **SubagentStart** | Subagente criado | Nome do tipo de agente | Não | Configuração de subagente |
| **SubagentStop** | Subagente termina | Nome do tipo de agente | Sim | Validação de subagente |
| **Stop** | Claude termina de responder | (nenhum) | Sim | Verificação de conclusão de tarefa |
| **StopFailure** | Erro de API encerra turno | (nenhum) | Não | Recuperação de erros, log |
| **TeammateIdle** | Membro da equipe de agentes ocioso | (nenhum) | Sim | Coordenação de membros |
| **TaskCompleted** | Tarefa marcada como completa | (nenhum) | Sim | Ações pós-tarefa |
| **TaskCreated** | Tarefa criada via TaskCreate | (nenhum) | Não | Rastreamento de tarefas, log |
| **ConfigChange** | Arquivo de configuração muda | (nenhum) | Sim (exceto política) | Reagir a atualizações de config |
| **CwdChanged** | Diretório de trabalho muda | (nenhum) | Não | Configuração específica de diretório |
| **FileChanged** | Arquivo monitorado muda | (nenhum) | Não | Monitoramento de arquivo, rebuild |
| **PreCompact** | Antes da compactação de contexto | manual/auto | Não | Ações pré-compactação |
| **PostCompact** | Após compactação concluída | (nenhum) | Não | Ações pós-compactação |
| **WorktreeCreate** | Worktree sendo criado | (nenhum) | Sim (retorno de caminho) | Inicialização de worktree |
| **WorktreeRemove** | Worktree sendo removido | (nenhum) | Não | Limpeza de worktree |
| **Elicitation** | Servidor MCP solicita entrada do usuário | (nenhum) | Sim | Validação de entrada |
| **ElicitationResult** | Usuário responde à elicitação | (nenhum) | Sim | Processamento de resposta |
| **SessionEnd** | Sessão termina | (nenhum) | Não | Limpeza, log final |

### PreToolUse

Executa após o Claude criar parâmetros de ferramenta e antes do processamento. Use para validar ou modificar entradas de ferramentas.

**Configuração:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**Matchers comuns:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Controle de saída:**
- `permissionDecision`: `"allow"`, `"deny"` ou `"ask"`
- `permissionDecisionReason`: Explicação para a decisão
- `updatedInput`: Parâmetros de entrada da ferramenta modificados

### PostToolUse

Executa imediatamente após a conclusão da ferramenta. Use para verificação, log ou fornecimento de contexto ao Claude.

**Configuração:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**Controle de saída:**
- Decisão `"block"` solicita ao Claude com feedback
- `additionalContext`: Contexto adicionado para o Claude

### UserPromptSubmit

Executa quando o usuário envia um prompt, antes do Claude processá-lo.

**Configuração:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**Controle de saída:**
- `decision`: `"block"` para impedir o processamento
- `reason`: Explicação se bloqueado
- `additionalContext`: Contexto adicionado ao prompt

### Stop e SubagentStop

Executam quando o Claude termina de responder (Stop) ou um subagente conclui (SubagentStop). Suporta avaliação baseada em prompt para verificação inteligente de conclusão de tarefas.

**Campo de entrada adicional:** Ambos os hooks `Stop` e `SubagentStop` recebem um campo `last_assistant_message` em sua entrada JSON, contendo a mensagem final do Claude ou do subagente antes de parar. Útil para avaliar a conclusão de tarefas.

**Configuração:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Avalie se o Claude completou todas as tarefas solicitadas.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### SubagentStart

Executa quando um subagente começa a executar. A entrada do matcher é o nome do tipo de agente, permitindo que hooks visem tipos específicos de subagente.

**Configuração:**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

Executa quando a sessão inicia ou retoma. Pode persistir variáveis de ambiente.

**Matchers:** `startup`, `resume`, `clear`, `compact`

**Funcionalidade especial:** Use `CLAUDE_ENV_FILE` para persistir variáveis de ambiente (também disponível nos hooks `CwdChanged` e `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

Executa quando a sessão termina para realizar limpeza ou log final. Não pode bloquear o encerramento.

**Valores do campo reason:**
- `clear` - Usuário limpou a sessão
- `logout` - Usuário saiu
- `prompt_input_exit` - Usuário saiu via entrada de prompt
- `other` - Outro motivo

**Configuração:**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### Evento Notification

Matchers atualizados para eventos de notificação:
- `permission_prompt` - Notificação de solicitação de permissão
- `idle_prompt` - Notificação de estado ocioso
- `auth_success` - Sucesso de autenticação
- `elicitation_dialog` - Diálogo exibido ao usuário

## Hooks com Escopo de Componente

Hooks podem ser anexados a componentes específicos (skills, agentes, comandos) em seu frontmatter:

**Em SKILL.md, agent.md ou command.md:**

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # Executar apenas uma vez por sessão
---
```

**Eventos suportados para hooks de componente:** `PreToolUse`, `PostToolUse`, `Stop`

Isso permite definir hooks diretamente no componente que os utiliza, mantendo código relacionado junto.

### Hooks no Frontmatter de Subagente

Quando um hook `Stop` é definido no frontmatter de um subagente, ele é automaticamente convertido em um hook `SubagentStop` com escopo para aquele subagente. Isso garante que o hook de parada só dispare quando aquele subagente específico concluir, em vez de quando a sessão principal parar.

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # O hook Stop acima é automaticamente convertido em SubagentStop para este subagente
---
```

## Evento PermissionRequest

Trata solicitações de permissão com formato de saída personalizado:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Mensagem personalizada",
      "interrupt": false
    }
  }
}
```

## Entrada e Saída do Hook

### Entrada JSON (via stdin)

Todos os hooks recebem entrada JSON via stdin:

```json
{
  "session_id": "abc123",
  "transcript_path": "/caminho/para/transcript.jsonl",
  "cwd": "/diretório/de/trabalho/atual",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/caminho/para/arquivo.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "main",
  "worktree": "/caminho/para/worktree"
}
```

**Campos comuns:**

| Campo | Descrição |
|-------|-----------|
| `session_id` | Identificador único da sessão |
| `transcript_path` | Caminho para o arquivo de transcrição da conversa |
| `cwd` | Diretório de trabalho atual |
| `hook_event_name` | Nome do evento que disparou o hook |
| `agent_id` | Identificador do agente executando este hook |
| `agent_type` | Tipo de agente (`"main"`, nome do tipo de subagente, etc.) |
| `worktree` | Caminho para o worktree git, se o agente estiver executando em um |

### Códigos de Saída

| Código de Saída | Significado | Comportamento |
|-----------------|-------------|---------------|
| **0** | Sucesso | Continua, analisa stdout JSON |
| **2** | Erro bloqueante | Bloqueia operação, stderr exibido como erro |
| **Outros** | Erro não bloqueante | Continua, stderr exibido em modo verbose |

### Saída JSON (stdout, código de saída 0)

```json
{
  "continue": true,
  "stopReason": "Mensagem opcional se parar",
  "suppressOutput": false,
  "systemMessage": "Mensagem de aviso opcional",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "Arquivo está no diretório permitido",
    "updatedInput": {
      "file_path": "/caminho/modificado.js"
    }
  }
}
```

## Variáveis de Ambiente

| Variável | Disponibilidade | Descrição |
|----------|-----------------|-----------|
| `CLAUDE_PROJECT_DIR` | Todos os hooks | Caminho absoluto para a raiz do projeto |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Caminho do arquivo para persistir variáveis de ambiente |
| `CLAUDE_CODE_REMOTE` | Todos os hooks | `"true"` se executando em ambientes remotos |
| `${CLAUDE_PLUGIN_ROOT}` | Hooks de plugin | Caminho para o diretório do plugin |
| `${CLAUDE_PLUGIN_DATA}` | Hooks de plugin | Caminho para o diretório de dados do plugin |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Hooks SessionEnd | Timeout configurável em milissegundos para hooks SessionEnd (substitui o padrão) |

## Hooks Baseados em Prompt

Para eventos `Stop` e `SubagentStop`, você pode usar avaliação baseada em LLM:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Revise se todas as tarefas estão completas. Retorne sua decisão.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**Schema de Resposta do LLM:**
```json
{
  "decision": "approve",
  "reason": "Todas as tarefas concluídas com sucesso",
  "continue": false,
  "stopReason": "Tarefa completa"
}
```

## Exemplos

### Exemplo 1: Validador de Comando Bash (PreToolUse)

**Arquivo:** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Bloqueando comando rm -rf / perigoso"),
    (r"\bsudo\s+rm", "Bloqueando comando sudo rm"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Saída 2 = erro bloqueante

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Configuração:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### Exemplo 2: Scanner de Segurança (PostToolUse)

**Arquivo:** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Possível senha hardcoded"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Possível chave de API hardcoded"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Avisos de segurança para {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Exemplo 3: Auto-Formatar Código (PostToolUse)

**Arquivo:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# Lê JSON do stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# Formata com base na extensão do arquivo
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### Exemplo 4: Validador de Prompt (UserPromptSubmit)

**Arquivo:** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Perigoso: exclusão de banco de dados"),
    (r"rm\s+-rf\s+/", "Perigoso: exclusão de raiz"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Bloqueado: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### Exemplo 5: Hook Stop Inteligente (Baseado em Prompt)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Revise se o Claude completou todas as tarefas solicitadas. Verifique: 1) Todos os arquivos foram criados/modificados? 2) Houve erros não resolvidos? Se incompleto, explique o que está faltando.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Exemplo 6: Rastreador de Uso de Contexto (Par de Hooks)

Rastreie o consumo de tokens por solicitação usando hooks `UserPromptSubmit` (pré-mensagem) e `Stop` (pós-resposta) juntos.

**Arquivo:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Tracks token consumption per request.

Uses UserPromptSubmit as "pre-message" hook and Stop as "post-response" hook
to calculate the delta in token usage for each request.

Token Counting Methods:
1. Character estimation (default): ~4 chars per token, no dependencies
2. tiktoken (optional): More accurate (~90-95%), requires: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# Configuration
CONTEXT_LIMIT = 128000  # Claude's context window (adjust for your model)
USE_TIKTOKEN = False    # Set True if tiktoken is installed for better accuracy


def get_state_file(session_id: str) -> str:
    """Get temp file path for storing pre-message token count, isolated by session."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Count tokens in text.

    Uses tiktoken with p50k_base encoding if available (~90-95% accuracy),
    otherwise falls back to character estimation (~80-90% accuracy).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Fall back to estimation

    # Character-based estimation: ~4 characters per token for English
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Read and concatenate all content from transcript file."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # Extract text content from various message formats
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """Pre-message hook: Save current token count before request."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Save to temp file for later comparison
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Post-response hook: Calculate and report token delta."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Load pre-message count
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # Calculate delta
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # Report usage
    method = "tiktoken" if USE_TIKTOKEN else "estimated"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% used, ~{remaining:,} remaining)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"This request: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**Configuração:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**Como funciona:**
1. `UserPromptSubmit` dispara antes de seu prompt ser processado — salva a contagem de tokens atual
2. `Stop` dispara após o Claude responder — calcula o delta e reporta o uso
3. Cada sessão é isolada via `session_id` no nome do arquivo temporário

**Métodos de Contagem de Tokens:**

| Método | Precisão | Dependências | Velocidade |
|--------|----------|--------------|------------|
| Estimativa por caracteres | ~80-90% | Nenhuma | <1ms |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10ms |

> **Nota:** A Anthropic não lançou um tokenizador offline oficial. Ambos os métodos são aproximações. A transcrição inclui prompts do usuário, respostas do Claude e saídas de ferramentas, mas NÃO prompts de sistema ou contexto interno.

### Exemplo 7: Script de Configuração de Permissões do Modo Auto (Script de Configuração Única)

Um script de configuração única que preenche `~/.claude/settings.json` com ~67 regras de permissão seguras equivalentes à linha de base do modo auto do Claude Code — sem nenhum hook, sem lembrar escolhas futuras. Execute uma vez; seguro para re-executar (pula regras já presentes).

**Arquivo:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Pré-visualizar o que seria adicionado
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Aplicar
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**O que é adicionado:**

| Categoria | Exemplos |
|-----------|---------|
| Ferramentas nativas | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Git somente leitura | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git escrita (local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Gerenciadores de pacotes | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build e teste | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell comum | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**O que é intencionalmente excluído** (nunca adicionado por este script):
- `rm -rf`, `sudo`, force push, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, deploys em produção

## Hooks de Plugin

Plugins podem incluir hooks em seu arquivo `hooks/hooks.json`:

**Arquivo:** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**Variáveis de Ambiente em Hooks de Plugin:**
- `${CLAUDE_PLUGIN_ROOT}` - Caminho para o diretório do plugin
- `${CLAUDE_PLUGIN_DATA}` - Caminho para o diretório de dados do plugin

Isso permite que plugins incluam validação e automação de hooks personalizados.

## Hooks de Ferramentas MCP

Ferramentas MCP seguem o padrão `mcp__<servidor>__<ferramenta>`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Operação de memória registrada\"}'"
          }
        ]
      }
    ]
  }
}
```

## Considerações de Segurança

### Aviso

**USE POR SUA CONTA E RISCO**: Hooks executam comandos shell arbitrários. Você é o único responsável por:
- Comandos que você configura
- Permissões de acesso/modificação de arquivos
- Possível perda de dados ou danos ao sistema
- Testar hooks em ambientes seguros antes do uso em produção

### Notas de Segurança

- **Confiança no workspace necessária:** Os comandos de saída de hook `statusLine` e `fileSuggestion` agora requerem aceitação de confiança no workspace antes de entrar em vigor.
- **Hooks HTTP e variáveis de ambiente:** Hooks HTTP requerem uma lista explícita `allowedEnvVars` para usar interpolação de variável de ambiente em URLs. Isso previne vazamento acidental de variáveis de ambiente sensíveis para endpoints remotos.
- **Hierarquia de configurações gerenciadas:** A configuração `disableAllHooks` agora respeita a hierarquia de configurações gerenciadas, significando que configurações em nível de organização podem forçar a desativação de hooks que usuários individuais não podem substituir.

### Boas Práticas

| Faça | Não Faça |
|------|----------|
| Valide e sanitize todas as entradas | Confie cegamente nos dados de entrada |
| Coloque aspas em variáveis shell: `"$VAR"` | Use sem aspas: `$VAR` |
| Bloqueie travessia de caminho (`..`) | Permita caminhos arbitrários |
| Use caminhos absolutos com `$CLAUDE_PROJECT_DIR` | Hardcode de caminhos |
| Pule arquivos sensíveis (`.env`, `.git/`, chaves) | Processe todos os arquivos |
| Teste hooks em isolamento primeiro | Implante hooks não testados |
| Use `allowedEnvVars` explícito para hooks HTTP | Exponha todas as variáveis de ambiente para webhooks |

## Depuração

### Ativar Modo Debug

Execute o Claude com flag de debug para logs detalhados de hooks:

```bash
claude --debug
```

### Modo Verbose

Use `Ctrl+O` no Claude Code para ativar o modo verbose e ver o progresso de execução dos hooks.

### Testar Hooks Independentemente

```bash
# Testar com entrada JSON de amostra
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Verificar código de saída
echo $?
```

## Exemplo de Configuração Completa

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verifique se todas as tarefas estão completas antes de parar.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## Detalhes de Execução do Hook

| Aspecto | Comportamento |
|---------|---------------|
| **Timeout** | 60 segundos padrão, configurável por comando |
| **Paralelização** | Todos os hooks correspondentes executam em paralelo |
| **Deduplicação** | Comandos de hook idênticos são deduplicados |
| **Ambiente** | Executa no diretório atual com o ambiente do Claude Code |

## Resolução de Problemas

### Hook Não Executa
- Verifique se a sintaxe da configuração JSON está correta
- Verifique se o padrão do matcher corresponde ao nome da ferramenta
- Certifique-se de que o script existe e é executável: `chmod +x script.sh`
- Execute `claude --debug` para ver logs de execução de hooks
- Verifique se o hook lê JSON do stdin (não de argumentos de comando)

### Hook Bloqueia Inesperadamente
- Teste o hook com JSON de amostra: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- Verifique o código de saída: deve ser 0 para permitir, 2 para bloquear
- Verifique a saída de stderr (mostrada no código de saída 2)

### Erros de Análise JSON
- Sempre leia do stdin, não de argumentos de comando
- Use análise JSON adequada (não manipulação de string)
- Trate campos ausentes com elegância

## Instalação

### Passo 1: Criar Diretório de Hooks
```bash
mkdir -p ~/.claude/hooks
```

### Passo 2: Copiar Hooks de Exemplo
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Passo 3: Configurar nas Configurações
Edite `~/.claude/settings.json` ou `.claude/settings.json` com a configuração de hook mostrada acima.

## Conceitos Relacionados

- **[Checkpoints e Rewind](../08-checkpoints/)** - Salvar e restaurar o estado da conversa
- **[Comandos de Barra](../01-slash-commands/)** - Criar comandos de barra personalizados
- **[Skills](../03-skills/)** - Capacidades autônomas reutilizáveis
- **[Subagentes](../04-subagents/)** - Execução de tarefas delegada
- **[Plugins](../07-plugins/)** - Pacotes de extensão agrupados
- **[Recursos Avançados](../09-advanced-features/)** - Explorar capacidades avançadas do Claude Code

## Recursos Adicionais

- **[Documentação Oficial de Hooks](https://code.claude.com/docs/en/hooks)** - Referência completa de hooks
- **[Referência CLI](https://code.claude.com/docs/en/cli-reference)** - Documentação da interface de linha de comando
- **[Guia de Memória](../02-memory/)** - Configuração de contexto persistente

---
**Última Atualização**: 16 de abril de 2026
**Versão do Claude Code**: 2.1.112
**Fontes**:
- https://docs.anthropic.com/en/docs/claude-code/hooks
- https://www.anthropic.com/news/claude-opus-4-7
- https://support.claude.com/en/articles/12138966-release-notes
**Modelos Compatíveis**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
