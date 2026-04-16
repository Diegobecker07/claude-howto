<!-- i18n-source: 03-skills/blog-draft/SKILL.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: blog-draft
description: Redigir um post de blog a partir de ideias e recursos. Usar quando usuários querem escrever um post de blog, criar conteúdo a partir de pesquisa, ou redigir artigos. Guia através de pesquisa, brainstorm, esboço e redação iterativa com controle de versão.
---

## Entrada do Usuário

```text
$ARGUMENTS
```

Você **DEVE** considerar a entrada do usuário antes de prosseguir. O usuário deve fornecer:
- **Ideia/Tópico**: O conceito ou tema principal do post de blog
- **Recursos**: URLs, arquivos ou referências para pesquisa (opcional, mas recomendado)
- **Público-alvo**: Para quem é o post de blog (opcional)
- **Tom/Estilo**: Formal, casual, técnico, etc. (opcional)

**IMPORTANTE**: Se o usuário está solicitando atualizações em um **post de blog existente**, pule os passos 0-8 e comece diretamente no **Passo 9**. Leia os arquivo(s) de rascunho existentes primeiro, depois prossiga com o processo de iteração.

## Fluxo de Execução

Siga esses passos sequencialmente. **Não pule passos nem prossiga sem aprovação do usuário onde indicado.**

### Passo 0: Criar Pasta do Projeto

1. Gere um nome de pasta usando o formato: `AAAA-MM-DD-nome-curto-topico`
   - Use a data de hoje
   - Crie um slug curto e amigável para URL a partir do tópico (letras minúsculas, hífens, máx. 5 palavras)

2. Crie a estrutura de pastas:
   ```
   blog-posts/
   └── AAAA-MM-DD-nome-curto-topico/
       └── resources/
   ```

3. Confirme a criação da pasta com o usuário antes de prosseguir.

### Passo 1: Pesquisa e Coleta de Recursos

1. Crie a subpasta `resources/` no diretório do post de blog

2. Para cada recurso fornecido:
   - **URLs**: Busque e salve informações-chave em `resources/` como arquivos markdown
   - **Arquivos**: Leia e resuma em `resources/`
   - **Tópicos**: Use busca na web para coletar informações atualizadas

3. Para cada recurso, crie um arquivo de resumo em `resources/`:
   - `resources/source-1-[nome-curto].md`
   - `resources/source-2-[nome-curto].md`
   - etc.

4. Cada resumo deve incluir:
   ```markdown
   # Fonte: [Título/URL]

   ## Pontos-Chave
   - Ponto 1
   - Ponto 2

   ## Citações/Dados Relevantes
   - Citação ou estatística 1
   - Citação ou estatística 2

   ## Como Isso se Relaciona ao Tópico
   Breve explicação de relevância
   ```

5. Apresente o resumo da pesquisa ao usuário.

### Passo 2: Brainstorm e Esclarecimento

1. Com base na ideia e nos recursos pesquisados, apresente:
   - **Temas principais** identificados na pesquisa
   - **Ângulos possíveis** para o post de blog
   - **Pontos-chave** que devem ser abordados
   - **Lacunas** de informação que precisam de esclarecimento

2. Faça perguntas de esclarecimento:
   - Qual é a principal mensagem que você quer que os leitores levem?
   - Há pontos específicos da pesquisa que você quer enfatizar?
   - Qual é o tamanho-alvo? (curto: 500-800 palavras, médio: 1000-1500, longo: 2000+)
   - Algum ponto que você quer excluir?

3. **Aguarde as respostas do usuário antes de prosseguir.**

### Passo 3: Propor Esboço

1. Crie um esboço estruturado incluindo:

   ```markdown
   # Esboço do Post de Blog: [Título]

   ## Meta Informações
   - **Público-Alvo**: [quem]
   - **Tom**: [estilo]
   - **Tamanho-Alvo**: [contagem de palavras]
   - **Mensagem Principal**: [mensagem-chave]

   ## Estrutura Proposta

   ### Gancho/Introdução
   - Ideia para gancho inicial
   - Contextualização
   - Declaração de tese

   ### Seção 1: [Título]
   - Ponto-chave A
   - Ponto-chave B
   - Evidência de apoio de [fonte]

   ### Seção 2: [Título]
   - Ponto-chave A
   - Ponto-chave B

   [Continue para todas as seções...]

   ### Conclusão
   - Resumo dos pontos-chave
   - Chamada para ação ou pensamento final

   ## Fontes a Citar
   - Fonte 1
   - Fonte 2
   ```

2. Apresente o esboço ao usuário e **peça aprovação ou modificações**.

### Passo 4: Salvar Esboço Aprovado

1. Quando o usuário aprovar o esboço, salve-o em `OUTLINE.md` na pasta do post de blog.

2. Confirme que o esboço foi salvo.

### Passo 5: Commit do Esboço (se estiver em repositório git)

1. Verifique se o diretório atual é um repositório git.

2. Se sim:
   - Stage os novos arquivos: pasta do post, resources e OUTLINE.md
   - Crie commit com a mensagem: `docs: Add outline for blog post - [nome-topico]`
   - Faça push para o remoto

3. Se não for um repositório git, pule este passo e informe o usuário.

### Passo 6: Escrever Rascunho

1. Com base no esboço aprovado, escreva o rascunho completo do post de blog.

2. Siga a estrutura de OUTLINE.md exatamente.

3. Inclua:
   - Introdução envolvente com gancho
   - Cabeçalhos de seção claros
   - Evidências e exemplos de apoio da pesquisa
   - Transições suaves entre seções
   - Conclusão sólida com mensagem principal
   - **Citações**: Todas as comparações, estatísticas, dados e afirmações factuais DEVEM citar a fonte original

4. Salve o rascunho como `draft-v0.1.md` na pasta do post de blog.

5. Formato:
   ```markdown
   # [Título do Post de Blog]

   *[Opcional: subtítulo ou slogan]*

   [Conteúdo completo com citações inline...]

   ---

   ## Referências
   - [1] Título da Fonte 1 - URL ou Citação
   - [2] Título da Fonte 2 - URL ou Citação
   - [3] Título da Fonte 3 - URL ou Citação
   ```

6. **Requisitos de Citação**:
   - Cada dado, estatística ou comparação DEVE ter uma citação inline
   - Use referências numeradas [1], [2], etc., ou citações nomeadas [Nome da Fonte]
   - Vincule citações à seção de Referências no final
   - Exemplo: "Estudos mostram que 65% dos desenvolvedores preferem TypeScript [1]"
   - Exemplo: "React supera Vue em velocidade de renderização em 20% [React Benchmarks 2024]"

### Passo 7: Commit do Rascunho (se estiver em repositório git)

1. Verifique se está em repositório git.

2. Se sim:
   - Stage o arquivo de rascunho
   - Crie commit com a mensagem: `docs: Add draft v0.1 for blog post - [nome-topico]`
   - Faça push para o remoto

3. Se não for repositório git, pule e informe o usuário.

### Passo 8: Apresentar Rascunho para Revisão

1. Apresente o conteúdo do rascunho ao usuário.

2. Peça feedback:
   - Impressão geral?
   - Seções que precisam de expansão ou redução?
   - Ajustes de tom necessários?
   - Informações faltando?
   - Edições ou reescritas específicas?

3. **Aguarde a resposta do usuário.**

### Passo 9: Iterar ou Finalizar

**Se o usuário solicitar alterações:**
1. Anote todas as modificações solicitadas
2. Volte ao Passo 6 com os seguintes ajustes:
   - Incremente o número de versão (v0.2, v0.3, etc.)
   - Incorpore todo o feedback
   - Salve como `draft-v[X.Y].md`
   - Repita os Passos 7-8

**Se o usuário aprovar:**
1. Confirme a versão final do rascunho
2. Opcionalmente renomeie para `final.md` se o usuário solicitar
3. Resuma o processo de criação do post de blog:
   - Total de versões criadas
   - Principais alterações entre versões
   - Contagem final de palavras
   - Arquivos criados

## Rastreamento de Versões

Todos os rascunhos são preservados com versionamento incremental:
- `draft-v0.1.md` - Rascunho inicial
- `draft-v0.2.md` - Após primeira rodada de feedback
- `draft-v0.3.md` - Após segunda rodada de feedback
- etc.

Isso permite acompanhar a evolução do post de blog e reverter se necessário.

## Estrutura de Arquivos de Saída

```
blog-posts/
└── AAAA-MM-DD-nome-topico/
    ├── resources/
    │   ├── source-1-nome.md
    │   ├── source-2-nome.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (se houver iterações)
    └── draft-v0.3.md (se houver mais iterações)
```

## Dicas para Qualidade

- **Gancho**: Comece com uma pergunta, fato surpreendente ou cenário relacionável
- **Fluxo**: Cada parágrafo deve se conectar ao próximo
- **Evidência**: Apoie afirmações com dados da pesquisa
- **Citações**: SEMPRE cite fontes para:
  - Todas as estatísticas e dados (ex: "De acordo com [Fonte], 75% de...")
  - Comparações entre produtos, serviços ou abordagens (ex: "X é 2x mais rápido que Y [Fonte]")
  - Afirmações factuais sobre tendências de mercado, descobertas de pesquisa ou benchmarks
  - Use citações inline com formato: [Nome da Fonte] ou [Autor, Ano]
- **Voz**: Mantenha tom consistente ao longo do texto
- **Tamanho**: Respeite a contagem de palavras-alvo
- **Legibilidade**: Use parágrafos curtos, listas onde apropriado
- **CTA**: Termine com uma chamada para ação clara ou pergunta que instigue reflexão

## Notas

- Sempre aguarde aprovação do usuário nos pontos de verificação indicados
- Preserve todas as versões de rascunho para histórico
- Use busca na web para informações atualizadas quando URLs forem fornecidas
- Se os recursos forem insuficientes, peça mais ao usuário ou sugira pesquisa adicional
- Adapte o tom com base no público-alvo (técnico, geral, empresarial, etc.)
