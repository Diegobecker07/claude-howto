<!-- i18n-source: 08-checkpoints/README.md -->
<!-- i18n-source-sha: 63a1416 -->
<!-- i18n-date: 2026-04-14 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Checkpoints e Rewind

Checkpoints permitem salvar o estado da conversa e voltar para pontos anteriores na sua sessão do Claude Code. Isso é essencial para explorar abordagens diferentes, recuperar-se de erros ou comparar soluções alternativas.

## Visão geral

Checkpoints permitem salvar o estado da conversa e voltar para pontos anteriores, possibilitando experimentação segura e exploração de múltiplas abordagens. Eles são instantâneos do estado da sua conversa, incluindo:
- Todas as mensagens trocadas
- Modificações feitas em arquivos
- Histórico de uso de ferramentas
- Contexto da sessão

Checkpoints são valiosos ao explorar abordagens diferentes, recuperar-se de erros ou comparar soluções alternativas.

## Conceitos-chave

| Conceito | Descrição |
|---------|-------------|
| **Checkpoint** | Instantâneo do estado da conversa, incluindo mensagens, arquivos e contexto |
| **Rewind** | Retornar a um checkpoint anterior, descartando alterações posteriores |
| **Branch Point** | Checkpoint a partir do qual várias abordagens são exploradas |

## Acesso aos Checkpoints

Você pode acessar e gerenciar checkpoints de duas formas principais:

### Usando atalho de teclado
Pressione `Esc` duas vezes (`Esc` + `Esc`) para abrir a interface de checkpoints e navegar pelos pontos salvos.

### Usando comando slash
Use o comando `/rewind` (alias: `/checkpoint`) para acesso rápido:

```bash
# Abrir a interface de rewind
/rewind

# Ou usar o alias
/checkpoint
```

## Opções de Rewind

Quando você faz rewind, aparece um menu com cinco opções:

1. **Restaurar código e conversa** -- Reverte arquivos e mensagens para aquele checkpoint
2. **Restaurar conversa** -- Faz rewind apenas das mensagens, mantendo o código atual como está
3. **Restaurar código** -- Reverte apenas as alterações em arquivos, mantendo o histórico completo da conversa
4. **Resumir daqui** -- Compacta a conversa a partir deste ponto em diante em um resumo gerado por IA, liberando espaço na janela de contexto. As mensagens anteriores ao ponto selecionado permanecem intactas. Nenhum arquivo no disco é alterado. As mensagens originais são preservadas na transcrição da sessão. Opcionalmente, você pode fornecer instruções para focar o resumo em tópicos específicos.
5. **Deixar pra lá** -- Cancela e retorna ao estado atual

> **Nota**: Depois de restaurar a conversa ou resumir, o prompt original da mensagem selecionada volta para o campo de entrada, para que você possa reenviar ou editar.

## Checkpoints Automáticos

O Claude Code cria checkpoints automaticamente para você:

- **Cada prompt do usuário** - Um novo checkpoint é criado a cada entrada do usuário
- **Persistentes** - Checkpoints persistem entre sessões
- **Limpeza automática** - Checkpoints são limpos automaticamente após 30 dias

Isso significa que você sempre pode voltar para qualquer ponto anterior da conversa, de alguns minutos atrás até dias antes.

## Casos de uso

| Cenário | Fluxo |
|----------|----------|
| **Explorando abordagens** | Salvar → Tentar A → Salvar → Rewind → Tentar B → Comparar |
| **Refatoração segura** | Salvar → Refatorar → Testar → Se falhar: Rewind |
| **Teste A/B** | Salvar → Design A → Salvar → Rewind → Design B → Comparar |
| **Recuperação de erro** | Notar problema → Rewind para o último estado bom |

## Usando Checkpoints

### Visualização e rewind

Pressione `Esc` duas vezes ou use `/rewind` para abrir o navegador de checkpoints. Você verá uma lista de todos os checkpoints disponíveis com carimbos de data e hora. Selecione qualquer checkpoint para voltar para aquele estado.

### Detalhes do checkpoint

Cada checkpoint mostra:
- Carimbo de data e hora de criação
- Arquivos que foram modificados
- Número de mensagens na conversa
- Ferramentas que foram usadas

## Exemplos práticos

### Exemplo 1: Explorando abordagens diferentes

```
Usuário: Vamos adicionar uma camada de cache na API

Claude: Vou adicionar cache com Redis aos seus endpoints da API...
[Faz alterações no checkpoint A]

Usuário: Na verdade, vamos tentar cache em memória em vez disso

Claude: Vou fazer rewind para explorar uma abordagem diferente...
[O usuário pressiona Esc+Esc e faz rewind para o checkpoint A]
[Implementa cache em memória no checkpoint B]

Usuário: Agora posso comparar as duas abordagens
```

### Exemplo 2: Recuperando-se de erros

```
Usuário: Refatore o módulo de autenticação para usar JWT

Claude: Vou refatorar o módulo de autenticação...
[Faz alterações extensas]

Usuário: Espera, isso quebrou a integração OAuth. Vamos voltar.

Claude: Vou ajudar você a fazer rewind até antes da refatoração...
[O usuário pressiona Esc+Esc e seleciona o checkpoint anterior à refatoração]

Usuário: Vamos tentar uma abordagem mais conservadora desta vez
```

### Exemplo 3: Experimentação segura

```
Usuário: Vamos tentar reescrever isto em um estilo funcional
[Cria checkpoint antes da experimentação]

Claude: [Faz alterações experimentais]

Usuário: Os testes estão falhando. Vamos fazer rewind.
[O usuário pressiona Esc+Esc e faz rewind para o checkpoint]

Claude: Reverti as alterações. Vamos tentar uma abordagem diferente.
```

### Exemplo 4: Ramificação de abordagens

```
Usuário: Quero comparar dois designs de banco de dados
[Anota o checkpoint - chame-o de "Start"]

Claude: Vou criar o primeiro design...
[Implementa o Schema A]

Usuário: Agora vou voltar e tentar a segunda abordagem
[O usuário pressiona Esc+Esc e faz rewind para "Start"]

Claude: Agora vou implementar o Schema B...
[Implementa o Schema B]

Usuário: Ótimo! Agora tenho os dois schemas para escolher
```

## Retenção de checkpoints

O Claude Code gerencia seus checkpoints automaticamente:

- Checkpoints são criados automaticamente a cada prompt do usuário
- Checkpoints antigos são mantidos por até 30 dias
- Os checkpoints são limpos automaticamente para evitar crescimento ilimitado do armazenamento

## Padrões de fluxo

### Estratégia de ramificação para exploração

Ao explorar várias abordagens:

```
1. Comece com a implementação inicial → Checkpoint A
2. Tente a Abordagem 1 → Checkpoint B
3. Faça rewind para o Checkpoint A
4. Tente a Abordagem 2 → Checkpoint C
5. Compare os resultados de B e C
6. Escolha a melhor abordagem e continue
```

### Padrão de refatoração segura

Ao fazer mudanças significativas:

```
1. Estado atual → Checkpoint (automático)
2. Inicie a refatoração
3. Execute os testes
4. Se os testes passarem → Continue trabalhando
5. Se os testes falharem → Faça rewind e tente outra abordagem
```

## Boas práticas

Como os checkpoints são criados automaticamente, você pode se concentrar no trabalho sem se preocupar em salvar o estado manualmente. Ainda assim, mantenha estas práticas em mente:

### Usando checkpoints de forma eficaz

✅ **Faça:**
- Revise os checkpoints disponíveis antes de fazer rewind
- Use rewind quando quiser explorar direções diferentes
- Mantenha checkpoints para comparar abordagens diferentes
- Entenda o que cada opção de rewind faz (restaurar código e conversa, restaurar conversa, restaurar código ou resumir)

❌ **Não faça:**
- Não dependa apenas de checkpoints para preservar código
- Não espere que checkpoints acompanhem mudanças externas do sistema de arquivos
- Não use checkpoints como substituto para commits git

## Configuração

Checkpoints são um comportamento padrão integrado no Claude Code e não exigem nenhuma configuração para ativação. Cada prompt do usuário cria automaticamente um checkpoint.

A única configuração relacionada a checkpoints é `cleanupPeriodDays`, que controla por quanto tempo sessões e checkpoints são mantidos:

```json
{
  "cleanupPeriodDays": 30
}
```

- `cleanupPeriodDays`: Número de dias para manter o histórico da sessão e os checkpoints (padrão: `30`)

## Limitações

Checkpoints têm as seguintes limitações:

- **Alterações de comandos Bash NÃO são rastreadas** - Operações como `rm`, `mv`, `cp` no sistema de arquivos não são capturadas nos checkpoints
- **Alterações externas NÃO são rastreadas** - Mudanças feitas fora do Claude Code (no editor, terminal etc.) não são capturadas
- **Não substituem controle de versão** - Use git para mudanças permanentes e auditáveis no seu código

## Solução de problemas

### Checkpoints ausentes

**Problema**: O checkpoint esperado não foi encontrado

**Solução**:
- Verifique se os checkpoints foram limpos
- Verifique o espaço em disco
- Confirme se `cleanupPeriodDays` está definido alto o suficiente (padrão: 30 dias)

### Rewind falhou

**Problema**: Não é possível fazer rewind para o checkpoint

**Solução**:
- Certifique-se de que não há conflitos com alterações não commitadas
- Verifique se o checkpoint está corrompido
- Tente fazer rewind para outro checkpoint

## Integração com git

Checkpoints complementam o git, mas não o substituem:

| Recurso | Git | Checkpoints |
|---------|-----|-------------|
| Escopo | Sistema de arquivos | Conversa + arquivos |
| Persistência | Permanente | Baseada na sessão |
| Granularidade | Commits | Qualquer ponto |
| Velocidade | Mais lenta | Instantânea |
| Compartilhamento | Sim | Limitado |

Use os dois juntos:
1. Use checkpoints para experimentação rápida
2. Use commits git para mudanças finalizadas
3. Crie um checkpoint antes de operações git
4. Faça commit dos estados de checkpoint bem-sucedidos no git

## Guia de início rápido

### Fluxo básico

1. **Trabalhe normalmente** - O Claude Code cria checkpoints automaticamente
2. **Quer voltar?** - Pressione `Esc` duas vezes ou use `/rewind`
3. **Escolha o checkpoint** - Selecione da lista para voltar
4. **Selecione o que restaurar** - Escolha entre restaurar código e conversa, restaurar conversa, restaurar código, resumir daqui ou cancelar
5. **Continue trabalhando** - Você voltou para aquele ponto

### Atalhos de teclado

- **`Esc` + `Esc`** - Abre o navegador de checkpoints
- **`/rewind`** - Forma alternativa de acessar checkpoints
- **`/checkpoint`** - Alias de `/rewind`

## Quando fazer rewind: monitoramento de contexto

Checkpoints permitem voltar no tempo, mas como saber *quando* você deveria fazer isso? À medida que a conversa cresce, a janela de contexto do Claude fica cheia e a qualidade do modelo se degrada silenciosamente. Você pode acabar enviando código com um modelo meio cego sem perceber.

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** resolve isso adicionando **zonas de contexto** em tempo real à barra de status do Claude Code. Ele acompanha onde você está na janela de contexto - de **Plan** (verde, seguro para planejar e codificar) até **Code** (amarelo, evite iniciar novos planos) e **Dump** (laranja, finalize e faça rewind). Quando a zona muda, você sabe que é hora de criar um checkpoint e recomeçar em vez de insistir com a saída degradada.

## Conceitos relacionados

- **[Recursos avançados](../09-advanced-features/)** - Modo de planejamento e outros recursos avançados
- **[Gerenciamento de memória](../02-memory/)** - Gerenciar histórico de conversa e contexto
- **[Comandos slash](../01-slash-commands/)** - Atalhos acionados pelo usuário
- **[Hooks](../06-hooks/)** - Automação orientada a eventos
- **[Plugins](../07-plugins/)** - Pacotes de extensão incluídos

## Recursos adicionais

- [Documentação oficial de checkpointing](https://code.claude.com/docs/en/checkpointing) - Referência oficial
- [Guia de recursos avançados](../09-advanced-features/) - Pensamento estendido e outros recursos

## Resumo

Checkpoints são um recurso automático no Claude Code que permite explorar diferentes abordagens com segurança, sem medo de perder trabalho. Cada prompt do usuário cria um novo checkpoint automaticamente, então você pode voltar a qualquer ponto anterior da sessão.

Principais benefícios:
- Experimente sem medo com múltiplas abordagens
- Recupere-se rapidamente de erros
- Compare soluções diferentes lado a lado
- Integre com segurança com sistemas de controle de versão

Lembre-se: checkpoints não substituem git. Use checkpoints para experimentação rápida e git para mudanças permanentes no código.

---
**Última atualização**: 11 de abril de 2026
**Versão do Claude Code**: 2.1.101
**Fontes**:
- https://code.claude.com/docs/en/checkpointing
**Modelos compatíveis**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5

*Parte da série de guias [Claude How To](../)*
