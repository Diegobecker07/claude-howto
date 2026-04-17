<!-- i18n-source: 09-advanced-features/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Recursos Avançados

Guia abrangente para as capacidades avançadas do Claude Code, incluindo modo de planejamento, raciocínio estendido, modo auto, tarefas em segundo plano, modos de permissão, modo de impressão (não-interativo), gerenciamento de sessão, recursos interativos, canais, ditado por voz, controle remoto, sessões web, app de desktop, lista de tarefas, sugestões de prompt, worktrees git, sandbox, configurações gerenciadas e configuração.

## Índice

1. [Visão Geral](#visão-geral)
2. [Modo de Planejamento](#modo-de-planejamento)
3. [Ultraplan (Elaboração de Plano na Nuvem)](#ultraplan-elaboração-de-plano-na-nuvem)
4. [Raciocínio Estendido](#raciocínio-estendido)
5. [Modo Auto](#modo-auto)
6. [Tarefas em Segundo Plano](#tarefas-em-segundo-plano)
7. [Ferramenta Monitor (Streams Orientados a Eventos)](#ferramenta-monitor-streams-orientados-a-eventos)
8. [Tarefas Agendadas](#tarefas-agendadas)
9. [Modos de Permissão](#modos-de-permissão)
10. [Modo Headless](#modo-headless)
11. [Gerenciamento de Sessão](#gerenciamento-de-sessão)
12. [Recursos Interativos](#recursos-interativos)
13. [Ditado por Voz](#ditado-por-voz)
14. [Canais](#canais)
15. [Integração Chrome](#integração-chrome)
16. [Controle Remoto](#controle-remoto)
17. [Sessões Web](#sessões-web)
18. [App de Desktop](#app-de-desktop)
19. [Lista de Tarefas](#lista-de-tarefas)
20. [Sugestões de Prompt](#sugestões-de-prompt)
21. [Worktrees Git](#worktrees-git)
22. [Sandbox](#sandbox)
23. [Configurações Gerenciadas (Enterprise)](#configurações-gerenciadas-enterprise)
24. [Configuração e Ajustes](#configuração-e-ajustes)
25. [Equipes de Agentes](#equipes-de-agentes)
26. [Boas Práticas](#boas-práticas)
27. [Recursos Adicionais](#recursos-adicionais)

---

## Visão Geral

Os recursos avançados do Claude Code estendem as capacidades principais com planejamento, raciocínio, automação e mecanismos de controle. Esses recursos possibilitam fluxos de trabalho sofisticados para tarefas de desenvolvimento complexas, revisão de código, automação e gerenciamento de múltiplas sessões.

**Os principais recursos avançados incluem:**
- **Modo de Planejamento**: Criar planos de implementação detalhados antes de codificar
- **Raciocínio Estendido**: Raciocínio profundo para problemas complexos
- **Modo Auto**: Classificador de segurança em segundo plano que analisa cada ação antes da execução (Pré-visualização de Pesquisa)
- **Tarefas em Segundo Plano**: Executar operações longas sem bloquear a conversa
- **Modos de Permissão**: Controlar o que o Claude pode fazer (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Modo de Impressão**: Executar o Claude Code de forma não-interativa para automação e CI/CD (`claude -p`)
- **Gerenciamento de Sessão**: Gerenciar múltiplas sessões de trabalho
- **Recursos Interativos**: Atalhos de teclado, entrada multilinha e histórico de comandos
- **Ditado por Voz**: Entrada de voz push-to-talk com suporte a STT em 20 idiomas
- **Canais**: Servidores MCP enviam mensagens para sessões em execução (Pré-visualização de Pesquisa)
- **Controle Remoto**: Controlar o Claude Code do Claude.ai ou do app Claude
- **Sessões Web**: Executar o Claude Code no navegador em claude.ai/code
- **App de Desktop**: App standalone para revisão visual de diff e múltiplas sessões
- **Lista de Tarefas**: Rastreamento de tarefas persistente entre compactações de contexto
- **Sugestões de Prompt**: Sugestões inteligentes de comandos baseadas no contexto
- **Worktrees Git**: Branches de worktree isolados para trabalho paralelo
- **Sandbox**: Isolamento de filesystem e rede em nível de SO
- **Configurações Gerenciadas**: Implantação enterprise via plist, Registry ou arquivos gerenciados
- **Configuração**: Personalizar comportamento com arquivos de configuração JSON

---

## Modo de Planejamento

O modo de planejamento permite que o Claude pense em tarefas complexas antes de implementá-las, criando um plano detalhado que você pode revisar e aprovar.

### O que é o Modo de Planejamento?

O modo de planejamento é uma abordagem de duas fases:
1. **Fase de Planejamento**: Claude analisa a tarefa e cria um plano de implementação detalhado
2. **Fase de Implementação**: Após aprovação, Claude executa o plano

### Quando Usar o Modo de Planejamento

✅ Use o modo de planejamento para:
- Refatoração complexa de múltiplos arquivos
- Implementações de novos recursos
- Mudanças arquiteturais
- Migrações de banco de dados
- Redesigns de API maiores

❌ Não use o modo de planejamento para:
- Correções de bugs simples
- Mudanças de formatação
- Edições de arquivo único
- Consultas rápidas

### Ativando o Modo de Planejamento

**Comando de barra**:
```bash
/plan Implement user authentication system
```

**Flag CLI**:
```bash
claude --permission-mode plan
```

**Definir como padrão**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Atalho de teclado**:
- `Shift + Tab` - Alternar modos de permissão (incluindo plan)
- `Alt + M` - Alternar modos de permissão (Windows/Linux)

### Benefícios do Modo de Planejamento

- **Abordagem de implementação estruturada**: Detalhamento detalhado das etapas de implementação
- **Revisão e aprovação**: Aprovar ou ajustar o plano antes da execução
- **Identificação de riscos**: Identificar problemas potenciais antes da implementação
- **Fases claras**: Fases e marcos de implementação organizados

### Exemplo: Implementação de Recurso

```
Usuário: /plan Add a real-time notification system

Claude: Vou criar um plano para implementar notificações em tempo real.

## Plano de Implementação

### Fase 1: Configuração de Infraestrutura
1. Instalar bibliotecas WebSocket (socket.io)
2. Configurar servidor WebSocket
3. Configurar gerenciamento de conexão

### Fase 2: Implementação do Backend
4. Criar serviço de notificação
5. Implementar fila de notificações
6. Adicionar esquema de banco de dados para notificações
7. Criar endpoints de API

### Fase 3: Integração do Frontend
8. Configurar cliente WebSocket
9. Criar componentes de UI de notificação
10. Implementar gerenciamento de estado de notificações
11. Adicionar permissões de notificação

### Fase 4: Testes e Implantação
12. Escrever testes unitários
13. Escrever testes de integração
14. Atualizar documentação
15. Implantar no staging

Tempo estimado: 3-4 horas
Arquivos a modificar: 12
Novos arquivos a criar: 8

Pronto para prosseguir? (yes/no/modify plan)

Usuário: yes

Claude: [Inicia a implementação seguindo o plano]
```

### Modificações no Plano

```
Usuário: Modify the plan - skip the queue for now, we'll add it later

Claude: Plano atualizado:
[Mostra o plano modificado sem a fila]

Usuário: Looks good, proceed

Claude: [Implementa o plano modificado]
```

### Configuração do Modo de Planejamento

O modo de planejamento é ativado via flag CLI ou comando de barra:

```bash
# Ativar modo de plano via CLI
claude --permission-mode plan

# Ou usar o comando de barra /plan dentro do REPL
/plan Implement user authentication system
```

**Alias de modelo para planejamento**: Use `opusplan` como alias de modelo para usar Opus para planejamento e Sonnet para execução:

```bash
claude --model opusplan "design and implement the new API"
```

**Editar plano externamente**: Pressione `Ctrl+G` para abrir o plano atual em seu editor externo para modificações detalhadas.

---

## Ultraplan (Elaboração de Plano na Nuvem)

> **Novo na v2.1.101**: O Ultraplan agora cria automaticamente um Claude Code na web na primeira vez que você o invoca — sem configuração manual, sem esperar um container esquentar antes do início do rascunho.

> **Nota**: O Ultraplan é uma pré-visualização de pesquisa e requer Claude Code v2.1.91 ou mais recente.

`/ultraplan` passa uma tarefa de planejamento do seu CLI local para uma sessão do Claude Code na web em execução no modo de plano. O Claude elabora o plano na nuvem enquanto seu terminal fica livre para outro trabalho, depois você revisa o rascunho no navegador e escolhe onde executar — na mesma sessão na nuvem ou teleportado de volta ao seu terminal.

### Quando Usar o Ultraplan

- Você quer uma superfície de revisão mais rica do que o terminal: comentários inline, reações com emoji, uma barra lateral de esquema e histórico persistente.
- Você quer elaboração autônoma enquanto continua codificando localmente — a sessão na nuvem pesquisa o repositório e escreve o plano sem bloquear seu CLI.
- O plano precisa de revisão das partes interessadas antes da execução — uma URL web compartilhável é melhor do que colar rolagem do terminal.

### Requisitos

- Uma conta do Claude Code na web.
- Um repositório GitHub (a sessão na nuvem clona seu repositório para elaborar com base no código real).
- **Não disponível** no Amazon Bedrock, Google Cloud Vertex AI ou Microsoft Foundry.

### Três Formas de Lançar

- **Comando**: `/ultraplan <prompt>` — invocação explícita.
- **Palavra-chave**: inclua a palavra `ultraplan` em qualquer parte de um prompt normal e o Claude roteia a solicitação para a nuvem.
- **De um plano local**: após o Claude terminar um plano localmente, escolha "No, refine with Ultraplan on Claude Code on the web" no diálogo de aprovação para transferir o rascunho para pesquisa mais profunda.

### Exemplo de Uso

```bash
/ultraplan migrate the auth service from sessions to JWTs
```

O Claude reconhece, cria o ambiente na nuvem (criado automaticamente na primeira execução na v2.1.101+) e retorna um link de sessão que você pode abrir no navegador.

### Indicadores de Status

| Status | Significado |
|--------|-------------|
| `◇ ultraplan` | Claude está pesquisando seu codebase e elaborando o plano |
| `◇ ultraplan needs your input` | Claude tem uma pergunta de esclarecimento; abra o link da sessão para responder |
| `◆ ultraplan ready` | O plano está pronto para revisar no navegador |

### Opções de Execução

Uma vez que o plano esteja pronto, você tem dois caminhos de execução. Aprove o plano no navegador para executar na mesma sessão na nuvem — o Claude implementa as alterações remotamente e abre um pull request na UI web. Ou escolha "Approve plan and teleport back to terminal" para implementar localmente. O diálogo de teleporte para o terminal oferece três escolhas:

- **Implement here** — executar o plano aprovado na sua sessão de terminal atual.
- **Start new session** — abrir uma sessão nova no mesmo diretório de trabalho e implementar lá.
- **Cancel** — salva o plano em um arquivo para você retomá-lo mais tarde.

> **Aviso**: O Controle Remoto desconecta quando o ultraplan inicia. Ambos os recursos compartilham a interface claude.ai/code, então apenas um pode estar ativo por vez.

---

## Raciocínio Estendido

O raciocínio estendido permite que o Claude gaste mais tempo raciocínando sobre problemas complexos antes de fornecer uma solução.

### O que é o Raciocínio Estendido?

O raciocínio estendido é um processo de raciocínio deliberado, passo a passo, onde o Claude:
- Decompõe problemas complexos
- Considera múltiplas abordagens
- Avalia compromissos
- Raciocína sobre casos extremos

### Ativando o Raciocínio Estendido

**Atalho de teclado**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) - Alternar raciocínio estendido

**Ativação automática**:
- Ativado por padrão para todos os modelos (Opus 4.7, Sonnet 4.6, Haiku 4.5)
- Opus 4.7: Raciocínio adaptativo com níveis de esforço: `low` (○), `medium` (◐), `high` (●), `max` (apenas Opus 4.7)
- Outros modelos: Orçamento fixo de até 31.999 tokens

**Métodos de configuração**:
- Alternar: `Alt+T` / `Option+T`, ou via `/config`
- Ver raciocínio: `Ctrl+O` (modo verbose)
- Definir esforço: comando `/effort` ou flag `--effort`

**Orçamento personalizado**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Nível de esforço** (apenas Opus 4.7):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), ou max (apenas Opus 4.7)
```

**Flag CLI**:
```bash
claude --effort high "complex architectural review"
```

**Comando de barra**:
```
/effort high
```

> **Nota:** A palavra-chave "ultrathink" nos prompts ativa o modo de raciocínio profundo. Os níveis de esforço `low`, `medium`, `high` e `max` (apenas Opus 4.7) controlam quanto raciocínio o Claude realiza.

### Benefícios do Raciocínio Estendido

- **Raciocínio profundo**: Gastar mais tempo pensando sobre problemas complexos
- **Melhores decisões arquiteturais**: Fazer escolhas informadas com avaliação abrangente
- **Consideração de casos extremos**: Pensar sobre problemas e cenários potenciais
- **Análise minuciosa**: Abordagem estruturada para resolução de problemas complexos

### Exemplo: Decisão Arquitetural

```
Usuário: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Deixe-me pensar cuidadosamente sobre esta decisão arquitetural...

<extended_thinking>
## Análise de Contexto
- Tamanho da equipe: 5 desenvolvedores
- Tráfego esperado: 10k usuários diários inicialmente
- Necessidade de escalar para 100k+ usuários
- Recursos limitados de DevOps
- Prazo de 6 meses para MVP

## Abordagem 1: Microsserviços
Prós:
+ Escalabilidade independente
+ Flexibilidade tecnológica
+ Independência de equipe
+ Isolamento de falhas

Contras:
- Complexidade operacional
- Sobrecarga de rede
- Rastreamento distribuído necessário
- Requer expertise em DevOps
- Desenvolvimento inicial mais lento

## Abordagem 2: Monólito
Prós:
+ Implantação mais simples
+ Desenvolvimento inicial mais rápido
+ Depuração mais fácil
+ Menor sobrecarga operacional
+ Código base único

Contras:
- Desafios de escalabilidade mais tarde
- Implantações tudo-ou-nada
- Bloqueio tecnológico
- Potencial para acoplamento forte

## Fatores de Decisão
1. Tamanho da equipe (5 devs) → Favorece monólito
2. Recursos de DevOps (limitados) → Favorece monólito
3. Prazo (6 meses) → Favorece monólito
4. Escala futura (100k usuários) → Alcançável com monólito + cache
5. Orçamento de complexidade → Limitado

## Recomendação
Comece com um **monólito modular**:
- Unidade de implantação única
- Limites de módulo claros
- Interfaces limpas entre módulos
- Preparar para extração futura para microsserviços se necessário

Isso oferece:
✓ Desenvolvimento inicial rápido
✓ Baixa complexidade operacional
✓ Opção de extrair serviços mais tarde
✓ Arquitetura clara

Caminho de migração: Quando atingir 50k+ usuários ou módulos específicos precisarem de escalabilidade independente, extraia esses módulos para microsserviços.
</extended_thinking>

**Recomendação**: Implemente um monólito modular com limites de módulo claros.

Esta abordagem equilibra suas restrições atuais (tamanho da equipe, prazo, recursos de DevOps) com necessidades futuras de escalabilidade. Você pode migrar módulos específicos para microsserviços mais tarde quando houver uma necessidade de negócio clara.
```

### Configuração do Raciocínio Estendido

O raciocínio estendido é controlado via variáveis de ambiente, atalhos de teclado e flags CLI:

```bash
# Definir orçamento de tokens de raciocínio
export MAX_THINKING_TOKENS=16000

# Definir nível de esforço (apenas Opus 4.7): low (○), medium (◐), high (●), ou max (apenas Opus 4.7)
export CLAUDE_CODE_EFFORT_LEVEL=high
```

Alterne durante uma sessão com `Alt+T` / `Option+T`, defina o esforço com `/effort`, ou configure via `/config`.

---

## Modo Auto

O Modo Auto é um modo de permissão de Pré-visualização de Pesquisa (março de 2026) que usa um classificador de segurança em segundo plano para analisar cada ação antes da execução. Permite que o Claude trabalhe autonomamente enquanto bloqueia operações perigosas.

### Requisitos

- **Plano**: Team, Enterprise ou API (não disponível nos planos Pro ou Max)
- **Modelo**: Claude Sonnet 4.6 ou Opus 4.7
- **Provedor**: Apenas API da Anthropic (não suportado no Bedrock, Vertex ou Foundry)
- **Classificador**: Executa no Claude Sonnet 4.6 (adiciona custo extra de tokens)

### Ativando o Modo Auto

```bash
# Desbloquear o modo auto com flag CLI
claude --enable-auto-mode

# Depois cicle para ele com Shift+Tab no REPL
```

Ou defina como modo de permissão padrão:

```bash
claude --permission-mode auto
```

Configuração via config:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Como o Classificador Funciona

O classificador em segundo plano avalia cada ação usando a seguinte ordem de decisão:

1. **Regras de allow/deny** -- Regras de permissão explícitas são verificadas primeiro
2. **Somente leitura/edições aprovadas automaticamente** -- Leituras e edições de arquivo passam automaticamente
3. **Classificador** -- O classificador em segundo plano analisa a ação
4. **Fallback** -- Volta a solicitar após 3 bloqueios consecutivos ou 20 bloqueios totais

### Ações Bloqueadas por Padrão

O modo auto bloqueia as seguintes ações por padrão:

| Ação Bloqueada | Exemplo |
|----------------|---------|
| Instalações via pipe-para-shell | `curl \| bash` |
| Envio de dados sensíveis externamente | Chaves de API, credenciais pela rede |
| Deploys em produção | Comandos de deploy apontando para produção |
| Exclusão em massa | `rm -rf` em diretórios grandes |
| Mudanças IAM | Modificações de permissão e função |
| Force push para main | `git push --force origin main` |

### Ações Permitidas por Padrão

| Ação Permitida | Exemplo |
|----------------|---------|
| Operações em arquivos locais | Ler, escrever, editar arquivos do projeto |
| Instalação de dependências declaradas | `npm install`, `pip install` do manifesto |
| HTTP somente leitura | `curl` para buscar documentação |
| Push para branch atual | `git push origin feature-branch` |

### Configurando o Modo Auto

**Imprimir regras padrão como JSON**:
```bash
claude auto-mode defaults
```

**Configurar infraestrutura confiável** via a configuração gerenciada `autoMode.environment` para implantações enterprise. Isso permite que administradores definam ambientes CI/CD confiáveis, alvos de implantação e padrões de infraestrutura.

### Comportamento de Fallback

Quando o classificador está incerto, o modo auto volta a solicitar ao usuário:
- Após **3 bloqueios consecutivos** do classificador
- Após **20 bloqueios totais** do classificador em uma sessão

Isso garante que o usuário sempre mantenha o controle quando o classificador não pode aprovar uma ação com confiança.

### Configurando Permissões Equivalentes ao Modo Auto (Sem Plano Team)

Se você não tem um plano Team ou quer uma abordagem mais simples sem o classificador em segundo plano, você pode preencher seu `~/.claude/settings.json` com uma linha de base conservadora de regras de permissão seguras. O script começa com regras somente leitura e de inspeção local, depois permite que você opte por edições, testes, escritas git locais, instalações de pacotes e ações GitHub apenas quando quiser.

**Arquivo:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Pré-visualizar o que seria adicionado (sem alterações escritas)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Aplicar a linha de base conservadora
python3 09-advanced-features/setup-auto-mode-permissions.py

# Adicionar mais capacidade apenas quando precisar
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

O script adiciona regras nestas categorias:

| Categoria | Exemplos |
|-----------|---------|
| Ferramentas nativas somente leitura | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| Inspeção local | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| Edições opcionais | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| Teste/build opcional | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| Git escrita opcional | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git (escrita local) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Gerenciadores de pacotes | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Build e teste | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Shell comum | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

Operações perigosas (`rm -rf`, `sudo`, force push, `DROP TABLE`, `terraform destroy`, etc.) são intencionalmente excluídas. O script é idempotente — executá-lo duas vezes não duplicará regras.

---

## Tarefas em Segundo Plano

Tarefas em segundo plano permitem que operações de longa duração sejam executadas sem bloquear sua conversa.

### O que São Tarefas em Segundo Plano?

Tarefas em segundo plano executam assincronamente enquanto você continua trabalhando:
- Suítes de testes longas
- Processos de build
- Migrações de banco de dados
- Scripts de implantação
- Ferramentas de análise

**Uso Básico:**
```bash
Usuário: Run tests in background

Claude: Tarefa iniciada bg-1234

/task list           # Mostrar todas as tarefas
/task status bg-1234 # Verificar progresso
/task show bg-1234   # Ver saída
/task cancel bg-1234 # Cancelar tarefa
```

### Iniciando Tarefas em Segundo Plano

```
Usuário: Run the full test suite in the background

Claude: Iniciando testes em segundo plano (task-id: bg-1234)
Você pode continuar trabalhando enquanto os testes executam.

[Você pode continuar a conversa]

Usuário: Meanwhile, let's refactor the auth module

Claude: [Trabalha no módulo auth enquanto os testes executam]

[Mais tarde, quando os testes completam]

Claude: 📢 Tarefa em segundo plano bg-1234 completada:
✅ 245 testes passaram
❌ 3 testes falharam
Ver resultados: /task show bg-1234
```

### Gerenciando Tarefas em Segundo Plano

**Listar tarefas ativas**:
```
Usuário: /task list

Tarefas em segundo plano ativas:
1. [bg-1234] Executando testes (50% completo, 2min restante)
2. [bg-1235] Construindo imagem Docker (25% completo, 8min restante)
3. [bg-1236] Implantando no staging (90% completo, 30seg restante)
```

**Verificar status da tarefa**:
```
Usuário: /task status bg-1234

Tarefa bg-1234: Executando testes
Status: Em progresso
Progresso: 120/245 testes (49%)
Iniciado: 2025-11-08 10:30:15
Conclusão estimada: 2025-11-08 10:34:22
```

**Ver saída da tarefa**:
```
Usuário: /task show bg-1234

[Mostra saída ao vivo da execução de testes]
```

**Cancelar tarefa**:
```
Usuário: /task cancel bg-1234

Tarefa em segundo plano bg-1234 cancelada
```

### Exemplo: Desenvolvimento Paralelo

```
Usuário: Run the build in the background

Claude: Iniciando build... (task-id: bg-5001)

Usuário: Also run the linter in background

Claude: Iniciando linter... (task-id: bg-5002)

Usuário: While those run, let's implement the new API endpoint

Claude: [Implementa endpoint de API enquanto build e linter executam]

[10 minutos depois]

Claude: 📢 Build concluído com sucesso (bg-5001)
📢 Linter encontrou 12 problemas (bg-5002)

Usuário: Show me the linter issues

Claude: [Mostra saída do linter de bg-5002]
```

### Configuração

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Ferramenta Monitor (Streams Orientados a Eventos)

> **Novo na v2.1.98**: A ferramenta Monitor permite que o Claude observe a saída de um comando em segundo plano e reaja no momento em que um evento correspondente aparece — substituindo loops de polling e `sleep` para aguardar processos de longa duração.

O Monitor se anexa a qualquer comando shell que escreva no stdout. Cada linha de stdout do comando se torna uma notificação que acorda a sessão. O Claude especifica o comando; o harness transmite a saída e entrega eventos conforme disparam. Veja a seção relacionada [Tarefas em Segundo Plano](#tarefas-em-segundo-plano) para lançar os processos subjacentes.

### Por que é Importante

O polling com `/loop` ou `sleep` consome uma rodada completa de API a cada ciclo, independentemente de algo ter mudado. O Monitor fica em silêncio até que um evento dispare, consumindo **zero tokens** enquanto o comando está quieto. Quando um evento ocorre, o Claude reage imediatamente — sem descoberta atrasada aguardando o próximo tick de polling. Para qualquer coisa que execute por mais de alguns minutos, isso é mais barato e mais rápido do que loops de polling.

### Dois Padrões Comuns

**Filtros de stream** observam saída contínua de uma fonte de longa duração. O comando executa para sempre; cada linha correspondente é um evento.

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**Filtros de poll-and-emit** verificam uma fonte periodicamente e só emitem quando algo muda. Use isso para APIs, bancos de dados ou qualquer coisa sem um stream nativo.

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

### Exemplo Concreto

"Inicie meu servidor de desenvolvimento e monitore-o para erros." O Claude lança o servidor como uma tarefa em segundo plano, anexa um filtro Monitor (`tail -F server.log | grep --line-buffered -E "ERROR|FATAL"`), e a sessão fica silenciosa. No momento em que uma linha de erro aparece no log, o Claude acorda, lê o erro e pode reagir — reiniciar o servidor, corrigir o bug ou surfá-lo para você — sem que você precise fazer check-in.

> **Aviso**: Ao fazer pipe para `grep`, **sempre** use `grep --line-buffered`. Sem isso, o grep armazena stdout em chunks de 4KB, o que pode atrasar eventos por minutos em streams de baixo tráfego. Esta é a principal forma como o Monitor quebra na prática — se seu filtro parece silencioso quando não deveria, verifique o flag `--line-buffered` primeiro.

---

## Tarefas Agendadas

Tarefas Agendadas permitem que você execute prompts automaticamente em um agendamento recorrente ou como lembretes únicos. As tarefas têm escopo de sessão — elas executam enquanto o Claude Code está ativo e são limpas quando a sessão termina. Disponível desde v2.1.72+.

### O comando `/loop`

```bash
# Intervalo explícito
/loop 5m check if the deployment finished

# Linguagem natural
/loop check build status every 30 minutes
```

Expressões cron padrão de 5 campos também são suportadas para agendamento preciso.

### Lembretes únicos

Defina lembretes que disparam uma vez em um horário específico:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Gerenciando tarefas agendadas

| Ferramenta | Descrição |
|------------|-----------|
| `CronCreate` | Criar uma nova tarefa agendada |
| `CronList` | Listar todas as tarefas agendadas ativas |
| `CronDelete` | Remover uma tarefa agendada |

**Limites e comportamento**:
- Até **50 tarefas agendadas** por sessão
- Com escopo de sessão — limpas quando a sessão termina
- Tarefas recorrentes expiram automaticamente após **3 dias**
- Tarefas só disparam enquanto o Claude Code está em execução — sem recuperação para disparos perdidos

### Detalhes de comportamento

| Aspecto | Detalhe |
|---------|---------|
| **Jitter recorrente** | Até 10% do intervalo (máx 15 minutos) |
| **Jitter único** | Até 90 segundos nas fronteiras :00/:30 |
| **Disparos perdidos** | Sem recuperação — pulados se o Claude Code não estava em execução |
| **Persistência** | Não persistido entre reinicializações |

### Tarefas Agendadas na Nuvem

Use `/schedule` para criar tarefas agendadas na nuvem que executam na infraestrutura da Anthropic:

```
/schedule daily at 9am run the test suite and report failures
```

Tarefas agendadas na nuvem persistem entre reinicializações e não requerem que o Claude Code esteja em execução localmente.

### Desativando tarefas agendadas

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### Exemplo: monitorando uma implantação

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Dica**: Tarefas agendadas têm escopo de sessão. Para automação persistente que sobrevive a reinicializações, use pipelines CI/CD, GitHub Actions ou tarefas agendadas do App de Desktop.

---

## Modos de Permissão

Modos de permissão controlam quais ações o Claude pode tomar sem aprovação explícita.

### Modos de Permissão Disponíveis

| Modo | Comportamento |
|------|---------------|
| `default` | Somente leitura de arquivos; solicita para todas as outras ações |
| `acceptEdits` | Leitura e edição de arquivos; solicita para comandos |
| `plan` | Somente leitura de arquivos (modo de pesquisa, sem edições) |
| `auto` | Todas as ações com verificações do classificador de segurança em segundo plano (Pré-visualização de Pesquisa) |
| `bypassPermissions` | Todas as ações, sem verificações de permissão (perigoso) |
| `dontAsk` | Apenas ferramentas pré-aprovadas executam; todas as outras negadas |

Cicle pelos modos com `Shift+Tab` no CLI. Defina um padrão com o flag `--permission-mode` ou a configuração `permissions.defaultMode`.

### Métodos de Ativação

**Atalho de teclado**:
```bash
Shift + Tab  # Ciclar por todos os 6 modos
```

**Comando de barra**:
```bash
/plan                  # Entrar no modo de plano
```

**Flag CLI**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Configuração**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Exemplos de Modo de Permissão

#### Modo Padrão
O Claude solicita confirmação em ações significativas:

```
Usuário: Fix the bug in auth.ts

Claude: Preciso modificar src/auth.ts para corrigir o bug.
A alteração atualizará a lógica de validação de senha.

Aprovar esta alteração? (yes/no/show)
```

#### Modo de Plano
Revisar plano de implementação antes da execução:

```
Usuário: /plan Implement user authentication system

Claude: Vou criar um plano para implementar autenticação.

## Plano de Implementação
[Plano detalhado com fases e etapas]

Pronto para prosseguir? (yes/no/modify)
```

#### Modo de Aceitar Edições
Aceitar automaticamente modificações de arquivo:

```
Usuário: acceptEdits
Usuário: Fix the bug in auth.ts

Claude: [Faz alterações sem perguntar]
```

### Casos de Uso

**Revisão de Código**:
```
Usuário: claude --permission-mode plan
Usuário: Review this PR and suggest improvements

Claude: [Lê o código, fornece feedback, mas não pode modificar]
```

**Programação em Par**:
```
Usuário: claude --permission-mode default
Usuário: Let's implement the feature together

Claude: [Solicita aprovação antes de cada alteração]
```

**Tarefas Automatizadas**:
```
Usuário: claude --permission-mode acceptEdits
Usuário: Fix all linting issues in the codebase

Claude: [Aceita automaticamente edições de arquivo sem perguntar]
```

---

## Modo Headless

O modo de impressão (`claude -p`) permite que o Claude Code execute sem entrada interativa, perfeito para automação e CI/CD. Este é o modo não-interativo, substituindo o flag `--headless` mais antigo.

### O que é o Modo de Impressão?

O modo de impressão permite:
- Execução automatizada de scripts
- Integração CI/CD
- Processamento em lote
- Tarefas agendadas

### Executando no Modo de Impressão (Não-Interativo)

```bash
# Executar tarefa específica
claude -p "Run all tests"

# Processar conteúdo via pipe
cat error.log | claude -p "Analyze these errors"

# Integração CI/CD (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Exemplos Adicionais de Uso do Modo de Impressão

```bash
# Executar uma tarefa específica com captura de saída
claude -p "Run all tests and generate coverage report"

# Com saída estruturada
claude -p --output-format json "Analyze code quality"

# Com entrada do stdin
echo "Analyze code quality" | claude -p "explain this"
```

### Exemplo: Integração CI/CD

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Configuração do Modo de Impressão

O modo de impressão (`claude -p`) suporta vários flags para automação:

```bash
# Limitar turnos autônomos
claude -p --max-turns 5 "refactor this module"

# Saída JSON estruturada
claude -p --output-format json "analyze this codebase"

# Com validação de schema
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Desativar persistência de sessão
claude -p --no-session-persistence "one-off analysis"
```

---

## Gerenciamento de Sessão

Gerenciar múltiplas sessões do Claude Code efetivamente.

### Comandos de Gerenciamento de Sessão

| Comando | Descrição |
|---------|-----------|
| `/resume` | Retomar uma conversa por ID ou nome |
| `/rename` | Nomear a sessão atual |
| `/fork` | Fazer fork da sessão atual em um novo branch |
| `claude -c` | Continuar conversa mais recente |
| `claude -r "session"` | Retomar sessão por nome ou ID |

### Retomando Sessões

**Continuar última conversa**:
```bash
claude -c
```

**Retomar uma sessão nomeada**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Renomear a sessão atual** (dentro do REPL):
```
/rename auth-refactor
```

### Fazendo Fork de Sessões

Faça fork de uma sessão para tentar uma abordagem alternativa sem perder o original:

```
/fork
```

Ou via CLI:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Persistência de Sessão

Sessões são salvas automaticamente e podem ser retomadas:

```bash
# Continuar última conversa
claude -c

# Retomar sessão específica por nome ou ID
claude -r "auth-refactor"

# Retomar e fazer fork para experimentação
claude --resume auth-refactor --fork-session "alternative approach"
```

---

## Recursos Interativos

### Atalhos de Teclado

O Claude Code suporta atalhos de teclado para eficiência. Aqui está a referência completa da documentação oficial:

| Atalho | Descrição |
|--------|-----------|
| `Ctrl+C` | Cancelar entrada/geração atual |
| `Ctrl+D` | Sair do Claude Code |
| `Ctrl+G` | Editar plano no editor externo |
| `Ctrl+L` | Limpar tela do terminal |
| `Ctrl+O` | Alternar saída verbose (ver raciocínio) |
| `Ctrl+R` | Pesquisa reversa no histórico |
| `Ctrl+T` | Alternar visualização da lista de tarefas |
| `Ctrl+B` | Tarefas em execução em segundo plano |
| `Esc+Esc` | Reverter código/conversa |
| `Shift+Tab` / `Alt+M` | Alternar modos de permissão |
| `Option+P` / `Alt+P` | Trocar modelo |
| `Option+T` / `Alt+T` | Alternar raciocínio estendido |

**Edição de Linha (atalhos readline padrão):**

| Atalho | Ação |
|--------|------|
| `Ctrl + A` | Mover para o início da linha |
| `Ctrl + E` | Mover para o final da linha |
| `Ctrl + K` | Cortar até o final da linha |
| `Ctrl + U` | Cortar até o início da linha |
| `Ctrl + W` | Excluir palavra para trás |
| `Ctrl + Y` | Colar (yank) |
| `Tab` | Autocompletar |
| `↑ / ↓` | Histórico de comandos |

### Personalizando atalhos de teclado

Crie atalhos de teclado personalizados executando `/keybindings`, que abre `~/.claude/keybindings.json` para edição (v2.1.18+).

**Formato de configuração**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

Defina um binding como `null` para desvincular um atalho padrão.

### Contextos disponíveis

Os atalhos de teclado têm escopo para contextos específicos de UI:

| Contexto | Ações de Tecla |
|----------|----------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | Navegação de configurações específica do contexto |
| **Tabs** | Troca e gerenciamento de abas |
| **Help** | Navegação do painel de ajuda |

Há 18 contextos no total, incluindo `Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker` e `Select`.

### Suporte a acordes

Atalhos de teclado suportam sequências de acordes (combinações de múltiplas teclas):

```
"ctrl+k ctrl+s"   → Sequência de duas teclas: pressione ctrl+k, depois ctrl+s
"ctrl+shift+p"    → Teclas modificadoras simultâneas
```

**Sintaxe de teclas**:
- **Modificadores**: `ctrl`, `alt` (ou `opt`), `shift`, `meta` (ou `cmd`)
- **Maiúsculas implica Shift**: `K` é equivalente a `shift+k`
- **Teclas especiais**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, teclas de seta

### Teclas reservadas e conflitantes

| Tecla | Status | Notas |
|-------|--------|-------|
| `Ctrl+C` | Reservada | Não pode ser realocada (interrupção) |
| `Ctrl+D` | Reservada | Não pode ser realocada (saída) |
| `Ctrl+B` | Conflito de terminal | Tecla de prefixo tmux |
| `Ctrl+A` | Conflito de terminal | Tecla de prefixo GNU Screen |
| `Ctrl+Z` | Conflito de terminal | Suspensão de processo |

> **Dica**: Se um atalho não funcionar, verifique conflitos com seu emulador de terminal ou multiplexador.

### Autocompletar com Tab

O Claude Code fornece autocompletar inteligente com Tab:

```
Usuário: /rew<TAB>
→ /rewind

Usuário: /plu<TAB>
→ /plugin

Usuário: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### Histórico de Comandos

Acessar comandos anteriores:

```
Usuário: <↑>  # Comando anterior
Usuário: <↓>  # Próximo comando
Usuário: Ctrl+R  # Pesquisar histórico

(reverse-i-search)`test': run all tests
```

### Entrada Multilinha

Para consultas complexas, use o modo multilinha:

```bash
Usuário: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Exemplo:**

```
Usuário: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processa a solicitação multilinha]
```

### Edição Inline

Editar comandos antes de enviar:

```
Usuário: Deploy to prodcution<Backspace><Backspace>uction

[Edite no local antes de enviar]
```

### Modo Vim

Ativar keybindings Vi/Vim para edição de texto:

**Ativação**:
- Use o comando `/vim` ou `/config` para ativar
- Troca de modo com `Esc` para NORMAL, `i/a/o` para INSERT

**Teclas de navegação**:
- `h` / `l` - Mover esquerda/direita
- `j` / `k` - Mover para baixo/cima
- `w` / `b` / `e` - Mover por palavra
- `0` / `$` - Mover para início/fim da linha
- `gg` / `G` - Pular para início/fim do texto

**Objetos de texto**:
- `iw` / `aw` - Palavra interna/ao redor
- `i"` / `a"` - String entre aspas interna/ao redor
- `i(` / `a(` - Parênteses internos/ao redor

### Modo Bash

Executar comandos shell diretamente com o prefixo `!`:

```bash
! npm test
! git status
! cat src/index.js
```

Use isso para execução rápida de comandos sem trocar de contexto.

---

## Ditado por Voz

O Ditado por Voz fornece entrada de voz push-to-talk para o Claude Code, permitindo que você fale seus prompts em vez de digitá-los.

### Ativando o Ditado por Voz

```
/voice
```

### Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| **Push-to-talk** | Segure uma tecla para gravar, solte para enviar |
| **20 idiomas** | Suporte a reconhecimento de fala em 20 idiomas |
| **Atalho personalizado** | Configure a tecla push-to-talk via `/keybindings` |
| **Requisito de conta** | Requer uma conta Claude.ai para processamento STT |

### Configuração

Personalize o atalho push-to-talk em seu arquivo de atalhos (`/keybindings`). O ditado por voz usa sua conta Claude.ai para processamento de fala para texto.

---

## Canais

Canais é um recurso de Pré-visualização de Pesquisa que envia eventos de serviços externos para uma sessão do Claude Code em execução via servidores MCP. As fontes incluem Telegram, Discord, iMessage e webhooks arbitrários, permitindo que o Claude reaja a notificações em tempo real sem polling.

### Inscrevendo-se em Canais

```bash
# Inscrever-se em plugins de canal na inicialização
claude --channels discord,telegram

# Inscrever-se em múltiplas fontes
claude --channels discord,telegram,imessage,webhooks
```

### Integrações Suportadas

| Integração | Descrição |
|------------|-----------|
| **Discord** | Receber e responder a mensagens do Discord em sua sessão |
| **Telegram** | Receber e responder a mensagens do Telegram em sua sessão |
| **iMessage** | Receber notificações do iMessage em sua sessão |
| **Webhooks** | Receber eventos de fontes de webhook arbitrárias |

### Configuração

Configure canais com o flag `--channels` na inicialização. Para implantações enterprise, use a configuração gerenciada para controlar quais plugins de canal são permitidos:

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

A configuração gerenciada `allowedChannelPlugins` controla quais plugins de canal são permitidos em toda a organização.

### Como Funciona

1. Servidores MCP atuam como plugins de canal que se conectam a serviços externos
2. Mensagens e eventos recebidos são enviados para a sessão ativa do Claude Code
3. O Claude pode ler e responder a mensagens dentro do contexto da sessão
4. Plugins de canal devem ser aprovados via a configuração gerenciada `allowedChannelPlugins`
5. Sem polling necessário — os eventos são enviados em tempo real

---

## Integração Chrome

A Integração Chrome conecta o Claude Code ao seu navegador Chrome ou Microsoft Edge para automação e depuração web ao vivo. Este é um recurso beta disponível desde v2.0.73+ (suporte Edge adicionado na v1.0.36+).

### Ativando a Integração Chrome

**Na inicialização**:

```bash
claude --chrome      # Ativar conexão Chrome
claude --no-chrome   # Desativar conexão Chrome
```

**Dentro de uma sessão**:

```
/chrome
```

Selecione "Enabled by default" para ativar a Integração Chrome para todas as sessões futuras. O Claude Code compartilha o estado de login do seu navegador, então pode interagir com aplicações web autenticadas.

### Capacidades

| Capacidade | Descrição |
|------------|-----------|
| **Depuração ao vivo** | Ler logs do console, inspecionar elementos DOM, depurar JavaScript em tempo real |
| **Verificação de design** | Comparar páginas renderizadas com maquetes de design |
| **Validação de formulários** | Testar submissões de formulários, validação de entrada e tratamento de erros |
| **Teste de aplicações web** | Interagir com aplicações autenticadas (Gmail, Google Docs, Notion, etc.) |
| **Extração de dados** | Raspar e processar conteúdo de páginas web |
| **Gravação de sessão** | Gravar interações do navegador como arquivos GIF |

### Permissões por site

A extensão Chrome gerencia acesso por site. Conceda ou revogue acesso para sites específicos a qualquer momento através do popup da extensão. O Claude Code só interage com sites que você explicitamente permitiu.

### Como funciona

O Claude Code controla o navegador em uma janela visível — você pode ver as ações acontecendo em tempo real. Quando o navegador encontra uma página de login ou CAPTCHA, o Claude pausa e aguarda você tratá-lo manualmente antes de continuar.

### Limitações conhecidas

- **Suporte a navegador**: Apenas Chrome e Edge — Brave, Arc e outros navegadores Chromium não são suportados
- **WSL**: Não disponível no Windows Subsystem for Linux
- **Provedores de terceiros**: Não suportado com provedores de API Bedrock, Vertex ou Foundry
- **Idle do service worker**: O service worker da extensão Chrome pode ficar ocioso durante sessões longas

> **Dica**: A Integração Chrome é um recurso beta. O suporte a navegadores pode se expandir em versões futuras.

---

## Controle Remoto

O Controle Remoto permite que você continue uma sessão do Claude Code em execução localmente a partir do seu telefone, tablet ou qualquer navegador. Sua sessão local continua rodando em sua máquina — nada é movido para a nuvem. Disponível nos planos Pro, Max, Team e Enterprise (v2.1.51+).

### Iniciando o Controle Remoto

**Via CLI**:

```bash
# Iniciar com nome de sessão padrão
claude remote-control

# Iniciar com um nome personalizado
claude remote-control --name "Auth Refactor"
```

**Dentro de uma sessão**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Flags disponíveis**:

| Flag | Descrição |
|------|-----------|
| `--name "title"` | Título personalizado da sessão para fácil identificação |
| `--verbose` | Mostrar logs detalhados de conexão |
| `--sandbox` | Ativar isolamento de filesystem e rede |
| `--no-sandbox` | Desativar sandbox (padrão) |

### Conectando a uma sessão

Três formas de se conectar de outro dispositivo:

1. **URL da sessão** — Impresso no terminal quando a sessão inicia; abra em qualquer navegador
2. **Código QR** — Pressione `spacebar` após iniciar para exibir um código QR escaneável
3. **Encontrar por nome** — Navegue por suas sessões em claude.ai/code ou no app Claude para mobile (iOS/Android)

### Segurança

- **Nenhuma porta de entrada** aberta em sua máquina
- **Apenas HTTPS de saída** via TLS
- **Credenciais com escopo** — múltiplos tokens de curta duração e escopo limitado
- **Isolamento de sessão** — cada sessão remota é independente

### Controle Remoto vs Claude Code na Web

| Aspecto | Controle Remoto | Claude Code na Web |
|---------|----------------|-------------------|
| **Execução** | Executa em sua máquina | Executa na nuvem da Anthropic |
| **Ferramentas locais** | Acesso total a servidores MCP locais, arquivos e CLI | Sem dependências locais |
| **Caso de uso** | Continuar trabalho local de outro dispositivo | Começar do zero de qualquer navegador |

### Limitações

- Uma sessão remota por instância do Claude Code
- O terminal deve permanecer aberto na máquina host
- A sessão expira após ~10 minutos se a rede estiver inacessível

### Casos de uso

- Controlar o Claude Code de um dispositivo móvel ou tablet enquanto está longe da mesa
- Usar a UI mais rica do claude.ai enquanto mantém a execução de ferramentas local
- Revisões rápidas de código em movimento com seu ambiente de desenvolvimento local completo

---

## Sessões Web

Sessões Web permitem que você execute o Claude Code diretamente no navegador em claude.ai/code, ou crie sessões web via CLI.

### Criando uma Sessão Web

```bash
# Criar uma nova sessão web via CLI
claude --remote "implement the new API endpoints"
```

Isso inicia uma sessão do Claude Code no claude.ai que você pode acessar de qualquer navegador.

### Retomando Sessões Web Localmente

Se você iniciou uma sessão na web e quer continuar localmente:

```bash
# Retomar uma sessão web no terminal local
claude --teleport
```

Ou dentro de um REPL interativo:
```
/teleport
```

### Casos de Uso

- Iniciar trabalho em uma máquina e continuar em outra
- Compartilhar uma URL de sessão com membros da equipe
- Usar a UI web para revisão visual de diff, depois trocar para terminal para execução

---

## App de Desktop

O App de Desktop do Claude Code fornece uma aplicação standalone com revisão visual de diff, sessões paralelas e conectores integrados. Disponível para macOS e Windows (planos Pro, Max, Team e Enterprise).

### Instalação

Baixe de [claude.ai](https://claude.ai) para sua plataforma:
- **macOS**: Build universal (Apple Silicon e Intel)
- **Windows**: Instaladores x64 e ARM64 disponíveis

Veja o [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) para instruções de configuração.

### Transferindo do CLI

Transfira sua sessão CLI atual para o App de Desktop:

```
/desktop
```

### Funcionalidades principais

| Funcionalidade | Descrição |
|----------------|-----------|
| **Visualização de diff** | Revisão visual de arquivo por arquivo com comentários inline; o Claude lê comentários e revisa |
| **Pré-visualização do app** | Inicia automaticamente servidores de desenvolvimento com um navegador embutido para verificação ao vivo |
| **Monitoramento de PR** | Integração com GitHub CLI com auto-correção de falhas de CI e auto-merge quando verificações passam |
| **Sessões paralelas** | Múltiplas sessões na barra lateral com isolamento automático de worktree Git |
| **Tarefas agendadas** | Tarefas recorrentes (por hora, diárias, dias úteis, semanais) que executam enquanto o app está aberto |
| **Renderização rica** | Código, markdown e renderização de diagrama com destaque de sintaxe |

### Configuração de pré-visualização do app

Configure o comportamento do servidor de desenvolvimento em `.claude/launch.json`:

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### Conectores

Conecte serviços externos para contexto mais rico:

| Conector | Capacidade |
|----------|------------|
| **GitHub** | Monitoramento de PR, rastreamento de issues, revisão de código |
| **Slack** | Notificações, contexto de canal |
| **Linear** | Rastreamento de issues, gerenciamento de sprint |
| **Notion** | Documentação, acesso à base de conhecimento |
| **Asana** | Gerenciamento de tarefas, rastreamento de projetos |
| **Calendar** | Consciência de agenda, contexto de reunião |

> **Nota**: Conectores não estão disponíveis para sessões remotas (nuvem).

### Sessões remotas e SSH

- **Sessões remotas**: Executam na infraestrutura da nuvem da Anthropic; continuam mesmo quando o app é fechado. Acessíveis de claude.ai/code ou do app Claude mobile
- **Sessões SSH**: Conecte-se a máquinas remotas via SSH com acesso total ao filesystem e ferramentas remotas. O Claude Code deve estar instalado na máquina remota

### Modos de permissão no Desktop

O App de Desktop suporta os mesmos 4 modos de permissão que o CLI:

| Modo | Comportamento |
|------|---------------|
| **Ask permissions** (padrão) | Revisar e aprovar cada edição e comando |
| **Auto accept edits** | Edições de arquivo aprovadas automaticamente; comandos requerem aprovação manual |
| **Plan mode** | Revisar abordagem antes de qualquer alteração ser feita |
| **Bypass permissions** | Execução automática (apenas sandbox, controlado pelo administrador) |

### Funcionalidades Enterprise

- **Console de administração**: Controlar acesso à aba Code e configurações de permissão para a organização
- **Implantação MDM**: Implantar via MDM no macOS ou MSIX no Windows
- **Integração SSO**: Exigir login único para membros da organização
- **Configurações gerenciadas**: Gerenciar centralmente a configuração da equipe e disponibilidade de modelos

---

## Lista de Tarefas

O recurso de Lista de Tarefas fornece rastreamento de tarefas persistente que sobrevive a compactações de contexto (quando o histórico de conversa é aparado para caber na janela de contexto).

### Alternando a Lista de Tarefas

Pressione `Ctrl+T` para alternar a visualização da lista de tarefas durante uma sessão.

### Tarefas Persistentes

Tarefas persistem entre compactações de contexto, garantindo que itens de trabalho de longa duração não sejam perdidos quando o contexto da conversa é aparado. Particularmente útil para implementações complexas de múltiplas etapas.

### Diretórios de Tarefas Nomeados

Use a variável de ambiente `CLAUDE_CODE_TASK_LIST_ID` para criar diretórios de tarefas nomeados compartilhados entre sessões:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

Isso permite que múltiplas sessões compartilhem a mesma lista de tarefas, útil para fluxos de trabalho em equipe ou projetos de múltiplas sessões.

---

## Sugestões de Prompt

Sugestões de Prompt exibem comandos de exemplo em cinza com base em seu histórico git e contexto de conversa atual.

### Como Funciona

- Sugestões aparecem como texto em cinza abaixo do seu prompt de entrada
- Pressione `Tab` para aceitar a sugestão
- Pressione `Enter` para aceitar e enviar imediatamente
- Sugestões são conscientes do contexto, extraindo do histórico git e estado da conversa

### Desativando Sugestões de Prompt

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Worktrees Git

Worktrees Git permitem que você inicie o Claude Code em um worktree isolado, possibilitando trabalho paralelo em diferentes branches sem fazer stash ou trocar.

### Iniciando em um Worktree

```bash
# Iniciar o Claude Code em um worktree isolado
claude --worktree
# ou
claude -w
```

### Localização do Worktree

Worktrees são criados em:
```
<repo>/.claude/worktrees/<name>
```

### Sparse Checkout para Monorepos

Use a configuração `worktree.sparsePaths` para realizar sparse-checkout em monorepos, reduzindo o uso de disco e o tempo de clone:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Ferramentas e Hooks de Worktree

| Item | Descrição |
|------|-----------|
| `ExitWorktree` | Ferramenta para sair e limpar o worktree atual |
| `WorktreeCreate` | Evento de hook disparado quando um worktree é criado |
| `WorktreeRemove` | Evento de hook disparado quando um worktree é removido |

### Limpeza Automática

Se nenhuma alteração for feita no worktree, ele é automaticamente limpo quando a sessão termina.

### Casos de Uso

- Trabalhar em um branch de feature enquanto mantém o branch main intocado
- Executar testes em isolamento sem afetar o diretório de trabalho
- Tentar alterações experimentais em um ambiente descartável
- Sparse-checkout de pacotes específicos em monorepos para inicialização mais rápida

---

## Sandbox

O Sandbox fornece isolamento de filesystem e rede em nível de SO para comandos Bash executados pelo Claude Code. É complementar às regras de permissão e fornece uma camada adicional de segurança.

### Ativando o Sandbox

**Comando de barra**:
```
/sandbox
```

**Flags CLI**:
```bash
claude --sandbox       # Ativar sandbox
claude --no-sandbox    # Desativar sandbox
```

### Configurações

| Configuração | Descrição |
|-------------|-----------|
| `sandbox.enabled` | Ativar ou desativar sandbox |
| `sandbox.failIfUnavailable` | Falhar se sandbox não puder ser ativado |
| `sandbox.filesystem.allowWrite` | Caminhos permitidos para acesso de escrita |
| `sandbox.filesystem.allowRead` | Caminhos permitidos para acesso de leitura |
| `sandbox.filesystem.denyRead` | Caminhos negados para acesso de leitura |
| `sandbox.enableWeakerNetworkIsolation` | Ativar isolamento de rede mais fraco no macOS |

### Exemplo de Configuração

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### Como Funciona

- Comandos Bash executam em um ambiente sandboxed com acesso restrito ao filesystem
- O acesso à rede pode ser isolado para prevenir conexões externas não intencionais
- Funciona junto com regras de permissão para defesa em profundidade
- No macOS, use `sandbox.enableWeakerNetworkIsolation` para restrições de rede (isolamento total de rede não está disponível no macOS)

### Casos de Uso

- Executar código não confiável ou gerado com segurança
- Prevenir modificações acidentais em arquivos fora do projeto
- Restringir acesso à rede durante tarefas automatizadas

---

## Configurações Gerenciadas (Enterprise)

As Configurações Gerenciadas permitem que administradores enterprise implantem a configuração do Claude Code em toda a organização usando ferramentas de gerenciamento nativas da plataforma.

### Métodos de Implantação

| Plataforma | Método | Desde |
|-----------|--------|-------|
| macOS | Arquivos plist gerenciados (MDM) | v2.1.51+ |
| Windows | Registro do Windows | v2.1.51+ |
| Multiplataforma | Arquivos de configuração gerenciados | v2.1.51+ |
| Multiplataforma | Drop-ins gerenciados (diretório `managed-settings.d/`) | v2.1.83+ |

### Drop-ins Gerenciados

Desde v2.1.83, administradores podem implantar múltiplos arquivos de configurações gerenciadas em um diretório `managed-settings.d/`. Arquivos são mesclados em ordem alfabética, permitindo configuração modular entre equipes:

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Configurações Gerenciadas Disponíveis

| Configuração | Descrição |
|-------------|-----------|
| `disableBypassPermissionsMode` | Impedir usuários de ativar o bypass de permissões |
| `availableModels` | Restringir quais modelos os usuários podem selecionar |
| `allowedChannelPlugins` | Controlar quais plugins de canal são permitidos |
| `autoMode.environment` | Configurar infraestrutura confiável para o modo auto |
| Políticas personalizadas | Políticas de permissão e ferramenta específicas da organização |

### Exemplo: plist do macOS

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Configuração e Ajustes

### Locais dos Arquivos de Configuração

1. **Config global**: `~/.claude/config.json`
2. **Config do projeto**: `./.claude/config.json`
3. **Config do usuário**: `~/.config/claude-code/settings.json`

### Exemplo de Configuração Completa

**Configuração de recursos avançados principais:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**Exemplo de configuração estendida:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Variáveis de Ambiente

Substitua a config com variáveis de ambiente:

```bash
# Seleção de modelo
export ANTHROPIC_MODEL=claude-opus-4-7
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-7
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# Configuração de API
export ANTHROPIC_API_KEY=sk-ant-...

# Configuração de raciocínio
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# Alternadores de recursos
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Definido pelo flag --bare

# Configuração MCP
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Gerenciamento de tarefas
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Equipes de agentes (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Configuração de subagente e plugin
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Subprocess e streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### Comandos de Gerenciamento de Configuração

```
Usuário: /config
[Abre menu de configuração interativo]
```

O comando `/config` fornece um menu interativo para alternar configurações como:
- Raciocínio estendido on/off
- Saída verbose
- Modo de permissão
- Seleção de modelo

### Configuração por Projeto

Crie `.claude/config.json` em seu projeto:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Equipes de Agentes

Equipes de Agentes é um recurso experimental que permite que múltiplas instâncias do Claude Code colaborem em uma tarefa. Está desativado por padrão.

### Ativando Equipes de Agentes

Ative via variável de ambiente ou configurações:

```bash
# Variável de ambiente
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

Ou adicione ao seu JSON de configurações:

```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
}
```

### Como Equipes de Agentes Funcionam

- Um **líder de equipe** coordena a tarefa geral e delega subtarefas para membros
- **Membros** trabalham independentemente, cada um com sua própria janela de contexto
- Uma **lista de tarefas compartilhada** permite autocoordernação entre membros da equipe
- Use definições de subagente (`.claude/agents/` ou flag `--agents`) para definir funções e especializações dos membros

### Modos de Exibição

Equipes de Agentes suportam dois modos de exibição, configurados com o flag `--teammate-mode`:

| Modo | Descrição |
|------|-----------|
| `in-process` (padrão) | Membros executam dentro do mesmo processo do terminal |
| `tmux` | Cada membro recebe um painel dividido dedicado (requer tmux ou iTerm2) |
| `auto` | Seleciona automaticamente o melhor modo de exibição |

```bash
# Usar painéis divididos tmux para exibição de membros
claude --teammate-mode tmux

# Usar explicitamente o modo in-process
claude --teammate-mode in-process
```

### Casos de Uso

- Tarefas de refatoração grandes onde diferentes membros tratam módulos diferentes
- Revisão de código paralela e implementação
- Alterações coordenadas em múltiplos arquivos em uma codebase

> **Nota**: Equipes de Agentes é experimental e pode mudar em versões futuras. Veja [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) para a referência completa.

---

## Boas Práticas

### Modo de Planejamento
- ✅ Use para tarefas complexas de múltiplas etapas
- ✅ Revise os planos antes de aprovar
- ✅ Modifique os planos quando necessário
- ❌ Não use para tarefas simples

### Raciocínio Estendido
- ✅ Use para decisões arquiteturais
- ✅ Use para resolução de problemas complexos
- ✅ Revise o processo de raciocínio
- ❌ Não use para consultas simples

### Tarefas em Segundo Plano
- ✅ Use para operações de longa duração
- ✅ Monitore o progresso das tarefas
- ✅ Trate falhas de tarefa graciosamente
- ❌ Não inicie muitas tarefas concorrentes

### Permissões
- ✅ Use `plan` para revisão de código (somente leitura)
- ✅ Use `default` para desenvolvimento interativo
- ✅ Use `acceptEdits` para fluxos de trabalho de automação
- ✅ Use `auto` para trabalho autônomo com proteções de segurança
- ❌ Não use `bypassPermissions` a menos que seja absolutamente necessário

### Sessões
- ✅ Use sessões separadas para tarefas diferentes
- ✅ Salve estados de sessão importantes
- ✅ Limpe sessões antigas
- ❌ Não misture trabalho não relacionado em uma sessão

---

## Recursos Adicionais

Para mais informações sobre o Claude Code e recursos relacionados:

- [Documentação Oficial do Modo Interativo](https://code.claude.com/docs/en/interactive-mode)
- [Documentação Oficial do Modo Headless](https://code.claude.com/docs/en/headless)
- [Referência CLI](https://code.claude.com/docs/en/cli-reference)
- [Guia de Checkpoints](../08-checkpoints/) - Gerenciamento de sessão e retrocesso
- [Comandos de Barra](../01-slash-commands/) - Referência de comandos
- [Guia de Memória](../02-memory/) - Contexto persistente
- [Guia de Skills](../03-skills/) - Capacidades autônomas
- [Guia de Subagentes](../04-subagents/) - Execução de tarefas delegada
- [Guia MCP](../05-mcp/) - Acesso a dados externos
- [Guia de Hooks](../06-hooks/) - Automação orientada a eventos
- [Guia de Plugins](../07-plugins/) - Extensões agrupadas
- [Documentação Oficial de Tarefas Agendadas](https://code.claude.com/docs/en/scheduled-tasks)
- [Documentação Oficial de Integração Chrome](https://code.claude.com/docs/en/chrome)
- [Documentação Oficial de Controle Remoto](https://code.claude.com/docs/en/remote-control)
- [Documentação Oficial de Atalhos de Teclado](https://code.claude.com/docs/en/keybindings)
- [Documentação Oficial do App de Desktop](https://code.claude.com/docs/en/desktop)
- [Documentação Oficial de Equipes de Agentes](https://code.claude.com/docs/en/agent-teams)

---
**Última Atualização**: 16 de abril de 2026
**Versão do Claude Code**: 2.1.112
**Fontes**:
- https://docs.anthropic.com/en/docs/claude-code
- https://www.anthropic.com/news/claude-opus-4-7
- https://support.claude.com/en/articles/12138966-release-notes
**Modelos Compatíveis**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
