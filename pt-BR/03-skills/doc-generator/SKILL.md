<!-- i18n-source: 03-skills/doc-generator/SKILL.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: api-documentation-generator
description: Gerar documentação de API abrangente e precisa a partir do código-fonte. Usar ao criar ou atualizar documentação de API, gerar especificações OpenAPI, ou quando usuários mencionam docs de API, endpoints ou documentação.
---

# Skill de Gerador de Documentação de API

## Gera

- Especificações OpenAPI/Swagger
- Documentação de endpoints de API
- Exemplos de uso de SDK
- Guias de integração
- Referências de códigos de erro
- Guias de autenticação

## Estrutura da Documentação

### Para Cada Endpoint

```markdown
## GET /api/v1/users/:id

### Descrição
Breve explicação do que este endpoint faz

### Parâmetros

| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id | string | Sim | ID do usuário |

### Resposta

**200 Sucesso**
```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**404 Não Encontrado**
```json
{
  "error": "USER_NOT_FOUND",
  "message": "O usuário não existe"
}
```

### Exemplos

**cURL**
```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \
  -H "Authorization: Bearer SEU_TOKEN"
```

**JavaScript**
```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**
```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```
```
