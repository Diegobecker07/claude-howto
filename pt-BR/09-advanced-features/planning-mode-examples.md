<!-- i18n-source: 09-advanced-features/planning-mode-examples.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Exemplos de Modo de Planejamento

Exemplos do mundo real demonstrando o uso efetivo do modo de planejamento no Claude Code.

## Exemplo 1: Construindo uma API REST

### Sem Modo de Planejamento

```
Usuário: Construa uma API REST para um blog

Claude: Vou criar a API...
[Começa a codar imediatamente, pode perder requisitos]
```

### Com Modo de Planejamento

```
Usuário: /plan Construa uma API REST para um blog

Claude: Deixa eu criar um plano abrangente para a API do blog.

## Plano de Implementação da API REST do Blog

### Fase 1: Configuração do Projeto (15 min)
1. Inicializar projeto Node.js com Express
2. Configurar TypeScript
3. Instalar dependências (express, pg, jwt, joi)
4. Configurar variáveis de ambiente
5. Configurar estrutura do projeto

### Fase 2: Camada de Banco de Dados (30 min)
6. Projetar schema do banco de dados
   - tabela users (id, email, password_hash, created_at)
   - tabela posts (id, user_id, title, content, published, created_at, updated_at)
   - tabela comments (id, post_id, user_id, content, created_at)
7. Criar arquivos de migration
8. Configurar connection pool do banco de dados
9. Implementar modelos do banco de dados

### Fase 3: Autenticação (45 min)
10. Implementar endpoint de registro de usuário
11. Implementar endpoint de login com JWT
12. Criar middleware de autenticação
13. Adicionar hash de senha com bcrypt
14. Implementar lógica de refresh de token

### Fase 4: API de Posts (40 min)
15. GET /api/posts — Listar todos os posts publicados (com paginação)
16. GET /api/posts/:id — Obter post único
17. POST /api/posts — Criar novo post (requer autenticação)
18. PUT /api/posts/:id — Atualizar post (requer autenticação, verificação de propriedade)
19. DELETE /api/posts/:id — Deletar post (requer autenticação, verificação de propriedade)
20. GET /api/users/:id/posts — Obter posts do usuário

### Fase 5: API de Comentários (30 min)
21. GET /api/posts/:id/comments — Obter comentários do post
22. POST /api/posts/:id/comments — Adicionar comentário (requer autenticação)
23. DELETE /api/comments/:id — Deletar comentário (requer autenticação, verificação de propriedade)

### Fase 6: Validação e Tratamento de Erros (30 min)
24. Adicionar validação de requisições com Joi
25. Implementar tratamento global de erros
26. Adicionar sanitização de entrada
27. Implementar rate limiting

### Fase 7: Testes (60 min)
28. Escrever testes unitários para modelos
29. Escrever testes de integração para endpoints de autenticação
30. Escrever testes de integração para endpoints de posts
31. Escrever testes de integração para endpoints de comentários
32. Atingir cobertura de código ≥80%

### Fase 8: Documentação e Deploy (30 min)
33. Gerar documentação da API com Swagger
34. Criar README com instruções de configuração
35. Adicionar configuração do Docker
36. Configurar pipeline CI/CD

**Tempo Estimado**: 4,5 horas
**Arquivos a Criar**: ~25
**Tecnologias-Chave**: Express, PostgreSQL, JWT, TypeScript

**Resumo dos Endpoints da API**:
- Autenticação: 2 endpoints
- Posts: 6 endpoints
- Comentários: 3 endpoints
- Total: 11 endpoints

Pronto para prosseguir? (sim/não/modificar)

Usuário: sim

Claude: Iniciando Fase 1: Configuração do Projeto...
[Implementa cada fase sistematicamente]
```

## Exemplo 2: Migração de Banco de Dados

### Com Modo de Planejamento

```
Usuário: /plan Migrar do MongoDB para o PostgreSQL

Claude: Esta é uma migração complexa. Deixa eu criar um plano detalhado.

## Plano de Migração do MongoDB para o PostgreSQL

### Fase 1: Análise e Preparação (Dia 1)
1. Analisar o schema atual do MongoDB
2. Identificar relacionamentos e restrições de dados
3. Documentar volume atual de dados e taxa de crescimento
4. Projetar schema equivalente no PostgreSQL
5. Planejar mapeamentos de tipos de dados
6. Identificar possíveis desafios de migração

### Fase 2: Configuração do PostgreSQL (Dia 1)
7. Configurar banco de dados PostgreSQL
8. Criar schema com tabelas, índices, restrições
9. Configurar connection pooling
10. Configurar estratégia de backup

### Fase 3: Implementação de Dupla Escrita (Dias 2-3)
11. Criar camada de abstração do banco de dados
12. Implementar dupla escrita para ambos os bancos de dados
13. Adicionar verificações de consistência de dados
14. Fazer deploy da dupla escrita para staging
15. Monitorar problemas

### Fase 4: Migração de Dados (Dia 4)
16. Criar scripts de exportação de dados para MongoDB
17. Criar scripts de importação de dados para PostgreSQL
18. Implementar lógica de transformação de dados
19. Executar migração inicial em cópia dos dados de produção
20. Validar integridade dos dados migrados

### Fase 5: Cutover Gradual (Dias 5-7)
21. Ativar dupla escrita em produção
22. Migrar dados históricos em lotes
23. Validar consistência de dados continuamente
24. Monitorar ambos os bancos de dados
25. Corrigir problemas de sincronização de dados

### Fase 6: PostgreSQL como Primário (Dia 8)
26. Mudar operações de leitura para PostgreSQL
27. Monitorar desempenho das queries
28. Otimizar queries lentas
29. Continuar dupla escrita por segurança

### Fase 7: Desativação do MongoDB (Dias 9-10)
30. Parar de escrever no MongoDB
31. Manter MongoDB como backup por 2 semanas
32. Remover dependências do MongoDB do código
33. Arquivar dados do MongoDB
34. Desativar instância do MongoDB

**Tempo Estimado**: 10 dias
**Nível de Risco**: Alto
**Estratégia de Rollback**: Manter MongoDB rodando com dupla escrita
**Critérios de Sucesso**:
- Zero perda de dados
- <5% de regressão de desempenho
- Todos os testes passando

**Riscos Principais**:
1. Inconsistência de dados durante a migração
2. Degradação de desempenho das queries
3. Downtime da aplicação
4. Perda de dados

**Mitigação**:
- Padrão de dupla escrita por segurança
- Cutover gradual
- Monitoramento contínuo
- Capacidade de rollback rápido

Prosseguir com este plano? (sim/não/modificar)

Usuário: Modificar — vamos adicionar um plano de rollback para cada fase

Claude: Plano atualizado com procedimentos de rollback para cada fase...
```

## Exemplo 3: Refatoração de Frontend

```
Usuário: /plan Refatorar nosso app React de componentes de classe para hooks

Claude: Vou criar um plano de refatoração sistemático.

## Plano de Migração de Classes React para Hooks

### Fase 1: Preparação e Análise (2 horas)
1. Auditar todos os componentes de classe (encontrar todos os arquivos .jsx/.tsx)
2. Categorizar por complexidade:
   - Simples (apenas estado): ~15 componentes
   - Médio (métodos de ciclo de vida): ~23 componentes
   - Complexo (múltiplos ciclos de vida, refs): ~8 componentes
3. Identificar bibliotecas de terceiros que precisam de atualização
4. Criar grafo de dependências de componentes
5. Planejar ordem de migração (nós folha primeiro)

### Fase 2: Configuração e Ferramentas (1 hora)
6. Atualizar React para v18+
7. Configurar regras ESLint para hooks
8. Criar templates de conversão
9. Configurar testes automatizados
10. Criar checkpoint antes de começar

### Fase 3: Migrar Componentes Simples (4 horas)
11. Converter componentes stateful simples (15 componentes)
12. Substituir this.state por useState
13. Substituir this.setState por setters de estado
14. Testar cada componente após a conversão
15. Atualizar testes

### Fase 4: Migrar Componentes Médios (8 horas)
16. Converter componentes com métodos de ciclo de vida (23 componentes)
17. Substituir componentDidMount por useEffect
18. Substituir componentDidUpdate por useEffect
19. Substituir componentWillUnmount por cleanup do useEffect
20. Testar minuciosamente

### Fase 5: Migrar Componentes Complexos (12 horas)
21. Converter componentes complexos (8 componentes)
22. Substituir refs por useRef
23. Extrair hooks customizados para lógica compartilhada
24. Tratar casos extremos (múltiplos useEffect)
25. Testes extensivos

### Fase 6: Extração de Lógica Compartilhada (6 horas)
26. Identificar lógica duplicada entre componentes
27. Criar hooks customizados:
    - useAuth
    - useFetch
    - useLocalStorage
    - useDebounce
28. Refatorar componentes para usar hooks customizados
29. Testar hooks customizados independentemente

### Fase 7: Otimização de Desempenho (4 horas)
30. Adicionar React.memo onde necessário
31. Otimizar com useCallback
32. Otimizar com useMemo
33. Fazer profile e corrigir regressões de desempenho

### Fase 8: Limpeza e Documentação (2 horas)
34. Remover utilitários de componentes de classe não utilizados
35. Atualizar documentação
36. Atualizar diretrizes de código
37. Criar guia de migração para a equipe

**Tempo Estimado**: 5 dias (39 horas)
**Arquivos a Modificar**: 46 componentes
**Nível de Risco**: Médio

**Ordem de Migração**:
1. Componentes folha (sem dependências)
2. Componentes de nível médio
3. Componentes container de nível superior
4. App.jsx (por último)

**Estratégia de Testes**:
- Testes unitários para cada componente
- Testes de integração para fluxos de usuário
- Testes de regressão visual
- Benchmarks de desempenho

**Métricas de Sucesso**:
- Todos os testes passando
- Sem regressões visuais
- Desempenho mantido ou melhorado
- Tamanho do bundle não aumentado significativamente

Prosseguir? (sim/não/modificar)
```

## Exemplo 4: Implementação de Segurança

```
Usuário: /plan Implementar segurança abrangente para nosso app web

Claude: Deixa eu criar um plano de implementação de segurança completo.

## Plano de Implementação de Segurança para Aplicação Web

### Fase 1: Auditoria de Segurança (Dia 1)
1. Executar scanners de segurança automatizados (npm audit, Snyk)
2. Revisar dependências para vulnerabilidades
3. Verificar conformidade com OWASP Top 10
4. Auditar fluxos de autenticação
5. Revisar práticas de tratamento de dados
6. Documentar lacunas de segurança atuais

### Fase 2: Endurecimento da Autenticação (Dias 2-3)
7. Implementar requisitos fortes de senha
8. Adicionar medidor de força de senha
9. Implementar rate limiting no login
10. Adicionar bloqueio de conta após tentativas falhadas
11. Implementar 2FA (TOTP)
12. Adicionar melhorias no gerenciamento de sessão
13. Implementar fluxo seguro de redefinição de senha

### Fase 3: Autorização e Controle de Acesso (Dias 3-4)
14. Implementar RBAC (Controle de Acesso Baseado em Papéis)
15. Adicionar verificações de permissão em todos os endpoints
16. Implementar princípio do menor privilégio
17. Adicionar log de auditoria para operações sensíveis
18. Implementar permissões em nível de recurso

### Fase 4: Proteção de Dados (Dias 4-5)
19. Implementar criptografia em repouso (campos sensíveis)
20. Garantir TLS/SSL para todas as comunicações
21. Implementar armazenamento seguro de sessão
22. Adicionar mascaramento de dados PII nos logs
23. Implementar políticas de retenção de dados
24. Adicionar tratamento seguro de upload de arquivos

### Fase 5: Validação e Sanitização de Entrada (Dias 5-6)
25. Implementar validação de entrada em todos os endpoints
26. Adicionar proteção XSS (Content Security Policy)
27. Implementar prevenção de injeção SQL (queries parametrizadas)
28. Adicionar proteção CSRF
29. Implementar limites de tamanho de requisição
30. Adicionar validação de tipo de arquivo em uploads

### Fase 6: Headers e Configuração de Segurança (Dia 6)
31. Adicionar headers de segurança:
    - Strict-Transport-Security
    - X-Content-Type-Options
    - X-Frame-Options
    - X-XSS-Protection
    - Content-Security-Policy
32. Configurar CORS adequadamente
33. Desabilitar métodos HTTP desnecessários
34. Remover headers de versão do servidor

### Fase 7: Monitoramento e Logging (Dia 7)
35. Implementar logging de eventos de segurança
36. Adicionar detecção de anomalias
37. Configurar detecção de intrusão
38. Implementar alertas em tempo real
39. Criar dashboard de segurança

### Fase 8: Testes e Documentação (Dias 8-9)
40. Realizar teste de penetração
41. Executar scanners de segurança
42. Testar todos os recursos de segurança
43. Criar documentação de segurança
44. Treinar equipe em práticas de segurança
45. Criar plano de resposta a incidentes

### Fase 9: Conformidade e Políticas (Dia 10)
46. Verificação de conformidade com LGPD/GDPR
47. Criar política de privacidade
48. Implementar direitos dos titulares de dados
49. Adicionar consentimento de cookies
50. Criar documentação de políticas de segurança

**Tempo Estimado**: 10 dias
**Nível de Risco**: Crítico
**Prioridade**: Alta

**Resumo de Melhorias de Segurança**:
- Autenticação: 7 melhorias
- Autorização: 5 melhorias
- Proteção de Dados: 6 melhorias
- Validação de Entrada: 6 melhorias
- Infraestrutura: 9 melhorias
- Monitoramento: 5 melhorias

**Conformidade**: OWASP Top 10, LGPD/GDPR

**Critérios de Sucesso**:
- Zero vulnerabilidades críticas
- Todos os itens do OWASP Top 10 mitigados
- Score de segurança >90/100
- Todos os problemas do teste de penetração resolvidos

Prosseguir? (sim/não/modificar)
```

## Exemplo 5: Otimização de Desempenho

```
Usuário: /plan Otimizar nosso site de e-commerce lento

Claude: Deixa eu criar um plano abrangente de otimização de desempenho.

## Plano de Otimização de Desempenho para E-commerce

### Fase 1: Auditoria de Desempenho (4 horas)
1. Executar auditoria do Lighthouse
2. Analisar perfil de desempenho do Chrome DevTools
3. Medir Core Web Vitals:
   - LCP (Largest Contentful Paint)
   - FID (First Input Delay)
   - CLS (Cumulative Layout Shift)
4. Identificar gargalos de desempenho
5. Criar métricas de baseline de desempenho

**Métricas Atuais**:
- LCP: 4,2s (alvo: <2,5s)
- FID: 280ms (alvo: <100ms)
- CLS: 0,25 (alvo: <0,1)
- Carregamento da Página: 8,3s (alvo: <3s)

### Fase 2: Otimização de Imagens (6 horas)
6. Converter imagens para formato WebP
7. Implementar imagens responsivas
8. Adicionar lazy loading para imagens
9. Otimizar tamanhos de imagem (compressão)
10. Implementar CDN para imagens
11. Adicionar placeholders de imagem

**Impacto Esperado**: -40% no tempo de carregamento

### Fase 3: Code Splitting e Lazy Loading (8 horas)
12. Implementar code splitting baseado em rota
13. Fazer lazy load de componentes não críticos
14. Dividir bundles de fornecedores
15. Otimizar tamanhos de chunks
16. Implementar imports dinâmicos
17. Adicionar preloading para recursos críticos

**Impacto Esperado**: -30% no tamanho do bundle inicial

### Fase 4: Estratégia de Cache (6 horas)
18. Implementar cache do navegador (Cache-Control)
19. Adicionar service worker para suporte offline
20. Implementar cache de respostas da API
21. Adicionar cache Redis para queries de banco de dados
22. Implementar stale-while-revalidate
23. Configurar cache do CDN

**Impacto Esperado**: -50% no tempo de resposta da API

### Fase 5: Otimização de Banco de Dados (8 horas)
24. Adicionar índices ao banco de dados
25. Otimizar queries lentas (>100ms)
26. Implementar cache de resultados de queries
27. Adicionar connection pooling
28. Desnormalizar onde apropriado
29. Implementar read replicas do banco de dados

**Impacto Esperado**: -60% no tempo de query do banco de dados

### Fase 6: Otimização de Frontend (10 horas)
30. Minificar e comprimir JavaScript
31. Minificar e comprimir CSS
32. Remover CSS não utilizado (PurgeCSS)
33. Implementar CSS crítico
34. Adiar JavaScript não crítico
35. Reduzir tamanho do DOM
36. Otimizar renderização React (memo, useMemo)
37. Implementar scroll virtual para listas longas

**Impacto Esperado**: -35% no tempo de execução do JavaScript

### Fase 7: Otimização de Rede (4 horas)
38. Ativar HTTP/2
39. Implementar resource hints (preconnect, prefetch)
40. Reduzir número de requisições HTTP
41. Ativar compressão Brotli
42. Otimizar scripts de terceiros

**Impacto Esperado**: -25% no tempo de rede

### Fase 8: Monitoramento e Testes (4 horas)
43. Configurar monitoramento de desempenho (Datadog/New Relic)
44. Adicionar Monitoramento de Usuário Real (RUM)
45. Criar orçamentos de desempenho
46. Configurar Lighthouse CI automatizado
47. Testar em dispositivos reais

**Tempo Estimado**: 50 horas (2 semanas)

**Métricas Alvo** (percentil 90):
- LCP: <2,0s (de 4,2s) ✅
- FID: <50ms (de 280ms) ✅
- CLS: <0,05 (de 0,25) ✅
- Carregamento: <2,5s (de 8,3s) ✅

**Impacto Esperado na Receita**:
- 100ms mais rápido = 1% de aumento na conversão
- Melhoria alvo de 5,8s = ~58% de aumento na conversão
- Receita adicional estimada: Significativa

**Ordem de Prioridade**:
1. Otimização de imagens (ganhos rápidos)
2. Code splitting (alto impacto)
3. Cache (alto impacto)
4. Otimização de banco de dados (crítico)
5. Otimização de frontend (polimento)

Prosseguir com este plano? (sim/não/modificar)
```

## Pontos-Chave

### Benefícios do Modo de Planejamento

1. **Clareza**: Roadmap claro antes de começar
2. **Estimativas**: Estimativas de tempo e esforço
3. **Avaliação de Riscos**: Identificar possíveis problemas cedo
4. **Priorização**: Ordem lógica das tarefas
5. **Aprovação**: Revisar e aprovar antes da execução
6. **Modificação**: Ajustar o plano com base no feedback

### Quando Usar o Modo de Planejamento

✅ **Sempre usar para**:
- Projetos multi-dias
- Colaborações em equipe
- Mudanças críticas no sistema
- Aprender novos conceitos
- Refatoração complexa

❌ **Não usar para**:
- Correções de bugs
- Pequenos ajustes
- Queries simples
- Experimentos rápidos

### Boas Práticas

1. **Revise os planos com cuidado** antes de aprovar
2. **Modifique os planos** quando identificar problemas
3. **Divida** tarefas complexas
4. **Estime** prazos realistas
5. **Inclua estratégias de rollback**
6. **Adicione critérios de sucesso**
7. **Planeje testes** em cada fase

---
**Última Atualização**: 9 de abril de 2026
