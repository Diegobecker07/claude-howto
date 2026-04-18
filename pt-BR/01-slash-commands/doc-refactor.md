<!-- i18n-source: 01-slash-commands/doc-refactor.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->
---
name: Documentation Refactor
description: Reestruturar documentação do projeto para clareza e acessibilidade
tags: documentation, refactoring, organization
---

# Refatoração de Documentação

Refatore a estrutura de documentação do projeto adaptada ao tipo de projeto:

1. **Analisar o projeto**: Identificar tipo (biblioteca/API/web app/CLI/microsserviços), arquitetura e personas de usuários
2. **Centralizar docs**: Mover documentação técnica para `docs/` com referências cruzadas adequadas
3. **README.md raiz**: Simplificar como ponto de entrada com visão geral, quickstart, resumo de módulos/componentes, licença, contatos
4. **Docs de componente**: Adicionar arquivos README de nível de módulo/pacote/serviço com instruções de setup e teste
5. **Organizar `docs/`** por categorias relevantes:
   - Arquitetura, Referência de API, Banco de Dados, Design, Solução de Problemas, Implantação, Contribuição (adaptar às necessidades do projeto)
6. **Criar guias** (selecionar aplicáveis):
   - Guia do Usuário: Documentação para usuários finais de aplicações
   - Documentação de API: Endpoints, autenticação, exemplos para APIs
   - Guia de Desenvolvimento: Setup, testes, fluxo de contribuição
   - Guia de Implantação: Implantação em produção para serviços/apps
7. **Usar Mermaid** para todos os diagramas (arquitetura, fluxos, esquemas)

Mantenha a documentação concisa, escaneável e contextual ao tipo de projeto.

---
**Última Atualização**: 9 de abril de 2026
