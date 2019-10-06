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
- <a href="https://alvarofpp.github.io/mre/de">
    de <span>:de:</span>
  </a>
- <a href="https://alvarofpp.github.io/mre/dk">
    dk <span>:denmark:</span>
  </a>
- <a href="https://alvarofpp.github.io/mre/en_US">
    en-US <span>:us:</span>
  </a>
- <a href="https://alvarofpp.github.io/mre/es_ES">
    es-ES <span>:es:</span>
  </a>
- <a href="https://alvarofpp.github.io/mre/pt_BR">
    pt-BR <span>:brazil:</span>
  </a>

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
from mre import Regex, Set

# All digits
digits = Set(Regex("0-9"))

rgx_cep = Regex(
    digits.quantifier(5),
    Regex("-").quantifier(0, 1),
    digits.quantifier(3),
)

# Output: [0-9]{5}-?[0-9]{3}
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
