# Klasser

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
    - [Range](#range)

## <a name="regex">Regex</a>

Dette er forældreklassen til alle andre klasser i denne pakke. RegEx'et håndteres i variablen `self.rgx`. Konstruktøren kan modtage et hvilket som helst antal af argumenter, men de skal være af en af følgende typer: `str`, `int` eller `Regex`-klassen selv. For bedre forståelse:

- `str`: konkatenerer til variablen `self.rgx`;
- `int`: laver [*backreferences*](https://www.regular-expressions.info/backref.html);
- `Regex`: konkatenerer værdien af `self.rgx` for det videregivne objekt til `self.rgx`-variablen af det modtagende objekt.

Måder at erklære et **Regex**:

```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

### Konstanter

Konstanter tilgængelige i **Regex**-klassen:

| Konstant | Værdi |
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

### Metoder

Beskrivelser af metoder og overloads.

#### \_\_str\_\_

Returnerer værdien gemt i `self.rgx`.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

#### \_\_eq\_\_

Sammenligninger er mulige mellem typerne `str` og `Regex`:

- `== str`: sammenligner `self.rgx` med værdien af den videregivne variabel;
- `== Regex`: sammenligner `self.rgx` (tilgået via **get**-metoden) med værdien af `self.rgx` for det videregivne objekt (også tilgået via **get**-metoden).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

#### \_\_iadd\_\_

Forventer variable af typerne `str` og `Regex`. For bedre forståelse:

- `+= str`: konkatenerer `self.rgx` med værdien af den videregivne variabel;
- `+= Regex`: konkatenerer `self.rgx` med værdien af variablen `self.rgx` for det videregivne objekt (tilgået via **get**-metoden).

Overloadet ændrer direkte værdien af `self.rgx`. I tilfælde af operationer som **Set** af et objekt, vil det ændres til værdien indsat mellem to brackets.

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

Forventer variable af typerne `str` og `Regex`. I modsætning til overloadet af **\_\_iadd\_\_**, returnerer dette overload et nyt **Regex**-objekt.

- `+ str`: konkatenerer `self.rgx` (tilgået via **get**-metoden) med værdien af den videregivne variabel;
- `+ Regex`: konkatenerer `self.rgx` (tilgået via **get**-metoden) med værdien af `self.rgx` for det videregivne objekt (også tilgået via **get**-metoden).

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

#### get

Returnerer værdien gemt i `self.rgx`.

```python
from mre import Regex

regex = Regex("stored value")
print(regex.get())  # "stored value"
```

#### quantifier

Har følgende parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Brugt til at kvantificere hvor ofte et Regex må/burde optræde (fra `n` til `m`). Returnerer et nyt **Regex**.

I særlige tilfælde bliver et symbol tilføjet. Disse tilfælde er:

| n | m | without_maximum | Symbol | Adgang |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |

Udover disse særlige tilfælde kan kvantificering forekomme som følgende:

- `{n}`: bør forekomme `n` gange;
- `{n, m}`: kan forekomme fra `n` op til `m` gange.

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

Har et parameter af typen `int` (`group_n`), som bruges til at angive hvilken gruppe du vil bruge til at lave en *backreference*. Returnerer et **Regex**, som laver [*backreferences*](https://www.regular-expressions.info/backref.html) af den angivne gruppe.

En alternativ måde at kalde denne metode på er ved at give en `int` til konstruktøren.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

## <a name="quantifier">Quantifier</a>

Denne klasse fungerer som et alternativ til at kalde **Regex.quantifier**. Konstruktøren har fire parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Det første parameter referer til det RegEx, du vil lave. De andre tre bruges til at kalde metoden **Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

## <a name="set">Set</a>

Denne klasse repræsenterer et set i RegEx. Konstruktøren er identisk til **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

### Metoder

Denne klasse nedarver metoderne fra **Regex**-klassen og overskriver følgende:

#### get

Returnerer værdien gemt i `self.rgx`, men indsat i brackets.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

#### quantifier

Returnerer et nyt **Regex**-objekt med en quantifier for det pågældende set.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="group">Group</a>

Denne klasse repræsenterer en gruppe i RegEx. Konstruktøren har to parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

Hvis argumentet for `non_capturing` er `True`, tilføjes symbolet der angiver *RegEx Engine* til at returnere en ikke-indfangende gruppe (`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

### Metoder

Denne klasse nedarver metoderne fra **Regex**-klassen og overskriver følgende:

#### get

Returnerer værdien gemt i `self.rgx`, men indsat i parenteser.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

#### quantifier

Returnerer et nyt **Regex**-objekt med en quantifier til gruppen.

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="anchor">Anchor</a>

Denne klasse repræsenterer et forankret RegEx (RegEx'et skal starte og slutte som defineret). Konstruktøren har to parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

Hvis argumentet for `negate` er `True`, tilføjes det inverse mønster, som i at RegEx'et ikke må starte og slutte som defineret.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

### Metoder

Denne klasse nedarver metoderne fra **Regex**-klassen og overskriver følgende:

#### get

Returnerer værdien gemt i `self.rgx`, men forankret.

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

## <a name="range">helper.Range</a>

Denne klasse er ment til at hjælpe med at lave et RegEx, der angiver en karakter-klasse i form af en *range*. Konstruktøren har to parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

Ideelt set bør du bruge denne klasse sammen med et **Set**. I et **Set** har bindestregen en "magisk" værdi, der gør den i stand til at tildele en rækkevidde. Uden for et set har en bindestreg kun værdien af en bindestreg. Så hvis du vil have små bogstaver, skal du bruge `[a-z]` i stedet for `a-z`. `a-z` angiver, at du kun vil have værdierne `a`, `-` og `z`.

```python
from mre.helper import Range

# alle cifre
digits = Range(0, 9)
# alle bogstaver
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

### Metoder

Denne klasse nedarver metoderne fra **Regex**-klassen og har dens egne metoder.

#### digits

Har to parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Returnerer en *range*, der er defineret som cifrene mellem `minimum` og `maximum`.

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

Har fire parametre:

| Parameter | Type | Standardværdi |
| --------- | ---- | ------------ |
| `minimum` | `char` | `A` |
| `maximum` | `char` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Returnerer en *range*, der er defineret som bogstaverne mellem `minimum` og `maximum`.

```python
from mre.helper import Range

# alle bogstaver
regex_range_one = Range('A', 'z')
regex_range_two = Range().letters()
regex_range_three = Range().letters('A', 'z')
regex_range_four = Range().letters(uppercase=True, lowercase=True)
# alle store bogstaver
regex_range_five = Range().letters(uppercase=True)
# alle små bogstaver
regex_range_six = Range().letters(lowercase=True)

print(regex_range_one)  # "A-z"
print(regex_range_two)  # "A-z"
print(regex_range_three)  # "A-z"
print(regex_range_four)  # "A-z"
print(regex_range_five)  # "A-Z"
print(regex_range_six)  # "a-z"
```

# Eksempler

To måder at lave et RegEx for et **CEP** (braziliansk postnummer) (`[0-9]{5}-?[0-9]{3}`):

```python
from mre import Regex, Set

# alle cifre
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

# alle cifre [0-9]
digits = Set(Range().digits())
# bindestregen må forekomme nul eller én gange
hyphen = Quantifier("-", 0, 1)

rgx_cep = Regex(
    digits.quantifier(5), hyphen,
    digits.quantifier(3),
)
```

RegEx for et **CPF** (braziliansk registernummer for skatteydere) (`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):

```python
from mre import Regex, Set
from mre.helper import Range

# alle cifre
all_digits = Set(Range(0, 9))
# punktummet må forekomme nul eller én gange
dot = Regex(Regex.DOT).quantifier(0, 1)
# bindestregen må forekomme nul eller én gange
hyphen = Regex('-').quantifier(0, 1)

rgx_cpf = Regex(
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), hyphen,
    all_digits.quantifier(2),
)
```

RegEx for et **CNPJ** (ID i det brazilianske National Registry of Legal Entities) (`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):

```python
from mre import Regex, Quantifier

# alle cifre
digits = Regex(Regex.DIGIT)
# punktummet må forekomme nul eller én gange
dot = Regex(Regex.DOT).quantifier(0, 1)
# skråstregen må forekomme nul eller én gange
slash = Regex(Regex.SLASH).quantifier(0, 1)
# bindestregen må forekomme nul eller én gange
hyphen = Quantifier("-", 0, 1)

rgx_cnpj = Regex(
    digits.quantifier(2), dot,
    digits.quantifier(3), dot,
    digits.quantifier(3), slash,
    digits.quantifier(4), hyphen,
    digits.quantifier(2),
)
```
