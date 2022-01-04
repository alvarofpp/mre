# MRE

Un paquete de Python que permite create expresiones regulares (RegEx).
Su proposito es hacer que la creacion de un RegEx se mas facil de leer.

## Instalación de MRE

Instala el paquete MRE usando pip:

```python
pip install mre
```

## Clases

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
  - [Range](#range)

### <a name="regex">Regex</a>

Esta es la clase base de todas las demas clases en este paquete, el RegEx es manejado en la
variable `self.rgx`. Tu constructor puede recibir cualquier número de entradas, pero requiere
los siguientes tipos: `str`, `int` y la clasa `RegEx` misma. Para mejor entendimiento:

- `str`: concatena a la variable `self.rgx`;
- `int`: realiza [*backreferences*](https://www.regular-expressions.info/backref.html);
- `Regex`: concatena el valor de `self.rgx` del objecto ingresado a la variable `self.rgx`
  del objeto receptor.

Maneras de declarar un **Regex**:

```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

#### Constantes

Constantes disponibles en la clase **Regex**:

| Constant | Value |
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

#### Métodos

Descripciones de los métodos y sobrecargas.

##### \_\_str\_\_

Retorna el valor almacenado en `self.rgx`.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

##### \_\_eq\_\_

Las comparaciones son posibles con los tipos `str` y `Regex`:

- `== str`: compara `self.rgx` al valor de la variable ingresada;
- `== Regex`: compara `self.rgx` (accedido mediante el método **get**) al valor de `self.rgx`
  del objecto receptor (tambien accedido mediante el método **get**).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

##### \_\_iadd\_\_

Espera que la variable de tipo `str` y `Regex`. Para mayor entendimiento:

- `+= str`: concatena `self.rgx` con el valor de la variable ingresada;
- `+= Regex`: concatena `self.rgx` con el valor de la variable `self.rgx` del object ingresado
  (accedido mediante el método **get**).

La sobrecarga cambia directamente el valor de `self.rgx`. En caso de operacions como **Set**
de un objecto, cambiar el valor entre paréntesis.

```python
from mre import Regex, Set

regex = Regex("Hello")
regex += " world"
print(regex)  # "Hello world"

regex_set = Set("Hello")  # [Hello]
regex_set += " world"
print(regex_set)  # "[Hello world]"
```

##### \_\_add\_\_

Espera variables de tipo `str` y `Regex`. A diference de la sobrecarga de **\_\_iadd\_\_**,
esta sobrecarga retorna un nuevo objecto **Regex**.

- `+ str`: concatena `self.rgx` (accedido mediante el método **get**) con el valor de la
  variable ingresada;
- `+ Regex`: concatenates `self.rgx` (accedido mediante el método **get**) con el valor de
  `self.rgx` del objecto ingresado (tambien accedido mediante el método **get**).

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

##### get

Retorna el valor almacenado en `self.rgx`.

```python
from mre import Regex

regex = Regex("stored value")
print(regex.get())  # "stored value"
```

##### quantifier

Tiene los siguientes parámetros:

| Parámetro | Tipo | Valor por Defecto |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Usado para cuantificar que tan frecuente un Regex podria/deberia aparecer (de `n` a `m`).
Retorna un nuevo **Regex**.

En casos especifícos, un simbolo es añadido. Estos son los casos:

| n | m | without_maximum | Simbolo | Acceso |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |

Adicionalmente a estos casos especifícos, la cuantificación puede ocurrir de la siguiente forma:

- `{n}`: deberia ocurrir `n` veces;
- `{n, m}`: puede ocurrir desde `n` hasta `m` veces.

```python
from mre import Regex

digits = Regex("[0-9]")

print(digits.quantifier(3))  # "[0-9]{3}"
print(digits.quantifier(3, 5))  # "[0-9]{3,5}"
print(digits.quantifier(0, 1))  # "[0-9]?"
print(digits.quantifier(0, without_maximum=True))  # "[0-9]*"
print(digits.quantifier(1, without_maximum=True))  # "[0-9]+"
```

##### backreferences

Tiene un parámetro de tipo `int` (`group_n`) el cuál es usado par indicar cual grupo quieres
que realize un *backreference*. Retorna un **Regex** el cual realiza
[*backreferences*](https://www.regular-expressions.info/backref.html) del grupo indicado.

Una forma alternativa de llamar este metodo, es proporcionando un `int` al constructor.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

### <a name="quantifier">Quantifier</a>

Esta clase funciona como una alternativa al llamado de **Regex.quantifier**. El constructor
tiene 4 parámetros:

| Parámetro | Tipo | Valor por defecto |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

El primer parámetro refiere al RegEx que quieres crear, los otros tres son usados para
llamar al método **Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

### <a name="set">Set</a>

Esta clase representa un set en RegEx. El constructor es identico a **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

#### Métodos

Esta clase hereda los métodos de la clase **Regex**, anulando lo siguiente.

##### get

Retorna el valor almacenado en `self.rgx`, pero dentro de paréntesis.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

##### quantifier

Retorna un nuevo object **Regex** con un cuantificador para el set.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

### <a name="group">Group</a>

Esta clase representa a un grupo en RegEx. El constructor tiene dos parámetros:

| Párametro | Tipo | Valor por defecto |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

Si el argumento para `non_capturing` es `True`, el simbolo indicando *RegEx Engine* a
retornar un grupo de no captura le es agregado(`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

#### Métodos

Esta clase hereda los métodos de la clase **Regex**, anulando lo siguiente.

##### get

Retorna el valor almacenado en `self.rgx`, pero dentro de paréntesis.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

##### quantifier

Retorna un nuevo object **Regex** con un cuantificador para el grupo.

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

### <a name="anchor">Anchor</a>

Esta clase representa un RegEx anclado (el RegEx debe comenzar y terminar tal y como es definido).
El constructor tiene 2 parámetros:

| Parámetro | Tipo | Valor por defecto |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

Si el argumento para `negate` es `True`, el simbolo de patrón inverso es añadido, ie. el
RegEx no debe comenzar y terminar tal y como esta definido.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

#### Métodos

Esta clase hereda los métodos de la clase **Regex**, anulando lo siguiente.

##### get

Retorna el valor almacenado en `self.rgx`, pero anclado.

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

### <a name="range">helper.Range</a>

Esta clase tiene como propósito asistir en creando un RegEx que indica una clase carácter
en forma de un *range*. El constructor tiene dos parámetros:

| Parámetro | Tipo | Valor por defecto |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

Idealmente dberias usar esta clase junto a **Set**. Dentro de un **Set** el guión tiene un
valor "magico", que le permite asignar un rango. Afuera de un set un guión tiene solo el
valor del guión. Así que si quiere letras minúsculas, deberias usar `[a-z]` en vez de `a-z`.
`a-z` solo indica que quieres los valores `a`, `-` y `z`.

```python
from mre.helper import Range

# all digits
digits = Range(0, 9)
# all letters
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

#### Métodos

Esta clase hereda los métodos de la clase **Regex** y tiene sus propios métodos.

##### digits

Tiene dos parámetros:

| Parámetro | Tipo | Valor por defecto |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Retorna un *range* que es definido como los dígitos entre `minimun` y `maximum`.

```python
from mre.helper import Range

regex_range_one = Range(0, 9)
regex_range_two = Range.digits()
regex_range_three = Range(0, 6)
regex_range_four = Range.digits(0, 6)

print(regex_range_one)  # "0-9"
print(regex_range_two)  # "0-9"
print(regex_range_three)  # "0-6"
print(regex_range_four)  # "0-6"
```

##### letters

Tiene cuatro parámetros:

| Parámetro | Tipo | Valor por defecto |
| --------- | ---- | ------------ |
| `minimum` | `char` | `A` |
| `maximum` | `char` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Retorna un *range* que es definido como las letras entre `minimun` y `maximum`.

```python
from mre.helper import Range

# all letters
regex_range_one = Range('A', 'z')
regex_range_two = Range.letters()
regex_range_three = Range.letters('A', 'z')
regex_range_four = Range.letters(uppercase=True, lowercase=True)
# all capital letters
regex_range_five = Range.letters(uppercase=True)
# all lowercase letters
regex_range_six = Range.letters(lowercase=True)

print(regex_range_one)  # "A-z"
print(regex_range_two)  # "A-z"
print(regex_range_three)  # "A-z"
print(regex_range_four)  # "A-z"
print(regex_range_five)  # "A-Z"
print(regex_range_six)  # "a-z"
```

## Ejemplos

2 formas de crear un RegEx para un **CEP** (código postal brasileño) (`[0-9]{5}-?[0-9]{3}`):

```python
from mre import Regex, Set

# all digits
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

# all digits [0-9]
digits = Set(Range.digits())
# the hyphen may appear zero or one times
hyphen = Quantifier("-", 0, 1)

rgx_cep = Regex(
    digits.quantifier(5), hyphen,
    digits.quantifier(3),
)
```

RegEx para un **CPF** (número de registro de contribuyente) (`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):

```python
from mre import Regex, Set
from mre.helper import Range

# all digits
all_digits = Set(Range(0, 9))
# the dot may appear zero or one times
dot = Regex(Regex.DOT).quantifier(0, 1)
# the hyphen may appear zero or one times
hyphen = Regex('-').quantifier(0, 1)

rgx_cpf = Regex(
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), hyphen,
    all_digits.quantifier(2),
)
```

RegEx para un **CNPJ** (ID en el Registro Nacional de Entidades Legales brasileño)
(`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):

```python
from mre import Regex, Quantifier

# all digits
digits = Regex(Regex.DIGIT)
# the dot may appear zero or one times
dot = Regex(Regex.DOT).quantifier(0, 1)
# the slash may appear zero or one times
slash = Regex(Regex.SLASH).quantifier(0, 1)
# the hyphen may appear zero or one times
hyphen = Quantifier("-", 0, 1)

rgx_cnpj = Regex(
    digits.quantifier(2), dot,
    digits.quantifier(3), dot,
    digits.quantifier(3), slash,
    digits.quantifier(4), hyphen,
    digits.quantifier(2),
)
```
