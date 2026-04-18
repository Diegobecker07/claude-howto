<!-- i18n-source: resources/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - Assets de Marca

Coleção completa de logotipos, ícones e favicons para o projeto Claude How To. Todos os assets usam o design V3.0: uma bússola com símbolo de colchete de código (`>`), representando navegação guiada pelo código — usando uma paleta Preto/Branco/Cinza com destaque em Verde Brilhante (#22C55E).

## Estrutura de Diretórios

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # Logotipo principal - Modo claro (520×120px)
│   └── claude-howto-logo-dark.svg  # Logotipo principal - Modo escuro (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # Ícone do app - Modo claro (256×256px)
│   └── claude-howto-icon-dark.svg  # Ícone do app - Modo escuro (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px (principal)
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

Assets adicionais em `assets/logo/`:
```
assets/logo/
├── logo-full.svg       # Marca + wordmark (horizontal)
├── logo-mark.svg       # Apenas o símbolo da bússola (120×120px)
├── logo-wordmark.svg   # Apenas texto
├── logo-icon.svg       # Ícone do app (512×512, arredondado)
├── favicon.svg         # Otimizado para 16×16
├── logo-white.svg      # Versão branca para fundos escuros
└── logo-black.svg      # Versão monocromática preta
```

## Visão Geral dos Assets

### Conceito de Design (V3.0)

**Bússola com Colchete de Código** — orientação encontra o código:
- **Anel da Bússola** = Navegação, encontrar seu caminho
- **Agulha Norte (Verde)** = Direção, progresso no caminho de aprendizado
- **Agulha Sul (Preto)** = Ancoragem, base sólida
- **Colchete `>`** = Prompt do terminal, código, contexto CLI
- **Marcações** = Precisão, aprendizado estruturado

### Logotipos

**Arquivos**:
- `logos/claude-howto-logo.svg` (Modo claro)
- `logos/claude-howto-logo-dark.svg` (Modo escuro)

**Especificações**:
- **Tamanho**: 520×120 px
- **Propósito**: Logotipo principal de cabeçalho/marca com wordmark
- **Uso**:
  - Cabeçalhos de website
  - Badges de README
  - Materiais de marketing
  - Materiais impressos
- **Formato**: SVG (totalmente escalável)
- **Modos**: Claro (fundo branco) e Escuro (fundo #0A0A0A)

### Ícones

**Arquivos**:
- `icons/claude-howto-icon.svg` (Modo claro)
- `icons/claude-howto-icon-dark.svg` (Modo escuro)

**Especificações**:
- **Tamanho**: 256×256 px
- **Propósito**: Ícone de aplicativo, avatares, miniaturas
- **Uso**:
  - Ícones de app
  - Avatares de perfil
  - Miniaturas de redes sociais
  - Cabeçalhos de documentação
- **Formato**: SVG (totalmente escalável)
- **Modos**: Claro (fundo branco) e Escuro (fundo #0A0A0A)

**Elementos de Design**:
- Anel de bússola com marcações cardinais e intercardinais
- Agulha norte verde (direção/orientação)
- Agulha sul preta (fundação)
- Colchete de código `>` ao centro (terminal/CLI)
- Ponto central verde de destaque

### Favicons

Versões otimizadas em múltiplos tamanhos para uso web:

| Arquivo | Tamanho | DPI | Uso |
|---------|---------|-----|-----|
| `favicon-16.svg` | 16×16 px | 1x | Abas do navegador (navegadores mais antigos) |
| `favicon-32.svg` | 32×32 px | 1x | Favicon padrão do navegador |
| `favicon-64.svg` | 64×64 px | 1x-2x | Displays de alta resolução (HiDPI) |
| `favicon-128.svg` | 128×128 px | 2x | Ícone touch da Apple, favoritos |
| `favicon-256.svg` | 256×256 px | 4x | Navegadores modernos, ícones PWA |

**Notas de Otimização**:
- 16px: Geometria mínima — apenas anel, agulhas e chevron
- 32px: Adiciona marcações cardinais
- 64px+: Detalhe completo com marcações intercardinais
- Todos mantêm consistência visual com o ícone principal
- O formato SVG garante exibição nítida em qualquer tamanho

## Integração HTML

### Configuração Básica de Favicon

```html
<!-- Favicon do navegador -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Ícone touch da Apple (tela inicial mobile) -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA e navegadores modernos -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### Configuração Completa

```html
<head>
  <!-- Favicon principal -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Ícone touch da Apple -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- Ícones PWA -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- Referência ao manifest PWA (se usar manifest.json) -->
  <meta name="theme-color" content="#000000">
</head>
```

## Paleta de Cores

### Cores Principais
- **Preto**: `#000000` (Texto principal, traços, agulha sul)
- **Branco**: `#FFFFFF` (Fundos claros)
- **Cinza**: `#6B7280` (Texto secundário, marcações menores)

### Cor de Destaque
- **Verde Brilhante**: `#22C55E` (Agulha norte, ponto central, linhas de destaque — apenas para destaques, nunca como fundo)

### Modo Escuro
- **Fundo**: `#0A0A0A` (Quase preto)

### Variáveis CSS
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Configuração Tailwind
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### Diretrizes de Uso
- Use preto para texto principal e elementos estruturais
- Use cinza para elementos secundários/de suporte
- Use verde **apenas** para destaques — agulha, pontos, linhas de destaque
- Nunca use verde como cor de fundo
- Mantenha o contraste WCAG AA (mínimo de 4,5:1)

## Diretrizes de Design

### Uso do Logotipo
- Use em fundos brancos ou escuros (#0A0A0A)
- Escalone proporcionalmente
- Inclua espaço livre ao redor do logotipo (mínimo: altura do logotipo / 2)
- Use as variantes claro/escuro fornecidas para fundos apropriados

### Uso do Ícone
- Use em tamanhos padrão: 16, 32, 64, 128, 256px
- Mantenha as proporções da bússola
- Escalone proporcionalmente

### Uso do Favicon
- Use o tamanho apropriado para o contexto
- 16-32px: Abas do navegador, favoritos
- 64px: Ícones de sites favicon
- 128px+: Telas iniciais Apple/Android

## Otimização de SVG

Todos os arquivos SVG são design plano, sem gradientes ou filtros:
- Geometria limpa baseada em traços
- Sem rasters embutidos
- Caminhos otimizados
- ViewBox responsivo

Para otimização web:
```bash
# Comprimir SVG mantendo a qualidade
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## Conversão para PNG

Para converter SVG para PNG para suporte em navegadores mais antigos:

```bash
# Usando ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# Usando Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## Acessibilidade

- Altas taxas de contraste de cores (em conformidade com WCAG AA — mínimo de 4,5:1)
- Formas geométricas limpas reconhecíveis em todos os tamanhos
- Formato vetorial escalável
- Sem texto nos ícones (texto adicionado separadamente no wordmark)
- Sem dependência de cores vermelho-verde para significado

## Atribuição

Estes assets fazem parte do projeto Claude How To.

**Licença**: MIT (veja o arquivo LICENSE do projeto)

## Histórico de Versões

- **v3.0** (Fevereiro de 2026): Design bússola-colchete com paleta Preto/Branco/Cinza + destaque Verde
- **v2.0** (Janeiro de 2026): Design de estrela com 12 raios inspirado no Claude com paleta esmeralda
- **v1.0** (Janeiro de 2026): Design original de ícone de progressão baseado em hexágono

---

**Última Atualização**: Fevereiro de 2026
**Versão Atual**: 3.0 (Bússola-Colchete)
**Todos os Assets**: SVG pronto para produção, totalmente escalável, acessível WCAG AA
