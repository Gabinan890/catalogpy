#Copyright (C) 2026 Gabriele Ristori

#Funzione elencation() ordina in ordine alfabetico le stringhe e facoltativamente può filtrare anche per lunghezza le parole

def elencation(words=None, min=None, max=None):
    if(words==None):
        inp=input("Inserisci le parole/Insert the words ")
        min=input("Inserisci il minimo/Insert the minimum")
        max=input("Inserisci il massimo/Insert de maximum")
    words=inp.replace(","," ").split()
    List=[]
    ì=0
    if(min!=None and max!=None and min!="" and max!=""):
        for w in words:
            if(w>=min and w<=max):
                List.append(w)
                ì+=1
        if(ì==0):
            print("Errore non ci sono parole dentro List")
            return "Errore non ci sono parole dentro List"
        else:
            elencation_list=sorted(List)
            print(elencation_list)
            return elencation_list
    else:
        for w in words:
            List.append(w)
            ì+=1
        if(ì==0):
            print("Errore non ci sono parole dentro List")
            return "Errore non ci sono parole dentro List"
        else:
            elencation_list=sorted(List)
            print(elencation_list)
            return elencation_list

#Prima funzione elencation() aggiornata e riscritta senza AI

def ordination(words=None, min_len=0, max_len=float('inf')):
    
    #Ordina e restituisce una lista di parole in ordine alfabetico, numerandole.
    
    if words is None:
        ind = input("Dammi delle parole e te le metto in ordine alfabetico e numerate:\n")
        words = ind.split()

    parole = [p for p in words if min_len <= len(p) <= max_len]
    parole.sort()
    risultato = [f"{i}. {parola}" for i, parola in enumerate(parole, start=1)]
    return "\n".join(risultato)

def order_longer(words=None, min_len=0, max_len=float('inf')):
    
    #Ordina e restituisce una lista di parole dalla più lunga alla più corta.
    
    if words is None:
        inp = input("Dammi delle parole e te le metto in ordine dalla più lunga alla più corta\n")
        words = inp.split()

    inlista = [w for w in words if min_len <= len(w) <= max_len]
    inlista.sort(key=len, reverse=True)
    return "\n".join(inlista)

def order_shortest(words=None, min_len=0, max_len=float('inf')):
    
    #Ordina e restituisce una lista di parole dalla più corta alla più lunga.
    
    if words is None:
        inp = input("Dammi delle parole e te la metto in ordine dalla più lunga alla più corta\n")
        words = inp.split()

    inlista = [w for w in words if min_len <= len(w) <= max_len]
    inlista.sort(key=len)
    return "\n".join(inlista)

def remove_words(words=None, min_len=0, max_len=float('inf')):
    
    # Rimuove le parole che non rispettano i parametri di lunghezza.

    if words is None:
        inp = input("Dammi delle parole e ti rimuovo quelle che non rispettano i parametri di lunghezza\n")
        words = inp.split()

    inlista = [w for w in words if min_len <= len(w) <= max_len]
    return "\n".join(inlista)

def unique_words(words=None, min_len=0, max_len=float('inf')):
    
    # Restituisce solo le parole uniche in ordine alfabetico.

    if words is None:
        inp = input("Dammi delle parole e ti restituisco solo quelle uniche\n")
        words = inp.split()

    # Rimuove i duplicati mantenendo l'ordine originale
    unique = list(dict.fromkeys(words))

    # Filtra e ordina le parole uniche
    filtered_and_sorted = [w for w in unique if min_len <= len(w) <= max_len]
    filtered_and_sorted.sort()

    return "\n".join(filtered_and_sorted)


# Questo codice è scritto maggiormente con AI ma non per molto ancora. :)

