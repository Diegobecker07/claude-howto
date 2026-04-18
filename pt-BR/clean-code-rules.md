<!-- i18n-source: clean-code-rules.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# Regras de Código Limpo para Geração de Código com IA

Estas regras guiam a geração de código para produzir código de qualidade profissional e manutenível.

## Nomes Significativos
- Use nomes que revelam a intenção e explicam por que algo existe
- Evite desinformação e distinções sem sentido (ex.: `data`, `info`, `manager`)
- Use nomes pronunciáveis e pesquisáveis
- Nomes de classe: substantivos (ex.: `UserAccount`, `PaymentProcessor`)
- Nomes de método: verbos (ex.: `calculateTotal`, `sendEmail`)
- Evite mapeamento mental e codificações (notação húngara, prefixos)

## Funções
- Mantenha funções pequenas (< 20 linhas ideal)
- Faça apenas uma coisa — Princípio da Responsabilidade Única
- Um nível de abstração por função
- Limite os argumentos: 0-2 ideal, 3 máximo, evite argumentos flag
- Sem efeitos colaterais — a função deve fazer o que seu nome diz
- Separe comandos (mudam estado) de queries (retornam informação)
- Prefira exceções a códigos de erro

## Comentários
- O código deve ser auto-explicativo — evite comentários quando possível
- Bons comentários: informações legais, avisos, TODOs, documentação de API pública
- Maus comentários: redundantes, enganosos ou explicando código ruim
- Nunca comente código — delete-o (o controle de versão preserva o histórico)
- Se precisar de um comentário, considere refatorar o código

## Formatação
- Mantenha arquivos pequenos e focados
- Formatação vertical: conceitos relacionados próximos, linhas em branco separam conceitos
- Formatação horizontal: limite o comprimento da linha (80-120 caracteres)
- Use indentação consistente e estilo de equipe
- Agrupe funções relacionadas

## Objetos e Estruturas de Dados
- Objetos: oculte dados por trás de abstrações, exponha comportamento por métodos
- Estruturas de dados: exponham dados, tenham comportamento mínimo
- Lei de Demeter: fale apenas com amigos imediatos, evite `a.getB().getC().doSomething()`
- Não exponha a estrutura interna por getters/setters cegamente

## Tratamento de Erros
- Use exceções, não códigos de retorno ou flags de erro
- Escreva `try-catch-finally` primeiro quando o código pode falhar
- Forneça contexto nas mensagens de exceção
- Não retorne `null` — retorne coleções vazias ou use Optional/Maybe
- Não passe `null` como argumento

## Classes
- Classes pequenas: medidas por responsabilidades, não por linhas
- Princípio da Responsabilidade Única: uma razão para mudar
- Alta coesão: variáveis de classe usadas por muitos métodos
- Baixo acoplamento: dependências mínimas entre classes
- Princípio Aberto/Fechado: aberto para extensão, fechado para modificação

## Testes Unitários
- Rápidos, Independentes, Repetíveis, Auto-validados, Pontuais (F.I.R.S.T.)
- Uma asserção por teste (ou um conceito)
- Qualidade do código de teste igual ao código de produção
- Nomes de teste legíveis que descrevem o que está sendo testado
- Padrão Arrange-Act-Assert

## Princípios de Qualidade de Código
- **DRY (Don't Repeat Yourself)**: Sem duplicação
- **YAGNI (You Aren't Gonna Need It)**: Não construa para futuros hipotéticos
- **KISS (Keep It Simple)**: Evite complexidade desnecessária
- **Regra do Escoteiro**: Deixe o código mais limpo do que encontrou

## Code Smells a Evitar
- Funções ou classes longas
- Código duplicado
- Código morto (variáveis, funções, parâmetros não utilizados)
- Feature envy (método mais interessado em outra classe)
- Intimidade inadequada (classes sabendo demais umas sobre as outras)
- Listas longas de parâmetros
- Obsessão por primitivos (usar primitivos em excesso em vez de pequenos objetos)
- Declarações switch/case (considere polimorfismo)
- Campos temporários (variáveis de classe usadas apenas às vezes)

## Concorrência
- Mantenha código concorrente separado do resto
- Limite o escopo de dados sincronizados/bloqueados
- Use coleções thread-safe
- Mantenha seções sincronizadas pequenas
- Conheça seus modelos de execução e primitivos

## Design de Sistema
- Separe construção de uso (injeção de dependências)
- Use factories, builders para criação de objetos complexos
- Programe para interfaces, não para implementações
- Prefira composição à herança
- Aplique padrões de design quando simplificam, não para demonstrar conhecimento

## Refatoração
- Refatore continuamente, não em grandes lotes
- Sempre tenha testes passando antes e depois
- Passos pequenos: uma mudança por vez
- Refatorações comuns: Extract Method, Rename, Move, Inline

## Documentação
- Código auto-documentado > comentários > documentos externos
- APIs públicas precisam de documentação clara
- Inclua exemplos na documentação
- Mantenha documentos próximos ao código (idealmente no código)

---

**Filosofia Central**: O código é lido 10x mais do que escrito. Otimize para legibilidade e manutenibilidade, não para esperteza.

---
**Última Atualização**: 9 de Abril de 2026
