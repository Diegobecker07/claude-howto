#!/bin/bash
# i18n-source: 06-hooks/pre-commit.sh
# i18n-source-sha: d4369ce
# i18n-date: 2026-04-16
# Executa testes antes do commit
# Hook: PreToolUse (matcher: Bash) - verifica se o comando é um git commit
# Nota: Não existe evento de hook "PreCommit". Use PreToolUse com um matcher Bash
# e inspecione o comando para detectar operações de git commit.

echo "🧪 Executando testes antes do commit..."

# Verifica se package.json existe (projeto Node.js)
if [ -f "package.json" ]; then
  if grep -q "\"test\":" package.json; then
    npm test
    if [ $? -ne 0 ]; then
      echo "❌ Testes falharam! Commit bloqueado."
      exit 1
    fi
  fi
fi

# Verifica se pytest está disponível (projeto Python)
if [ -f "pytest.ini" ] || [ -f "setup.py" ]; then
  if command -v pytest &> /dev/null; then
    pytest
    if [ $? -ne 0 ]; then
      echo "❌ Testes falharam! Commit bloqueado."
      exit 1
    fi
  fi
fi

# Verifica se go.mod existe (projeto Go)
if [ -f "go.mod" ]; then
  go test ./...
  if [ $? -ne 0 ]; then
    echo "❌ Testes falharam! Commit bloqueado."
    exit 1
  fi
fi

# Verifica se Cargo.toml existe (projeto Rust)
if [ -f "Cargo.toml" ]; then
  cargo test
  if [ $? -ne 0 ]; then
    echo "❌ Testes falharam! Commit bloqueado."
    exit 1
  fi
fi

echo "✅ Todos os testes passaram! Prosseguindo com o commit."
exit 0
