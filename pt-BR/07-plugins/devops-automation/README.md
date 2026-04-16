<!-- i18n-source: 07-plugins/devops-automation/README.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Plugin DevOps Automation

Automação completa de DevOps para deploy, monitoramento e resposta a incidentes.

## Funcionalidades

✅ Deploys automatizados
✅ Procedimentos de rollback
✅ Monitoramento de saúde do sistema
✅ Fluxos de resposta a incidentes
✅ Integração com Kubernetes

## Instalação

```bash
/plugin install devops-automation
```

## O Que Está Incluído

### Slash Commands
- `/deploy` - Fazer deploy para produção ou staging
- `/rollback` - Reverter para a versão anterior
- `/status` - Verificar a saúde do sistema
- `/incident` - Tratar incidentes em produção

### Subagentes
- `deployment-specialist` - Operações de deploy
- `incident-commander` - Coordenação de incidentes
- `alert-analyzer` - Análise de saúde do sistema

### Servidores MCP
- Integração com Kubernetes

### Scripts
- `deploy.sh` - Automação de deploy
- `rollback.sh` - Automação de rollback
- `health-check.sh` - Utilitários de verificação de saúde

### Hooks
- `pre-deploy.js` - Validação pré-deploy
- `post-deploy.js` - Tarefas pós-deploy

## Uso

### Deploy para Staging
```
/deploy staging
```

### Deploy para Produção
```
/deploy production
```

### Rollback
```
/rollback production
```

### Verificar Status
```
/status
```

### Tratar Incidente
```
/incident
```

## Requisitos

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- Acesso ao cluster configurado

## Configuração

Configure seu Kubernetes config:
```bash
export KUBECONFIG=~/.kube/config
```

## Exemplo de Fluxo de Trabalho

```
Usuário: /deploy production

Claude:
1. Executa hook pré-deploy (valida kubectl, conexão com o cluster)
2. Delega para o subagente deployment-specialist
3. Executa o script deploy.sh
4. Monitora o progresso do deploy via MCP do Kubernetes
5. Executa hook pós-deploy (aguarda pods, smoke tests)
6. Fornece resumo do deploy

Resultado:
✅ Deploy concluído
📦 Versão: v2.1.0
🚀 Pods: 3/3 prontos
⏱️  Tempo: 2m 34s
```
