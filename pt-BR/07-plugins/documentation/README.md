<!-- i18n-source: 07-plugins/documentation/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin Documentation

Geração e manutenção abrangente de documentação para o seu projeto.

## Funcionalidades

✅ Geração de documentação de API
✅ Criação e atualização de README
✅ Sincronização de documentação
✅ Melhoria de comentários de código
✅ Geração de exemplos

## Instalação

```bash
/plugin install documentation
```

## O Que Está Incluído

### Slash Commands
- `/generate-api-docs` - Gerar documentação de API
- `/generate-readme` - Criar ou atualizar README
- `/sync-docs` - Sincronizar docs com alterações de código
- `/validate-docs` - Validar documentação

### Subagents
- `api-documenter` - Especialista em documentação de API
- `code-commentator` - Melhoria de comentários de código
- `example-generator` - Criação de exemplos de código

### Templates
- `api-endpoint.md` - Template de documentação de endpoint de API
- `function-docs.md` - Template de documentação de função
- `adr-template.md` - Template de Architecture Decision Record

### Servidores MCP
- Integração com GitHub para sincronização de documentação

## Uso

### Gerar Documentação de API
```
/generate-api-docs
```

### Criar README
```
/generate-readme
```

### Sincronizar Documentação
```
/sync-docs
```

### Validar Documentação
```
/validate-docs
```

## Requisitos

- Claude Code 1.0+
- Acesso ao GitHub (opcional)

## Exemplo de Fluxo de Trabalho

```
Usuário: /generate-api-docs

Claude:
1. Escaneia todos os endpoints de API em /src/api/
2. Delega para o Subagent api-documenter
3. Extrai assinaturas de função e JSDoc
4. Organiza por módulo/endpoint
5. Usa o template api-endpoint.md
6. Gera documentação markdown abrangente
7. Inclui exemplos em curl, JavaScript e Python

Resultado:
✅ Documentação de API gerada
📄 Arquivos criados:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Cobertura: 23/23 endpoints documentados
```

## Uso dos Templates

### Template de Endpoint de API
Use para documentar endpoints de API REST com exemplos completos.

### Template de Documentação de Função
Use para documentar funções/métodos individuais.

### Template ADR
Use para documentar decisões de arquitetura.

## Configuração

Configure seu token do GitHub para sincronização de documentação:
```bash
export GITHUB_TOKEN="seu_github_token"
```

## Melhores Práticas

- Mantenha a documentação próxima ao código
- Atualize os docs com as alterações de código
- Inclua exemplos práticos
- Valide regularmente
- Use templates para consistência
