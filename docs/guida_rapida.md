# catalogpy :)

## Installazione
Come installarlo? Semplice basta usare **pip**!
```bash
pip install catalogpy
```
Funzionalità e Utilizzo
Ogni funzione è progettata per eseguire un'operazione specifica. Puoi importare e usare solo le funzioni di cui hai bisogno.

```from catalogpy.catalog import elencation

words = ["mela", "kiwi", "banana", "arancia"]
result = elencation(words, min_len=4, max_len=6)
print(result)
# Output:
# kiwi
# mela

order_longer(words=None, min_len=0, max_len=inf)
Ordina le parole dalla più lunga alla più corta.

from catalogpy.catalog import order_longer

words = ["cat", "elephant", "dog", "bird"]
result = order_longer(words)
print(result)
# Output:
# elephant
# bird
# cat
# dog

order_shortest(words=None, min_len=0, max_len=inf)
Ordina le parole dalla più corta alla più lunga.

from catalogpy.catalog import order_shortest

words = ["cat", "elephant", "dog", "bird"]
result = order_shortest(words)
print(result)
# Output:
# cat
# dog
# bird
# elephant

unique_words(words=None, min_len=0, max_len=inf)
Restituisce un elenco di parole uniche, rimuovendo i duplicati. Le parole vengono filtrate e poi ordinate.

from catalogpy.catalog import unique_words

words = ["gatto", "cane", "gatto", "topo", "cane"]
result = unique_words(words)
print(result)
# Output:
# cane
# gatto
# topo
```



