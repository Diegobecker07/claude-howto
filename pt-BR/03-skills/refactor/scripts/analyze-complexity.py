#!/usr/bin/env python3
"""
Analisador de Complexidade de Código

Analisa métricas de complexidade de código para arquivos Python, JavaScript e TypeScript.
Ajuda a medir o impacto da refatoração comparando métricas antes/depois.

Uso:
    python analyze-complexity.py <arquivo>
    python analyze-complexity.py <arquivo_antes> <arquivo_depois>  # Modo de comparação
    python analyze-complexity.py --dir <diretório>                 # Analisar diretório

Métricas:
    - Complexidade Ciclomática: Pontos de decisão no código
    - Complexidade Cognitiva: Quão difícil é de entender
    - Índice de Manutenibilidade: Score geral de manutenibilidade (0-100)
    - Linhas de Código: Total de linhas
    - Contagem de Funções: Número de funções/métodos
    - Comprimento Médio de Função: Linhas por função
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class FunctionMetrics:
    """Métricas para uma única função."""
    name: str
    start_line: int
    end_line: int
    lines: int
    cyclomatic_complexity: int
    cognitive_complexity: int
    parameter_count: int


@dataclass
class FileMetrics:
    """Métricas para um arquivo."""
    filename: str
    lines_of_code: int
    blank_lines: int
    comment_lines: int
    function_count: int
    class_count: int
    cyclomatic_complexity: int
    cognitive_complexity: int
    maintainability_index: float
    avg_function_length: float
    max_function_length: int
    functions: List[FunctionMetrics]


class ComplexityAnalyzer:
    """Analisa complexidade de código para múltiplas linguagens."""

    # Padrões para diferentes linguagens
    PATTERNS = {
        'python': {
            'function': r'^\s*def\s+(\w+)\s*\(',
            'class': r'^\s*class\s+(\w+)',
            'decision': [r'\bif\b', r'\belif\b', r'\bfor\b', r'\bwhile\b',
                        r'\bexcept\b', r'\band\b(?!$)', r'\bor\b(?!$)',
                        r'\bcase\b', r'\btry\b'],
            'comment': r'^\s*#',
            'multiline_comment_start': r'^\s*["\'][\"\'][\"\']',
            'multiline_comment_end': r'["\'][\"\'][\"\']',
        },
        'javascript': {
            'function': r'(?:function\s+(\w+)|(\w+)\s*[=:]\s*(?:async\s+)?(?:function|\([^)]*\)\s*=>))',
            'class': r'class\s+(\w+)',
            'decision': [r'\bif\b', r'\belse\s+if\b', r'\bfor\b', r'\bwhile\b',
                        r'\bcatch\b', r'\b\?\b', r'\b&&\b', r'\b\|\|\b',
                        r'\bcase\b', r'\btry\b'],
            'comment': r'^\s*//',
            'multiline_comment_start': r'/\*',
            'multiline_comment_end': r'\*/',
        },
        'typescript': {
            'function': r'(?:function\s+(\w+)|(\w+)\s*[=:]\s*(?:async\s+)?(?:function|\([^)]*\)\s*=>))',
            'class': r'class\s+(\w+)',
            'decision': [r'\bif\b', r'\belse\s+if\b', r'\bfor\b', r'\bwhile\b',
                        r'\bcatch\b', r'\b\?\b', r'\b&&\b', r'\b\|\|\b',
                        r'\bcase\b', r'\btry\b'],
            'comment': r'^\s*//',
            'multiline_comment_start': r'/\*',
            'multiline_comment_end': r'\*/',
        }
    }

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.language = self._detect_language()
        self.patterns = self.PATTERNS.get(self.language, self.PATTERNS['python'])

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            self.code = f.read()
        self.lines = self.code.split('\n')

    def _detect_language(self) -> str:
        """Detecta a linguagem de programação pela extensão do arquivo."""
        ext = os.path.splitext(self.filepath)[1].lower()
        ext_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.jsx': 'javascript',
            '.ts': 'typescript',
            '.tsx': 'typescript',
        }
        return ext_map.get(ext, 'python')

    def calculate_cyclomatic_complexity(self, code: Optional[str] = None) -> int:
        """
        Calcula a complexidade ciclomática pelo método de McCabe.
        CC = E - N + 2P onde E=arestas, N=nós, P=componentes conectados
        Simplificado: Conta pontos de decisão + 1
        """
        if code is None:
            code = self.code

        complexity = 1  # Complexidade base

        for pattern in self.patterns['decision']:
            matches = re.findall(pattern, code)
            complexity += len(matches)

        return complexity

    def calculate_cognitive_complexity(self, code: Optional[str] = None) -> int:
        """
        Calcula a complexidade cognitiva.
        Mede quão difícil é de entender o código.
        Considera profundidade de aninhamento e quebras no fluxo de controle.
        """
        if code is None:
            code = self.code

        lines = code.split('\n')
        cognitive = 0
        nesting_depth = 0
        in_function = False

        for line in lines:
            stripped = line.strip()

            # Rastreia limites de função
            if re.search(self.patterns['function'], line):
                in_function = True
                nesting_depth = 0

            # Incrementa para estruturas de fluxo de controle
            if re.search(r'\b(if|for|while|switch)\b', stripped):
                nesting_depth += 1
                cognitive += nesting_depth  # Estruturas aninhadas custam mais

            elif re.search(r'\b(elif|else if|else|catch|finally)\b', stripped):
                cognitive += nesting_depth  # Mesmo nível que o pai

            # Rastreia aninhamento por chaves/indentação
            if self.language in ['javascript', 'typescript']:
                nesting_depth += stripped.count('{') - stripped.count('}')
                nesting_depth = max(0, nesting_depth)

            # Bônus para quebras no fluxo linear
            if re.search(r'\b(break|continue|return|throw)\b', stripped):
                if nesting_depth > 1:
                    cognitive += 1

            # Bônus para recursão
            # (simplificado: apenas verifica se a função chama a si mesma)

        return cognitive

    def calculate_maintainability_index(self) -> float:
        """
        Calcula o Índice de Manutenibilidade (0-100).
        Baseado em Volume de Halstead, Complexidade Ciclomática e Linhas de Código.

        MI = max(0, (171 - 5.2*ln(V) - 0.23*CC - 16.2*ln(LOC)) * 100/171)

        Interpretação:
        - 85-100: Altamente manutenível
        - 65-84: Moderadamente manutenível
        - 50-64: Difícil de manter
        - 0-49: Muito difícil de manter
        """
        import math

        loc = len([l for l in self.lines if l.strip()])
        cc = self.calculate_cyclomatic_complexity()

        # Aproximação simplificada do Volume de Halstead
        # Conta operadores e operandos únicos
        operators = len(re.findall(r'[+\-*/%=<>!&|^~]', self.code))
        operands = len(re.findall(r'\b\w+\b', self.code))
        volume = (operators + operands) * math.log2(max(1, operators + operands))

        # Calcula MI
        mi = 171 - 5.2 * math.log(max(1, volume)) - 0.23 * cc - 16.2 * math.log(max(1, loc))
        mi = max(0, min(100, mi * 100 / 171))

        return round(mi, 2)

    def count_lines(self) -> Dict[str, int]:
        """Conta diferentes tipos de linhas."""
        total = len(self.lines)
        blank = 0
        comment = 0
        in_multiline_comment = False

        for line in self.lines:
            stripped = line.strip()

            # Verifica comentários multilinha
            if re.search(self.patterns['multiline_comment_start'], stripped):
                in_multiline_comment = True
            if re.search(self.patterns['multiline_comment_end'], stripped):
                in_multiline_comment = False
                comment += 1
                continue

            if in_multiline_comment:
                comment += 1
            elif not stripped:
                blank += 1
            elif re.match(self.patterns['comment'], stripped):
                comment += 1

        return {
            'total': total,
            'blank': blank,
            'comment': comment,
            'code': total - blank - comment
        }

    def find_functions(self) -> List[FunctionMetrics]:
        """Encontra todas as funções e calcula suas métricas individuais."""
        functions = []
        current_function = None
        function_start = 0
        brace_depth = 0

        for i, line in enumerate(self.lines):
            # Verifica definição de função
            match = re.search(self.patterns['function'], line)
            if match:
                # Salva a função anterior se existir
                if current_function:
                    func_code = '\n'.join(self.lines[function_start:i])
                    functions.append(self._create_function_metrics(
                        current_function, function_start, i - 1, func_code
                    ))

                current_function = match.group(1) or match.group(2) if match.lastindex and match.lastindex > 1 else match.group(1)
                function_start = i
                brace_depth = 0

            # Rastreia chaves para JS/TS
            if self.language in ['javascript', 'typescript']:
                brace_depth += line.count('{') - line.count('}')

        # Não esquecer a última função
        if current_function:
            func_code = '\n'.join(self.lines[function_start:])
            functions.append(self._create_function_metrics(
                current_function, function_start, len(self.lines) - 1, func_code
            ))

        return functions

    def _create_function_metrics(self, name: str, start: int, end: int, code: str) -> FunctionMetrics:
        """Cria métricas para uma única função."""
        lines = end - start + 1

        # Conta parâmetros (simplificado)
        param_match = re.search(r'\(([^)]*)\)', code.split('\n')[0])
        param_count = 0
        if param_match and param_match.group(1).strip():
            param_count = len([p for p in param_match.group(1).split(',') if p.strip()])

        return FunctionMetrics(
            name=name,
            start_line=start + 1,
            end_line=end + 1,
            lines=lines,
            cyclomatic_complexity=self.calculate_cyclomatic_complexity(code),
            cognitive_complexity=self.calculate_cognitive_complexity(code),
            parameter_count=param_count
        )

    def analyze(self) -> FileMetrics:
        """Realiza análise completa do arquivo."""
        line_counts = self.count_lines()
        functions = self.find_functions()

        # Conta classes
        class_count = len(re.findall(self.patterns['class'], self.code))

        # Calcula médias
        func_lengths = [f.lines for f in functions] if functions else [0]
        avg_func_length = sum(func_lengths) / len(func_lengths)
        max_func_length = max(func_lengths)

        return FileMetrics(
            filename=self.filename,
            lines_of_code=line_counts['code'],
            blank_lines=line_counts['blank'],
            comment_lines=line_counts['comment'],
            function_count=len(functions),
            class_count=class_count,
            cyclomatic_complexity=self.calculate_cyclomatic_complexity(),
            cognitive_complexity=self.calculate_cognitive_complexity(),
            maintainability_index=self.calculate_maintainability_index(),
            avg_function_length=round(avg_func_length, 1),
            max_function_length=max_func_length,
            functions=functions
        )


def print_metrics(metrics: FileMetrics, verbose: bool = False) -> None:
    """Imprime métricas em formato legível."""
    print("=" * 60)
    print(f"ANÁLISE DE COMPLEXIDADE DO CÓDIGO: {metrics.filename}")
    print("=" * 60)

    print("\n📊 VISÃO GERAL")
    print("-" * 40)
    print(f"  Linhas de Código:          {metrics.lines_of_code}")
    print(f"  Linhas em Branco:          {metrics.blank_lines}")
    print(f"  Linhas de Comentário:      {metrics.comment_lines}")
    print(f"  Funções/Métodos:           {metrics.function_count}")
    print(f"  Classes:                   {metrics.class_count}")

    print("\n📈 MÉTRICAS DE COMPLEXIDADE")
    print("-" * 40)
    print(f"  Complexidade Ciclomática:  {metrics.cyclomatic_complexity}")
    print(f"  Complexidade Cognitiva:    {metrics.cognitive_complexity}")
    print(f"  Índice de Manutenibilidade:{metrics.maintainability_index}")

    # Interpreta manutenibilidade
    mi = metrics.maintainability_index
    if mi >= 85:
        mi_label = "Altamente manutenível ✅"
    elif mi >= 65:
        mi_label = "Moderadamente manutenível 🔶"
    elif mi >= 50:
        mi_label = "Difícil de manter ⚠️"
    else:
        mi_label = "Muito difícil de manter ❌"
    print(f"    → {mi_label}")

    print("\n📐 MÉTRICAS DE FUNÇÃO")
    print("-" * 40)
    print(f"  Comprimento Médio de Função: {metrics.avg_function_length} linhas")
    print(f"  Comprimento Máximo de Função:{metrics.max_function_length} linhas")

    if verbose and metrics.functions:
        print("\n📋 DETALHES DAS FUNÇÕES")
        print("-" * 40)
        for f in sorted(metrics.functions, key=lambda x: x.cyclomatic_complexity, reverse=True):
            flag = " ⚠️" if f.cyclomatic_complexity > 10 or f.lines > 50 else ""
            print(f"  {f.name}() [linhas {f.start_line}-{f.end_line}]{flag}")
            print(f"    - Linhas: {f.lines}, CC: {f.cyclomatic_complexity}, "
                  f"Cognitiva: {f.cognitive_complexity}, Params: {f.parameter_count}")

    print("\n" + "=" * 60)


def print_comparison(before: FileMetrics, after: FileMetrics) -> None:
    """Imprime comparação entre duas análises."""
    print("=" * 70)
    print("COMPARAÇÃO DE COMPLEXIDADE DO CÓDIGO")
    print("=" * 70)

    print(f"\n{'Métrica':<30} {'Antes':<15} {'Depois':<15} {'Mudança':<10}")
    print("-" * 70)

    def fmt_change(before_val, after_val, lower_is_better=True):
        diff = after_val - before_val
        if lower_is_better:
            symbol = "✅" if diff < 0 else ("⚠️" if diff > 0 else "➖")
        else:
            symbol = "✅" if diff > 0 else ("⚠️" if diff < 0 else "➖")
        return f"{diff:+.1f} {symbol}" if isinstance(diff, float) else f"{diff:+d} {symbol}"

    metrics = [
        ("Linhas de Código", before.lines_of_code, after.lines_of_code, True),
        ("Contagem de Funções", before.function_count, after.function_count, False),
        ("Contagem de Classes", before.class_count, after.class_count, False),
        ("Complexidade Ciclomática", before.cyclomatic_complexity, after.cyclomatic_complexity, True),
        ("Complexidade Cognitiva", before.cognitive_complexity, after.cognitive_complexity, True),
        ("Índice de Manutenibilidade", before.maintainability_index, after.maintainability_index, False),
        ("Comprimento Médio de Função", before.avg_function_length, after.avg_function_length, True),
        ("Comprimento Máximo de Função", before.max_function_length, after.max_function_length, True),
    ]

    for name, b_val, a_val, lower_better in metrics:
        change = fmt_change(b_val, a_val, lower_better)
        print(f"{name:<30} {b_val:<15} {a_val:<15} {change:<10}")

    print("\n" + "=" * 70)

    # Avaliação geral
    print("\n🎯 AVALIAÇÃO")
    print("-" * 40)

    improvements = 0
    regressions = 0

    if after.maintainability_index > before.maintainability_index:
        print("  ✅ Manutenibilidade melhorou")
        improvements += 1
    elif after.maintainability_index < before.maintainability_index:
        print("  ⚠️ Manutenibilidade diminuiu")
        regressions += 1

    if after.cyclomatic_complexity < before.cyclomatic_complexity:
        print("  ✅ Complexidade reduzida")
        improvements += 1
    elif after.cyclomatic_complexity > before.cyclomatic_complexity:
        print("  ⚠️ Complexidade aumentou")
        regressions += 1

    if after.avg_function_length < before.avg_function_length:
        print("  ✅ Funções em média menores")
        improvements += 1
    elif after.avg_function_length > before.avg_function_length:
        print("  ⚠️ Funções em média maiores")
        regressions += 1

    print(f"\n  Resumo: {improvements} melhorias, {regressions} regressões")
    print("=" * 70)


def analyze_directory(directory: str, verbose: bool = False) -> None:
    """Analisa todos os arquivos suportados em um diretório."""
    supported_extensions = ['.py', '.js', '.jsx', '.ts', '.tsx']
    files = []

    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in supported_extensions):
                files.append(os.path.join(root, filename))

    if not files:
        print(f"Nenhum arquivo suportado encontrado em {directory}")
        return

    print(f"Analisando {len(files)} arquivo(s) em {directory}...\n")

    total_loc = 0
    total_cc = 0
    total_functions = 0
    all_metrics = []

    for filepath in sorted(files):
        try:
            analyzer = ComplexityAnalyzer(filepath)
            metrics = analyzer.analyze()
            all_metrics.append(metrics)

            total_loc += metrics.lines_of_code
            total_cc += metrics.cyclomatic_complexity
            total_functions += metrics.function_count

            if verbose:
                print_metrics(metrics, verbose=True)
            else:
                flag = " ⚠️" if metrics.maintainability_index < 65 else ""
                print(f"  {metrics.filename}: LOC={metrics.lines_of_code}, "
                      f"CC={metrics.cyclomatic_complexity}, MI={metrics.maintainability_index}{flag}")
        except Exception as e:
            print(f"  Erro ao analisar {filepath}: {e}")

    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    print(f"  Arquivos analisados:       {len(all_metrics)}")
    print(f"  Total de linhas de código: {total_loc}")
    print(f"  Complexidade total:        {total_cc}")
    print(f"  Total de funções:          {total_functions}")

    if all_metrics:
        avg_mi = sum(m.maintainability_index for m in all_metrics) / len(all_metrics)
        print(f"  Manutenibilidade média:    {avg_mi:.1f}")


def main():
    parser = argparse.ArgumentParser(
        description='Analisa métricas de complexidade de código',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s meuarquivo.py                    Analisa arquivo único
  %(prog)s antes.py depois.py               Compara duas versões
  %(prog)s --dir src/                       Analisa diretório
  %(prog)s -v meuarquivo.py                 Saída detalhada com métricas de função
        """
    )
    parser.add_argument('files', nargs='*', help='Arquivo(s) a analisar')
    parser.add_argument('--dir', '-d', help='Diretório a analisar')
    parser.add_argument('--verbose', '-v', action='store_true', help='Mostra métricas detalhadas de função')
    parser.add_argument('--json', '-j', action='store_true', help='Saída em formato JSON')

    args = parser.parse_args()

    if args.dir:
        analyze_directory(args.dir, args.verbose)
    elif len(args.files) == 1:
        analyzer = ComplexityAnalyzer(args.files[0])
        metrics = analyzer.analyze()

        if args.json:
            import json
            print(json.dumps({
                'filename': metrics.filename,
                'lines_of_code': metrics.lines_of_code,
                'cyclomatic_complexity': metrics.cyclomatic_complexity,
                'cognitive_complexity': metrics.cognitive_complexity,
                'maintainability_index': metrics.maintainability_index,
                'function_count': metrics.function_count,
                'avg_function_length': metrics.avg_function_length,
            }, indent=2))
        else:
            print_metrics(metrics, args.verbose)
    elif len(args.files) == 2:
        before_analyzer = ComplexityAnalyzer(args.files[0])
        after_analyzer = ComplexityAnalyzer(args.files[1])
        before_metrics = before_analyzer.analyze()
        after_metrics = after_analyzer.analyze()
        print_comparison(before_metrics, after_metrics)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
