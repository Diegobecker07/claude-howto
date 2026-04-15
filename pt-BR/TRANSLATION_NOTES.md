<!-- i18n-source: uk/TRANSLATION_NOTES.md -->
<!-- i18n-source-sha: b8a7b1f -->
<!-- i18n-date: 2026-04-14 -->

# Glossário e Guia de Estilo da Tradução

> **Importante:** este documento define as regras para traduzir a documentação do Claude Code para português do Brasil. Leia antes de começar qualquer arquivo novo.

## Terminologia técnica

Use estes termos como referência para manter consistência em toda a tradução:

| English | Português (Brasil) | Observação |
|---------|---------------------|------------|
| slash command | comando slash | Mantemos "slash" como nome da funcionalidade |
| hook | hook | Termo técnico consagrado |
| skill | skill / habilidade | Use "skill" quando o termo estiver nomeando a funcionalidade; use "habilidade" quando soar melhor no texto |
| subagent | subagente | Tradução preferida |
| agent | agente | Tradução preferida |
| memory | memória | Tradução preferida |
| checkpoint | checkpoint | Mantido como termo do produto |
| plugin | plugin | Termo técnico consagrado |
| pull request / PR | pull request / PR | Mantemos o termo GitHub |
| commit | commit | Mantido |
| branch | branch | Mantido em contexto Git |
| merge | merge | Mantido em contexto Git |
| MCP (Model Context Protocol) | MCP | Mantido como nome do protocolo |
| CLAUDE.md | CLAUDE.md | Nome do arquivo não muda |
| prompt | prompt | Mantido |
| workflow | workflow / fluxo de trabalho | Prefira a forma mais natural para o contexto |
| repository | repositório / repo | Traduza quando ajudar a leitura |
| issue | issue | Mantido em contexto GitHub |
| release | release | Mantido ou "lançamento", conforme o contexto |
| API | API | Mantido |
| CLI | CLI | Mantido |
| CI/CD | CI/CD | Mantido |
| pre-commit hook | pre-commit hook | Mantemos o nome da ferramenta |
| environment variable | variável de ambiente | Tradução preferida |
| dependencies | dependências | Tradução preferida |
| template | template / modelo | Prefira "modelo" quando ficar mais claro |
| worktree | worktree / árvore de trabalho | Traduza apenas se o contexto pedir |
| frontmatter | frontmatter | Mantido como termo técnico |
| token | token | Mantido |
| context window | janela de contexto | Tradução preferida |
| fork | fork | Mantido |
| clone | clonar | Verbo traduzido |
| sandbox | sandbox / ambiente isolado | Prefira a forma mais clara no texto |
| boilerplate | boilerplate / código repetitivo | Traduza quando o sentido for explicativo |
| debugging | depuração | Tradução preferida |
| linting | linting | Mantido como termo técnico |
| refactoring | refatoração | Tradução preferida |

## Regras de tradução

### 1. Código e comandos

**Regra principal:** mantenha 100% do código executável intacto. Traduza apenas comentários e texto explicativo.

### 2. Comentários no código

Traduza comentários para português do Brasil, mas nunca altere nomes de funções, classes, variáveis, arquivos ou diretórios.

### 3. Mermaid

Não traduza nada dentro de blocos `mermaid`. Mantemos diagramas exatamente como no original.

### 4. Caminhos e URLs

Não altere caminhos relativos, nomes de arquivos, URLs ou identificadores técnicos.

### 5. Links entre arquivos

Use caminhos relativos corretos dentro de `pt-BR/` e preserve os links para o inglês quando precisar apontar para o original.

### 6. Metadados de rastreio

Todo arquivo traduzido deve começar com estes comentários:

```markdown
<!-- i18n-source: caminho/do/arquivo-original.md -->
<!-- i18n-source-sha: abc1234 -->
<!-- i18n-date: 2026-04-14 -->
```

O SHA deve apontar para o commit curto da versão original usada como base.

### 7. Estilo textual

- Fale diretamente com `você`
- Prefira frases curtas e técnicas
- Evite formalismo excessivo
- Preserve consistência terminológica entre arquivos

## Checklist antes do commit

- [ ] Código, comandos e caminhos preservados
- [ ] Mermaid sem tradução
- [ ] Metadados `i18n-*` presentes
- [ ] Glossário aplicado de forma consistente
- [ ] Texto revisado em português natural
