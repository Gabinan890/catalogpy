def elencation(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        inp = input("Dammi delle parole e te le metto in ordine alfabetico\n")
        words = inp.split()
    lista = [w for w in words if min_len <= len(w) <= max_len]
    lista.sort()
    return "\n".join(lista)

def ordination(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        ind = input("Dammi delle parole e te le metto in ordine alfabetico e numerate:\n")
        words = ind.split()
    parole = [p for p in words if min_len <= len(p) <= max_len]
    parole.sort()
    risultato = [f"{i}. {parola}" for i, parola in enumerate(parole, start=1)]
    return "\n".join(risultato)

def order_longer(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        inp = input("Dammi delle parole e te le metto in ordine dalla più lunga alla più corta\n")
        words = inp.split()
    inlista = [w for w in words if min_len <= len(w) <= max_len]
    inlista.sort(key=len, reverse=True)
    return "\n".join(inlista)

def order_shortest(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        inp = input("Dammi delle parole e te la metto in ordine dalla più lunga alla più corta\n")
        words = inp.split()
    inlista = [w for w in words if min_len <= len(w) <= max_len]
    inlista.sort(key=len)
    return "\n".join(inlista)

def remove_words(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        inp = input("Dammi delle parole e ti rimuovo quelle che non rispettano i parametri di lunghezza\n")
        words = inp.split()
    if min_len == 0 and max_len == float('inf'):
        return ""
    inlista = [w for w in words if min_len <= len(w) <= max_len]
    return "\n".join(inlista)