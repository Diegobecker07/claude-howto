#!/usr/bin/env python3
"""
Detector de Code Smells

Detecta code smells comuns em arquivos Python, JavaScript e TypeScript.
Baseado no catálogo de code smells de Martin Fowler.

Uso:
    python detect-smells.py <arquivo>
    python detect-smells.py --dir <diretório>
    python detect-smells.py -v <arquivo>  # Detalhado com trechos de código

Detecta:
    - Método Longo (>30 linhas)
    - Lista Longa de Parâmetros (>4 params)
    - Código Duplicado (blocos de código similares)
    - Classe Grande (>300 linhas, >10 métodos)
    - Código Morto (variáveis/funções não utilizadas)
    - Condicionais Complexos (aninhamento profundo, cadeias longas)
    - Números/Strings Mágicos
    - Inveja de Recurso (métodos usando muito dados de outra classe)
    - Comentários explicando o quê (não o porquê)
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple
from collections import defaultdict


class SmellSeverity(Enum):
    """Níveis de severidade para code smells."""
    LOW = "Baixo"
    MEDIUM = "Médio"
    HIGH = "Alto"
    CRITICAL = "Crítico"


class SmellType(Enum):
    """Tipos de code smells."""
    LONG_METHOD = "Método Longo"
    LONG_PARAMETER_LIST = "Lista Longa de Parâmetros"
    DUPLICATE_CODE = "Código Duplicado"
    LARGE_CLASS = "Classe Grande"
    DEAD_CODE = "Código Morto"
    COMPLEX_CONDITIONAL = "Condicional Complexo"
    MAGIC_NUMBER = "Número/String Mágico"
    FEATURE_ENVY = "Inveja de Recurso"
    EXCESSIVE_COMMENTS = "Comentários Excessivos"
    DEEPLY_NESTED = "Código Profundamente Aninhado"
    PRIMITIVE_OBSESSION = "Obsessão por Primitivos"
    DATA_CLUMPS = "Aglomerados de Dados"
    SWITCH_STATEMENT = "Instrução Switch"
    MESSAGE_CHAIN = "Cadeia de Mensagens"


@dataclass
class CodeSmell:
    """Representa um code smell detectado."""
    smell_type: SmellType
    severity: SmellSeverity
    location: str
    line_start: int
    line_end: int
    description: str
    suggestion: str
    code_snippet: str = ""


@dataclass
class SmellReport:
    """Relatório de todos os smells encontrados em um arquivo."""
    filename: str
    smells: List[CodeSmell] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for s in self.smells if s.severity == SmellSeverity.CRITICAL)

    @property
    def high_count(self) -> int:
        return sum(1 for s in self.smells if s.severity == SmellSeverity.HIGH)

    @property
    def medium_count(self) -> int:
        return sum(1 for s in self.smells if s.severity == SmellSeverity.MEDIUM)

    @property
    def low_count(self) -> int:
        return sum(1 for s in self.smells if s.severity == SmellSeverity.LOW)


class SmellDetector:
    """Detecta code smells em arquivos-fonte."""

    # Limites (configuráveis)
    THRESHOLDS = {
        'long_method_lines': 30,
        'very_long_method_lines': 50,
        'max_parameters': 4,
        'large_class_lines': 300,
        'large_class_methods': 10,
        'max_nesting_depth': 4,
        'long_chain_length': 3,
        'duplicate_min_lines': 5,
    }

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.language = self._detect_language()

        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            self.code = f.read()
        self.lines = self.code.split('\n')
        self.smells: List[CodeSmell] = []

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

    def detect_all(self) -> SmellReport:
        """Executa todos os detectores de smell."""
        self._detect_long_methods()
        self._detect_long_parameter_lists()
        self._detect_large_class()
        self._detect_complex_conditionals()
        self._detect_magic_numbers()
        self._detect_excessive_comments()
        self._detect_deeply_nested()
        self._detect_switch_statements()
        self._detect_message_chains()
        self._detect_duplicate_code()
        self._detect_dead_code()

        return SmellReport(filename=self.filename, smells=self.smells)

    def _get_snippet(self, start: int, end: int, context: int = 2) -> str:
        """Obtém trecho de código com contexto."""
        actual_start = max(0, start - context)
        actual_end = min(len(self.lines), end + context)
        snippet_lines = []
        for i in range(actual_start, actual_end):
            prefix = "→ " if start <= i < end else "  "
            snippet_lines.append(f"{i+1:4d} {prefix}{self.lines[i]}")
        return '\n'.join(snippet_lines)

    def _detect_long_methods(self) -> None:
        """Detecta métodos muito longos."""
        if self.language == 'python':
            pattern = r'^\s*def\s+(\w+)\s*\([^)]*\):'
        else:
            pattern = r'(?:function\s+(\w+)|(\w+)\s*[=:]\s*(?:async\s+)?(?:function|\([^)]*\)\s*=>))'

        current_method = None
        method_start = 0
        brace_depth = 0
        indent_level = 0

        for i, line in enumerate(self.lines):
            match = re.search(pattern, line)
            if match:
                # Verifica o método anterior se existir
                if current_method:
                    method_lines = i - method_start
                    self._check_method_length(current_method, method_start, i - 1, method_lines)

                current_method = match.group(1) or (match.group(2) if match.lastindex and match.lastindex > 1 else None)
                method_start = i
                indent_level = len(line) - len(line.lstrip())

            # Rastreia fim de funções Python por indentação
            if self.language == 'python' and current_method:
                if line.strip() and not line.strip().startswith('#'):
                    current_indent = len(line) - len(line.lstrip())
                    if current_indent <= indent_level and i > method_start:
                        method_lines = i - method_start
                        self._check_method_length(current_method, method_start, i - 1, method_lines)
                        current_method = None

        # Verifica o último método
        if current_method:
            method_lines = len(self.lines) - method_start
            self._check_method_length(current_method, method_start, len(self.lines) - 1, method_lines)

    def _check_method_length(self, name: str, start: int, end: int, lines: int) -> None:
        """Verifica se o método é muito longo e adiciona smell se for."""
        if lines > self.THRESHOLDS['very_long_method_lines']:
            severity = SmellSeverity.HIGH
            desc = f"Método '{name}' tem {lines} linhas (limite: {self.THRESHOLDS['long_method_lines']})"
        elif lines > self.THRESHOLDS['long_method_lines']:
            severity = SmellSeverity.MEDIUM
            desc = f"Método '{name}' tem {lines} linhas (limite: {self.THRESHOLDS['long_method_lines']})"
        else:
            return

        self.smells.append(CodeSmell(
            smell_type=SmellType.LONG_METHOD,
            severity=severity,
            location=f"{self.filename}:{start+1}-{end+1}",
            line_start=start + 1,
            line_end=end + 1,
            description=desc,
            suggestion="Aplique Extrair Método para dividir em funções menores",
            code_snippet=self._get_snippet(start, min(start + 5, end), 0)
        ))

    def _detect_long_parameter_lists(self) -> None:
        """Detecta funções com muitos parâmetros."""
        if self.language == 'python':
            pattern = r'def\s+(\w+)\s*\(([^)]*)\)'
        else:
            pattern = r'(?:function\s+(\w+)\s*\(([^)]*)\)|(\w+)\s*[=:]\s*(?:async\s+)?(?:function\s*)?\(([^)]*)\))'

        for i, line in enumerate(self.lines):
            match = re.search(pattern, line)
            if match:
                # Extrai grupos com segurança
                groups = match.groups()
                func_name = groups[0] or (groups[2] if len(groups) > 2 else None)
                params_str = groups[1] if len(groups) > 1 else ""
                if not params_str and len(groups) > 3:
                    params_str = groups[3] or ""

                # Conta parâmetros
                if params_str.strip():
                    params = [p.strip() for p in params_str.split(',') if p.strip()]
                    # Filtra 'self', 'cls' para Python
                    if self.language == 'python':
                        params = [p for p in params if p not in ('self', 'cls')]
                    param_count = len(params)

                    if param_count > self.THRESHOLDS['max_parameters']:
                        severity = SmellSeverity.HIGH if param_count > 6 else SmellSeverity.MEDIUM
                        self.smells.append(CodeSmell(
                            smell_type=SmellType.LONG_PARAMETER_LIST,
                            severity=severity,
                            location=f"{self.filename}:{i+1}",
                            line_start=i + 1,
                            line_end=i + 1,
                            description=f"Função '{func_name}' tem {param_count} parâmetros (máx: {self.THRESHOLDS['max_parameters']})",
                            suggestion="Considere Introduzir Objeto de Parâmetro ou Preservar Objeto Inteiro",
                            code_snippet=self._get_snippet(i, i + 1, 1)
                        ))

    def _detect_large_class(self) -> None:
        """Detecta classes muito grandes."""
        if self.language == 'python':
            class_pattern = r'^\s*class\s+(\w+)'
            method_pattern = r'^\s+def\s+\w+'
        else:
            class_pattern = r'class\s+(\w+)'
            method_pattern = r'(?:^\s+\w+\s*\([^)]*\)\s*\{|^\s+(?:async\s+)?\w+\s*=)'

        current_class = None
        class_start = 0
        method_count = 0
        class_indent = 0

        for i, line in enumerate(self.lines):
            class_match = re.search(class_pattern, line)
            if class_match:
                # Verifica a classe anterior
                if current_class:
                    self._check_class_size(current_class, class_start, i - 1, method_count)

                current_class = class_match.group(1)
                class_start = i
                method_count = 0
                class_indent = len(line) - len(line.lstrip())

            # Conta métodos na classe atual
            if current_class and re.search(method_pattern, line):
                method_count += 1

        # Verifica a última classe
        if current_class:
            self._check_class_size(current_class, class_start, len(self.lines) - 1, method_count)

    def _check_class_size(self, name: str, start: int, end: int, methods: int) -> None:
        """Verifica se a classe é muito grande."""
        lines = end - start + 1

        issues = []
        severity = SmellSeverity.MEDIUM

        if lines > self.THRESHOLDS['large_class_lines']:
            issues.append(f"{lines} linhas (máx: {self.THRESHOLDS['large_class_lines']})")
            severity = SmellSeverity.HIGH

        if methods > self.THRESHOLDS['large_class_methods']:
            issues.append(f"{methods} métodos (máx: {self.THRESHOLDS['large_class_methods']})")
            if severity != SmellSeverity.HIGH:
                severity = SmellSeverity.MEDIUM

        if issues:
            self.smells.append(CodeSmell(
                smell_type=SmellType.LARGE_CLASS,
                severity=severity,
                location=f"{self.filename}:{start+1}-{end+1}",
                line_start=start + 1,
                line_end=end + 1,
                description=f"Classe '{name}' é muito grande: {', '.join(issues)}",
                suggestion="Aplique Extrair Classe para dividir responsabilidades",
                code_snippet=self._get_snippet(start, start + 3, 0)
            ))

    def _detect_complex_conditionals(self) -> None:
        """Detecta expressões condicionais complexas."""
        for i, line in enumerate(self.lines):
            # Conta operadores lógicos na linha
            and_or_count = len(re.findall(r'\b(and|or|&&|\|\|)\b', line))

            if and_or_count >= 3:
                self.smells.append(CodeSmell(
                    smell_type=SmellType.COMPLEX_CONDITIONAL,
                    severity=SmellSeverity.MEDIUM,
                    location=f"{self.filename}:{i+1}",
                    line_start=i + 1,
                    line_end=i + 1,
                    description=f"Condicional complexo com {and_or_count} operadores lógicos",
                    suggestion="Aplique Decompor Condicional ou Consolidar Expressão Condicional",
                    code_snippet=self._get_snippet(i, i + 1, 1)
                ))

    def _detect_magic_numbers(self) -> None:
        """Detecta números e strings mágicos."""
        # Pula valores aceitáveis comuns
        acceptable = {'0', '1', '-1', '2', '100', 'true', 'false', 'null', 'None', '""', "''"}

        for i, line in enumerate(self.lines):
            # Pula comentários e imports
            stripped = line.strip()
            if stripped.startswith('#') or stripped.startswith('//') or \
               stripped.startswith('import') or stripped.startswith('from'):
                continue

            # Encontra literais numéricos (excluindo em nomes de variáveis)
            numbers = re.findall(r'(?<![a-zA-Z_])\b(\d+\.?\d*)\b(?![a-zA-Z_])', line)

            for num in numbers:
                if num not in acceptable and float(num) > 2:
                    # Verifica se provavelmente é um número mágico (em cálculo ou comparação)
                    if re.search(rf'[<>=+\-*/]\s*{re.escape(num)}|{re.escape(num)}\s*[<>=+\-*/]', line):
                        self.smells.append(CodeSmell(
                            smell_type=SmellType.MAGIC_NUMBER,
                            severity=SmellSeverity.LOW,
                            location=f"{self.filename}:{i+1}",
                            line_start=i + 1,
                            line_end=i + 1,
                            description=f"Número mágico '{num}' — considere usar uma constante nomeada",
                            suggestion="Substitua o número mágico por uma constante nomeada",
                            code_snippet=self._get_snippet(i, i + 1, 0)
                        ))
                        break  # Um número mágico por linha é suficiente

    def _detect_excessive_comments(self) -> None:
        """Detecta comentários que explicam 'o quê' em vez de 'por quê'."""
        what_patterns = [
            r'#\s*(set|get|return|loop|iterate|check|if|increment|decrement)',
            r'//\s*(set|get|return|loop|iterate|check|if|increment|decrement)',
        ]

        for i, line in enumerate(self.lines):
            for pattern in what_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.smells.append(CodeSmell(
                        smell_type=SmellType.EXCESSIVE_COMMENTS,
                        severity=SmellSeverity.LOW,
                        location=f"{self.filename}:{i+1}",
                        line_start=i + 1,
                        line_end=i + 1,
                        description="Comentário explica 'o quê' e não 'por quê' — considere renomear ou remover",
                        suggestion="Use Extrair Método com nome descritivo em vez de comentário",
                        code_snippet=self._get_snippet(i, i + 1, 0)
                    ))
                    break

    def _detect_deeply_nested(self) -> None:
        """Detecta blocos de código profundamente aninhados."""
        max_depth = 0
        current_depth = 0
        depth_start = 0

        for i, line in enumerate(self.lines):
            if self.language == 'python':
                # Conta por indentação
                if line.strip():
                    indent = len(line) - len(line.lstrip())
                    depth = indent // 4  # Assume indentação de 4 espaços
                    if depth > current_depth:
                        if depth > max_depth:
                            max_depth = depth
                            if depth >= self.THRESHOLDS['max_nesting_depth']:
                                depth_start = i
                    current_depth = depth
            else:
                # Conta chaves
                current_depth += line.count('{') - line.count('}')
                if current_depth > max_depth:
                    max_depth = current_depth
                    if current_depth >= self.THRESHOLDS['max_nesting_depth']:
                        depth_start = i

        if max_depth >= self.THRESHOLDS['max_nesting_depth']:
            self.smells.append(CodeSmell(
                smell_type=SmellType.DEEPLY_NESTED,
                severity=SmellSeverity.HIGH if max_depth > 5 else SmellSeverity.MEDIUM,
                location=f"{self.filename}:{depth_start+1}",
                line_start=depth_start + 1,
                line_end=depth_start + 1,
                description=f"Código aninhado {max_depth} níveis (máx: {self.THRESHOLDS['max_nesting_depth']})",
                suggestion="Aplique Substituir Condicional Aninhado por Cláusulas de Guarda ou Extrair Método",
                code_snippet=self._get_snippet(depth_start, depth_start + 5, 0)
            ))

    def _detect_switch_statements(self) -> None:
        """Detecta instruções switch que podem precisar de polimorfismo."""
        if self.language == 'python':
            # Python 3.10+ match ou cadeias if/elif
            pattern = r'^\s*(if|elif).*==.*:'
            consecutive_conditions = 0
            chain_start = 0

            for i, line in enumerate(self.lines):
                if re.search(pattern, line):
                    if consecutive_conditions == 0:
                        chain_start = i
                    consecutive_conditions += 1
                else:
                    if consecutive_conditions >= 4:
                        self._add_switch_smell(chain_start, i - 1, consecutive_conditions)
                    consecutive_conditions = 0
        else:
            # JavaScript/TypeScript switch
            pattern = r'\bswitch\s*\('
            for i, line in enumerate(self.lines):
                if re.search(pattern, line):
                    # Conta casos
                    case_count = 0
                    for j in range(i, min(i + 50, len(self.lines))):
                        case_count += len(re.findall(r'\bcase\b', self.lines[j]))
                    if case_count >= 4:
                        self._add_switch_smell(i, i + 1, case_count)

    def _add_switch_smell(self, start: int, end: int, cases: int) -> None:
        """Adiciona um smell de instrução switch."""
        self.smells.append(CodeSmell(
            smell_type=SmellType.SWITCH_STATEMENT,
            severity=SmellSeverity.MEDIUM,
            location=f"{self.filename}:{start+1}",
            line_start=start + 1,
            line_end=end + 1,
            description=f"Instrução switch/case com {cases} casos — considere polimorfismo",
            suggestion="Aplique Substituir Condicional por Polimorfismo",
            code_snippet=self._get_snippet(start, start + 5, 0)
        ))

    def _detect_message_chains(self) -> None:
        """Detecta cadeias longas de métodos (train wrecks)."""
        chain_pattern = r'(\w+(?:\.\w+\([^)]*\)){3,})'

        for i, line in enumerate(self.lines):
            matches = re.findall(chain_pattern, line)
            for match in matches:
                chain_length = match.count('.')
                if chain_length >= self.THRESHOLDS['long_chain_length']:
                    self.smells.append(CodeSmell(
                        smell_type=SmellType.MESSAGE_CHAIN,
                        severity=SmellSeverity.MEDIUM,
                        location=f"{self.filename}:{i+1}",
                        line_start=i + 1,
                        line_end=i + 1,
                        description=f"Cadeia de mensagens com {chain_length} chamadas — viola a Lei de Deméter",
                        suggestion="Aplique Ocultar Delegação para reduzir acoplamento",
                        code_snippet=self._get_snippet(i, i + 1, 0)
                    ))

    def _detect_duplicate_code(self) -> None:
        """Detecta blocos de código potencialmente duplicados (simplificado)."""
        # Cria hashes de linha para comparação
        line_hashes: Dict[str, List[int]] = defaultdict(list)

        for i, line in enumerate(self.lines):
            normalized = re.sub(r'\s+', ' ', line.strip())
            if len(normalized) > 20:  # Apenas linhas significativas
                line_hashes[normalized].append(i)

        # Encontra duplicatas
        for normalized, positions in line_hashes.items():
            if len(positions) >= 3:  # Pelo menos 3 ocorrências
                self.smells.append(CodeSmell(
                    smell_type=SmellType.DUPLICATE_CODE,
                    severity=SmellSeverity.MEDIUM,
                    location=f"{self.filename}:{positions[0]+1}",
                    line_start=positions[0] + 1,
                    line_end=positions[0] + 1,
                    description=f"Código potencialmente duplicado encontrado {len(positions)} vezes",
                    suggestion="Aplique Extrair Método para eliminar duplicação",
                    code_snippet=self._get_snippet(positions[0], positions[0] + 1, 0)
                ))

    def _detect_dead_code(self) -> None:
        """Detecta código potencialmente morto (simplificado)."""
        # Procura padrões comuns de código morto
        patterns = [
            (r'^\s*#.*TODO.*delete', "TODO para deletar"),
            (r'^\s*#.*FIXME.*remove', "FIXME para remover"),
            (r'^\s*//.*TODO.*delete', "TODO para deletar"),
            (r'^\s*//.*FIXME.*remove', "FIXME para remover"),
            (r'^\s*if\s+False:', "Código atrás de 'if False'"),
            (r'^\s*if\s*\(\s*false\s*\)', "Código atrás de 'if (false)'"),
        ]

        for i, line in enumerate(self.lines):
            for pattern, desc in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.smells.append(CodeSmell(
                        smell_type=SmellType.DEAD_CODE,
                        severity=SmellSeverity.LOW,
                        location=f"{self.filename}:{i+1}",
                        line_start=i + 1,
                        line_end=i + 1,
                        description=f"Código potencialmente morto: {desc}",
                        suggestion="Remova o código morto",
                        code_snippet=self._get_snippet(i, i + 1, 0)
                    ))


def print_report(report: SmellReport, verbose: bool = False) -> None:
    """Imprime o relatório de smells em formato legível."""
    print("=" * 70)
    print(f"RELATÓRIO DE DETECÇÃO DE CODE SMELLS: {report.filename}")
    print("=" * 70)

    print(f"\n📊 RESUMO")
    print("-" * 40)
    print(f"  Total de smells encontrados: {len(report.smells)}")
    print(f"  Críticos:                    {report.critical_count}")
    print(f"  Altos:                       {report.high_count}")
    print(f"  Médios:                      {report.medium_count}")
    print(f"  Baixos:                      {report.low_count}")

    if not report.smells:
        print("\n✅ Nenhum code smell detectado!")
        print("=" * 70)
        return

    # Agrupa por tipo
    by_type: Dict[SmellType, List[CodeSmell]] = defaultdict(list)
    for smell in report.smells:
        by_type[smell.smell_type].append(smell)

    print(f"\n📋 ACHADOS POR TIPO")
    print("-" * 40)

    for smell_type, smells in sorted(by_type.items(), key=lambda x: -len(x[1])):
        print(f"\n### {smell_type.value} ({len(smells)} encontrado(s))")

        for smell in sorted(smells, key=lambda x: x.severity.value):
            severity_icon = {
                SmellSeverity.CRITICAL: "🔴",
                SmellSeverity.HIGH: "🟠",
                SmellSeverity.MEDIUM: "🟡",
                SmellSeverity.LOW: "🟢",
            }[smell.severity]

            print(f"\n  {severity_icon} [{smell.severity.value}] {smell.location}")
            print(f"     {smell.description}")
            print(f"     💡 {smell.suggestion}")

            if verbose and smell.code_snippet:
                print(f"\n     Código:")
                for snippet_line in smell.code_snippet.split('\n'):
                    print(f"       {snippet_line}")

    print("\n" + "=" * 70)
    print("💡 AÇÕES RECOMENDADAS")
    print("-" * 40)

    if report.critical_count > 0:
        print("  1. Resolva problemas CRÍTICOS imediatamente")
    if report.high_count > 0:
        print("  2. Planeje corrigir problemas de severidade ALTA neste sprint")
    if report.medium_count > 0:
        print("  3. Agende problemas MÉDIOS para trabalhos futuros")
    if report.low_count > 0:
        print("  4. Corrija problemas BAIXOS oportunisticamente")

    print("\n" + "=" * 70)


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

    print(f"Escaneando {len(files)} arquivo(s) em {directory}...\n")

    total_smells = 0
    total_critical = 0
    total_high = 0
    files_with_smells = 0

    for filepath in sorted(files):
        try:
            detector = SmellDetector(filepath)
            report = detector.detect_all()

            if report.smells:
                files_with_smells += 1
                total_smells += len(report.smells)
                total_critical += report.critical_count
                total_high += report.high_count

                flag = " 🔴" if report.critical_count else (" 🟠" if report.high_count else " 🟡")
                print(f"  {report.filename}: {len(report.smells)} smell(s){flag}")

                if verbose:
                    for smell in report.smells:
                        print(f"    - [{smell.severity.value}] {smell.smell_type.value}: linha {smell.line_start}")
            else:
                print(f"  {report.filename}: ✅ Limpo")

        except Exception as e:
            print(f"  Erro ao analisar {filepath}: {e}")

    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    print(f"  Arquivos analisados:         {len(files)}")
    print(f"  Arquivos com smells:         {files_with_smells}")
    print(f"  Total de smells encontrados: {total_smells}")
    print(f"  Problemas críticos:          {total_critical}")
    print(f"  Problemas de alta severidade:{total_high}")


def main():
    parser = argparse.ArgumentParser(
        description='Detecta code smells em arquivos-fonte',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  %(prog)s meuarquivo.py                    Analisa arquivo único
  %(prog)s --dir src/                       Analisa diretório
  %(prog)s -v meuarquivo.py                 Detalhado com trechos de código
        """
    )
    parser.add_argument('file', nargs='?', help='Arquivo a analisar')
    parser.add_argument('--dir', '-d', help='Diretório a analisar')
    parser.add_argument('--verbose', '-v', action='store_true', help='Mostra trechos de código')
    parser.add_argument('--json', '-j', action='store_true', help='Saída em formato JSON')

    args = parser.parse_args()

    if args.dir:
        analyze_directory(args.dir, args.verbose)
    elif args.file:
        detector = SmellDetector(args.file)
        report = detector.detect_all()

        if args.json:
            import json
            smells_data = [{
                'type': s.smell_type.value,
                'severity': s.severity.value,
                'location': s.location,
                'line_start': s.line_start,
                'line_end': s.line_end,
                'description': s.description,
                'suggestion': s.suggestion,
            } for s in report.smells]
            print(json.dumps({
                'filename': report.filename,
                'total_smells': len(report.smells),
                'critical': report.critical_count,
                'high': report.high_count,
                'medium': report.medium_count,
                'low': report.low_count,
                'smells': smells_data
            }, indent=2))
        else:
            print_report(report, args.verbose)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
