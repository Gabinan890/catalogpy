
# catalogpy :)

[![PyPI Version](https://img.shields.io/pypi/v/catalogpy)](https://pypi.org/project/catalogpy/)
[![Total Downloads](https://static.pepy.tech/badge/catalogpy)](https://pepy.tech/project/catalogpy)
[![License](https://img.shields.io/pypi/l/catalogpy)](https://pypi.org/project/catalogpy/)

# Chose the language

* [Documentazione in italiano](#documentazione-in-italiano)
* [Documentation in english](#documentation-in-english)

## Documentazione in italiano
catalogpy è una libreria che ti permette di ordinare le tue stringhe, e mantenere il tuo codice più pulito!

## Installazione
Come installarlo? Semplice basta usare **pip**!
```bash
pip install catalogpy
```

## Funzionalità e Utilizzo
Ogni funzione è progettata per eseguire un'operazione specifica. Puoi importare e usare solo le funzioni di cui hai bisogno.

```elencation(words, min, max, text)```

Ordina le parole in ordine alfabetico e le restituisce in una stringa, filtrate per lunghezza.

```from catalogpy.catalog import elencation

words = ["mela", "kiwi", "banana", "arancia"]
elencation(words, min=4, max=6)
# Output:
# ['kiwi', 'mela']
```

-----

```ordination(start, words, min, max, text)```

Restituisce una lista di stringhe in ordine alfabetico numerandole. Modificando il parametro start è possibile decidere da che numero iniziare a numerare la lista di parole di default è impostato su 1.

```from catalogpy.catalog import ordination

words = ["mela, "kiwi", "banana", "arancia"]
print(ordination(4, words, min=4, max=6)
# Output:
# ['4. kiwi', '5. mela']
```

-----

```unique_words(ord, words, min, max, text)```

Restituisce un elenco di parole uniche, rimuovendo i duplicati. Le parole vengono filtrate e se vuoi usando il parametro ord puoi decidere se ordinare in ordine alfabetico le parole di default il parametro è su False.

```from catalogpy.catalog import unique_words

words = ["gatto", "cane", "gatto", "topo", "cane"]
unique_words(True, words)
# Output:
# ['cane', 'gatto', 'topo']
```
-----
#Licenza
#Italiano
Questo progetto è distribuito sotto licenza GNU GPL v3. Consulta file LICENSE per dettagli.

-----

## Documentation in english
catalogpy is a library that allow to you to order your string, and mantain clean your code!

## Installation
How to dowload it? It's simple just use **pip**!
```bash
pip install catalogpy
```

## Funtionalities and utility

Each function is designed to execute an a specific operation. You can import and use only the function that you need.

```elencation(words, min, max, text)```

Order the word in alphabetical order and return them into a string, you can also filter the word by lenght.

```from catalogpy.catalog import elencation

words = ["mela", "kiwi", "banana", "arancia"]
elencation(words, min=4, max=6)
# Output:
# ['kiwi', 'mela']
```

-----

```ordination(start, words, min, max, text)```

Return a list of string in alphabetical order numbering them. If you modify the start parameter it's possible modify from what number start the counter that is 1 in default.

```from catalogpy.catalog import ordination

words = ["mela, "kiwi", "banana", "arancia"]
print(ordination(4, words, min=4, max=6)
# Output:
# ['4. kiwi', '5. mela']
```

-----

```unique_words(ord, words, min, max, text)```

Return an list of unique words remove al the duplicates. The words are filtered and if you want with the ord parameter you can order in alphabetical order the words, the parameter is False as default.

```from catalogpy.catalog import unique_words

words = ["gatto", "cane", "gatto", "topo", "cane"]
unique_words(True, words)
# Output:
# ['cane', 'gatto', 'topo']
```
-----
#License

This project is under the GNU GPL v3 license. Read then file LICENSE for more info.
