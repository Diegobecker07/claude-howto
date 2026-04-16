<!-- i18n-source: 01-slash-commands/generate-api-docs.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
description: Criar documentação de API abrangente a partir do código-fonte
---

# Gerador de Documentação de API

Gere documentação de API através de:

1. Varredura de todos os arquivos em `/src/api/`
2. Extração de assinaturas de funções e comentários JSDoc
3. Organização por endpoint/módulo
4. Criação de markdown com exemplos
5. Inclusão de schemas de request/response
6. Adição de documentação de erros

Formato de saída:
- Arquivo Markdown em `/docs/api.md`
- Incluir exemplos curl para todos os endpoints
- Adicionar tipos TypeScript

---
**Última Atualização**: 9 de abril de 2026
