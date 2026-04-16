#!/usr/bin/env python3
"""
Compara a complexidade ciclomática do código antes e depois das alterações.
Ajuda a identificar se a refatoração realmente simplifica a estrutura do código.
"""

import re
import sys


class ComplexityAnalyzer:
    """Analisa métricas de complexidade do código."""

    def __init__(self, code: str):
        self.code = code
        self.lines = code.split("\n")

    def calculate_cyclomatic_complexity(self) -> int:
        """
        Calcula a complexidade ciclomática usando o método de McCabe.
        Conta pontos de decisão: if, elif, else, for, while, except, and, or
        """
        complexity = 1  # Complexidade base

        # Conta pontos de decisão
        decision_patterns = [
            r"\bif\b",
            r"\belif\b",
            r"\bfor\b",
            r"\bwhile\b",
            r"\bexcept\b",
            r"\band\b(?!$)",
            r"\bor\b(?!$)",
        ]

        for pattern in decision_patterns:
            matches = re.findall(pattern, self.code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self) -> int:
        """
        Calcula a complexidade cognitiva — quão difícil é de entender?
        Baseado em profundidade de aninhamento e fluxo de controle.
        """
        cognitive = 0
        nesting_depth = 0

        for line in self.lines:
            # Rastreia profundidade de aninhamento
            if re.search(r"^\s*(if|for|while|def|class|try)\b", line):
                nesting_depth += 1
                cognitive += nesting_depth
            elif re.search(r"^\s*(elif|else|except|finally)\b", line):
                cognitive += nesting_depth

            # Reduz aninhamento quando desindentando
            if line and not line[0].isspace():
                nesting_depth = 0

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        O Índice de Manutenibilidade varia de 0 a 100.
        > 85: Excelente
        > 65: Bom
        > 50: Regular
        < 50: Ruim
        """
        lines = len(self.lines)
        cyclomatic = self.calculate_cyclomatic_complexity()
        cognitive = self.calculate_cognitive_complexity()

        # Cálculo simplificado do MI
        mi = (
            171
            - 5.2 * (cyclomatic / lines)
            - 0.23 * (cognitive)
            - 16.2 * (lines / 1000)
        )

        return max(0, min(100, mi))

    def get_complexity_report(self) -> dict:
        """Gera relatório abrangente de complexidade."""
        return {
            "cyclomatic_complexity": self.calculate_cyclomatic_complexity(),
            "cognitive_complexity": self.calculate_cognitive_complexity(),
            "maintainability_index": round(self.calculate_maintainability_index(), 2),
            "lines_of_code": len(self.lines),
            "avg_line_length": round(
                sum(len(l) for l in self.lines) / len(self.lines), 2
            )
            if self.lines
            else 0,
        }


def compare_files(before_file: str, after_file: str) -> None:
    """Compara métricas de complexidade entre duas versões de código."""

    with open(before_file) as f:
        before_code = f.read()

    with open(after_file) as f:
        after_code = f.read()

    before_analyzer = ComplexityAnalyzer(before_code)
    after_analyzer = ComplexityAnalyzer(after_code)

    before_metrics = before_analyzer.get_complexity_report()
    after_metrics = after_analyzer.get_complexity_report()

    print("=" * 60)
    print("COMPARAÇÃO DE COMPLEXIDADE DO CÓDIGO")
    print("=" * 60)

    print("\nANTES:")
    print(f"  Complexidade Ciclomática:    {before_metrics['cyclomatic_complexity']}")
    print(f"  Complexidade Cognitiva:      {before_metrics['cognitive_complexity']}")
    print(f"  Índice de Manutenibilidade:  {before_metrics['maintainability_index']}")
    print(f"  Linhas de Código:            {before_metrics['lines_of_code']}")
    print(f"  Comprimento Médio de Linha:  {before_metrics['avg_line_length']}")

    print("\nDEPOIS:")
    print(f"  Complexidade Ciclomática:    {after_metrics['cyclomatic_complexity']}")
    print(f"  Complexidade Cognitiva:      {after_metrics['cognitive_complexity']}")
    print(f"  Índice de Manutenibilidade:  {after_metrics['maintainability_index']}")
    print(f"  Linhas de Código:            {after_metrics['lines_of_code']}")
    print(f"  Comprimento Médio de Linha:  {after_metrics['avg_line_length']}")

    print("\nALTERAÇÕES:")
    cyclomatic_change = (
        after_metrics["cyclomatic_complexity"] - before_metrics["cyclomatic_complexity"]
    )
    cognitive_change = (
        after_metrics["cognitive_complexity"] - before_metrics["cognitive_complexity"]
    )
    mi_change = (
        after_metrics["maintainability_index"] - before_metrics["maintainability_index"]
    )
    loc_change = after_metrics["lines_of_code"] - before_metrics["lines_of_code"]

    print(f"  Complexidade Ciclomática:    {cyclomatic_change:+d}")
    print(f"  Complexidade Cognitiva:      {cognitive_change:+d}")
    print(f"  Índice de Manutenibilidade:  {mi_change:+.2f}")
    print(f"  Linhas de Código:            {loc_change:+d}")

    print("\nAVALIAÇÃO:")
    if mi_change > 0:
        print("  ✅ Código é MAIS manutenível")
    elif mi_change < 0:
        print("  ⚠️  Código é MENOS manutenível")
    else:
        print("  ➡️  Manutenibilidade inalterada")

    if cyclomatic_change < 0:
        print("  ✅ Complexidade DIMINUIU")
    elif cyclomatic_change > 0:
        print("  ⚠️  Complexidade AUMENTOU")
    else:
        print("  ➡️  Complexidade inalterada")

    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python compare-complexity.py <arquivo_antes> <arquivo_depois>")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
