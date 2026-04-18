<!-- i18n-source: 03-skills/code-review/templates/review-checklist.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Checklist de Revisão de Código

## Checklist de Segurança
- [ ] Sem credenciais ou segredos hardcoded
- [ ] Validação de entrada em todos os inputs do usuário
- [ ] Prevenção de injeção SQL (queries parametrizadas)
- [ ] Proteção CSRF em operações que alteram estado
- [ ] Prevenção de XSS com escape adequado
- [ ] Verificações de autenticação em endpoints protegidos
- [ ] Verificações de autorização em recursos
- [ ] Hash seguro de senhas (bcrypt, argon2)
- [ ] Sem dados sensíveis nos logs
- [ ] HTTPS aplicado

## Checklist de Desempenho
- [ ] Sem queries N+1
- [ ] Uso adequado de índices
- [ ] Cache implementado onde benéfico
- [ ] Sem operações bloqueantes na thread principal
- [ ] Async/await usado corretamente
- [ ] Datasets grandes paginados
- [ ] Conexões de banco de dados em pool
- [ ] Expressões regulares otimizadas
- [ ] Sem criação desnecessária de objetos
- [ ] Memory leaks prevenidos

## Checklist de Qualidade
- [ ] Funções com menos de 50 linhas
- [ ] Nomenclatura de variáveis clara
- [ ] Sem código duplicado
- [ ] Tratamento de erros adequado
- [ ] Comentários explicam o POR QUÊ, não o QUÊ
- [ ] Sem console.logs em produção
- [ ] Verificação de tipos (TypeScript/JSDoc)
- [ ] Princípios SOLID seguidos
- [ ] Padrões de projeto aplicados corretamente
- [ ] Código autodocumentado

## Checklist de Testes
- [ ] Testes unitários escritos
- [ ] Casos extremos cobertos
- [ ] Cenários de erro testados
- [ ] Testes de integração presentes
- [ ] Cobertura > 80%
- [ ] Sem testes instáveis (flaky)
- [ ] Dependências externas mockadas
- [ ] Nomes de testes claros
