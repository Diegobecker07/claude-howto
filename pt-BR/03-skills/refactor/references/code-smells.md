<!-- i18n-source: 03-skills/refactor/references/code-smells.md -->
<!-- i18n-source-sha: d4369ce -->
<!-- i18n-date: 2026-04-16 -->

# Catálogo de Code Smells

Uma referência abrangente de code smells baseada em *Refactoring* (2ª Edição) de Martin Fowler. Code smells são sintomas de problemas mais profundos — indicam que algo pode estar errado no design do seu código.

> "Um code smell é uma indicação superficial que normalmente corresponde a um problema mais profundo no sistema." — Martin Fowler

---

## Inchaços (Bloaters)

Code smells que representam algo que cresceu demais para ser tratado de forma eficaz.

### Método Longo (Long Method)

**Sinais:**
- Método com mais de 30–50 linhas
- Necessidade de rolar para ver o método inteiro
- Múltiplos níveis de aninhamento
- Comentários explicando o que cada seção faz

**Por que é ruim:**
- Difícil de entender
- Difícil de testar isoladamente
- Alterações causam consequências inesperadas
- Lógica duplicada fica escondida dentro

**Refatorações:**
- Extract Method
- Replace Temp with Query
- Introduce Parameter Object
- Replace Method with Method Object
- Decompose Conditional

**Exemplo (Antes):**
```javascript
function processOrder(order) {
  // Validate order (20 lines)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... more validation

  // Calculate totals (30 lines)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... tax, shipping, discounts

  // Send notifications (20 lines)
  // ... email logic
}
```

**Exemplo (Depois):**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### Classe Grande (Large Class)

**Sinais:**
- Classe com muitas variáveis de instância (>7–10)
- Classe com muitos métodos (>15–20)
- Nome de classe vago (Manager, Handler, Processor)
- Métodos que não usam todas as variáveis de instância

**Por que é ruim:**
- Viola o Princípio da Responsabilidade Única
- Difícil de testar
- Alterações se propagam por funcionalidades não relacionadas
- Difícil de reutilizar partes

**Refatorações:**
- Extract Class
- Extract Subclass
- Extract Interface

**Detecção:**
```
Lines of code > 300
Number of methods > 15
Number of fields > 10
```

---

### Obsessão por Primitivos (Primitive Obsession)

**Sinais:**
- Uso de primitivos para conceitos de domínio (string para e-mail, int para dinheiro)
- Arrays de primitivos em vez de objetos
- Constantes de string para códigos de tipo
- Números/strings mágicos

**Por que é ruim:**
- Sem validação no nível do tipo
- Lógica espalhada pelo código
- Fácil de passar valores errados
- Conceitos de domínio ausentes

**Refatorações:**
- Replace Primitive with Object
- Replace Type Code with Class
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**Exemplo (Antes):**
```javascript
const user = {
  email: 'john@example.com',     // Just a string
  phone: '1234567890',           // Just a string
  status: 'active',              // Magic string
  balance: 10050                 // Cents as integer
};
```

**Exemplo (Depois):**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### Lista de Parâmetros Longa (Long Parameter List)

**Sinais:**
- Métodos com 4+ parâmetros
- Parâmetros que sempre aparecem juntos
- Flags booleanas alterando o comportamento do método
- null/undefined passado frequentemente

**Por que é ruim:**
- Difícil de chamar corretamente
- Confusão com a ordem dos parâmetros
- Indica que o método faz coisas demais
- Difícil de adicionar novos parâmetros

**Refatorações:**
- Introduce Parameter Object
- Preserve Whole Object
- Replace Parameter with Method Call
- Remove Flag Argument

**Exemplo (Antes):**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**Exemplo (Depois):**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### Agrupamentos de Dados (Data Clumps)

**Sinais:**
- Os mesmos 3+ campos aparecem juntos repetidamente
- Parâmetros que sempre andam juntos
- Classes com subconjuntos de campos que pertencem juntos

**Por que é ruim:**
- Lógica de tratamento duplicada
- Abstração ausente
- Mais difícil de estender
- Indica classe oculta

**Refatorações:**
- Extract Class
- Introduce Parameter Object
- Preserve Whole Object

**Exemplo:**
```javascript
// Data clump: (x, y, z) coordinates
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// Extract Point3D class
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## Abusadores de Orientação a Objetos (Object-Orientation Abusers)

Smells que indicam uso incompleto ou incorreto dos princípios de OOP.

### Declarações Switch (Switch Statements)

**Sinais:**
- Longas cadeias de switch/case ou if/else
- O mesmo switch em múltiplos lugares
- Switch em códigos de tipo
- Adicionar novos casos requer alterações em toda parte

**Por que é ruim:**
- Viola o Princípio Aberto/Fechado
- Alterações se propagam por todos os locais de switch
- Difícil de estender
- Frequentemente indica polimorfismo ausente

**Refatorações:**
- Replace Conditional with Polymorphism
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**Exemplo (Antes):**
```javascript
function calculatePay(employee) {
  switch (employee.type) {
    case 'hourly':
      return employee.hours * employee.rate;
    case 'salaried':
      return employee.salary / 12;
    case 'commissioned':
      return employee.sales * employee.commission;
  }
}
```

**Exemplo (Depois):**
```javascript
class HourlyEmployee {
  calculatePay() {
    return this.hours * this.rate;
  }
}

class SalariedEmployee {
  calculatePay() {
    return this.salary / 12;
  }
}
```

---

### Campo Temporário (Temporary Field)

**Sinais:**
- Variáveis de instância usadas apenas em alguns métodos
- Campos definidos condicionalmente
- Inicialização complexa para determinados casos

**Por que é ruim:**
- Confuso — o campo existe mas pode ser null
- Difícil de entender o estado do objeto
- Indica lógica condicional oculta

**Refatorações:**
- Extract Class
- Introduce Null Object
- Replace Temp Field with Local

---

### Herança Recusada (Refused Bequest)

**Sinais:**
- Subclasse não usa métodos/dados herdados
- Subclasse sobrescreve para não fazer nada
- Herança usada para reuso de código, não para relação É-UM

**Por que é ruim:**
- Abstração errada
- Viola o Princípio de Substituição de Liskov
- Hierarquia enganosa

**Refatorações:**
- Push Down Method/Field
- Replace Subclass with Delegate
- Replace Inheritance with Delegation

---

### Classes Alternativas com Interfaces Diferentes (Alternative Classes with Different Interfaces)

**Sinais:**
- Duas classes que fazem coisas semelhantes
- Nomes de métodos diferentes para o mesmo conceito
- Poderiam ser usadas de forma intercambiável

**Por que é ruim:**
- Implementações duplicadas
- Sem interface comum
- Difícil de alternar entre elas

**Refatorações:**
- Rename Method
- Move Method
- Extract Superclass
- Extract Interface

---

## Impeditivos de Mudança (Change Preventers)

Smells que tornam as alterações difíceis — mudar uma coisa exige mudar muitas outras.

### Mudança Divergente (Divergent Change)

**Sinais:**
- Uma classe é alterada por múltiplas razões diferentes
- Mudanças em áreas distintas provocam edições na mesma classe
- A classe é uma "God class"

**Por que é ruim:**
- Viola a Responsabilidade Única
- Alta frequência de alterações
- Conflitos de merge

**Refatorações:**
- Extract Class
- Extract Superclass
- Extract Subclass

**Exemplo:**
Uma classe `User` muda por causa de:
- Alterações de autenticação
- Alterações de perfil
- Alterações de cobrança
- Alterações de notificação

→ Extrair: `AuthService`, `ProfileService`, `BillingService`, `NotificationService`

---

### Cirurgia de Espingarda (Shotgun Surgery)

**Sinais:**
- Uma alteração requer edições em muitas classes
- Uma pequena funcionalidade exige tocar em 10+ arquivos
- As mudanças ficam espalhadas e são difíceis de encontrar

**Por que é ruim:**
- Fácil de esquecer algum lugar
- Alto acoplamento
- Alterações sujeitas a erros

**Refatorações:**
- Move Method
- Move Field
- Inline Class

**Detecção:**
Procure por: adicionar um campo requer mudanças em >5 arquivos.

---

### Hierarquias de Herança Paralelas (Parallel Inheritance Hierarchies)

**Sinais:**
- Criar uma subclasse em uma hierarquia requer criar outra em uma hierarquia paralela
- Prefixos de classe coincidem (ex.: `DatabaseOrder`, `DatabaseProduct`)

**Por que é ruim:**
- Manutenção duplicada
- Acoplamento entre hierarquias
- Fácil de esquecer um lado

**Refatorações:**
- Move Method
- Move Field
- Eliminar uma das hierarquias

---

## Dispensáveis (Dispensables)

Algo desnecessário que deveria ser removido.

### Comentários Excessivos (Comments)

**Sinais:**
- Comentários explicando o que o código faz
- Código comentado
- TODOs/FIXMEs que persistem indefinidamente
- Pedidos de desculpa em comentários

**Por que é ruim:**
- Comentários mentem (ficam desatualizados)
- O código deve ser auto-documentado
- Código morto causa confusão

**Refatorações:**
- Extract Method (o nome explica o quê)
- Rename (clareza sem comentários)
- Remover código comentado
- Introduce Assertion

**Comentários bons vs. ruins:**
```javascript
// RUIM: Explica o quê
// Loop through users and check if active
for (const user of users) {
  if (user.status === 'active') { }
}

// BOM: Explica o porquê
// Active users only - inactive are handled by cleanup job
const activeUsers = users.filter(u => u.isActive);
```

---

### Código Duplicado (Duplicate Code)

**Sinais:**
- Mesmo código em múltiplos lugares
- Código semelhante com pequenas variações
- Padrões de copiar e colar

**Por que é ruim:**
- Correções de bugs precisam ser feitas em múltiplos lugares
- Risco de inconsistência
- Base de código inchada

**Refatorações:**
- Extract Method
- Extract Class
- Pull Up Method (em hierarquias)
- Form Template Method

**Regra de Detecção:**
Qualquer código duplicado 3+ vezes deve ser extraído.

---

### Classe Preguiçosa (Lazy Class)

**Sinais:**
- A classe não faz o suficiente para justificar sua existência
- Wrapper sem valor agregado
- Resultado de over-engineering

**Por que é ruim:**
- Sobrecarga de manutenção
- Indireção desnecessária
- Complexidade sem benefício

**Refatorações:**
- Inline Class
- Collapse Hierarchy

---

### Código Morto (Dead Code)

**Sinais:**
- Código inalcançável
- Variáveis/métodos/classes não utilizados
- Código comentado
- Código por trás de condições impossíveis

**Por que é ruim:**
- Confusão
- Carga de manutenção
- Retarda a compreensão

**Refatorações:**
- Remove Dead Code
- Safe Delete

**Detecção:**
```bash
# Look for unused exports
# Look for unreferenced functions
# IDE "unused" warnings
```

---

### Generalidade Especulativa (Speculative Generality)

**Sinais:**
- Classes abstratas com apenas uma subclasse
- Parâmetros não utilizados "para uso futuro"
- Métodos que apenas delegam
- "Framework" para um único caso de uso

**Por que é ruim:**
- Complexidade sem benefício
- YAGNI (You Ain't Gonna Need It)
- Mais difícil de entender

**Refatorações:**
- Collapse Hierarchy
- Inline Class
- Remove Parameter
- Rename Method

---

## Acopladores (Couplers)

Smells que representam acoplamento excessivo entre classes.

### Inveja de Funcionalidade (Feature Envy)

**Sinais:**
- Método usa mais dados de outra classe do que da própria
- Muitas chamadas de getter para outro objeto
- Dados e comportamento estão separados

**Por que é ruim:**
- Local errado para o comportamento
- Encapsulamento ruim
- Difícil de manter

**Refatorações:**
- Move Method
- Move Field
- Extract Method (depois mover)

**Exemplo (Antes):**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // Uses customer data heavily
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**Exemplo (Depois):**
```javascript
class Customer {
  getDiscountedPriceFor(price) {
    if (this.loyaltyYears > 5) {
      return price * this.discountRate;
    }
    return price;
  }
}
```

---

### Intimidade Inadequada (Inappropriate Intimacy)

**Sinais:**
- Classes acessam partes privadas uma da outra
- Referências bidirecionais
- Subclasses sabem demais sobre os pais

**Por que é ruim:**
- Alto acoplamento
- Mudanças em cascata
- Difícil de modificar uma sem a outra

**Refatorações:**
- Move Method
- Move Field
- Change Bidirectional to Unidirectional
- Extract Class
- Hide Delegate

---

### Cadeias de Mensagens (Message Chains)

**Sinais:**
- Longas cadeias de chamadas de método: `a.getB().getC().getD().getValue()`
- O cliente depende da estrutura de navegação
- Código "acidente de trem"

**Por que é ruim:**
- Frágil — qualquer alteração quebra a cadeia
- Viola a Lei de Demeter
- Acoplamento à estrutura

**Refatorações:**
- Hide Delegate
- Extract Method
- Move Method

**Exemplo:**
```javascript
// Ruim: Cadeia de mensagens
const managerName = employee.getDepartment().getManager().getName();

// Melhor: Ocultar delegação
const managerName = employee.getManagerName();
```

---

### Intermediário (Middle Man)

**Sinais:**
- Classe que apenas delega para outra
- Metade dos métodos são delegações
- Sem valor agregado

**Por que é ruim:**
- Indireção desnecessária
- Sobrecarga de manutenção
- Arquitetura confusa

**Refatorações:**
- Remove Middle Man
- Inline Method

---

## Guia de Severidade de Smells

| Severidade | Descrição | Ação |
|------------|-----------|------|
| **Crítico** | Bloqueia o desenvolvimento, causa bugs | Corrigir imediatamente |
| **Alto** | Carga de manutenção significativa | Corrigir no sprint atual |
| **Médio** | Perceptível, mas gerenciável | Planejar para o futuro próximo |
| **Baixo** | Inconveniência menor | Corrigir oportunisticamente |

---

## Checklist de Detecção Rápida

Use este checklist ao escanear o código:

- [ ] Algum método com mais de 30 linhas?
- [ ] Alguma classe com mais de 300 linhas?
- [ ] Algum método com mais de 4 parâmetros?
- [ ] Algum bloco de código duplicado?
- [ ] Algum switch/case em códigos de tipo?
- [ ] Algum código não utilizado?
- [ ] Algum método usando intensamente dados de outra classe?
- [ ] Alguma longa cadeia de chamadas de método?
- [ ] Algum comentário explicando "o quê" em vez do "porquê"?
- [ ] Algum primitivo que deveria ser um objeto?

---

## Leitura Adicional

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2ª ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
