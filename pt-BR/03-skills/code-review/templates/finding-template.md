<!-- i18n-source: 03-skills/code-review/templates/finding-template.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Template de Achado de Revisão de Código

Use este template ao documentar cada problema encontrado durante a revisão de código.

---

## Problema: [TÍTULO]

### Severidade
- [ ] Crítico (bloqueia o deploy)
- [ ] Alto (deve corrigir antes do merge)
- [ ] Médio (deve corrigir em breve)
- [ ] Baixo (seria bom ter)

### Categoria
- [ ] Segurança
- [ ] Desempenho
- [ ] Qualidade de Código
- [ ] Manutenibilidade
- [ ] Testes
- [ ] Padrão de Projeto
- [ ] Documentação

### Localização
**Arquivo:** `src/components/UserCard.tsx`

**Linhas:** 45-52

**Função/Método:** `renderUserDetails()`

### Descrição do Problema

**O quê:** Descreva qual é o problema.

**Por que importa:** Explique o impacto e por que precisa ser corrigido.

**Comportamento atual:** Mostre o código ou comportamento problemático.

**Comportamento esperado:** Descreva o que deveria acontecer em vez disso.

### Exemplo de Código

#### Atual (Problemático)

```typescript
// Mostra o problema de query N+1
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query por usuário!
  renderUserPosts(posts);
});
```

#### Correção Sugerida

```typescript
// Otimizado com query JOIN
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### Análise de Impacto

| Aspecto | Impacto | Severidade |
|---------|---------|------------|
| Desempenho | 100+ queries para 20 usuários | Alto |
| Experiência do Usuário | Carregamento lento da página | Alto |
| Escalabilidade | Quebra em escala | Crítico |
| Manutenibilidade | Difícil de depurar | Médio |

### Problemas Relacionados

- Problema similar em `AdminUserList.tsx` linha 120
- PR relacionado: #456
- Issue relacionada: #789

### Recursos Adicionais

- [Problema de Query N+1](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Documentação de JOIN de Banco de Dados](https://docs.example.com/joins)

### Notas do Revisor

- Este é um padrão comum neste código-fonte
- Considere adicionar isso ao guia de estilo de código
- Pode valer a pena criar uma função auxiliar

### Resposta do Autor (para feedback)

*A ser preenchido pelo autor do código:*

- [ ] Correção implementada no commit: `abc123`
- [ ] Status da correção: Completo / Em Progresso / Precisa de Discussão
- [ ] Perguntas ou preocupações: (descreva)

---

## Estatísticas de Achados (para o Revisor)

Ao revisar múltiplos achados, rastreie:

- **Total de Problemas Encontrados:** X
- **Críticos:** X
- **Altos:** X
- **Médios:** X
- **Baixos:** X

**Recomendação:** ✅ Aprovar / ⚠️ Solicitar Alterações / 🔄 Precisa de Discussão

**Qualidade Geral do Código:** 1-5 estrelas
