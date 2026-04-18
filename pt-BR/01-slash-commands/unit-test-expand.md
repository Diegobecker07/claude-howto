<!-- i18n-source: 01-slash-commands/unit-test-expand.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: Expand Unit Tests
description: Aumentar cobertura de testes visando branches não testados e casos extremos
tags: testing, coverage, unit-tests
---

# Expandir Testes Unitários

Expanda os testes unitários existentes adaptados ao framework de testes do projeto:

1. **Analisar cobertura**: Executar relatório de cobertura para identificar branches não testados, casos extremos e áreas de baixa cobertura
2. **Identificar lacunas**: Revisar código para branches lógicos, caminhos de erro, condições de contorno, entradas nulas/vazias
3. **Escrever testes** usando o framework do projeto:
   - Jest/Vitest/Mocha (JavaScript/TypeScript)
   - pytest/unittest (Python)
   - Go testing/testify (Go)
   - Rust test framework (Rust)
4. **Focar em cenários específicos**:
   - Tratamento de erros e exceções
   - Valores de contorno (mín/máx, vazio, nulo)
   - Casos extremos e casos de canto
   - Transições de estado e efeitos colaterais
5. **Verificar melhoria**: Executar cobertura novamente, confirmar aumento mensurável

Apresente apenas os novos blocos de código de teste. Siga os padrões e convenções de nomenclatura de testes existentes.

---
**Última Atualização**: 9 de abril de 2026
