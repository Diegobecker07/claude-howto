<!-- i18n-source: CLAUDE.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# CLAUDE.md

Este arquivo fornece orientações ao Claude Code (claude.ai/code) ao trabalhar com código neste repositório.

## Visão Geral do Projeto

Claude How To é um repositório de tutoriais sobre recursos do Claude Code. Este é um **documentation-as-code** — a saída primária são arquivos markdown organizados em módulos de aprendizado numerados, não uma aplicação executável.

**Arquitetura**: Cada módulo (01-10) cobre um recurso específico do Claude Code com templates copy-paste, diagramas Mermaid e exemplos. O sistema de build valida a qualidade da documentação e gera um e-book EPUB.

## Comandos Comuns

### Verificações de Qualidade Pré-commit

Toda documentação deve passar por quatro verificações de qualidade antes dos commits (elas são executadas automaticamente via hooks pré-commit):

```bash
# Instalar hooks pré-commit (executado em cada commit)
pre-commit install

# Executar todas as verificações manualmente
pre-commit run --all-files
```

As quatro verificações são:
1. **markdown-lint** — Estrutura e formatação Markdown via `markdownlint`
2. **cross-references** — Links internos, âncoras, sintaxe de code fence (script Python)
3. **mermaid-syntax** — Valida se todos os diagramas Mermaid são parseados corretamente (script Python)
4. **link-check** — URLs externas são acessíveis (script Python)
5. **build-epub** — O EPUB é gerado sem erros (em mudanças de `.md`)

### Configuração do Ambiente de Desenvolvimento

```bash
# Instalar uv (gerenciador de pacotes Python)
pip install uv

# Criar ambiente virtual e instalar dependências Python
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Instalar ferramentas Node.js (linter de markdown e validador Mermaid)
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli

# Instalar hooks pré-commit
uv pip install pre-commit
pre-commit install
```

### Testes

Scripts Python em `scripts/` têm testes unitários:

```bash
# Executar todos os testes
pytest scripts/tests/ -v

# Executar com cobertura
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Executar teste específico
pytest scripts/tests/test_build_epub.py -v
```

### Qualidade do Código

```bash
# Lint e formatar código Python
ruff check scripts/
ruff format scripts/

# Varredura de segurança
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# Verificação de tipos
mypy scripts/ --ignore-missing-imports
```

### Build EPUB

```bash
# Gerar e-book (renderiza diagramas Mermaid via API Kroki.io)
uv run scripts/build_epub.py

# Com opções
uv run scripts/build_epub.py --verbose --output custom-name.epub --max-concurrent 5
```

## Estrutura de Diretórios

```
├── 01-slash-commands/      # Atalhos invocados pelo usuário
├── 02-memory/              # Exemplos de contexto persistente
├── 03-skills/              # Capacidades reutilizáveis
├── 04-subagents/           # Assistentes de IA especializados
├── 05-mcp/                 # Exemplos de Model Context Protocol
├── 06-hooks/               # Automação orientada a eventos
├── 07-plugins/             # Recursos em pacote
├── 08-checkpoints/         # Snapshots de sessão
├── 09-advanced-features/   # Planejamento, pensamento, background
├── 10-cli/                 # Referência CLI
├── scripts/
│   ├── build_epub.py           # Gerador EPUB (renderiza Mermaid via API Kroki)
│   ├── check_cross_references.py   # Valida links internos
│   ├── check_links.py          # Verifica URLs externas
│   ├── check_mermaid.py        # Valida sintaxe Mermaid
│   └── tests/                  # Testes unitários para scripts
├── .pre-commit-config.yaml    # Definições de verificação de qualidade
└── README.md               # Guia principal (também índice de módulos)
```

## Diretrizes de Conteúdo

### Estrutura dos Módulos
Cada pasta numerada segue o padrão:
- **README.md** — Visão geral do recurso com exemplos
- **Arquivos de exemplo** — Templates copy-paste (`.md` para comandos, `.json` para configs, `.sh` para hooks)
- Arquivos organizados por complexidade do recurso e dependências

### Diagramas Mermaid
- Todos os diagramas devem ser parseados com sucesso (verificado pelo hook pré-commit)
- O build EPUB renderiza diagramas via API Kroki.io (requer internet)
- Use Mermaid para fluxogramas, diagramas de sequência e visuais de arquitetura

### Referências Cruzadas
- Use caminhos relativos para links internos (ex.: `(01-slash-commands/README.md)`)
- Code fences devem especificar linguagem (ex.: ` ```bash `, ` ```python `)
- Links de âncora usam o formato `#nome-do-cabeçalho`

### Validação de Links
- URLs externas devem ser acessíveis (verificado pelo hook pré-commit)
- Evite linkar para conteúdo efêmero
- Use permalinks sempre que possível

## Pontos-Chave de Arquitetura

1. **Pastas numeradas indicam a ordem de aprendizado** — O prefixo 01-10 representa a sequência recomendada para aprender recursos do Claude Code. Esta numeração é intencional; não reorganize alfabeticamente.

2. **Scripts são utilitários, não o produto** — Os scripts Python em `scripts/` suportam a qualidade da documentação e a geração EPUB. O conteúdo real está nas pastas de módulos numerados.

3. **O pré-commit é o guardião** — Todas as quatro verificações de qualidade devem passar antes de um PR ser aceito. O pipeline de CI executa essas mesmas verificações como uma segunda passagem.

4. **A renderização do Mermaid requer rede** — O build EPUB chama a API Kroki.io para renderizar diagramas. Falhas de build aqui são tipicamente problemas de rede ou sintaxe Mermaid inválida.

5. **Este é um tutorial, não uma biblioteca** — Ao adicionar conteúdo, foque em explicações claras, exemplos copy-paste e diagramas visuais. O valor está em ensinar conceitos, não em fornecer código reutilizável.

## Convenções de Commit

Siga o formato conventional commit:
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`
- `refactor(hooks): Simplify hook configuration examples`

O escopo deve corresponder ao nome da pasta quando aplicável.
