<!-- i18n-source: 02-memory/personal-CLAUDE.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Minhas Preferências de Desenvolvimento

## Sobre Mim
- **Nível de Experiência**: 8 anos de desenvolvimento full-stack
- **Linguagens Preferidas**: TypeScript, Python
- **Estilo de Comunicação**: Direto, com exemplos
- **Estilo de Aprendizado**: Diagramas visuais com código

## Preferências de Código

### Tratamento de Erros
Prefiro tratamento explícito de erros com blocos try-catch e mensagens de erro significativas.
Evite erros genéricos. Sempre registre erros para depuração.

### Comentários
Use comentários para o POR QUÊ, não para o QUÊ. O código deve ser autodocumentado.
Comentários devem explicar lógica de negócio ou decisões não óbvias.

### Testes
Prefiro TDD (desenvolvimento orientado a testes).
Escreva testes primeiro, depois a implementação.
Foque no comportamento, não nos detalhes de implementação.

### Arquitetura
Prefiro design modular e fracamente acoplado.
Use injeção de dependência para testabilidade.
Separe responsabilidades (Controllers, Services, Repositories).

## Preferências de Depuração
- Usar console.log com prefixo: `[DEBUG]`
- Incluir contexto: nome da função, variáveis relevantes
- Usar stack traces quando disponíveis
- Sempre incluir timestamps nos logs

## Comunicação
- Explicar conceitos complexos com diagramas
- Mostrar exemplos concretos antes de explicar a teoria
- Incluir trechos de código antes/depois
- Resumir pontos-chave ao final

## Organização do Projeto
Organizo meus projetos assim:
```
project/
  ├── src/
  │   ├── api/
  │   ├── services/
  │   ├── models/
  │   └── utils/
  ├── tests/
  ├── docs/
  └── docker/
```

## Ferramentas
- **IDE**: VS Code com keybindings vim
- **Terminal**: Zsh com Oh-My-Zsh
- **Formatação**: Prettier (comprimento de linha 100 chars)
- **Linter**: ESLint com config airbnb
- **Framework de Teste**: Jest com React Testing Library

---
**Última Atualização**: 9 de abril de 2026
