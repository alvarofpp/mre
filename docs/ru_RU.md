# MRE

Python пакет для создания регулярных выражений (RegEx). Его цель - облегчить чтение RegEx.

## Установка MRE

Установите пакет MRE, используя pip:

```python
pip install mre
```

## Классы

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
  - [Range](#range)

### <a name="regex">Regex</a>

Это родительский класс для всех других в этом пакете, RegEx обрабатывается в переменной `self.rgx`.
Ваш конструктор может принимать любое количество параметров, но они должны быть одного из
следующих типов: `str`, `int` и сам класс `Regex`. Для лучшего понимания:

- `str`: соединяет перекменную с `self.rgx`;
- `int`: выполняет [*обратные ссылки*](https://www.regular-expressions.info/backref.html);
- `Regex`: соединяет значение `self.rgx` переданного объекта c переменной `self.rgx` принимающего
  объекта.

Способы объявления **Regex**:

```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

#### Константы

Константы доступные в классе **Regex**:

| Константа | Значение |
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

#### Методы

Описание методов и перегрузок

##### \_\_str\_\_

Возвращает значение хранимое в `self.rgx`.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

##### \_\_eq\_\_

Сравнения возможны между типами `str` и `Regex`:

- `== str`: сравнивает `self.rgx` со значением переданной переменной;
- `== Regex`: сравнивает `self.rgx` (полученный через метод **get**) со значением `self.rgx`
  переданного объекта (также полученного через метод **get**).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

##### \_\_iadd\_\_

Ожидает переменную типа `str` и `Regex`. Для лучшего понимания:

- `+= str`: cоединяет `self.rgx` со значением переданной переменной;
- `+= Regex`: соединяет `self.rgx` со значением переменной  `self.rgx` переданного объекта
  (полученным через метод **get**).

Перегрузка непосредственно меняет значение `self.rgx`. В случае таких операций как **Set**
объекта, оно изменится на значение  между скобками.

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

Ожидает переменную типа `str` и `Regex`. В отличии от перегрузки **\_\_iadd\_\_**, данная
перегрузка возвращает новый объект **Regex**.

- `+ str`: соединяет `self.rgx` (полученный через метод **get**) со значением переданной
  переменной;
- `+ Regex`: соединяет `self.rgx` (полученный через метод **get**) со значением `self.rgx`
  переданного объекта (также полученного через метод **get**).

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

##### get

Возвращает значение хранимое в `self.rgx`.

```python
from mre import Regex

regex = Regex("stored value")
print(regex.get())  # "stored value"
```

##### quantifier

Имеет следующие параметры:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Используется для количественной оценки насколько часто Regex может/должен появляться
(из  `n` в `m`). Возвращает новый **Regex**.

В особых случаях добавляется символ. Вот эти случаи:

| n | m | without_maximum | Symbol | Access |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |

В добавление к этим особым случаям, количественная оценка может происходить следующим образом:

- `{n}`: должен произойти `n` раз;
- `{n, m}`: может произойти от `n` до `m` раз.

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

Имеет параметр с типом `int` (`group_n`) который используется для указания для какой группы
вы хотите применить  *backreference*. Возвращает **Regex** который выполняет
[*backreferences*](https://www.regular-expressions.info/backref.html) указанной группы.

Альтернативным методом вызова данного метода является передача `int` в конструктор.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

### <a name="quantifier">Quantifier</a>

Данный класс предоставляет альтернативу вызову **Regex.quantifier**. Конструктор имеет 4 параметра:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Первый параметр ссылается на RegEx, который вы хотите создать, остальные три используются
для вызова метода **Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

### <a name="set">Set</a>

Этот класс представляет собой set в RegEx. Конструктор идентичен **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

#### Методы

Этот класс наследует методы класса **Regex**, переопределяя следующие.

##### get

Возвращает значение, хранящееся в `self.rgx`, но в скобках.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

##### quantifier

Возвращает новые **Regex** объекты с квантификатором для set.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

### <a name="group">Group</a>

Этот класс представляет группу в RegEx. Конструктор имеет два параметра:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

Если аргументом для `non_capturing` является `True`, добавляется символ, указывающий
*RegEx Engine* вернуть результат как группу без захвата(`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

#### Методы

Этот класс наследует методы класса **Regex**, переопределяя следующие.

##### get

Возвращает значение, хранящееся в `self.rgx`, но в скобках.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

##### quantifier

Возвращает новые **Regex** объекты с квантификатором для группы

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

### <a name="anchor">Anchor</a>

Этот класс представляет привязанный (anchor) RegEx (RegEx должен начинаться и заканчиваться,
как указано). Конструктор имеет два параметра:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

Если аргумент для `negate` равен `True`, добавляется символ обратного шаблона, то есть RegEx
не должен начинаться и заканчиваться, как указано.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

#### Методы

Этот класс наследует методы класса **Regex**, переопределяя следующие.

##### get

Возвращает значение, хранящееся в `self.rgx`, но привязанное (anchored)

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

### <a name="range">helper.Range</a>

Этот класс предназначен для помощи в создании RegEx, который указывает класс символов в форме
*range*. Конструктор имеет два параметра:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

В идеале вы должны использовать этот класс вместе с **Set**. Внутри **Set** у дефиса
есть «магическое» значение, которое позволяет ему назначать диапазон. Вне set дефис имеет
только значение дефиса. Поэтому, если вам нужны строчные буквы, вы должны использовать `[a-z]`
вместо `a-z`. `a-z` означает, что вам нужны только значения `a`, `-` и `z`.

```python
from mre.helper import Range

# all digits
digits = Range(0, 9)
# all letters
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

#### Методы

Этот класс наследует методы класса **Regex** и имеет свои собственные методы.

##### digits

Имеет два параметра:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Возвращает *range*, который определяется как цифры между `minimum` и `maximum`.

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

Имеет четыре параметра:

| Параметр | Тип | Значение по-умолчанию |
| --------- | ---- | ------------ |
| `minimum` | `char` | `A` |
| `maximum` | `char` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Возвращает диапазон который задан как буквы между `minimum` и `maximum`.

```python
from mre.helper import Range

# все буквы
regex_range_one = Range('A', 'z')
regex_range_two = Range.letters()
regex_range_three = Range.letters('A', 'z')
# все заглавные буквы
regex_range_five = Range.letters(uppercase=True)
# все строчные буквы
regex_range_six = Range.letters(lowercase=True)

print(regex_range_one)  # "A-z"
print(regex_range_two)  # "A-z"
print(regex_range_three)  # "A-z"
print(regex_range_four)  # "A-z"
print(regex_range_five)  # "A-Z"
print(regex_range_six)  # "a-z"
```

## Примеры

2 способа создать RegEx для **CEP** (бразильский почтовый индекс) (`[0-9]{5}-?[0-9]{3}`):

```python
from mre import Regex, Set

# все цифры
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

# все цифры [0-9]
digits = Set(Range.digits())
# дефис может появляться ноль или один раз
hyphen = Quantifier("-", 0, 1)

rgx_cep = Regex(
    digits.quantifier(5), hyphen,
    digits.quantifier(3),
)
```

Регулярное выражение для **CPF** (регистрационный номер налогоплательщика Бразилии)
(`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):

```python
from mre import Regex, Set
from mre.helper import Range

# все цифры
all_digits = Set(Range(0, 9))
# точка может появиться ноль или один раз
dot = Regex(Regex.DOT).quantifier(0, 1)
# дефис может появляться ноль или один раз
hyphen = Regex('-').quantifier(0, 1)

rgx_cpf = Regex(
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), dot,
    all_digits.quantifier(3), hyphen,
    all_digits.quantifier(2),
)
```

Регулярное выражение для **CNPJ** (Удостоверение личности в бразильском национальном
реестре юридических лиц) (`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):

```python
from mre import Regex, Quantifier

# все цифры
digits = Regex(Regex.DIGIT)
# точка может появиться ноль или один раз
dot = Regex(Regex.DOT).quantifier(0, 1)
# косая черта (слеш) может появиться ноль или один раз
slash = Regex(Regex.SLASH).quantifier(0, 1)
# дефис может появляться ноль или один раз
hyphen = Quantifier("-", 0, 1)

rgx_cnpj = Regex(
    digits.quantifier(2), dot,
    digits.quantifier(3), dot,
    digits.quantifier(3), slash,
    digits.quantifier(4), hyphen,
    digits.quantifier(2),
)
```
