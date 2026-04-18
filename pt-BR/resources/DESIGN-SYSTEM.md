<!-- i18n-source: resources/DESIGN-SYSTEM.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Claude How To - Sistema de Design

## Identidade Visual

### Conceito de Design do Ícone: Bússola com Colchete de Código

O ícone do Claude How To usa uma **bússola com um colchete de código `>`** para representar navegação guiada pelo código:

```
     N (verde)
     ▲
     │
W ───>─── L     Bússola = Orientação/Direção
     │          > Colchete = Código/Terminal/CLI
     ▼
     S (preto)
```

Isso cria:
- **Clareza Visual**: Comunica imediatamente "guia de navegação de código"
- **Significado Simbólico**: Bússola = encontrar seu caminho; `>` = código/terminal
- **Escalabilidade**: Funciona em qualquer tamanho, de 16px a 512px
- **Alinhamento com a Marca**: Combina com a estética de ferramenta para desenvolvedores com paleta mínima

---

## Sistema de Cores

### Paleta

| Cor | Hex | RGB | Uso |
|-----|-----|-----|-----|
| Preto (Principal) | `#000000` | 0, 0, 0 | Traços principais, texto, agulha sul |
| Branco (Fundo) | `#FFFFFF` | 255, 255, 255 | Fundos claros |
| Cinza (Secundário) | `#6B7280` | 107, 114, 128 | Marcações menores, texto secundário |
| Verde Brilhante (Destaque) | `#22C55E` | 34, 197, 94 | Agulha norte, ponto central, linhas de destaque |
| Quase Preto (Fundo Escuro) | `#0A0A0A` | 10, 10, 10 | Fundos no modo escuro |

### Taxas de Contraste (WCAG)

- Preto no Branco: **21:1** AAA
- Cinza no Branco: **4,6:1** AA
- Verde no Branco: **3,2:1** (apenas decorativo, não para texto)
- Branco no Escuro: **19,5:1** AAA

### Regra da Cor de Destaque

**Verde Brilhante (#22C55E) é reservado apenas para destaques:**
- Agulha norte da bússola
- Ponto central
- Sublinhados/bordas de destaque
- Nunca como cor de fundo
- Nunca para texto de corpo

---

## Tipografia

### Fonte do Logotipo
- **Família**: Inter, SF Pro Display, -apple-system, Segoe UI, sans-serif
- **"Claude"**: 42px, peso 700 (negrito), Preto
- **"How-To"**: 32px, peso 500 (médio), Cinza (#6B7280)
- **Subtítulo**: 10px, peso 500, Cinza, espaçamento entre letras 1,5px, maiúsculas

### Fonte da Interface
- **Família**: Inter, SF Pro, fontes do sistema (sans-serif)
- **Peso**: 400-600
- **Estilo**: Limpo, legível

---

## Detalhes do Ícone

### Especificações da Bússola

A marca da bússola é construída a partir destes elementos geométricos:

```
Elemento              | Traço/Preenchimento | Cor
----------------------|---------------------|-------------------
Anel externo          | 3px traço           | Preto / Branco (modo escuro)
Marcação norte        | 2,5px traço         | Preto / Branco (modo escuro)
Outras marcações cardinais | 2px traço      | Cinza / Branco 50% (modo escuro)
Marcações intercardinais | 1,5px traço      | Cinza / Branco 40% (modo escuro)
Agulha norte          | polígono preenchido | #22C55E (sempre verde)
Agulha sul            | polígono preenchido | Preto / Branco (modo escuro)
Colchete >            | 3px traço           | Preto / Branco (modo escuro)
Ponto central         | círculo preenchido  | #22C55E (sempre verde)
```

### Progressão de Tamanhos

```
16px  → Apenas anel + agulhas + chevron (mínimo)
32px  → Adiciona marcações cardinais
64px  → Adiciona marcações intercardinais
128px → Detalhe completo, todos os elementos nítidos
256px → Máximo detalhe, traços grossos
```

---

## Diretrizes de Tamanho

### Tamanho do Logotipo

- **Mínimo**: 200px de largura (para web)
- **Recomendado**: 520px (tamanho nativo)
- **Máximo**: Ilimitado (formato vetorial)
- **Proporção**: ~4,3:1 (largura:altura)

### Tamanho do Ícone

- **Mínimo**: 16px (favicon)
- **Recomendado**: 64-256px (apps, avatares)
- **Máximo**: Ilimitado (formato vetorial)
- **Proporção**: 1:1 (quadrado)

---

## Espaçamento e Alinhamento

### Espaçamento do Logotipo

```
┌─────────────────────────────────────┐
│                                     │
│        Espaço Mínimo Livre          │
│        (altura do logotipo / 2)     │
│                                     │
│    [BÚSSOLA]  Claude                │
│               How-To                │
│                                     │
└─────────────────────────────────────┘
```

### Ponto Central do Ícone

Todos os ícones centralizam no ponto médio de seu canvas:
- 128×128 para canvas de 256px
- 64×64 para canvas de 128px
- Mantém alinhamento com outros elementos de UI

---

## Acessibilidade

### Contraste de Cores
- Todo o texto atende WCAG AA (mínimo de 4,5:1)
- O destaque verde é decorativo, não informacional
- Sem dependência de cores vermelho-verde

### Escalabilidade
- O formato vetorial garante clareza em qualquer tamanho
- Formas geométricas permanecem reconhecíveis em 16px
- Detalhe progressivo baseado no tamanho disponível

---

## Exemplos de Aplicação

### Cabeçalho Web
- Tamanho: logotipo 520×120px
- Arquivo: `logos/claude-howto-logo.svg`
- Fundo: Branco ou escuro (#0A0A0A)
- Padding: mínimo de 20px

### Ícone de App
- Tamanho: 256×256px
- Arquivo: `icons/claude-howto-icon.svg`
- Fundo: Branco ou escuro
- Uso: Atalhos de app, avatares

### Favicon do Navegador
- Tamanho: 32px (principal), 16px (fallback)
- Arquivo: `favicons/favicon-32.svg`
- Formato: SVG para exibição nítida

### Redes Sociais
- Perfil: ícone 256×256px
- Banner: logotipo 520×120px (centralizado)

### Documentação
- Cabeçalhos de Capítulo: Logotipo dimensionado para caber
- Ícones de Seção: favicon 64×64px
- Inline: favicon 32×32px

---

## Detalhes do Formato de Arquivo

### Estrutura SVG

Todos os arquivos SVG são design plano:
- Sem gradientes (apenas cores sólidas)
- Sem efeitos de filtro (sem desfoque, brilho ou sombra)
- Geometria limpa de traço e preenchimento
- ViewBox para escalonamento responsivo
- Código legível e comentado

### Compatibilidade Entre Navegadores

- Chrome/Edge: Suporte completo
- Firefox: Suporte completo
- Safari: Suporte completo
- iOS Safari: Suporte completo
- Todos os navegadores modernos: Suporte completo

---

## Personalização

### Alterando a Cor de Destaque

Para criar variantes com uma cor de destaque diferente:

1. Substitua todas as instâncias de `#22C55E` pela sua cor de destaque
2. Garanta que a taxa de contraste fique acima de 3:1 para elementos decorativos
3. Mantenha a estrutura preto/branco/cinza inalterada

### Escalonamento

```css
svg {
  width: 256px;
  height: 256px;
}
```

Os SVGs escalam automaticamente via viewBox — sem necessidade de transforms.

---

## Controle de Versão

Rastreie mudanças de design no git:
- Versione os arquivos SVG normalmente (são texto)
- Marque lançamentos com mudanças de design
- Inclua DESIGN-SYSTEM.md nos commits

---

**Última Atualização**: Fevereiro de 2026
**Versão do Sistema de Design**: 3.0
