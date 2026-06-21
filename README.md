
# catalogpy :)

[![PyPI Version](https://img.shields.io/pypi/v/catalogpy)](https://pypi.org/project/catalogpy/)
[![Total Downloads](https://static.pepy.tech/badge/catalogpy)](https://pepy.tech/project/catalogpy)
[![License](https://img.shields.io/pypi/l/catalogpy)](https://pypi.org/project/catalogpy/)

catalogpy è una libreria che ti permette di ordinare le tue stringhe, e mantenere il tuo codice più pulito!

## Installazione
Come installarlo? Semplice basta usare **pip**!
```bash
pip install catalogpy
```
Funzionalità e Utilizzo
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

```unique_words(words, min, max, text)```
Restituisce un elenco di parole uniche, rimuovendo i duplicati. Le parole vengono filtrate e poi ordinate.

```from catalogpy.catalog import unique_words

words = ["gatto", "cane", "gatto", "topo", "cane"]
unique_words(words)
# Output:
# ['cane', 'gatto', 'topo']
```
-----
#Licenza
Questo progetto è distribuito sotto licenza GNU GPL v3. Consulta file LICENSE per dettagli.
