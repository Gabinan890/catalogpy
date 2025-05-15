def elencation(min_len=0, max_len=float('inf')):
    lista = []
    inp = input("Dammi delle parole e te le metto in ordine alfabetico\n")
    inlista = inp.split()
    for i in inlista:
        if min_len <= len(i) <= max_len:
            lista.append(i)
    lista.sort()
    return "\n".join(lista)


def ordination(min_len=0, max_len=float('inf')):
    ind = input("Dammi delle parole e te le metto in ordine alfabetico e numerate:\n")
    parole = ind.split()
    parole = [p for p in parole if min_len <= len(p) <= max_len]
    parole.sort()

    risultato = []
    for i, parola in enumerate(parole, start=1):
        risultato.append(f"{i}. {parola}")

    return "\n".join(risultato)


def order_longer(min_len=0, max_len=float('inf')):
    lista = []
    inp = input("Dammi delle parole e te le metto in ordine dalla più lunga alla più corta\n")
    inlista = inp.split()
    inlista = [i for i in inlista if min_len <= len(i) <= max_len]
    inlista.sort(key=len, reverse=True)

    return "\n".join(inlista)


def order_shortest(min_len=0, max_len=float('inf')):
    lista = []
    inp = input("Dammi delle parole e te la metto in ordine dalla più lunga alla più corta\n")
    inlista = inp.split()
    inlista = [i for i in inlista if min_len <= len(i) <= max_len]
    inlista.sort(key=len)

    return "\n".join(inlista)


def remove_words(min_len=0, max_len=float('inf')):
    inp = input("Dammi delle parole e ti rimuovo quelle che non rispettano i parametri di lunghezza\n")
    inlista = inp.split()

    if min_len == 0 and max_len == float('inf'):
        return ""

    inlista = [i for i in inlista if min_len <= len(i) <= max_len]

    return "\n".join(inlista)
