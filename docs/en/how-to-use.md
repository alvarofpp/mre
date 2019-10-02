# Classes

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
    - [Range](#range)

## <a name="regex">Regex</a>
This is the parent class of all other classes in this package, the RegEx is being handled in variable `self.rgx`. Your constructor can receive any number of inputs, but they require the following types: `str`, `int` and the `Regex` class itself. For better understanding:

- `str`: concatenates to variable `self.rgx`;
- `int`: performs [*backreferences*](https://www.regular-expressions.info/backref.html);
- `Regex`: concatenates the value of `self.rgx` of the passed object to variable `self.rgx` of the receiving object.

Ways to declare a **Regex**:
```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

### Constants
Constants available in class **Regex**:

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

### Methods
Descriptions of methods and overloads.

#### \_\_str\_\_
Returns the value stored in `self.rgx`.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

#### \_\_eq\_\_
Comparisons are possible with `str` and `Regex` type:
- `== str`: compares `self.rgx` to the value of the passed variable;
- `== Regex`: compares `self.rgx` (accessed via method **get**) to the value of `self.rgx` of the passed object (also accessed via method **get**).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

#### \_\_iadd\_\_
Expects variables of type `str` and `Regex`. For better understanding:

- `+= str`: concatenates `self.rgx` with the value of the passed variable;
- `+= Regex`: concatenates `self.rgx` with the value of variable `self.rgx` of the passed object (accessed via method **get**).

The overload directly changes the value of `self.rgx`. In case of operations like **Set** of an object, it will change to the value between to brackets.

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
Expects variables of type `str` and `Regex`. Unlike the overload of **\_\_iadd\_\_**, this overload returns a new **Regex** object.

- `+ str`: concatenates `self.rgx` (accessed via method **get**) with the value of the passed variable;
- `+ Regex`: concatenates `self.rgx` (accessed via method **get**) with the value of `self.rgx` of the passed object (also accessed via method **get**).

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

#### get
Returns the value stored in `self.rgx`.

```python
from mre import Regex

regex = Regex("stored value")
print(regex.get())  # "stored value"
```

#### quantifier
Has the following parameters:

| Parameter | Type | Default value |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Used to quantify how often a Regex may/should appear (from `n` to `m`). Returns a new **Regex**.

In specific cases, a symbol is added. These cases are:

| n | m | without_maximum | Symbol | Access |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |

In addition to these specific cases, quantification may occur as follows:
- `{n}`: should occur `n` times;
- `{n, m}`: may occur from `n` up to `m` times.

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
Has a parameter of type `int` (`group_n`) which is used to indicate which group you want to perform a *backreference*. Returns a **Regex** which performs [*backreferences*](https://www.regular-expressions.info/backref.html) of the indicated group.

An alternative way of calling this method, is providing an `int` to the constructor.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

## <a name="quantifier">Quantifier</a>
This class serves as an alternative to calling **Regex.quantifier**. The constructor has 4 parameters:

| Parameter | Type | default value |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

The first parameter refers to the RegEx you want to create, the other three are used to call method **Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

## <a name="set">Set</a>
This class represents a set in RegEx. The constructor is identical to **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

### Methods
This class inherits the methods of class **Regex**, overriding the following.

#### get
Returns the value stored in `self.rgx`, but within brackets.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

#### quantifier
Returns a new **Regex** objects with a quantifier for the set.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="group">Group</a>
This class represents a group in RegEx. The constructor has two parameters:

| Parameter | Type | default value |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

If the argument for `non_capturing` is `True`, the symbol indicating *RegEx Engine* to return a non capturing group is added(`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

### Methods
This class inherits the methods of class **Regex**, overriding the following.

#### get
Returns the value stored in `self.rgx`, but within parentheses.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

#### quantifier
Returns a new **Regex** objects with a quantifier for the group.

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="anchor">Anchor</a>
This class respresents an anchored RegEx (the RegEx must start and end as defined). The constructor has two parameters:

| Parameter | Type | default value |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

If the argument for `negate` is `True`, the inverse pattern symbol is added, i.e. the RegEx must not start and end as defined.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

### Methods
This class inherits the methods of class **Regex**, overriding the following.

#### get
Returns the value stored in `self.rgx`, but anchored.

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

## <a name="range">helper.Range</a>
This class is intended to assist in creating a RegEx that indicates a character class in form of a *range*. The constructor has two parameters:

| Parameter | Type | default value |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

Ideally you should use this class together with a **Set**. Within a **Set** the hyphen has a "magic" value, that allows it to assign a range. Outside of a set a hyphen has only the hyphen value. So if you want lowercase letters, you should use `[a-z]` instead of `a-z`. `a-z` indicates you only want the values `a`, `-` and `z`.

```python
from mre.helper import Range

# all digits
digits = Range(0, 9)
# all letters
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

### Methods
This class inherits the methods of the **Regex** class and has its own methods.

#### digits
Has two parameters:

| Parameter | Type | default value |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Returns a *range* that is defined as the digits between `minimum` and `maximum`.

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
Has four parameters:

| Parameter | Type | default value |
| --------- | ---- | ------------ |
| `minimum` | `chr` | `A` |
| `maximum` | `chr` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Returns a *range* that is defined as the letters between `minimum` and `maximum`.

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

# Examples

2 ways to create a RegEx for a **CEP** (brazilian postal code) (`[0-9]{5}-?[0-9]{3}`):
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

RegEx for a **CPF** (brazilian tax payer registry number) (`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):

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

RegEx for a **CNPJ** (ID in the brazilian National Registry of Legal Entities) (`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):

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
