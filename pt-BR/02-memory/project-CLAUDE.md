<!-- i18n-source: 02-memory/project-CLAUDE.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Configuração do Projeto

## Visão Geral do Projeto
- **Nome**: Plataforma de E-commerce
- **Stack Tecnológica**: Node.js, PostgreSQL, React 18, Docker
- **Tamanho da Equipe**: 5 desenvolvedores
- **Prazo**: Q4 2025

## Arquitetura
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## Padrões de Desenvolvimento

### Estilo de Código
- Usar Prettier para formatação
- Usar ESLint com config airbnb
- Comprimento máximo de linha: 100 caracteres
- Usar indentação de 2 espaços

### Convenções de Nomenclatura
- **Arquivos**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Funções/Variáveis**: camelCase (getUserById)
- **Constantes**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Tabelas de Banco de Dados**: snake_case (user_accounts)

### Fluxo Git
- Nomes de branch: `feature/descricao` ou `fix/descricao`
- Mensagens de commit: Seguir conventional commits
- PR obrigatório antes do merge
- Todas as verificações CI/CD devem passar
- Mínimo de 1 aprovação necessária

### Requisitos de Testes
- Cobertura mínima de código: 80%
- Todos os caminhos críticos devem ter testes
- Usar Jest para testes unitários
- Usar Cypress para testes E2E
- Nomes de arquivos de teste: `*.test.ts` ou `*.spec.ts`

### Padrões de API
- Apenas endpoints RESTful
- Request/response em JSON
- Usar códigos de status HTTP corretamente
- Versionar endpoints de API: `/api/v1/`
- Documentar todos os endpoints com exemplos

### Banco de Dados
- Usar migrations para mudanças de schema
- Nunca hardcode credenciais
- Usar connection pooling
- Ativar log de queries em desenvolvimento
- Backups regulares obrigatórios

### Implantação
- Implantação baseada em Docker
- Orquestração com Kubernetes
- Estratégia de implantação blue-green
- Rollback automático em caso de falha
- Migrations de banco de dados executam antes do deploy

## Comandos Comuns

| Comando | Finalidade |
|---------|-----------|
| `npm run dev` | Iniciar servidor de desenvolvimento |
| `npm test` | Executar suíte de testes |
| `npm run lint` | Verificar estilo de código |
| `npm run build` | Build para produção |
| `npm run migrate` | Executar migrations de banco de dados |

## Contatos da Equipe
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## Problemas Conhecidos e Soluções Alternativas
- Pooling de conexão PostgreSQL limitado a 20 durante horários de pico
- Solução: Implementar fila de queries
- Problemas de compatibilidade com Safari 14 e async generators
- Solução: Usar transpilador Babel

## Projetos Relacionados
- Dashboard de Analytics: `/projects/analytics`
- App Mobile: `/projects/mobile`
- Painel Administrativo: `/projects/admin`

---
**Última Atualização**: 9 de abril de 2026
