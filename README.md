# Maker Regular Expression
<a href="https://pypi.org/project/mre/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/mre.svg">
</a>

This is a simple package to make regular expressions in Python.

```bash
pip install mre
```

- Test regex: [Regex101](https://regex101.com/);
- [Regular expression operations](https://docs.python.org/3/library/re.html).

<span>Documentation:</span>
- <a href="https://alvarofpp.github.io/mre/da_DK">
    da-DK <span>:denmark:</span>
  </a> <small>(v. 1.0)</small>
- <a href="https://alvarofpp.github.io/mre/de_DE">
    de-DE <span>:de:</span>
  </a> <small>(v. 1.0)</small>
- <a href="https://alvarofpp.github.io/mre/en_US">
    en-US <span>:us:</span>
  </a> <small>(v. 1.1)</small>
- <a href="https://alvarofpp.github.io/mre/es_ES">
    es-ES <span>:es:</span>
  </a> <small>(v. 1.0)</small>
- <a href="https://alvarofpp.github.io/mre/pt_BR">
    pt-BR <span>:brazil:</span>
  </a> <small>(v. 1.2)</small>
- <a href="https://alvarofpp.github.io/mre/ru_RU">
    ru-RU <span>:ru:</span>
  </a> <small>(v. 1.0)</small>
- <a href="https://alvarofpp.github.io/mre/uk_UA">
    uk-UA <span>:ukraine:</span>
  </a> <small>(v. 1.0)</small>

## Examples
```py
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

```py
from mre import Set
from mre.helper import Range

# All digits
digits = Set(Range(0, 9))
# Add comment
digits = digits.comment('Get all digits')

# Output: [0-9](?#Get all digits)
```

```py
from mre import Regex, Set, Comment

# All digits
digits = Set(Regex("0-9"))
# CEP comment
cep_comment = Comment('Get zip code Brazil on input')
# CEP regex
rgx_cep = Regex(
    digits.quantifier(5),
    Regex("-").quantifier(0, 1),
    digits.quantifier(3),
    cep_comment
)

# Output: [0-9]{5}-?[0-9]{3}(?#Get zip code Brazil on input)
```

## Contributing documentation

```bash
pip install -r requirements-dev.txt
```
Running documentation

```bash
mkdocs serve
```
Change or create files in the `docs` folder.
