<!-- i18n-source: 07-plugins/documentation/templates/api-endpoint.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# [MÉTODO] /api/v1/[endpoint]

## Descrição
Breve explicação do que este endpoint faz.

## Autenticação
Método de autenticação necessário (ex.: Bearer token).

## Parâmetros

### Parâmetros de Rota
| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| id | string | Sim | ID do recurso |

### Parâmetros de Query
| Nome | Tipo | Obrigatório | Descrição |
|------|------|-------------|-----------|
| page | integer | Não | Número da página (padrão: 1) |
| limit | integer | Não | Itens por página (padrão: 20) |

### Corpo da Requisição
```json
{
  "field": "value"
}
```

## Respostas

### 200 OK
```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "Example"
  }
}
```

### 400 Bad Request
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input"
  }
}
```

### 404 Not Found
```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found"
  }
}
```

## Exemplos

### cURL
```bash
curl -X GET "https://api.example.com/api/v1/endpoint" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json"
```

### JavaScript
```javascript
const response = await fetch('/api/v1/endpoint', {
  headers: {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json'
  }
});
const data = await response.json();
```

### Python
```python
import requests

response = requests.get(
    'https://api.example.com/api/v1/endpoint',
    headers={'Authorization': 'Bearer token'}
)
data = response.json()
```

## Limites de Taxa
- 1000 requisições por hora para usuários autenticados
- 100 requisições por hora para endpoints públicos

## Endpoints Relacionados
- [GET /api/v1/related](#)
- [POST /api/v1/related](#)
