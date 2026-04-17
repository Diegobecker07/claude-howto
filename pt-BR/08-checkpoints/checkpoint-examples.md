<!-- i18n-source: 08-checkpoints/checkpoint-examples.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
# Exemplos de Checkpoints

Exemplos do mundo real de uso efetivo de checkpoints no Claude Code.

Nota: Os checkpoints são criados automaticamente a cada prompt do usuário. Você não precisa salvá-los manualmente. Para retroceder, pressione `Esc` duas vezes (`Esc+Esc`) ou use `/rewind` para abrir o navegador de checkpoints.

## Exemplo 1: Migração de Banco de Dados

### Cenário
Você precisa migrar do MySQL para o PostgreSQL, mas quer explorar tanto uma migração direta quanto uma abordagem gradual de dupla escrita.

### Fluxo de Trabalho

```
Usuário: Vamos implementar uma migração direta do MySQL para o PostgreSQL
         [Checkpoint A criado automaticamente]

Claude: Vou implementar a migração direta...
[Muda o driver do banco de dados, atualiza queries, modifica o schema]

Usuário: Execute os testes
         [Checkpoint B criado automaticamente]

Claude: Executando testes...
❌ 15 testes falhando — problemas de connection pool

Usuário: Essa abordagem tem problemas. Vamos tentar o padrão de dupla escrita.
[Usuário pressiona Esc+Esc, seleciona Checkpoint A, escolhe "Restaurar código e conversa"]

Usuário: Agora implemente um padrão de dupla escrita onde escrevemos em ambos os bancos de dados

Claude: Vou implementar a migração com dupla escrita...
[Implementa camada de dupla escrita, estratégia de migração gradual]

Usuário: Execute os testes

Claude: Executando testes...
✅ Todos os testes passando

Usuário: A abordagem de dupla escrita é claramente mais segura. Vamos fazer o commit.
```

## Exemplo 2: Otimização de Desempenho

### Cenário
Múltiplas estratégias de otimização de desempenho para experimentar.

### Fluxo de Trabalho

```
Usuário: Vamos otimizar o tempo de resposta da API. Atual: 450ms
         [Checkpoint "Baseline" criado automaticamente]

Claude: Vou adicionar cache de queries de banco de dados...
[Implementa cache com Redis]

Usuário: Execute os testes de desempenho

Claude: Resultados: 280ms de tempo médio de resposta (melhoria de 38%)

Usuário: Deixa eu tentar uma abordagem diferente.
[Usuário pressiona Esc+Esc, seleciona checkpoint "Baseline", escolhe "Restaurar código e conversa"]

Usuário: Tente otimização de queries de banco de dados

Claude: Vou otimizar as queries de banco de dados...
[Adiciona índices, otimiza queries N+1]

Usuário: Execute os testes de desempenho

Claude: Resultados: 180ms de tempo médio de resposta (melhoria de 60%)

Usuário: Deixa eu tentar uma terceira abordagem.
[Usuário pressiona Esc+Esc, seleciona checkpoint "Baseline", escolhe "Restaurar código e conversa"]

Usuário: Tente compressão de resposta e CDN

Claude: Vou adicionar compressão e CDN...
[Implementa gzip, configura CDN]

Usuário: Execute os testes de desempenho

Claude: Resultados: 320ms de tempo médio de resposta (melhoria de 29%)

Usuário: A otimização de queries foi a melhor. Deixa eu voltar e combinar com o cache.
[Usuário pressiona Esc+Esc, seleciona o checkpoint após a otimização de queries, escolhe "Restaurar código e conversa"]

Usuário: Agora adicione cache Redis sobre essas queries otimizadas

Claude: [Adiciona cache Redis sobre as queries otimizadas]

Usuário: Execute os testes de desempenho

Claude: Resultados: 95ms de tempo médio de resposta (melhoria de 79%) 🎉

Usuário: Perfeito! Este é o vencedor. Vamos fazer o commit.
```

## Exemplo 3: Iteração de UI/UX

### Cenário
Experimentando diferentes layouts para um dashboard.

### Fluxo de Trabalho

```
Usuário: Vamos redesenhar o dashboard com um layout de sidebar
         [Checkpoint "Início" criado automaticamente]

Claude: [Implementa layout de sidebar]

Usuário: Me mostre uma captura de tela

Claude: [Mostra captura de tela]

Usuário: A sidebar parece apertada. Vamos tentar uma navegação superior.
[Usuário pressiona Esc+Esc, seleciona checkpoint "Início", escolhe "Restaurar código e conversa"]

Usuário: Tente um layout de navegação superior

Claude: [Implementa navegação superior]

Usuário: Me mostre uma captura de tela

Claude: [Mostra captura de tela]

Usuário: Melhor, mas vamos tentar um layout de grade de cards
[Usuário pressiona Esc+Esc, seleciona checkpoint "Início", escolhe "Restaurar código e conversa"]

Usuário: Tente um layout de grade de cards

Claude: [Implementa grade de cards]

Usuário: Me mostre uma captura de tela

Claude: [Mostra captura de tela]

Usuário: Ótimo! Mas podemos combinar a navegação superior com a grade de cards?
[Usuário pressiona Esc+Esc, seleciona o checkpoint após a grade de cards, escolhe "Restaurar código e conversa"]

Usuário: Adicione navegação superior ao layout de grade de cards

Claude: [Adiciona navegação superior à grade de cards]

Usuário: Perfeito! Este é o design final.
```

## Exemplo 4: Sessão de Depuração

### Cenário
Caçando um bug difícil com múltiplas hipóteses.

### Fluxo de Trabalho

```
Usuário: Há um vazamento de memória na aplicação
         [Checkpoint "Antes da depuração" criado automaticamente]

Claude: Deixa eu investigar...
[Analisa o código]

Usuário: Acho que está nos event listeners. Vamos corrigir esses.

Claude: [Corrige a limpeza dos event listeners]

Usuário: Execute o memory profiler

Claude: Ainda vazando Memory — os event listeners não eram o problema

Usuário: Deixa eu voltar e tentar uma hipótese diferente.
[Usuário pressiona Esc+Esc, seleciona checkpoint "Antes da depuração", escolhe "Restaurar código e conversa"]

Usuário: Talvez sejam as conexões de banco de dados?

Claude: [Implementa correções de connection pooling]

Usuário: Execute o memory profiler

Claude: Ainda vazando — não são as conexões também

Usuário: Deixa eu voltar e tentar outro ângulo.
[Usuário pressiona Esc+Esc, seleciona checkpoint "Antes da depuração", escolhe "Restaurar código e conversa"]

Usuário: Vamos verificar referências circulares

Claude: [Encontra e corrige referências circulares no cache]

Usuário: Execute o memory profiler

Claude: ✅ Vazamento de Memory corrigido! As referências circulares na camada de cache eram as culpadas.

Usuário: Excelente! Vamos fazer o commit dessa correção.
```

## Exemplo 5: Evolução do Design de API

### Cenário
Projetando uma API REST com múltiplas iterações.

### Fluxo de Trabalho

```
Usuário: Crie uma API REST para nossa plataforma de blog
         [Checkpoint "Antes do design da API" criado automaticamente]

Claude: [Cria API CRUD básica]

Usuário: Isso é muito simples. Vamos adicionar paginação e filtragem

Claude: [Adiciona paginação e filtragem]

Usuário: Precisamos de melhores relacionamentos entre recursos

Claude: [Implementa links HATEOAS]

Usuário: Na verdade, vamos tentar GraphQL em vez de REST
[Usuário pressiona Esc+Esc, seleciona checkpoint "Antes do design da API", escolhe "Restaurar código e conversa"]

Usuário: Implemente uma API GraphQL para nossa plataforma de blog

Claude: [Implementa API GraphQL]

Usuário: Acho que REST é melhor para nosso caso de uso.
[Usuário pressiona Esc+Esc, seleciona o checkpoint após HATEOAS, escolhe "Restaurar código e conversa"]

Usuário: Vamos finalizar a abordagem REST.
```

## Exemplo 6: Gerenciamento de Configuração

### Cenário
Testando diferentes abordagens de configuração.

### Fluxo de Trabalho

```
Usuário: Mova a configuração para variáveis de ambiente
         [Checkpoint "Config original" criado automaticamente]

Claude: [Implementa configuração por variáveis de ambiente]

Usuário: Teste em desenvolvimento

Claude: Funciona localmente mas problemas de deploy em produção

Usuário: Deixa eu tentar uma abordagem diferente.
[Usuário pressiona Esc+Esc, seleciona checkpoint "Config original", escolhe "Restaurar código e conversa"]

Usuário: Tente uma abordagem de arquivo de configuração com validação

Claude: [Implementa config YAML com validação de JSON schema]

Usuário: Teste em desenvolvimento

Claude: ✅ Funciona bem, bons erros de validação

Usuário: Podemos também suportar variáveis de ambiente para valores sensíveis?

Claude: [Adiciona override por variáveis de ambiente para segredos]

Usuário: Teste o deploy

Claude: ✅ Todos os ambientes funcionando corretamente

Usuário: Perfeito! Isso está pronto para produção.
```

## Exemplo 7: Estratégia de Testes

### Cenário
Implementando testes abrangentes.

### Fluxo de Trabalho

```
Usuário: Adicione testes unitários para o módulo de autenticação
         [Checkpoint criado automaticamente]

Claude: [Adiciona testes unitários com Jest]

Usuário: Execute os testes

Claude: 45 testes passando, 78% de cobertura

Usuário: Adicione também testes de integração

Claude: [Adiciona testes de integração]

Usuário: Execute os testes

Claude: 89 testes passando, 92% de cobertura, mas os testes estão lentos (3 minutos)

Usuário: Os testes estão muito lentos. Vamos otimizar.

Claude: [Otimiza o setup dos testes, adiciona execução paralela]

Usuário: Execute os testes

Claude: 89 testes passando, 92% de cobertura, 35 segundos ✅

Usuário: Ótimo! Agora adicione testes E2E para caminhos críticos

Claude: [Adiciona testes E2E com Playwright]

Usuário: Execute todos os testes

Claude: 112 testes passando, 94% de cobertura, 2 minutos

Usuário: Equilíbrio perfeito entre cobertura e velocidade!
```

## Exemplo 8: Usando Resumir a partir do Checkpoint

### Cenário
Após uma longa sessão de depuração, você quer condensar a conversa preservando o contexto.

### Fluxo de Trabalho

```
Usuário: [Após 20+ mensagens de depuração e exploração]

[Usuário pressiona Esc+Esc, seleciona um checkpoint inicial, escolhe "Resumir a partir daqui"]
[Opcionalmente fornece instruções: "Foque no que tentamos e o que funcionou"]

Claude: [Gera um resumo da conversa a partir desse ponto em diante]
[As mensagens originais são preservadas na transcrição]
[O resumo substitui a conversa visível, reduzindo o uso da janela de contexto]

Usuário: Agora vamos continuar com a abordagem que funcionou.
```

## Pontos-Chave

1. **Os checkpoints são automáticos**: Cada prompt do usuário cria um checkpoint — não é necessário salvar manualmente
2. **Use Esc+Esc ou /rewind**: Estas são as duas formas de acessar o navegador de checkpoints
3. **Escolha a opção de restauração correta**: Restaure código, conversa, ambos, ou resuma dependendo das suas necessidades
4. **Não tema a experimentação**: Os checkpoints tornam seguro tentar mudanças radicais
5. **Combine com git**: Use checkpoints para exploração, git para trabalho finalizado
6. **Resuma sessões longas**: Use "Resumir a partir daqui" para manter as conversas gerenciáveis

---
**Última Atualização**: 9 de abril de 2026
