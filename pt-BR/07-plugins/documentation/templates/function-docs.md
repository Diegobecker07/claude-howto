<!-- i18n-source: 07-plugins/documentation/templates/function-docs.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Função: `functionName`

## Descrição
Breve descrição do que a função faz.

## Assinatura
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## Parâmetros

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| param1 | Type1 | Sim | Descrição de param1 |
| param2 | Type2 | Não | Descrição de param2 |

## Retorna
**Tipo**: `ReturnType`

Descrição do que é retornado.

## Lança
- `Error`: Quando uma entrada inválida é fornecida
- `TypeError`: Quando o tipo errado é passado

## Exemplos

### Uso Básico
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### Uso Avançado
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## Notas
- Notas adicionais ou avisos
- Considerações de desempenho
- Melhores práticas

## Veja Também
- [Função Relacionada](#)
- [Documentação de API](#)
