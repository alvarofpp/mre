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

## Documentation

- [da-DK :denmark:](docs/da_DK.md) <small>(v. 0.8)</small>
- [de-DE :de:](docs/de_DE.md) <small>(v. 0.8)</small>
- [en-US :us:](docs/en_US.md) <small>(v. 0.9)</small>
- [es-ES :es:](docs/es_ES.md) <small>(v. 0.8)</small>
- [pt-BR :brazil:](docs/pt_BR.md) <small>(v. 0.10)</small>
- [ru-RU :ru:](docs/ru_RU.md) <small>(v. 0.8)</small>
- [uk-UA :ukraine:](docs/uk_UA.md) <small>(v. 0.8)</small>

## Examples

```python
from mre import Regex, Group

rgx_one = Regex("Hello world")  # Hello world
rgx_two = Regex("Hello", " world")  # Hello world
rgx_three = Regex("Hello") + " " + Regex("world")  # Hello world
rgx_four = Regex('<', Group('h[1-6]'), '>')  # <(h[1-6])>
rgx_five = Regex('<', Regex.SLASH, 1, '>')  # <\/\1>
```

```python
from mre import Set
from mre.helper import Range

# All digits
digits = Set(Range(0, 9))
# Add comment
digits = digits.comment('Get all digits')

# Output: [0-9](?#Get all digits)
```

```python
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

## Contributing
Contributions are more than welcome. Fork, improve and make a pull request. For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/mre/issues).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
