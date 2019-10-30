# Klassen

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
    - [Range](#range)

## <a name="regex">Regex</a>
Dies ist die Elternklasse von allen anderen Klassen in diesem Paket. Der reguläre Ausdruck wird in der Variable `self.rgx` verarbeitet. Der Konstruktor kann eine beliebige Anzahl an parametern erhalten, welche aber alle vom Typ `str`, `int` oder der `Regex` Klasse selber sein müssen. Zum besseren Verständnis:

- `str`: wird an die Variable `self.rgx` angehangen;
- `int`: führt eine [*backreferences*](https://www.regular-expressions.info/backref.html) aus
- `Regex`: fügt den Wert von `self.rgx` des übergebenen Objektes zu der Variable `self.rgx` des empfangenen Objektes hinzu.

Wege zur Dekleration eines **Regex**:
```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

### Konstanten
Verfügbare Konstanten in der **Regex** Klasse:

| Konstante | Wert |
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

### Methoden
Beschreibung der Methoden und der Überladungen.

#### \_\_str\_\_
Gibt den Wert, welcher in der Variable `self.rgx` gespeichert ist zurück.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

#### \_\_eq\_\_
Vergleiche sind möglich zwischen den Typen `str` und `Regex`:
- `== str`: vergleicht `self.rgx` mit dem Wert der übergebenen Variable.
- `== Regex`: vergleicht `self.rgx` (Zugriff über die Methode **get**) mit der Variable `self.rgx` des übergebenen Objektes (ebenfalls mittels der Methode **get**).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

#### \_\_iadd\_\_
Erwarted eine Variable vom Typ `str` oder `Regex`. Für das bessere Verständnis:

- `+= str`: fügt der Variable `self.rgx` den Wert des übergebenen Strings hinzu;
- `+= Regex`: fügt der Variable  `self.rgx` den Wert der Variable `self.rgx` des übergebenen Objektes (Zugriff mittels der Methode **get**) hinzu.

Die Überladung ändert direkt den Wert der Variable `self.rgx`. Im Falle einer Operation wie **Set** des Objektes, wird der Wert auf den Wert zwischen den Klammern gesetzt.

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
Erwarted eine Variable vom Typ `str` oder `Regex`.  Anders als die Überladung von **\_\_iadd\_\_**, gibt diese Überladung ein neues **Regex** Objekt zurück.

- `+ str`: fügt der Variable `self.rgx` (Zugriff mittels der Methode  **get**) den Wert des übergebenen Strings hinzu;
- `+ Regex`: fügt der Variable `self.rgx` (Zugriff mittels der Methode  **get**) den Wert der Variable `self.rgx` des übergebenen Objektes (ebenfalls Zugriff mittels der Methode **get**) hinzu.

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

#### get
Gibt den Wert, welcher in `self.rgx` gespeichert ist, zurück.

```python
from mre import Regex

regex = Regex("stored value")
print(regex.get())  # "stored value"
```

#### quantifier
Hat folgende Parameter:

| Parameter | Typ | Standardwert |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Benutzt um festzulegen, wie häufig ein regulärer Ausdruck auftreten sollte (von `n` nach `m`). Gibt ein neues **Regex** Objekt zurück.

In besonderen Fällen wird ein Zeichen hinzugefügt. Diese Fälle sind:

| n | m | without_maximum | Zeichen | Zugriff |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |

Zusätzlich zu diesen besonderen Fällen, kann die Quantifikation wie folgt auftreten:
- `{n}`: sollte `n` mal auftreten;
- `{n, m}`: kann von `n` bis zu `m` mal auftreten.

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
Hat einen Parameter vom Typ `int` (`group_n`) welcher dazu benutzt wird anzuzeigen, über welche Gruppe du eine *backreference* durchführen möchtest. Gibt ein Objekt vom Typ **Regex** zurück, welches eine [*backreferences*](https://www.regular-expressions.info/backref.html) der anzuzeigenden Gruppe durchführt

Ein alternativer Weg diese Funktion aufzurufen ist dem Konstruktor einen `int` bereitzustellen.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

## <a name="quantifier">Quantifier</a>
Diese Klasse stellt eine Alternative zum Aufruf **Regex.quantifier** dar. Der Konstruktor hat 4 Parameter:

| Parameter | Typ | dStandardwert |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Der erste Parameter verweist auf den regulären Ausdruck, welcher erstellt werden soll. Die anderen drei dienen dem Aufruf der Methode **Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

## <a name="set">Set</a>
Diese Klasse repräsentiert ein Set in RegEx. Der Konstruktor ist identisch zu **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

### Methoden
Diese Klasse erbt die Methoden der Klasse **Regex** und überschreibt folgende:

#### get
Gibt den Wert welcher in `self.rgx` gespeichert wird zurück, aber in Klammern.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

#### quantifier
Gibt ein neues **Regex** Objekt zurück mit einem Quantifier für das Set.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="group">Group</a>
Diese Klasse repräsentiert eine Gruppe in RegEx. Der Konstruktor hat zwei Parameter:

| Parameter | Typ | dStandardwert |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

Wenn der Ausdruck für `non_capturing` `True` ist, wird das Zeichen, welches die *RegEx Engine* anzeigt, wird der Non-Captured-Gruppe hinzugefügt (`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

### Methoden
Diese Klasse erbt die Methoden der Klasse **Regex** und überschreibt folgende:

#### get
Gibt den Wert welcher in `self.rgx` gespeichert wird zurück, aber in runden Klammern.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

#### quantifier
Gibt ein neues **Regex** Objekt zurück mit einem Quantifier für das Set.

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="anchor">Anchor</a>
Diese Klasse repräsentiert einen verankerten regulären Ausdruck (Der RegEx muss beginnen und enden wie definiert). Der Konstruktor hat zwei Parameter:

| Parameter | Typ | Standardwert |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

Wenn das Argument für `negate` `True` ist, wird das Inverse Pattern Zeichen hinzugefügt, zum Beispiel darf der RegEx nicht wie definiert beginnen und enden.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

### Methoden
Diese Klasse erbt die Methoden der Klasse **Regex** und überschreibt folgende:

#### get
Gibt den Wert welcher in `self.rgx` gespeichert wird zurück, aber verankert.

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

## <a name="range">helper.Range</a>
Diese Klasse dient dazu zu bei der Erstellung eines RegEx zu helfen, welches die die Zeichenklasse in Form einer *range* darstellt. Der Konstruktor hat zwei Parameter:

| Parameter | Typ | Standardwert |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

Idealerweise solltest du die Klasse zusammen mit einem **Set** nutzen. In einem **Set** hat der Bindestrich einen "magischen" Wert, welcher erlaubt eine Spanne zuzuweisen. Außerhalb eines Sets hat der Bindestrich nur den Bindesstrichwert. Wenn du also kleingeschriebene Buchstaben möchtest, solltest du `[a-z]` statt `a-z` nutzen. `a-z` zeigt nur an, dass du die Zeichen `a`, `-` und `z` möchtest.

```python
from mre.helper import Range

# all digits
digits = Range(0, 9)
# all letters
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

### Methoden
Diese Klasse erbt die Methoden der Klasse **Regex** und hat ihre eigenen Methoden.

#### digits
Hat zwei Parameter:

| Parameter | Typ | Standardwert |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Gibt eine Spanne(*range*) zurück, welche durch die Ziffern zwischen `minimum` und `maximum` definiert ist.

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
Hat vier Parameter:

| Parameter | Typ | Standard Wert |
| --------- | ---- | ------------ |
| `minimum` | `char` | `A` |
| `maximum` | `char` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Gibt eine Spanne (*range*) zrück, welche den Werten zwischen `minimum` und `maximum` entspricht.

```python
from mre.helper import Range

# all letters
regex_range_one = Range('A', 'z')
regex_range_two = Range().letters()
regex_range_three = Range().letters('A', 'z')
regex_range_four = Range().letters(uppercase=True, lowercase=True)
# all capital letters
regex_range_five = Range().letters(uppercase=True)
# all lowercase letters
regex_range_six = Range().letters(lowercase=True)

print(regex_range_one)  # "A-z"
print(regex_range_two)  # "A-z"
print(regex_range_three)  # "A-z"
print(regex_range_four)  # "A-z"
print(regex_range_five)  # "A-Z"
print(regex_range_six)  # "a-z"
```

# Beispiele

Es gibt zwei Möglichkeiten zum Erstellen eines RegEx für **CEP** (Brasilianische Postleitzahl) (`[0-9]{5}-?[0-9]{3}`):
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
digits = Set(Range().digits())
# the hyphen may appear zero or one times
hyphen = Quantifier("-", 0, 1)

rgx_cep = Regex(
    digits.quantifier(5), hyphen,
    digits.quantifier(3),
)
```

RegEx für eine **CPF** (Brasilianische Steuernummer) (`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):

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

RegEx für eine **CNPJ** (ID in der brasilianischen Datenbank für rechtliche Personen ) (`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):

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
