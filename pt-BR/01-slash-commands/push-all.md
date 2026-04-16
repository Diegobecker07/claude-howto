<!-- i18n-source: 01-slash-commands/push-all.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
description: Preparar todas as alterações, criar commit e enviar para o remoto (use com cautela)
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# Commit e Push de Tudo

⚠️ **ATENÇÃO**: Prepara TODAS as alterações, faz commit e envia para o remoto. Use apenas quando tiver certeza de que todas as alterações pertencem juntas.

## Fluxo de Trabalho

### 1. Analisar Alterações
Executar em paralelo:
- `git status` — Mostrar arquivos modificados/adicionados/excluídos/não rastreados
- `git diff --stat` — Mostrar estatísticas de alterações
- `git log -1 --oneline` — Mostrar commit recente para estilo de mensagem

### 2. Verificações de Segurança

**❌ PARAR e AVISAR se detectado:**
- Segredos: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- Chaves de API: Qualquer variável `*_API_KEY`, `*_SECRET`, `*_TOKEN` com valores reais (não placeholders como `your-api-key`, `xxx`, `placeholder`)
- Arquivos grandes: `>10MB` sem Git LFS
- Artefatos de build: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- Arquivos temporários: `.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**Validação de Chaves de API:**
Verificar arquivos modificados para padrões como:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ Chave real detectada!
AWS_SECRET_KEY=AKIA...         # ❌ Chave real detectada!
STRIPE_API_KEY=sk_live_...    # ❌ Chave real detectada!

# ✅ Placeholders aceitáveis:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ Verificar:**
- `.gitignore` configurado adequadamente
- Sem conflitos de merge
- Branch correto (avise se main/master)
- Chaves de API são apenas placeholders

### 3. Solicitar Confirmação

Apresentar resumo:
```
📊 Resumo das Alterações:
- X arquivos modificados, Y adicionados, Z excluídos
- Total: +AAA inserções, -BBB deleções

🔒 Segurança: ✅ Sem segredos | ✅ Sem arquivos grandes | ⚠️ [avisos]
🌿 Branch: [nome] → origin/[nome]

Vou executar: git add . → commit → push

Digite 'yes' para prosseguir ou 'no' para cancelar.
```

**AGUARDAR confirmação explícita de "yes" antes de prosseguir.**

### 4. Executar (Após Confirmação)

Executar sequencialmente:
```bash
git add .
git status  # Verificar staging
```

### 5. Gerar Mensagem de Commit

Analisar alterações e criar commit convencional:

**Formato:**
```
[tipo]: Resumo breve (máx 72 caracteres)

- Alteração principal 1
- Alteração principal 2
- Alteração principal 3
```

**Tipos:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**Exemplo:**
```
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. Commit e Push

```bash
git commit -m "$(cat <<'EOF'
[Mensagem de commit gerada]
EOF
)"
git push  # Se falhar: git pull --rebase && git push
git log -1 --oneline --decorate  # Verificar
```

### 7. Confirmar Sucesso

```
✅ Enviado com sucesso para o remoto!

Commit: [hash] [mensagem]
Branch: [branch] → origin/[branch]
Arquivos alterados: X (+inserções, -deleções)
```

## Tratamento de Erros

- **git add falha**: Verificar permissões, arquivos bloqueados, confirmar repositório inicializado
- **git commit falha**: Corrigir hooks de pre-commit, verificar config git (user.name/email)
- **git push falha**:
  - Non-fast-forward: `git pull --rebase && git push`
  - Sem branch remoto: `git push -u origin [branch]`
  - Branch protegido: Usar fluxo de PR em vez disso

## Quando Usar

✅ **Bom para:**
- Atualizações de documentação em múltiplos arquivos
- Feature com testes e docs
- Correções de bugs em múltiplos arquivos
- Formatação/refatoração em todo o projeto
- Mudanças de configuração

❌ **Evitar quando:**
- Incerto sobre o que está sendo commitado
- Contém segredos/dados sensíveis
- Branches protegidos sem revisão
- Conflitos de merge presentes
- Quer histórico de commit granular
- Hooks de pre-commit falhando

## Alternativas

Se o usuário quiser controle, sugerir:
1. **Staging seletivo**: Revisar/preparar arquivos específicos
2. **Staging interativo**: `git add -p` para seleção de patches
3. **Fluxo de PR**: Criar branch → push → PR (use o comando `/pr`)

**⚠️ Lembre-se**: Sempre revise as alterações antes de fazer push. Na dúvida, use comandos git individuais para mais controle.

---
**Última Atualização**: 9 de abril de 2026
