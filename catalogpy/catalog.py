def elencation(words=None, min_len=0, max_len=float('inf')):
    """
    Ordina e restituisce una lista di parole in ordine alfabetico,
    filtrando per lunghezza.
    """
    if words is None:
        inp = input("Dammi delle parole e te le metto in ordine alfabetico\n")
        words = inp.split()

    lista = [w for w in words if min_len <= len(w) <= max_len]
    lista.sort()
    return "\n".join(lista)


def ordination(words=None, min_len=0, max_len=float('inf')):
    """
    Ordina e restituisce una lista di parole in ordine alfabetico,
    numerandole.
    """
    if words is None:
        ind = input("Dammi delle parole e te le metto in ordine alfabetico e numerate:\n")
        words = ind.split()

    parole = [p for p in words if min_len <= len(p) <= max_len]
    parole.sort()
    risultato = [f"{i}. {parola}" for i, parola in enumerate(parole, start=1)]
    return "\n".join(risultato)


def order_longer(words=None, min_len=0, max_len=float('inf')):
    """
    Ordina e restituisce una lista di parole dalla più lunga alla più corta.
    """
    if words is None:
        inp = input("Dammi delle parole e te le metto in ordine dalla più lunga alla più corta\n")
        words = inp.split()

    inlista = [w for w in words if min_len <= len(w) <= max_len]
    inlista.sort(key=len, reverse=True)
    return "\n".join(inlista)


def order_shortest(words=None, min_len=0, max_len=float('inf')):
    """
    Ordina e restituisce una lista di parole dalla più corta alla più lunga.
    """
    if words is None:
        inp = input("Dammi delle parole e te la metto in ordine dalla più lunga alla più corta\n")
        words = inp.split()

    inlista = [w for w in words if min_len <= len(w) <= max_len]
    inlista.sort(key=len)
    return "\n".join(inlista)


def remove_words(words=None, min_len=0, max_len=float('inf')):
    """
    Rimuove le parole che non rispettano i parametri di lunghezza.
    """
    if words is None:
        inp = input("Dammi delle parole e ti rimuovo quelle che non rispettano i parametri di lunghezza\n")
        words = inp.split()

    inlista = [w for w in words if min_len <= len(w) <= max_len]
    return "\n".join(inlista)


def unique_words(words=None, min_len=0, max_len=float('inf')):
    """
    Restituisce solo le parole uniche in ordine alfabetico.
    """
    if words is None:
        inp = input("Dammi delle parole e ti restituisco solo quelle uniche\n")
        words = inp.split()

    # Rimuove i duplicati mantenendo l'ordine originale
    unique = list(dict.fromkeys(words))

    # Filtra e ordina le parole uniche
    filtered_and_sorted = [w for w in unique if min_len <= len(w) <= max_len]
    filtered_and_sorted.sort()

    return "\n".join(filtered_and_sorted)


