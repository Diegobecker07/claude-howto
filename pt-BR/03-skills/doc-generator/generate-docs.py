#!/usr/bin/env python3
import ast


class APIDocExtractor(ast.NodeVisitor):
    """Extrai documentação de API do código-fonte Python."""

    def __init__(self):
        self.endpoints = []

    def visit_FunctionDef(self, node):
        """Extrai documentação de funções."""
        if node.name.startswith("get_") or node.name.startswith("post_"):
            doc = ast.get_docstring(node)
            endpoint = {
                "name": node.name,
                "docstring": doc,
                "params": [arg.arg for arg in node.args.args],
                "returns": self._extract_return_type(node),
            }
            self.endpoints.append(endpoint)
        self.generic_visit(node)

    def _extract_return_type(self, node):
        """Extrai o tipo de retorno da anotação da função."""
        if node.returns:
            return ast.unparse(node.returns)
        return "Any"


def generate_markdown_docs(endpoints: list[dict]) -> str:
    """Gera documentação markdown a partir dos endpoints."""
    docs = "# Documentação da API\n\n"

    for endpoint in endpoints:
        docs += f"## {endpoint['name']}\n\n"
        docs += f"{endpoint['docstring']}\n\n"
        docs += f"**Parâmetros**: {', '.join(endpoint['params'])}\n\n"
        docs += f"**Retorna**: {endpoint['returns']}\n\n"
        docs += "---\n\n"

    return docs


if __name__ == "__main__":
    import sys

    with open(sys.argv[1]) as f:
        tree = ast.parse(f.read())

    extractor = APIDocExtractor()
    extractor.visit(tree)

    markdown = generate_markdown_docs(extractor.endpoints)
    print(markdown)
