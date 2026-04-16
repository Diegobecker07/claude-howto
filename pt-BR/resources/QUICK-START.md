<!-- i18n-source: resources/QUICK-START.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Início Rápido - Assets de Marca

## Copiar Assets para Seu Projeto

```bash
# Copiar todos os recursos para seu projeto web
cp -r resources/ /caminho/para/seu/website/

# Ou apenas os favicons para web
cp resources/favicons/* /caminho/para/seu/website/public/
```

## Adicionar ao HTML (Copie e Cole)

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## Usar em Markdown/Documentação

```markdown
# Claude How To

![Logo do Claude How To](resources/logos/claude-howto-logo.svg)

![Ícone](resources/icons/claude-howto-icon.svg)
```

## Tamanhos Recomendados

| Propósito | Tamanho | Arquivo |
|-----------|---------|---------|
| Cabeçalho do website | 520×120 | `logos/claude-howto-logo.svg` |
| Ícone de app | 256×256 | `icons/claude-howto-icon.svg` |
| Aba do navegador | 32×32 | `favicons/favicon-32.svg` |
| Tela inicial mobile | 128×128 | `favicons/favicon-128.svg` |
| App desktop | 256×256 | `favicons/favicon-256.svg` |
| Avatar pequeno | 64×64 | `favicons/favicon-64.svg` |

## Valores de Cores

```css
/* Use esses no seu CSS */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## Significado do Design do Ícone

**Bússola com Colchete de Código**:
- Anel da bússola = Navegação, caminho de aprendizado estruturado
- Agulha norte verde = Direção, progresso, orientação
- Agulha sul preta = Ancoragem, base sólida
- Colchete `>` = Prompt do terminal, código, contexto CLI
- Marcações = Precisão, passos estruturados

Isso simboliza "encontrar seu caminho pelo código com orientação clara."

## O Que Usar Onde

### Website
- **Cabeçalho**: Logotipo (`logos/claude-howto-logo.svg`)
- **Favicon**: 32px (`favicons/favicon-32.svg`)
- **Pré-visualização social**: Ícone (`icons/claude-howto-icon.svg`)

### GitHub
- **Badge do README**: Ícone (`icons/claude-howto-icon.svg`) em 64-128px
- **Avatar do repositório**: Ícone (`icons/claude-howto-icon.svg`)

### Redes Sociais
- **Foto de perfil**: Ícone (`icons/claude-howto-icon.svg`)
- **Banner**: Logotipo (`logos/claude-howto-logo.svg`)
- **Miniatura**: Ícone em 256×256px

### Documentação
- **Cabeçalhos de capítulo**: Logotipo ou ícone (dimensionado para caber)
- **Ícones de navegação**: Favicon (32-64px)

---

Veja [README.md](README.md) para documentação completa.
