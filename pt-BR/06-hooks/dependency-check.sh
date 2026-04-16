#!/bin/bash
# i18n-source: 06-hooks/dependency-check.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Verifica vulnerabilidades conhecidas nas dependências após arquivos de manifesto serem modificados.
# Hook: PostToolUse:Write

FILE=$1

if [ -z "$FILE" ]; then
  echo "Uso: $0 <caminho_do_arquivo>"
  exit 0
fi

# Usa basename para correspondência — $1 pode ser um caminho absoluto
BASENAME=$(basename "$FILE")

# Executa apenas quando um manifesto de dependências é escrito
case "$BASENAME" in
  package.json|package-lock.json|yarn.lock|pnpm-lock.yaml| \
  requirements.txt|Pipfile|Pipfile.lock|pyproject.toml| \
  go.mod|go.sum| \
  Cargo.toml|Cargo.lock| \
  Gemfile|Gemfile.lock| \
  composer.json|composer.lock| \
  pom.xml|build.gradle|build.gradle.kts)
    echo "📦 Manifesto de dependências atualizado: $FILE — verificando vulnerabilidades..."
    ;;
  *)
    exit 0
    ;;
esac

ISSUES_FOUND=0

# ── npm / yarn / pnpm ────────────────────────────────────────────────────────
if [[ "$BASENAME" == package*.json || "$BASENAME" == yarn.lock || "$BASENAME" == pnpm-lock.yaml ]]; then
  if command -v npm &>/dev/null; then
    echo "🔍 Executando npm audit..."
    if ! npm audit --audit-level=high --json 2>/dev/null | \
        python3 -c "
import sys, json
data = json.load(sys.stdin)
vulns = data.get('metadata', {}).get('vulnerabilities', {})
high = vulns.get('high', 0) + vulns.get('critical', 0)
if high:
    print(f'  ⚠️  {high} vulnerabilidades npm de alto/crítico encontradas. Execute: npm audit fix')
    sys.exit(1)
" 2>/dev/null; then
      ISSUES_FOUND=1
    else
      echo "  ✅ Nenhuma vulnerabilidade npm de alto/crítico"
    fi
  fi

  if command -v yarn &>/dev/null && [[ "$BASENAME" == yarn.lock ]]; then
    echo "🔍 Executando yarn audit..."
    if ! yarn audit --level high --json 2>/dev/null | \
        grep -q '"type":"auditAdvisory"' 2>/dev/null; then
      echo "  ✅ Nenhuma vulnerabilidade yarn de alto nível"
    else
      echo "  ⚠️  yarn audit encontrou vulnerabilidades. Execute: yarn audit --level high"
      ISSUES_FOUND=1
    fi
  fi
fi

# ── Python ───────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == requirements.txt || "$BASENAME" == Pipfile* || "$BASENAME" == pyproject.toml ]]; then
  if command -v pip-audit &>/dev/null; then
    echo "🔍 Executando pip-audit..."
    if pip-audit --format=json 2>/dev/null | \
        python3 -c "
import sys, json
data = json.load(sys.stdin)
vulns = [d for d in data.get('dependencies', []) if d.get('vulns')]
if vulns:
    for dep in vulns:
        for v in dep['vulns']:
            print(f'  ⚠️  {dep[\"name\"]} {dep[\"version\"]}: {v[\"id\"]} — {v[\"fix_versions\"]}')
    sys.exit(1)
" 2>/dev/null; then
      echo "  ✅ Nenhuma vulnerabilidade Python encontrada"
    else
      ISSUES_FOUND=1
      echo "  Execute: pip-audit para detalhes"
    fi
  elif command -v safety &>/dev/null; then
    echo "🔍 Executando safety check..."
    OUTPUT=$(safety check --short-report 2>&1)
    EXIT_CODE=$?
    if [ $EXIT_CODE -eq 0 ]; then
      echo "  ✅ Nenhuma vulnerabilidade Python encontrada"
    elif echo "$OUTPUT" | grep -qiE "vulnerability|CVE|insecure"; then
      echo "$OUTPUT"
      ISSUES_FOUND=1
    else
      echo "  ⚠️  safety check não pôde ser concluído (erro de rede ou configuração)" >&2
    fi
  fi
fi

# ── Go ───────────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == go.mod || "$BASENAME" == go.sum ]]; then
  if command -v govulncheck &>/dev/null; then
    echo "🔍 Executando govulncheck..."
    OUTPUT=$(govulncheck ./... 2>&1)
    EXIT_CODE=$?
    if [ $EXIT_CODE -eq 0 ]; then
      echo "  ✅ Nenhuma vulnerabilidade Go encontrada"
    elif echo "$OUTPUT" | grep -q "Vulnerability #"; then
      echo "$OUTPUT"
      ISSUES_FOUND=1
    else
      echo "  ⚠️  govulncheck não pôde ser concluído: $OUTPUT" >&2
    fi
  fi
fi

# ── Rust ─────────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == Cargo.toml || "$BASENAME" == Cargo.lock ]]; then
  if command -v cargo-audit &>/dev/null; then
    echo "🔍 Executando cargo audit..."
    if ! cargo audit 2>/dev/null; then
      ISSUES_FOUND=1
    else
      echo "  ✅ Nenhuma vulnerabilidade Rust encontrada"
    fi
  fi
fi

# ── Ruby ─────────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == Gemfile || "$BASENAME" == Gemfile.lock ]]; then
  if command -v bundler-audit &>/dev/null; then
    echo "🔍 Executando bundler-audit..."
    bundler-audit check --update 2>/dev/null || ISSUES_FOUND=1
  fi
fi

# ── Fallback genérico: trivy ──────────────────────────────────────────────────
if command -v trivy &>/dev/null; then
  echo "🔍 Executando trivy fs scan..."
  if ! trivy fs --exit-code 1 --severity HIGH,CRITICAL --quiet . 2>/dev/null; then
    ISSUES_FOUND=1
  else
    echo "  ✅ trivy não encontrou problemas de ALTO/CRÍTICO"
  fi
fi

if [ "$ISSUES_FOUND" -eq 0 ]; then
  echo "✅ Verificação de dependências concluída — nenhuma vulnerabilidade detectada"
else
  echo ""
  echo "⚠️  Vulnerabilidades detectadas. Revise e atualize as dependências antes de fazer commit."
  echo "   Este hook é apenas informativo e não bloqueará seu fluxo de trabalho."
fi

# Sempre sai com 0 — este hook avisa mas não bloqueia
exit 0
