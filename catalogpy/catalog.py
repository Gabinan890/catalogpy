def elencation():
    lista = []
    inp = input("Dammi delle parole e te la metto in ordine alfabetico\n")
    inlista = inp.split()
    for i in inlista:
        lista.append(i)
    lista.sort()
    return "\n".join(lista)

def ordination():
    ind = input("Dammi delle parole e te le metto in ordine alfabetico e numerate:\n")
    parole = ind.split()
    parole.sort()

    risultato = []
    for i, parola in enumerate(parole, start=1):
        risultato.append(f"{i}. {parola}")

    return "\n".join(risultato)

def order_longer():
    lista = []
    inp = input("Dammi delle parole e te la metto in ordine dalla più lunga alla più corta\n")
    inlista = inp.split()
    for i in inlista:
        lista.append(i)
    lista.sort(key=len, reverse=True)
    return "\n".join(lista)

def order_shortest():
    lista = []
    inp = input("Dammi delle parole e te la metto in ordine dalla più lunga alla più corta\n")
    inlista = inp.split()
    for i in inlista:
        lista.append(i)
    lista.sort(key=len)
    return "\n".join(lista)
