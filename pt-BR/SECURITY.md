<!-- i18n-source: SECURITY.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# Política de Segurança

## Visão Geral

A segurança do projeto Claude How To é importante para nós. Este documento descreve nossas práticas de segurança e explica como relatar vulnerabilidades de segurança de forma responsável.

## Versões Suportadas

Fornecemos atualizações de segurança para as seguintes versões:

| Versão | Status | Suporte Até |
|--------|--------|-------------|
| Mais recente (main) | ✅ Ativa | Atual + 6 meses |
| Versões 1.x | ✅ Ativa | Até a próxima versão principal |

**Nota**: Como um projeto de guia educacional, focamos em manter as melhores práticas atuais e a segurança da documentação em vez do suporte tradicional de versões. As atualizações são aplicadas diretamente ao branch main.

## Práticas de Segurança

### Segurança do Código

1. **Gerenciamento de Dependências**
   - Todas as dependências Python são fixadas em `requirements.txt`
   - Atualizações regulares via dependabot e revisão manual
   - Varredura de segurança com Bandit em cada commit
   - Hooks pré-commit para verificações de segurança

2. **Qualidade do Código**
   - Linting com Ruff detecta problemas comuns
   - Verificação de tipos com mypy previne vulnerabilidades relacionadas a tipos
   - Hooks pré-commit aplicam padrões
   - Todas as mudanças revisadas antes do merge

3. **Controle de Acesso**
   - Proteção de branch no branch `main`
   - Revisões necessárias antes do merge
   - Verificações de status devem passar antes do merge
   - Acesso de escrita limitado ao repositório

### Segurança da Documentação

1. **Sem Segredos nos Exemplos**
   - Todas as chaves de API nos exemplos são placeholders
   - Credenciais nunca são hardcoded
   - Arquivos `.env.example` mostram as variáveis necessárias
   - Avisos claros sobre gerenciamento de segredos

2. **Melhores Práticas de Segurança**
   - Exemplos demonstram padrões seguros
   - Avisos de segurança destacados na documentação
   - Links para guias de segurança oficiais
   - Tratamento de credenciais discutido nas seções relevantes

3. **Revisão de Conteúdo**
   - Toda documentação revisada para issues de segurança
   - Considerações de segurança nas diretrizes de contribuição
   - Validação de links externos e referências

### Segurança de Dependências

1. **Varredura**
   - Bandit varre todo o código Python em busca de vulnerabilidades
   - Verificações de vulnerabilidade de dependências via alertas de segurança do GitHub
   - Auditorias de segurança manuais regulares

2. **Atualizações**
   - Patches de segurança aplicados prontamente
   - Versões principais avaliadas cuidadosamente
   - Changelog inclui atualizações relacionadas à segurança

3. **Transparência**
   - Atualizações de segurança documentadas nos commits
   - Divulgações de vulnerabilidades tratadas de forma responsável
   - Advisories de segurança públicos quando apropriado

## Relatando uma Vulnerabilidade

### Issues de Segurança que nos Importam

Agradecemos relatórios sobre:
- **Vulnerabilidades de código** em scripts ou exemplos
- **Vulnerabilidades de dependências** em pacotes Python
- **Issues de criptografia** em qualquer exemplo de código
- **Falhas de autenticação/autorização** na documentação
- **Riscos de exposição de dados** em exemplos de configuração
- **Vulnerabilidades de injeção** (SQL, comando, etc.)
- **Issues SSRF/XXE/Path traversal**

### Issues de Segurança Fora do Escopo

Estes estão fora do escopo deste projeto:
- Vulnerabilidades no próprio Claude Code (reporte para a Anthropic)
- Issues com serviços externos ou bibliotecas (reporte para o upstream)
- Engenharia social ou educação do usuário (não aplicável a este guia)
- Vulnerabilidades teóricas sem prova de conceito
- Vulnerabilidades em dependências relatadas pelos canais oficiais

## Como Relatar

### Relatório Privado (Preferido)

**Para issues de segurança sensíveis, use o relatório privado de vulnerabilidades do GitHub:**

1. Acesse: https://github.com/luongnv89/claude-howto/security/advisories
2. Clique em "Report a vulnerability"
3. Preencha os detalhes da vulnerabilidade
4. Inclua:
   - Descrição clara da vulnerabilidade
   - Componente afetado (arquivo, seção, exemplo)
   - Impacto potencial
   - Passos para reproduzir (se aplicável)
   - Correção sugerida (se tiver uma)

**O que acontece em seguida:**
- Reconheceremos o recebimento dentro de 48 horas
- Investigaremos e avaliaremos a severidade
- Trabalharemos com você para desenvolver uma correção
- Coordenaremos o cronograma de divulgação
- Daremos crédito a você no advisory de segurança (a menos que prefira anonimato)

### Relatório Público

Para issues não sensíveis ou aquelas já públicas:

1. **Abra uma Issue do GitHub** com a label `security`
2. Inclua:
   - Título: `[SECURITY]` seguido de breve descrição
   - Descrição detalhada
   - Arquivo ou seção afetada
   - Impacto potencial
   - Correção sugerida

## Processo de Resposta a Vulnerabilidades

### Avaliação (24 horas)

1. Reconhecemos o recebimento do relatório
2. Avaliamos a severidade usando [CVSS v3.1](https://www.first.org/cvss/v3.1/specification-document)
3. Determinamos se está no escopo
4. Entramos em contato com você com a avaliação inicial

### Desenvolvimento (1-7 dias)

1. Desenvolvemos uma correção
2. Revisamos e testamos a correção
3. Criamos um advisory de segurança
4. Preparamos as notas de versão

### Divulgação (varia por severidade)

**Crítico (CVSS 9.0-10.0)**
- Correção lançada imediatamente
- Advisory público emitido
- Aviso de 24 horas aos relatores

**Alto (CVSS 7.0-8.9)**
- Correção lançada em 48-72 horas
- Aviso de 5 dias aos relatores
- Advisory público no lançamento

**Médio (CVSS 4.0-6.9)**
- Correção lançada na próxima atualização regular
- Advisory público no lançamento

**Baixo (CVSS 0.1-3.9)**
- Correção incluída na próxima atualização regular
- Advisory no lançamento

### Publicação

Publicamos advisories de segurança que incluem:
- Descrição da vulnerabilidade
- Componentes afetados
- Avaliação de severidade (pontuação CVSS)
- Versão da correção
- Soluções alternativas (se aplicável)
- Crédito ao relator (com permissão)

## Melhores Práticas para Relatores

### Antes de Relatar

- **Verifique o issue**: Você consegue reproduzi-lo de forma consistente?
- **Pesquise issues existentes**: Já foi relatado?
- **Verifique a documentação**: Há orientações sobre uso seguro?
- **Teste a correção**: Sua correção sugerida funciona?

### Ao Relatar

- **Seja específico**: Forneça caminhos de arquivo e números de linha exatos
- **Inclua contexto**: Por que isso é uma issue de segurança?
- **Mostre o impacto**: O que um atacante poderia fazer?
- **Forneça passos**: Como podemos reproduzir?
- **Sugira correções**: Como você corrigiria isso?

### Após Relatar

- **Seja paciente**: Temos recursos limitados
- **Seja responsivo**: Responda perguntas de acompanhamento rapidamente
- **Mantenha confidencialidade**: Não divulgue publicamente antes da correção
- **Respeite a coordenação**: Siga nosso cronograma de divulgação

## Cabeçalhos e Configuração de Segurança

### Segurança do Repositório

- **Proteção de branch**: Branch main requer 2 aprovações para mudanças
- **Verificações de status**: Todas as verificações de CI/CD devem passar
- **CODEOWNERS**: Revisores designados para arquivos-chave
- **Commits assinados**: Recomendado para colaboradores

### Segurança de Desenvolvimento

```bash
# Instalar hooks pré-commit
pre-commit install

# Executar varreduras de segurança localmente
bandit -c pyproject.toml -r scripts/
mypy scripts/ --ignore-missing-imports
ruff check scripts/
```

### Segurança de Dependências

```bash
# Verificar vulnerabilidades conhecidas
pip install safety
safety check

# Ou usar pip-audit
pip install pip-audit
pip-audit
```

## Diretrizes de Segurança para Colaboradores

### Ao Escrever Exemplos

1. **Nunca hardcode segredos**
   ```python
   # ❌ Ruim
   api_key = "sk-1234567890"

   # ✅ Bom
   api_key = os.getenv("API_KEY")
   ```

2. **Avise sobre implicações de segurança**
   ```markdown
   ⚠️ **Nota de Segurança**: Nunca faça commit de arquivos `.env` para o git.
   Adicione ao `.gitignore` imediatamente.
   ```

3. **Use padrões seguros**
   - Habilite autenticação por padrão
   - Use HTTPS onde aplicável
   - Valide e sanitize entradas
   - Use queries parametrizadas

4. **Documente considerações de segurança**
   - Explique por que a segurança importa
   - Mostre padrões seguros vs. inseguros
   - Faça link para fontes autoritativas
   - Inclua avisos com destaque

### Ao Revisar Contribuições

1. **Verifique segredos expostos**
   - Varra padrões comuns (api_key=, password=)
   - Revise arquivos de configuração
   - Verifique variáveis de ambiente

2. **Verifique práticas de codificação segura**
   - Sem credenciais hardcoded
   - Validação adequada de entrada
   - Autenticação/autorização segura
   - Tratamento seguro de arquivos

3. **Teste implicações de segurança**
   - Isso pode ser mal utilizado?
   - Qual é o pior caso?
   - Há casos extremos?

## Recursos de Segurança

### Padrões Oficiais
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Calculadora CVSS](https://www.first.org/cvss/calculator/3.1)

### Segurança Python
- [Advisories de Segurança Python](https://www.python.org/dev/security/)
- [Segurança PyPI](https://pypi.org/help/#security)
- [Documentação Bandit](https://bandit.readthedocs.io/)

### Gerenciamento de Dependências
- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [Alertas de Segurança do GitHub](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

### Segurança Geral
- [Anthropic Security](https://www.anthropic.com/)
- [Melhores Práticas de Segurança do GitHub](https://docs.github.com/en/code-security)

## Arquivo de Advisories de Segurança

Advisories de segurança anteriores estão disponíveis na aba [GitHub Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories).

## Contato

Para perguntas relacionadas à segurança ou para discutir práticas de segurança:

1. **Relatório de Segurança Privado**: Use o relatório privado de vulnerabilidades do GitHub
2. **Perguntas Gerais de Segurança**: Abra uma discussão com a tag `[SECURITY]`
3. **Feedback sobre Política de Segurança**: Crie uma issue com a label `security`

## Agradecimentos

Agradecemos aos pesquisadores de segurança e membros da comunidade que ajudam a manter este projeto seguro. Colaboradores que relatam vulnerabilidades de forma responsável serão reconhecidos em nossos advisories de segurança (a menos que prefiram anonimato).

## Atualizações de Política

Esta política de segurança é revisada e atualizada:
- Quando novas vulnerabilidades são descobertas
- Quando as melhores práticas de segurança evoluem
- Quando o escopo do projeto muda
- Anualmente como mínimo

**Última Atualização**: Janeiro de 2026
**Próxima Revisão**: Janeiro de 2027

---

Obrigado por ajudar a manter o Claude How To seguro! 🔒
