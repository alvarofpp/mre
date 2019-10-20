# clase

- [Regex](#regex)
- [Quantifier](#quantifier)
- [Set](#set)
- [Group](#group)
- [Anchor](#anchor)
- Helper
- [Range](#range)

## <a name="regex">Regex</a>

Aceasta este clasa părinte a tuturor celorlalte clase din acest pachet. Expresia regulată este procesată în variabila „self.rgx`. Constructorul poate avea orice număr de parametri, dar toate au tipul „str`,` int` sau clasa `Regex` în sine. Pentru o mai bună înțelegere:
- `str`: додається до змінної` self.rgx`
- `int`: виконує [*backreferences*](https://www.regular-expressions.info/backref.html)
- `Regex`: додає значення` self.rgx` даного об'єкта до змінної `self.rgx` отриманого об'єкта


Modalități de a declara o expresie obișnuită  **Regex**:
```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

### constante
Доступні константи класу **Regex**:

| Константа | Значення |
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

### metode
Опис методів і перевантажень.

#### \_\_str\_\_
Повертає значення, що зберігається в змінній `self.rgx`.

```python
from mre import Regex

regex = Regex("Hello world")
print(regex)  # "Hello world"
```

#### \_\_eq\_\_
Sunt posibile comparații între tipuri`str` та` Regex`:
- `== str`: порівнює` self.rgx` зі значенням переданої змінної.
- `== Regex`: порівнює `self.rgx` (Доступ через метод **get**) зі змінною `self.rgx` переданого об'єкта (також методом **get**).

```python
from mre import Regex

regex_one = Regex("Hello world")

print(regex_one == "Hello world")  # True
print(regex_one == "Hello world!")  # False

print(regex_one == Regex("Hello world"))  # True
print(regex_one == Regex("Hello world!"))  # False
```

#### \_\_iadd\_\_
Очікує змінну типу `str` або` Regex`. Для кращого розуміння:

- `+ = str`: об'єднує значення переданого рядка до змінної` self.rgx`;
- `+ = Regex`: об'єднує змінну` self.rgx` та змінну `self.rgx` даного об'єкта (доступ за допомогою методу **get**).


O suprasarcină schimbă direct valoarea variabilei „self.rgx`. În cazul unei operații precum ** Set ** un obiect, valoarea este setată între paranteze.

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
Очікує змінну типу `str` або` Regex`. На відміну від перевантаження **\_\_iadd\_\_**, це перевантаження повертає новий **Regex** об'єкт.

- `+ str`: об'єднує значення переданого рядка до змінної `self.rgx` (доступ за допомогою методу **get**);
- `+ Regex`: об'єднує змінну `self.rgx` (доступ за допомогою методу  **get**) та значення змінної `self.rgx` переданого об'єкта (також доступ за допомогою методу **get**).

```python
from mre import Regex

regex_one = Regex("Hello") + " " + Regex("world")
regex_two = Regex("Hello") + Regex(" world")

print(regex_one)  # "Hello world"
print(regex_two)  # "Hello world"
```

#### get
Повертає значення, збережене в `self.rgx`.

```python
from mre import Regex

regex = Regex("stored value")
print(regex.get())  # "stored value"
```

#### quantifier
Має такі параметри:

| Параметр | Тип | Стандартне значення |
| --------- | ---- | ------------ |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |

Використовується для кількісної оцінки того, як часто має з’являтися регулярний вираз (від `n` до` m`). Повертає новий об’єкт **Regex**.


În cazuri speciale, se adaugă un simbol. Acestea sunt următoarele cazuri:

| n | m | without_maximum | Символ | Доступ |
| --- | --- | --------------- | ------- | ------ |
| `0` | `1` | - | `?` | `Regex.ZERO_OR_ONE` |
| `0` | - | `True` | `*` | `Regex.ZERO_OR_MULTIPLE` |
| `1` | - | `True` | `+` | `Regex.ONE_OR_MULTIPLE` |


Pe lângă aceste cazuri speciale, cuantificarea poate fi următoarea:
- `{n}`: має відбутися `n` разів;
- `{n, m}`: може відбуватися від `n` до `m` разів.

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
Має параметр типу `int` (`group_n`) який використовується для вказівки, яку групу ви хочете використовувати для *backreference*. Повертає об'єкт типу **Regex**, який виконує [*backreferences*](https://www.regular-expressions.info/backref.html) групи, що відображається.


O modalitate alternativă de a apela această funcție este de a oferi constructorul `int`.

```python
from mre import Regex

regex_one = Regex().backreferences(1)
regex_two = Regex(2)

print(regex_one)  # "\1"
print(regex_two)  # "\2"
```

## <a name="quantifier">Quantifier</a>
Această clasă este o alternativă la apelul ** Regex.quantifier **. Acest constructor are 4 parametri:

| Параметр | Тип | Стандартне значення |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `n` | `int` | `0` |
| `m` | `int` | `0` |
| `without_maximum` | `bool` | `False` |


Primul parametru se referă la expresia regulată care trebuie creată. Celelalte trei sunt pentru apelarea metodei
**Regex.quantifier**.

```python
from mre import Regex, Quantifier

digits_one = Regex("[0-9]").quantifier(3, 5)
digits_two = Quantifier("[0-9]", 3, 5)

print(digits_one)  # "[0-9]{3,5}"
print(digits_two)  # "[0-9]{3,5}"
```

## <a name="set">Set</a>
Цей клас представляє набір (set) у RegEx. Конструктор ідентичний **Regex**.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"
```

### metode
Цей клас успадковує методи класу **Regex** і перевантажує наступні методи:

#### get
Повертає значення, збережене в  `self.rgx`, але в дужках.

```python
from mre import Set

regex_set = Set("0-9")
print(regex_set.get())  # "[0-9]"
```

#### quantifier
Повертає новий об'єкт **Regex** з кількісним показником для набору.

```python
from mre import Set

regex_set = Set("0-9")

print(regex_set)  # "[0-9]"
print(regex_set.quantifier(3))  # "[0-9]{3}"

print(type(regex_set))  # <class 'mre.Set.Set'>
print(type(regex_set.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="group">Group</a>
Цей клас представляє групу в RegEx. Конструктор має два параметри:

| Параметр | Тип | Стандартне значення |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `non_capturing` | `bool` | `False` |

Якщо вираз для `non_capturing` є `True`, символ, що відображає *RegEx Engine*, додається до групи Non-Captured-Gruppe (`?:`).

```python
from mre import Group

regex_group_one = Group('<h1>') + Group('[\w\s]+') + Group('</h1>')
regex_group_two = Group('<h1>', True) + Group('[\w\s]+') + Group('</h1>', True)

print(regex_group_one)  # (<h1>)([\w\s]+)(</h1>)
print(regex_group_two)  # (?:<h1>)([\w\s]+)(?:</h1>)
```

### metode
Цей клас успадковує методи класу **Regex** і перевантажує наступні методи:

#### get
Повертає значення, збережене в `self.rgx`, але в дужках.

```python
from mre import Group

regex_group_one = Group("<h1>")
regex_group_two = Group("</h1>", True)

print(regex_group_one.get())  # "(<h1>)"
print(regex_group_two.get())  # "(?:</h1>)"
```

#### quantifier
Повертає новий об'єкт **Regex** з кількісним показником для набору.

```python
from mre import Group

regex_group = Group("<h1>")

print(regex_group)  # "(<h1>)"
print(regex_group.quantifier(3))  # "(<h1>){3}"

print(type(regex_group))  # <class 'mre.Group.Group'>
print(type(regex_group.quantifier(3)))  # <class 'mre.Regex.Regex'>
```

## <a name="anchor">Anchor</a>

Această clasă este o expresie regulată legată (RegEx trebuie să înceapă și să se încheie după cum este specificat). Constructorul are doi parametri:

| Параметр | Тип | Стандартне значеняя |
| --------- | ---- | ------------ |
| `regex` | `str`, `int`, `Regex` | `""` |
| `negate` | `bool` | `False` |

Якщо аргумент для `negate` є `True` до символів додається зворотній шаблон (Inverse Pattern), тобто, RegEx не повинен починатися та закінчуватися, як вказано.

```python
from mre import Anchor

regex_anchor_one = Anchor("\\d{4}-\\w+.txt")
regex_anchor_two = Anchor("\\d{4}-\\w+.txt", True)

print(regex_anchor_one)  # "^\d{4}-\w+.txt$"
print(regex_anchor_two)  # "\b\d{4}-\w+.txt\B"
```

### metode
Цей клас успадковує методи класу **Regex** і перевантажує наступні методи:

#### get
Повертає значення, збережене в `self.rgx`, та закріплює його.

```python
from mre import Anchor

regex_anchor_one = Anchor("<h1>Hello world<\/h1>")
regex_anchor_two = Anchor("<h1>Hello world<\/h1>", True)

print(regex_anchor_one.get())  # "^<h1>Hello world</h1>$"
print(regex_anchor_two.get())  # "\b<h1>Hello world</h1>\B"
```

## <a name="range">helper.Range</a>
Цей клас створений, щоб допомогти створити RegEx, який представляє собою клас символів у вигляді *range*. Конструктор має два параметри:

| Параметр | Тип | Стандартне значеняя |
| --------- | ---- | ------------ |
| `minimum` | `str`, `int` | `0` |
| `maximum` | `str`, `int` | `"z"` |

В ідеалі вам слід використовувати клас разом із **Set**. У **Set** дефіс має "магічне" значення, що дозволяє призначити проміжок. Поза набору дефіс має лише значення дефісу. Тож якщо ви хочете малі літери, вам слід використовувати `[a-z]` замість `a-z`. `a-z` вказує лише на те, що ви бажаєте символи `a`, `-` і `z`.

```python
from mre.helper import Range

# all digits
digits = Range(0, 9)
# all letters
letters = Range('A', 'z')

print(digits)  # "0-9"
print(letters)  # "A-z"
```

### metode
Цей клас успадковує методи класу **Regex** і має свої методи.

#### digits
Має два параметри:

| Параметр | Тип | Стандартне значеняя |
| --------- | ---- | ------------ |
| `minimum` | `int` | `0` |
| `maximum` | `int` | `9` |

Повертає діапазон (*range*), визначений цифрами між  `minimum` і `maximum`.

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
Має чотири параметри:

| Параметр | Тип | Стандартне значення |
| --------- | ---- | ------------ |
| `minimum` | `chr` | `A` |
| `maximum` | `chr` | `z` |
| `uppercase` | `bool` | `False` |
| `lowercase` | `bool` | `False` |

Повертає діапазон (*range*), визначений цифрами між `minimum` і `maximum`.

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

# exemple

Є два способи створити RegEx для **CEP** (Бразильський поштовий індекс) (`[0-9]{5}-?[0-9]{3}`):
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

RegEx для **CPF** (Бразильський податковий номер) (`[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}`):

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

RegEx для **CNPJ** (Ідентифікатор (ID) у бразильській базі даних для юридичних осіб) (`\d{2}\.?\d{3}\.?\d{3}\/?\d{4}\-?\d{2}`):

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
