<!-- i18n-source: scripts/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Script de Build EPUB

Constrói um ebook EPUB a partir dos arquivos markdown do Claude How-To.

## Recursos

- Organiza capítulos pela estrutura de pastas (01-slash-commands, 02-memory, etc.)
- Renderiza diagramas Mermaid como imagens PNG via API Kroki.io
- Busca assíncrona e concorrente — renderiza todos os diagramas em paralelo
- Gera uma imagem de capa a partir do logotipo do projeto
- Converte links markdown internos para referências de capítulo EPUB
- Modo de erro estrito — falha se qualquer diagrama não puder ser renderizado

## Requisitos

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Conexão com a internet para renderização de diagramas Mermaid

## Início Rápido

```bash
# Forma mais simples — o uv cuida de tudo
uv run scripts/build_epub.py
```

## Configuração de Desenvolvimento

```bash
# Criar ambiente virtual
uv venv

# Ativar e instalar dependências
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# Executar testes
pytest scripts/tests/ -v

# Executar o script
python scripts/build_epub.py
```

## Opções de Linha de Comando

```
uso: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                   [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

opções:
  -h, --help            mostrar esta mensagem de ajuda e sair
  --root, -r ROOT       Diretório raiz (padrão: raiz do repositório)
  --output, -o OUTPUT   Caminho de saída (padrão: claude-howto-guide.epub)
  --verbose, -v         Habilitar logging detalhado
  --timeout TIMEOUT     Timeout da API em segundos (padrão: 30)
  --max-concurrent N    Máximo de requisições simultâneas (padrão: 10)
```

## Exemplos

```bash
# Build com saída detalhada
uv run scripts/build_epub.py --verbose

# Local de saída personalizado
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Limitar requisições simultâneas (em caso de limite de taxa)
uv run scripts/build_epub.py --max-concurrent 5
```

## Saída

Cria `claude-howto-guide.epub` no diretório raiz do repositório.

O EPUB inclui:
- Imagem de capa com o logotipo do projeto
- Índice com seções aninhadas
- Todo o conteúdo markdown convertido para HTML compatível com EPUB
- Diagramas Mermaid renderizados como imagens PNG

## Executando Testes

```bash
# Com ambiente virtual
source .venv/bin/activate
pytest scripts/tests/ -v

# Ou diretamente com uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## Dependências

Gerenciadas via metadados de script inline PEP 723:

| Pacote | Propósito |
|--------|-----------|
| `ebooklib` | Geração de EPUB |
| `markdown` | Conversão de Markdown para HTML |
| `beautifulsoup4` | Análise de HTML |
| `httpx` | Cliente HTTP assíncrono |
| `pillow` | Geração de imagem de capa |
| `tenacity` | Lógica de retry |

## Solução de Problemas

**Build falha com erro de rede**: Verifique a conectividade com a internet e o status do Kroki.io. Tente `--timeout 60`.

**Limite de taxa**: Reduza as requisições simultâneas com `--max-concurrent 3`.

**Logotipo ausente**: O script gera uma capa apenas com texto se `claude-howto-logo.png` não for encontrado.
