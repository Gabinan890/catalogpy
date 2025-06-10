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

def unique_words(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        inp = input("Dammi delle parole e ti restituisco solo quelle uniche\n")
        words = inp.split()
    # Mantieni solo parole nel range di lunghezza, poi rimuovi duplicati mantenendo l'ordine
    seen = set()
    unique = []
    for w in words:
        if min_len <= len(w) <= max_len and w not in seen:
            seen.add(w)
            unique.append(w)
    unique.sort()
    return "\n".join(unique)

def clean_words(words=None, min_len=0, max_len=float('inf')):
    if words is None:
        inp = input("Dammi delle parole e le ripulisco da caratteri speciali e numeri\n")
        words = inp.split()
    cleaned = []
    for w in words:
        # Mantieni solo lettere dalla a alla z (sia minuscole che maiuscole)
        new_w = ''.join(c for c in w if ('a' <= c <= 'z') or ('A' <= c <= 'Z'))
        if min_len <= len(new_w) <= max_len and new_w:
            cleaned.append(new_w)
    cleaned.sort()
    return "\n".join(cleaned)
