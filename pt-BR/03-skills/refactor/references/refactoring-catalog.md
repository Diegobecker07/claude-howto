<!-- i18n-source: 03-skills/refactor/references/refactoring-catalog.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# Catálogo de Refatorações

Um catálogo selecionado de técnicas de refatoração do livro *Refactoring* (2ª Edição) de Martin Fowler. Cada refatoração inclui motivação, mecânica passo a passo e exemplos.

> "Uma refatoração é definida pela sua mecânica — a sequência precisa de passos que você segue para realizar a mudança." — Martin Fowler

---

## Como Usar Este Catálogo

1. **Identifique o smell** usando a referência de code smells
2. **Encontre a refatoração correspondente** neste catálogo
3. **Siga a mecânica** passo a passo
4. **Teste após cada passo** para garantir que o comportamento foi preservado

**Regra de Ouro**: Se algum passo levar mais de 10 minutos, divida-o em passos menores.

---

## Refatorações Mais Comuns

### Extract Method (Extrair Método)

**Quando usar**: Método longo, código duplicado, necessidade de nomear um conceito

**Motivação**: Transformar um fragmento de código em um método cujo nome explica o propósito.

**Mecânica**:
1. Crie um novo método nomeado pelo que ele faz (não como)
2. Copie o fragmento de código para o novo método
3. Verifique as variáveis locais usadas no fragmento
4. Passe variáveis locais como parâmetros (ou declare no método)
5. Trate os valores de retorno adequadamente
6. Substitua o fragmento original por uma chamada ao novo método
7. Teste

**Antes**:
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // Calculate outstanding
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // Print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**Depois**:
```javascript
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

---

### Inline Method (Método Inline)

**Quando usar**: O corpo do método é tão claro quanto seu nome; delegação excessiva

**Motivação**: Remover indireção desnecessária quando o método não agrega valor.

**Mecânica**:
1. Verifique que o método não é polimórfico
2. Encontre todas as chamadas ao método
3. Substitua cada chamada pelo corpo do método
4. Teste após cada substituição
5. Remova a definição do método

**Antes**:
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**Depois**:
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### Extract Variable (Extrair Variável)

**Quando usar**: Expressão complexa difícil de entender

**Motivação**: Dar um nome a uma parte de uma expressão complexa.

**Mecânica**:
1. Verifique que a expressão não tem efeitos colaterais
2. Declare uma variável imutável
3. Atribua a ela o resultado da expressão (ou parte)
4. Substitua a expressão original pela variável
5. Teste

**Antes**:
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**Depois**:
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### Inline Variable (Variável Inline)

**Quando usar**: O nome da variável não comunica mais do que a expressão

**Motivação**: Remover indireção desnecessária.

**Mecânica**:
1. Verifique que o lado direito não tem efeitos colaterais
2. Se a variável não for imutável, torne-a assim e teste
3. Encontre a primeira referência e substitua pela expressão
4. Teste
5. Repita para todas as referências
6. Remova a declaração e atribuição
7. Teste

---

### Rename Variable (Renomear Variável)

**Quando usar**: O nome não comunica claramente o propósito

**Motivação**: Bons nomes são cruciais para código limpo.

**Mecânica**:
1. Se a variável for amplamente usada, considere encapsulá-la
2. Encontre todas as referências
3. Altere cada referência
4. Teste

**Dicas**:
- Use nomes que revelam a intenção
- Evite abreviações
- Use terminologia de domínio

```javascript
// Ruim
const d = 30;
const x = users.filter(u => u.a);

// Bom
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### Change Function Declaration (Alterar Declaração de Função)

**Quando usar**: O nome da função não explica o propósito; os parâmetros precisam de mudança

**Motivação**: Bons nomes de função tornam o código auto-documentado.

**Mecânica (Simples)**:
1. Remova parâmetros não necessários
2. Altere o nome
3. Adicione os parâmetros necessários
4. Teste

**Mecânica (Migração — para alterações complexas)**:
1. Se remover parâmetro, certifique-se de que não está sendo usado
2. Crie nova função com a declaração desejada
3. Faça a função antiga chamar a nova
4. Teste
5. Mude os chamadores para usar a nova função
6. Teste após cada um
7. Remova a função antiga

**Antes**:
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**Depois**:
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### Encapsulate Variable (Encapsular Variável)

**Quando usar**: Acesso direto a dados a partir de múltiplos lugares

**Motivação**: Fornecer um ponto de acesso claro para manipulação de dados.

**Mecânica**:
1. Crie funções getter e setter
2. Encontre todas as referências
3. Substitua leituras pelo getter
4. Substitua escritas pelo setter
5. Teste após cada alteração
6. Restrinja a visibilidade da variável

**Antes**:
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// Used in many places
spaceship.owner = defaultOwner;
```

**Depois**:
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### Introduce Parameter Object (Introduzir Objeto de Parâmetro)

**Quando usar**: Vários parâmetros que frequentemente andam juntos

**Motivação**: Agrupar dados que naturalmente pertencem juntos.

**Mecânica**:
1. Crie uma nova classe/estrutura para os parâmetros agrupados
2. Teste
3. Use Change Function Declaration para adicionar o novo objeto
4. Teste
5. Para cada parâmetro do grupo, remova-o da função e use o novo objeto
6. Teste após cada um

**Antes**:
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**Depois**:
```javascript
class DateRange {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }
}

function amountInvoiced(dateRange) { ... }
function amountReceived(dateRange) { ... }
function amountOverdue(dateRange) { ... }
```

---

### Combine Functions into Class (Combinar Funções em Classe)

**Quando usar**: Várias funções operam sobre os mesmos dados

**Motivação**: Agrupar funções com os dados sobre os quais operam.

**Mecânica**:
1. Aplique Encapsulate Record nos dados comuns
2. Mova cada função para a classe
3. Teste após cada movimentação
4. Substitua argumentos de dados pelo uso dos campos da classe

**Antes**:
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**Depois**:
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### Split Phase (Dividir Fase)

**Quando usar**: O código lida com duas coisas diferentes

**Motivação**: Separar o código em fases distintas com fronteiras claras.

**Mecânica**:
1. Crie uma segunda função para a segunda fase
2. Teste
3. Introduza uma estrutura de dados intermediária entre as fases
4. Teste
5. Extraia a primeira fase em sua própria função
6. Teste

**Antes**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  const shippingPerCase = (basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = quantity * shippingPerCase;
  return basePrice - discount + shippingCost;
}
```

**Depois**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const priceData = calculatePricingData(product, quantity);
  return applyShipping(priceData, shippingMethod);
}

function calculatePricingData(product, quantity) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  return { basePrice, quantity, discount };
}

function applyShipping(priceData, shippingMethod) {
  const shippingPerCase = (priceData.basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = priceData.quantity * shippingPerCase;
  return priceData.basePrice - priceData.discount + shippingCost;
}
```

---

## Movendo Funcionalidades (Moving Features)

### Move Method (Mover Método)

**Quando usar**: O método usa mais funcionalidades de outra classe do que da própria

**Motivação**: Coloque funções junto dos dados que mais usam.

**Mecânica**:
1. Examine todos os elementos do programa usados pelo método em sua classe
2. Verifique se o método é polimórfico
3. Copie o método para a classe alvo
4. Ajuste para o novo contexto
5. Faça o método original delegar para o alvo
6. Teste
7. Considere remover o método original

---

### Move Field (Mover Campo)

**Quando usar**: O campo é mais usado por outra classe

**Motivação**: Mantenha os dados com as funções que os usam.

**Mecânica**:
1. Encapsule o campo se ainda não estiver
2. Teste
3. Crie o campo na classe alvo
4. Atualize as referências para usar o campo alvo
5. Teste
6. Remova o campo original

---

### Move Statements into Function (Mover Declarações para a Função)

**Quando usar**: O mesmo código sempre aparece com uma chamada de função

**Motivação**: Remover duplicação movendo o código repetido para dentro da função.

**Mecânica**:
1. Extraia o código repetido em uma função se ainda não estiver
2. Mova as declarações para essa função
3. Teste
4. Se os chamadores não precisarem mais das declarações isoladas, remova-as

---

### Move Statements to Callers (Mover Declarações para os Chamadores)

**Quando usar**: O comportamento comum varia entre os chamadores

**Motivação**: Quando o comportamento precisa ser diferente, mova-o para fora da função.

**Mecânica**:
1. Use Extract Method no código a ser movido
2. Use Inline Method na função original
3. Remova a chamada inline
4. Mova o código extraído para cada chamador
5. Teste

---

## Organizando Dados (Organizing Data)

### Replace Primitive with Object (Substituir Primitivo por Objeto)

**Quando usar**: Um item de dados precisa de mais comportamento do que um simples valor

**Motivação**: Encapsular dados com seu comportamento.

**Mecânica**:
1. Aplique Encapsulate Variable
2. Crie uma classe de valor simples
3. Altere o setter para criar uma nova instância
4. Altere o getter para retornar o valor
5. Teste
6. Adicione comportamento mais rico à nova classe

**Antes**:
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // string: "high", "rush", etc.
  }
}

// Usage
if (order.priority === "high" || order.priority === "rush") { ... }
```

**Depois**:
```javascript
class Priority {
  constructor(value) {
    if (!Priority.legalValues().includes(value))
      throw new Error(`Invalid priority: ${value}`);
    this._value = value;
  }

  static legalValues() { return ['low', 'normal', 'high', 'rush']; }
  get value() { return this._value; }

  higherThan(other) {
    return Priority.legalValues().indexOf(this._value) >
           Priority.legalValues().indexOf(other._value);
  }
}

// Usage
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### Replace Temp with Query (Substituir Temp por Query)

**Quando usar**: Variável temporária contém o resultado de uma expressão

**Motivação**: Tornar o código mais claro extraindo a expressão em uma função.

**Mecânica**:
1. Verifique que a variável é atribuída apenas uma vez
2. Extraia o lado direito da atribuição em um método
3. Substitua as referências ao temp pela chamada do método
4. Teste
5. Remova a declaração e atribuição do temp

**Antes**:
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**Depois**:
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// In the method
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## Simplificando a Lógica Condicional (Simplifying Conditional Logic)

### Decompose Conditional (Decompor Condicional)

**Quando usar**: Declaração condicional complexa (if-then-else)

**Motivação**: Tornar a intenção clara extraindo condições e ações.

**Mecânica**:
1. Aplique Extract Method na condição
2. Aplique Extract Method no ramo then
3. Aplique Extract Method no ramo else (se presente)

**Antes**:
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**Depois**:
```javascript
if (isSummer(aDate, plan)) {
  charge = summerCharge(quantity, plan);
} else {
  charge = regularCharge(quantity, plan);
}

function isSummer(date, plan) {
  return !date.isBefore(plan.summerStart) && !date.isAfter(plan.summerEnd);
}

function summerCharge(quantity, plan) {
  return quantity * plan.summerRate;
}

function regularCharge(quantity, plan) {
  return quantity * plan.regularRate + plan.regularServiceCharge;
}
```

---

### Consolidate Conditional Expression (Consolidar Expressão Condicional)

**Quando usar**: Múltiplas condições com o mesmo resultado

**Motivação**: Deixar claro que as condições são uma única verificação.

**Mecânica**:
1. Verifique que não há efeitos colaterais nas condições
2. Combine as condições usando `and` ou `or`
3. Considere Extract Method na condição combinada

**Antes**:
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**Depois**:
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### Replace Nested Conditional with Guard Clauses (Substituir Condicional Aninhado por Cláusulas de Guarda)

**Quando usar**: Condicionais profundamente aninhados tornando o fluxo difícil de seguir

**Motivação**: Usar cláusulas de guarda para casos especiais, mantendo o fluxo normal claro.

**Mecânica**:
1. Encontre as condições de casos especiais
2. Substitua-as por cláusulas de guarda com retorno antecipado
3. Teste após cada alteração

**Antes**:
```javascript
function payAmount(employee) {
  let result;
  if (employee.isSeparated) {
    result = { amount: 0, reasonCode: "SEP" };
  } else {
    if (employee.isRetired) {
      result = { amount: 0, reasonCode: "RET" };
    } else {
      result = calculateNormalPay(employee);
    }
  }
  return result;
}
```

**Depois**:
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### Replace Conditional with Polymorphism (Substituir Condicional por Polimorfismo)

**Quando usar**: Switch/case baseado em tipo; lógica condicional variando por tipo

**Motivação**: Deixar os objetos gerenciarem seu próprio comportamento.

**Mecânica**:
1. Crie hierarquia de classes (se não existir)
2. Use Factory Function para criação de objetos
3. Mova a lógica condicional para o método da superclasse
4. Crie o método da subclasse para cada caso
5. Remova o condicional original

**Antes**:
```javascript
function plumages(birds) {
  return birds.map(b => plumage(b));
}

function plumage(bird) {
  switch (bird.type) {
    case 'EuropeanSwallow':
      return "average";
    case 'AfricanSwallow':
      return (bird.numberOfCoconuts > 2) ? "tired" : "average";
    case 'NorwegianBlueParrot':
      return (bird.voltage > 100) ? "scorched" : "beautiful";
    default:
      return "unknown";
  }
}
```

**Depois**:
```javascript
class Bird {
  get plumage() { return "unknown"; }
}

class EuropeanSwallow extends Bird {
  get plumage() { return "average"; }
}

class AfricanSwallow extends Bird {
  get plumage() {
    return (this.numberOfCoconuts > 2) ? "tired" : "average";
  }
}

class NorwegianBlueParrot extends Bird {
  get plumage() {
    return (this.voltage > 100) ? "scorched" : "beautiful";
  }
}

function createBird(data) {
  switch (data.type) {
    case 'EuropeanSwallow': return new EuropeanSwallow(data);
    case 'AfricanSwallow': return new AfricanSwallow(data);
    case 'NorwegianBlueParrot': return new NorwegianBlueParrot(data);
    default: return new Bird(data);
  }
}
```

---

### Introduce Special Case / Null Object (Introduzir Caso Especial / Objeto Nulo)

**Quando usar**: Verificações de null repetidas para casos especiais

**Motivação**: Retornar um objeto especial que trata o caso especial.

**Mecânica**:
1. Crie a classe de caso especial com a interface esperada
2. Adicione verificação isSpecialCase
3. Introduza método de fábrica
4. Substitua verificações de null pelo uso do objeto de caso especial
5. Teste

**Antes**:
```javascript
const customer = site.customer;
// ... many places checking
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**Depois**:
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// Factory method
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// Usage - no null checks needed
const customerName = customer.name;
```

---

## Refatorando APIs (Refactoring APIs)

### Separate Query from Modifier (Separar Query de Modificador)

**Quando usar**: Função retorna um valor e também tem efeitos colaterais

**Motivação**: Deixar claro quais operações têm efeitos colaterais.

**Mecânica**:
1. Crie uma nova função de query
2. Copie a lógica de retorno da função original
3. Modifique a original para retornar void
4. Substitua as chamadas que usam o valor de retorno
5. Teste

**Antes**:
```javascript
function alertForMiscreant(people) {
  for (const p of people) {
    if (p === "Don") {
      setOffAlarms();
      return "Don";
    }
    if (p === "John") {
      setOffAlarms();
      return "John";
    }
  }
  return "";
}
```

**Depois**:
```javascript
function findMiscreant(people) {
  for (const p of people) {
    if (p === "Don") return "Don";
    if (p === "John") return "John";
  }
  return "";
}

function alertForMiscreant(people) {
  if (findMiscreant(people) !== "") setOffAlarms();
}
```

---

### Parameterize Function (Parametrizar Função)

**Quando usar**: Várias funções fazendo coisas similares com valores diferentes

**Motivação**: Remover duplicação adicionando um parâmetro.

**Mecânica**:
1. Selecione uma função
2. Adicione parâmetro para o literal variável
3. Altere o corpo para usar o parâmetro
4. Teste
5. Mude os chamadores para usar a versão parametrizada
6. Remova as funções não mais utilizadas

**Antes**:
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**Depois**:
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// Usage
raise(person, 0.10);
raise(person, 0.05);
```

---

### Remove Flag Argument (Remover Argumento de Flag)

**Quando usar**: Parâmetro booleano que muda o comportamento da função

**Motivação**: Tornar o comportamento explícito por meio de funções separadas.

**Mecânica**:
1. Crie uma função explícita para cada valor da flag
2. Substitua cada chamada pela nova função adequada
3. Teste após cada alteração
4. Remova a função original

**Antes**:
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // premium booking logic
  } else {
    // regular booking logic
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**Depois**:
```javascript
function bookPremiumConcert(customer) {
  // premium booking logic
}

function bookRegularConcert(customer) {
  // regular booking logic
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## Lidando com Herança (Dealing with Inheritance)

### Pull Up Method (Subir Método)

**Quando usar**: O mesmo método em múltiplas subclasses

**Motivação**: Remover duplicação na hierarquia de classes.

**Mecânica**:
1. Inspecione os métodos para garantir que são idênticos
2. Verifique que as assinaturas são iguais
3. Crie um novo método na superclasse
4. Copie o corpo de uma subclasse
5. Exclua o método de uma subclasse e teste
6. Exclua os métodos das outras subclasses, testando cada um

---

### Push Down Method (Descer Método)

**Quando usar**: Comportamento relevante apenas para um subconjunto de subclasses

**Motivação**: Colocar o método onde ele é usado.

**Mecânica**:
1. Copie o método para cada subclasse que precisa dele
2. Remova o método da superclasse
3. Teste
4. Remova das subclasses que não precisam
5. Teste

---

### Replace Subclass with Delegate (Substituir Subclasse por Delegado)

**Quando usar**: Herança está sendo usada incorretamente; necessidade de mais flexibilidade

**Motivação**: Preferir composição à herança quando apropriado.

**Mecânica**:
1. Crie uma classe vazia para o delegado
2. Adicione campo na classe hospedeira que mantém o delegado
3. Crie construtor para o delegado, chamado a partir da hospedeira
4. Mova funcionalidades para o delegado
5. Teste após cada movimentação
6. Substitua herança por delegação

---

## Extract Class (Extrair Classe)

**Quando usar**: Classe grande com múltiplas responsabilidades

**Motivação**: Dividir a classe para manter a responsabilidade única.

**Mecânica**:
1. Decida como dividir as responsabilidades
2. Crie a nova classe
3. Mova campo da original para a nova classe
4. Teste
5. Mova métodos da original para a nova classe
6. Teste após cada movimentação
7. Revise e renomeie ambas as classes
8. Decida como expor a nova classe

**Antes**:
```javascript
class Person {
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get officeAreaCode() { return this._officeAreaCode; }
  set officeAreaCode(arg) { this._officeAreaCode = arg; }
  get officeNumber() { return this._officeNumber; }
  set officeNumber(arg) { this._officeNumber = arg; }

  get telephoneNumber() {
    return `(${this._officeAreaCode}) ${this._officeNumber}`;
  }
}
```

**Depois**:
```javascript
class Person {
  constructor() {
    this._telephoneNumber = new TelephoneNumber();
  }
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get telephoneNumber() { return this._telephoneNumber.toString(); }
  get officeAreaCode() { return this._telephoneNumber.areaCode; }
  set officeAreaCode(arg) { this._telephoneNumber.areaCode = arg; }
}

class TelephoneNumber {
  get areaCode() { return this._areaCode; }
  set areaCode(arg) { this._areaCode = arg; }
  get number() { return this._number; }
  set number(arg) { this._number = arg; }
  toString() { return `(${this._areaCode}) ${this._number}`; }
}
```

---

## Referência Rápida: Smell → Refatoração

| Code Smell | Refatoração Principal | Alternativa |
|------------|----------------------|-------------|
| Long Method | Extract Method | Replace Temp with Query |
| Duplicate Code | Extract Method | Pull Up Method |
| Large Class | Extract Class | Extract Subclass |
| Long Parameter List | Introduce Parameter Object | Preserve Whole Object |
| Feature Envy | Move Method | Extract Method + Move |
| Data Clumps | Extract Class | Introduce Parameter Object |
| Primitive Obsession | Replace Primitive with Object | Replace Type Code |
| Switch Statements | Replace Conditional with Polymorphism | Replace Type Code |
| Temporary Field | Extract Class | Introduce Null Object |
| Message Chains | Hide Delegate | Extract Method |
| Middle Man | Remove Middle Man | Inline Method |
| Divergent Change | Extract Class | Split Phase |
| Shotgun Surgery | Move Method | Inline Class |
| Dead Code | Remove Dead Code | - |
| Speculative Generality | Collapse Hierarchy | Inline Class |

---

## Leitura Adicional

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2ª ed.)
- Catálogo online: https://refactoring.com/catalog/
