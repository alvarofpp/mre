# Classes

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
  - [Range](#range)

## <a name="regex">Regex</a>
Essa é a classe pai de todas as classes do pacote, o RegEx que se está manipulando fica na variável `self.rgx`. Seu construtor pode receber qualquer quantidade de entradas, porém espera-se que sejam dos tipos: `str`, `int` e a própria classe `Regex`. Para entender melhor:

- `str`: concatena à variável `self.rgx`;
- `int`: realiza [*backreferences*](https://www.regular-expressions.info/backref.html);
- `Regex`: concatena o valor armazenado em `self.rgx` do objeto que se recebe na variável `self.rgx` do objeto que está recebendo.

Formas de se declarar um **Regex**:
```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

### Constantes
Constantes presentes na classe **Regex**:

| Constante | Valor |
| --------- | ----- |
| `ANY` | `.` |
| `DOT` | `\\.` |
| `DIGIT` | `\\d` |
| `WHITESPACE` | `\\s` |
| `WORD_CHARS` | `\\w` |
| `SLASH` | `\\/.` |
| `NOT_DIGIT` | `\\D` |
| `NOT_WHITESPACE` | `\\S` |
| `NOT_WORD_CHARS` | `\\W` |
| `ZERO_OR_ONE` | `?` |
| `ZERO_OR_MULTIPLE` | `*` |
| `ONE_OR_MULTIPLE` | `+` |
| `HYPHEN` | `\\-` |

### Métodos
Além das funções, também haverá a descrição das sobrecargas.

#### \_\_str\_\_
Retorna o valor salvo em `self.rgx`.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

#### \_\_eq\_\_
A comparação pode ser entre `str` ou `Regex`:
- `== str`: compara `self.rgx` ao valor da variável recebida;
- `== Regex`: compara `self.rgx` (acessado através do método **get**) ao valor da variável `self.rgx` do objeto recebido (também acessado através do método **get**).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

#### \_\_iadd\_\_
Espera-se variáveis de dois tipos: `str` e `Regex`. Para entender melhor:

- `+= str`: concatena `self.rgx` ao valor da variável recebida;
- `+= Regex`: concatena `self.rgx` ao valor da variável `self.rgx` do objeto recebido (acessado através do método **get**).

Essa sobrecarga altera diretamente a variável `self.rgx`, sendo assim nos casos de operação, por exemplo, em um objeto **Set**, irá alterar o valor entre os colchetes.

```python
from mre import Regex, Set

regex = Regex("Hello")
regex += " world"
print(regex)  # "Hello world"

regex_set = Set("Hello")  # [Hello]
regex_set += " world"
print(regex_set)  # "[Hello world]"
```

#### \_\_add\_\_
Espera-se variáveis de dois tipos: `str` e `Regex`. Diferentemente da sobrecarga **\_\_iadd\_\_**, essa sobrecarga retorna um novo objeto **Regex**.

- `+ str`: concatena `self.rgx` (acessado através do método **get**) ao valor da variável recebida;
- `+ Regex`: concatena `self.rgx` (acessado através do método **get**) ao valor da variável `self.rgx` do objeto recebido (também acessado através do método **get**).

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

#### get
Retorna o valor armazenado em `self.rgx`.

```python
from mre import Regex

regex = Regex("Valor armazenado")
print(regex.get())  # "Valor armazenado"
```

#### quantifier
Possui os seguintes parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Serve para quantificar as vezes que o RegEx deve/pode aparecer (de `n` até `m`). Retorna um novo objeto **Regex**.

Em casos específicos, há a adição de um símbolo. Esses casos são:

| n | m | without_maximum | Símbolo | Acesso |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |

Além desses casos específicos, a quantificação poderá ocorrer das formas:
- `{n}`: deve ocorrer `n` vezes;
- `{n, m}`: pode ocorrer de `n` até `m` vezes.

```python
from mre import Regex

digits = Regex("[0-9]")

print(digits.quantifier(3))  # "[0-9]{3}"
print(digits.quantifier(3, 5))  # "[0-9]{3,5}"
print(digits.quantifier(0, 1))  # "[0-9]?"
print(digits.quantifier(0, without_maximum=True))  # "[0-9]*"
print(digits.quantifier(1, without_maximum=True))  # "[0-9]+"
```

#### backreferences
Possui um parâmetro do tipo `int` (`group_n`) que serve para indicar qual grupo se deseja realizar a *backreference*. Retorna um **Regex** que realiza [*backreferences*](https://www.regular-expressions.info/backref.html) ao grupo indicado.

Um meio alternativo de chamar esse método é inserindo um `int` no construtor.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

## <a name="quantifier">Quantifier</a>
Essa classe serve como uma alternativa a chamada do método **Regex.quantifier**. Seu construtor recebe 4 parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

O primeiro é referente ao RegEx que se deseja construir, os 3 restantes são para a chamada do método **Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

## <a name="set">Set</a>
Essa classe representa um conjunto no RegEx. Seu construtor é o mesmo da classe **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

### Métodos
Essa classe herda os métodos da classe **Regex**, sobrescrevendo apenas os métodos a seguir.

#### get
Retorna o valor armazenado em `self.rgx`, mas entre colchetes.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

#### quantifier
Retorna um novo objeto **Regex** com o quantificador referente ao conjunto.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="group">Group</a>
Essa classe representa um grupo no RegEx. Seu construtor recebe 2 parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

Se o argumento referente a `non_capturing` for `True`, será adicionado os símbolos que indicam que a *RegEx Engine* não deve retornar o valor daquele grupo (`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

### Métodos
Essa classe herda os métodos da classe **Regex**, sobrescrevendo apenas os métodos a seguir.

#### get
Retorna o valor armazenado em `self.rgx`, mas entre parênteses.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

#### quantifier
Retorna um novo objeto **Regex** com o quantificador referente ao grupo.

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="anchor">Anchor</a>
Essa classe representa um RegEx com âncora (o RegEx deve começar e terminar como foi definido). Seu construtor recebe 2 parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

Se o argumento referente a `negate` for `True`, será adicionado os símbolos do inverso do padrão, ou seja, a RegEx não deve começar e terminar como definido.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

### Métodos
Essa classe herda os métodos da classe **Regex**, sobrescrevendo apenas os métodos a seguir.

#### get
Retorna o valor armazenado em `self.rgx`, mas entre parênteses.

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

## <a name="range">helper.Range</a>
Essa classe serve para ajudar na criação de um RegEx que indique uma classe de caracteres a partir de um *range*. Seu construtor recebe 2 parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

Idealmente usar essa classe junto a classe **Set**, pois dentro de um conjunto, o hífen possui um valor "mágico" que o permite dar essa função de atribuir *range*, fora do conjunto o hífen tem apenas valor de hífen. Logo, se você quiser, por exemplo, todas as letras minúsculas, deve usar `[a-z]` e não apenas `a-z`, pois assim você está apenas dizendo que quer `a`, `-` e `z`.

```python
from mre.helper import Range

# Todos os dígitos
digits = Range(0, 9)
# Todas as letras
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

### Métodos
Essa classe herda os métodos da classe **Regex**, além de possuir seus próprios métodos.

#### digits
Possui 2 parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Retorna um *range* que define os dígitos entre `minimum` e `maximum`.

```python
from mre.helper import Range

regex_range_one = Range(0, 9)
regex_range_two = Range().digits()
regex_range_three = Range(0, 6)
regex_range_four = Range().digits(0, 6)

print(regex_range_one)  # "0-9"
print(regex_range_two)  # "0-9"
print(regex_range_three)  # "0-6"
print(regex_range_four)  # "0-6"
```

#### letters
Possui 4 parâmetros:

| Parâmetro | Tipo | Valor padrão |
| --------- | ---- | ------------ |
| `minimum` | `chr` | `A` |
| `maximum` | `chr` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Retorna um *range* que define as letras entre `minimum` e `maximum`.

```python
from mre.helper import Range

# Todas as letras
regex_range_one = Range('A', 'z')
regex_range_two = Range().letters()
regex_range_three = Range().letters('A', 'z')
regex_range_four = Range().letters(uppercase=True, lowercase=True)
# Todas as letras maiúsculas
regex_range_five = Range().letters(uppercase=True)
# Todas as letras minúsculas
regex_range_six = Range().letters(lowercase=True)

print(regex_range_one)  # "A-z"
print(regex_range_two)  # "A-z"
print(regex_range_three)  # "A-z"
print(regex_range_four)  # "A-z"
print(regex_range_five)  # "A-Z"
print(regex_range_six)  # "a-z"
```

# Exemplos

2 formas de fazer o RegEx de **CEP** (`[0-9]{5}-?[0-9]{3}`)
```python
from mre import Regex, Set

# Todos os dígitos
digits = Set(Regex("0-9"))

rgx_cep = Regex(
    digits.quantifier(5),
    Regex("-").quantifier(0, 1),
    digits.quantifier(3),
)
```

```python
from mre import Regex, Quantifier, Set
from mre.helper import Range

# Todos os dígitos [0-9]
digits = Set(Range().digits())
# O hífen pode aparecer nenhuma ou uma vez
hyphen = Quantifier("-", 0, 1)

rgx_cep = Regex(
    digits.quantifier(5), hyphen,
    digits.quantifier(3),
)
```

RegEx de **CPF** (`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):
```python
from mre import Regex, Set
from mre.helper import Range

# Todos os dígitos
all_digits = Set(Range(0, 9))
# O ponto pode aparecer nenhuma ou uma vez
dot = Regex(Regex.DOT).quantifier(0, 1)
# O hífen pode aparecer nenhuma ou uma vez
hyphen = Regex('-').quantifier(0, 1)

rgx_cpf = Regex(
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), hyphen,
    all_digits.quantifier(2),
)
```

RegEx de **CNPJ** (`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):
```python
from mre import Regex, Quantifier

# Todos os dígitos
digits = Regex(Regex.DIGIT)
# O ponto pode aparecer nenhuma ou uma vez
dot = Regex(Regex.DOT).quantifier(0, 1)
# A barra pode aparecer nenhuma ou uma vez
slash = Regex(Regex.SLASH).quantifier(0, 1)
# O hífen pode aparecer nenhuma ou uma vez
hyphen = Quantifier("-", 0, 1)

rgx_cnpj = Regex(
    digits.quantifier(2), dot,
    digits.quantifier(3), dot,
    digits.quantifier(3), slash,
    digits.quantifier(4), hyphen,
    digits.quantifier(2),
)
```
