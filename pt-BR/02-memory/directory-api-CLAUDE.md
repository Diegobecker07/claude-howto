<!-- i18n-source: 02-memory/directory-api-CLAUDE.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Padrões do Módulo API

Este arquivo substitui o CLAUDE.md raiz para tudo em /src/api/

## Padrões Específicos de API

### Validação de Request
- Usar Zod para validação de schema
- Sempre validar entrada
- Retornar 400 com erros de validação
- Incluir detalhes de erros por campo

### Autenticação
- Todos os endpoints requerem token JWT
- Token no header Authorization
- Token expira após 24 horas
- Implementar mecanismo de refresh token

### Formato de Resposta

Todas as respostas devem seguir esta estrutura:

```json
{
  "success": true,
  "data": { /* dados reais */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

Respostas de erro:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Mensagem para o usuário",
    "details": { /* erros por campo */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### Paginação
- Usar paginação baseada em cursor (não offset)
- Incluir booleano `hasMore`
- Limitar tamanho máximo de página a 100
- Tamanho de página padrão: 20

### Rate Limiting
- 1000 requests por hora para usuários autenticados
- 100 requests por hora para endpoints públicos
- Retornar 429 quando excedido
- Incluir header retry-after

### Cache
- Usar Redis para cache de sessão
- Duração padrão de cache: 5 minutos
- Invalidar em operações de escrita
- Marcar chaves de cache com tipo de recurso

---
**Última Atualização**: 9 de abril de 2026
