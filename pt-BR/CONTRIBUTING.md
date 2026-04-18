<!-- i18n-source: CONTRIBUTING.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Contribuindo para o Claude How To

Obrigado pelo seu interesse em contribuir para este projeto! Este guia irá ajudá-lo a entender como contribuir de forma eficaz.

## Sobre Este Projeto

Claude How To é um guia visual e orientado a exemplos sobre o Claude Code. Fornecemos:
- **Diagramas Mermaid** explicando como os recursos funcionam
- **Templates prontos para produção** que você pode usar imediatamente
- **Exemplos do mundo real** com contexto e melhores práticas
- **Caminhos de aprendizado progressivos** do iniciante ao avançado

## Tipos de Contribuições

### 1. Novos Exemplos ou Templates
Adicione exemplos para recursos existentes (slash commands, skills, hooks, etc.):
- Código pronto para copiar e colar
- Explicações claras de como funciona
- Casos de uso e benefícios
- Dicas de solução de problemas

### 2. Melhorias de Documentação
- Esclarecer seções confusas
- Corrigir erros de digitação e gramática
- Adicionar informações ausentes
- Melhorar exemplos de código

### 3. Guias de Recursos
Crie guias para novos recursos do Claude Code:
- Tutoriais passo a passo
- Diagramas de arquitetura
- Padrões comuns e anti-padrões
- Fluxos de trabalho do mundo real

### 4. Relatórios de Bugs
Relate problemas que você encontrar:
- Descreva o que você esperava
- Descreva o que realmente aconteceu
- Inclua passos para reproduzir
- Adicione versão relevante do Claude Code e SO

### 5. Feedback e Sugestões
Ajude a melhorar o guia:
- Sugira melhores explicações
- Aponte lacunas na cobertura
- Recomende novas seções ou reorganização

## Primeiros Passos

### 1. Fork e Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. Criar um Branch
Use um nome de branch descritivo:
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. Configurar seu Ambiente

Os hooks pré-commit executam as mesmas verificações que o CI localmente antes de cada commit. As cinco verificações devem passar antes que um PR seja aceito.

**Dependências necessárias:**

```bash
# Ferramentas Python (uv é o gerenciador de pacotes deste projeto)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Linter de Markdown (Node.js)
npm install -g markdownlint-cli

# Validador de diagramas Mermaid (Node.js)
npm install -g @mermaid-js/mermaid-cli

# Instalar pré-commit e ativar hooks
uv pip install pre-commit
pre-commit install
```

**Verificar sua configuração:**

```bash
pre-commit run --all-files
```

Os hooks que executam em cada commit são:

| Hook | O que verifica |
|------|----------------|
| `markdown-lint` | Formatação e estrutura Markdown |
| `cross-references` | Links relativos, âncoras, code fences |
| `mermaid-syntax` | Todos os blocos ` ```mermaid ` são parseados corretamente |
| `link-check` | URLs externas são acessíveis |
| `build-epub` | EPUB gerado sem erros (em mudanças de `.md`) |

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
├── scripts/                # Scripts de build e utilitários
└── README.md               # Guia principal
```

## Como Contribuir com Exemplos

### Adicionando um Slash Command
1. Crie um arquivo `.md` em `01-slash-commands/`
2. Inclua:
   - Descrição clara do que faz
   - Casos de uso
   - Instruções de instalação
   - Exemplos de uso
   - Dicas de personalização
3. Atualize `01-slash-commands/README.md`

### Adicionando uma Skill
1. Crie um diretório em `03-skills/`
2. Inclua:
   - `SKILL.md` - Documentação principal
   - `scripts/` - Scripts auxiliares se necessário
   - `templates/` - Templates de prompt
   - Exemplo de uso no README
3. Atualize `03-skills/README.md`

### Adicionando um Subagent
1. Crie um arquivo `.md` em `04-subagents/`
2. Inclua:
   - Propósito e capacidades do agente
   - Estrutura do system prompt
   - Casos de uso de exemplo
   - Exemplos de integração
3. Atualize `04-subagents/README.md`

### Adicionando Configuração MCP
1. Crie um arquivo `.json` em `05-mcp/`
2. Inclua:
   - Explicação da configuração
   - Variáveis de ambiente necessárias
   - Instruções de configuração
   - Exemplos de uso
3. Atualize `05-mcp/README.md`

### Adicionando um Hook
1. Crie um arquivo `.sh` em `06-hooks/`
2. Inclua:
   - Shebang e descrição
   - Comentários claros explicando a lógica
   - Tratamento de erros
   - Considerações de segurança
3. Atualize `06-hooks/README.md`

## Diretrizes de Escrita

### Estilo Markdown
- Use cabeçalhos claros (H2 para seções, H3 para subseções)
- Mantenha parágrafos curtos e focados
- Use marcadores para listas
- Inclua blocos de código com especificação de linguagem
- Adicione linhas em branco entre seções

### Exemplos de Código
- Torne os exemplos prontos para copiar e colar
- Comente a lógica não óbvia
- Inclua versões simples e avançadas
- Mostre casos de uso do mundo real
- Destaque problemas potenciais

### Documentação
- Explique o "porquê" não apenas o "o quê"
- Inclua pré-requisitos
- Adicione seções de solução de problemas
- Faça links para tópicos relacionados
- Mantenha amigável para iniciantes

### JSON/YAML
- Use indentação adequada (2 ou 4 espaços de forma consistente)
- Adicione comentários explicando a configuração
- Inclua exemplos de validação

### Diagramas
- Use Mermaid quando possível
- Mantenha os diagramas simples e legíveis
- Inclua descrições abaixo dos diagramas
- Faça links para seções relevantes

## Diretrizes de Commit

Siga o formato conventional commit:
```
type(scope): description

[corpo opcional]
```

Tipos:
- `feat`: Nova funcionalidade ou exemplo
- `fix`: Correção de bug
- `docs`: Mudanças de documentação
- `refactor`: Reestruturação de código
- `style`: Mudanças de formatação
- `test`: Adições ou mudanças de testes
- `chore`: Build, dependências, etc.

Exemplos:
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## Antes de Enviar

### Checklist
- [ ] O código segue o estilo e as convenções do projeto
- [ ] Novos exemplos incluem documentação clara
- [ ] Arquivos README estão atualizados (tanto locais quanto raiz)
- [ ] Sem informações sensíveis (chaves de API, credenciais)
- [ ] Exemplos são testados e funcionando
- [ ] Links são verificados e corretos
- [ ] Arquivos têm permissões adequadas (scripts são executáveis)
- [ ] A mensagem de commit é clara e descritiva

### Teste Local
```bash
# Executar todas as verificações pré-commit (mesmas verificações que o CI)
pre-commit run --all-files

# Revisar suas mudanças
git diff
```

## Processo de Pull Request

1. **Crie PR com descrição clara**:
   - O que isso adiciona/corrige?
   - Por que é necessário?
   - Issues relacionadas (se houver)

2. **Inclua detalhes relevantes**:
   - Novo recurso? Inclua casos de uso
   - Documentação? Explique as melhorias
   - Exemplos? Mostre antes/depois

3. **Faça link para issues**:
   - Use `Closes #123` para fechar automaticamente issues relacionadas

4. **Seja paciente com revisões**:
   - Mantenedores podem sugerir melhorias
   - Itere com base no feedback
   - A decisão final cabe aos mantenedores

## Processo de Revisão de Código

Os revisores verificarão:
- **Precisão**: Funciona conforme descrito?
- **Qualidade**: Está pronto para produção?
- **Consistência**: Segue os padrões do projeto?
- **Documentação**: É claro e completo?
- **Segurança**: Há alguma vulnerabilidade?

## Reportando Issues

### Relatórios de Bug
Inclua:
- Versão do Claude Code
- Sistema operacional
- Passos para reproduzir
- Comportamento esperado
- Comportamento real
- Screenshots se aplicável

### Pedidos de Funcionalidade
Inclua:
- Caso de uso ou problema sendo resolvido
- Solução proposta
- Alternativas que você considerou
- Contexto adicional

### Issues de Documentação
Inclua:
- O que é confuso ou está faltando
- Melhorias sugeridas
- Exemplos ou referências

## Políticas do Projeto

### Informações Sensíveis
- Nunca faça commit de chaves de API, tokens ou credenciais
- Use valores de placeholder em exemplos
- Inclua `.env.example` para arquivos de configuração
- Documente variáveis de ambiente necessárias

### Qualidade do Código
- Mantenha os exemplos focados e legíveis
- Evite soluções excessivamente engenhosas
- Inclua comentários para lógica não óbvia
- Teste completamente antes de enviar

### Propriedade Intelectual
- Conteúdo original de propriedade do autor
- Projeto usa licença educacional
- Respeite direitos autorais existentes
- Forneça atribuição quando necessário

## Obtendo Ajuda

- **Perguntas**: Abra uma discussão no GitHub Issues
- **Ajuda Geral**: Verifique a documentação existente
- **Ajuda de Desenvolvimento**: Revise exemplos similares
- **Revisão de Código**: Marque os mantenedores nos PRs

## Reconhecimento

Os colaboradores são reconhecidos em:
- Seção de Colaboradores do README.md
- Página de colaboradores do GitHub
- Histórico de commits

## Segurança

Ao contribuir com exemplos e documentação, por favor siga práticas de codificação segura:

- **Nunca hardcode segredos ou chaves de API** - Use variáveis de ambiente
- **Avise sobre implicações de segurança** - Destaque riscos potenciais
- **Use padrões seguros** - Habilite recursos de segurança por padrão
- **Valide entradas** - Mostre validação e saneamento adequados de entrada
- **Inclua notas de segurança** - Documente considerações de segurança

Para issues de segurança, veja [SECURITY.md](SECURITY.md) para nosso processo de relato de vulnerabilidades.

## Código de Conduta

Estamos comprometidos em fornecer uma comunidade acolhedora e inclusiva. Por favor, leia [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) para nossos padrões completos da comunidade.

Em resumo:
- Seja respeitoso e inclusivo
- Aceite feedback com graciosidade
- Ajude outros a aprender e crescer
- Evite assédio ou discriminação
- Reporte issues aos mantenedores

Todos os colaboradores devem cumprir este código e tratar uns aos outros com gentileza e respeito.

## Licença

Ao contribuir para este projeto, você concorda que suas contribuições serão licenciadas sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## Perguntas?

- Verifique o [README](README.md)
- Revise [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- Veja os exemplos existentes
- Abra uma issue para discussão

Obrigado por contribuir! 🙏

---
**Última Atualização**: 9 de Abril de 2026
