#Copyright (C) 2026 Gabriele Ristori

#La documentazione è un po pigra scusate cercherò di risolvere in futuro :)

#Funzione elencation() ordina in ordine alfabetico le stringhe e facoltativamente può filtrare anche per lunghezza le parole

def elencation(words=None, min=None, max=None, text=None):
    if(words==None):
        if(text==None or len(text)!=3):
            inp=input("Inserisci le parole ")
            min=input("Inserisci il minimo ")
            max=input("Inserisci il massimo ")
        else:
            inp=input(text[0]+" ")
            min=input(text[1]+" ")
            max=input(text[2]+" ")
        words=inp.replace(","," ").split()
    List=[]
    i=0
    if((min!=None and min!="") or (max!="" and max!="")):
        for w in words:
            if(len(w)>=int(min) and len(w)<=int(max)):
                List.append(w)
                i+=1
    else:
        for w in words:
            List.append(w)
            i+=1
    if(i==0):
        print("Errore nessuna stringa in Lis")
        return "Errore"
    elencation_list=sorted(List)
    return elencation_list

#Prima funzione senza AI elencation() aggiornata e risscritta completamente bhe l'aggiornamento risale a qualche mese fa ma ho davvero poco tempo e sono pigro :)

#Vecchia versione di elencation() per ora me la salvo qui

"""
def elencation(words=None, min=None, max=None):
    if(words==None):
        #Implementazione lingua inglese ancora in fase di test :)
        #Mi sembrava brutto usare due lingue quindi ne uso solo una :) il mio inglese fa schifo lo so
        inp=input("Insert the words ")
        min=input("Insert the minimum ")
        max=input("Insert the maximum ")
    words=inp.replace(","," ").split()
    List=[]
    i=0
    if(min!=None and max!=None and min!="" and max!=""):
        for w in words:
            if(len(w)>=int(min) and len(w)<=int(max)):
                List.append(w)
                i+=1
    else:
        for w in words:
            List.append(w)
            i+=1
    if(i==0):
        return "Errore"
    elencation_list=sorted(List)
    return elencation_list
"""
#Prima funzione elencation() aggiornata e riscritta senza AI (vecchia!)

#ordination() serve ad ordinare in ordine alfabetico le stringhe numerandole

def ordination(start=1, words=None, min=None, max=None, text=None):
    inp=elencation(words, min, max, text)
    List=[]
    for numero, parola in enumerate(inp, start=start):
        List.append(f"{numero}. {parola}")
    return List
    #finalmente terza funzione fatta senza AI ordination() :)


#vecchia ordination() fatta con l'AI:

"""
    #Ordina e restituisce una lista di parole in ordine alfabetico, numerandole.
    
    if words is None:
        ind = input("Dammi delle parole e te le metto in ordine alfabetico e numerate:\n")
        words = ind.split()

    parole = [p for p in words if min_len <= len(p) <= max_len]
    parole.sort()
    risultato = [f"{i}. {parola}" for i, parola in enumerate(parole, start=1)]
    return "\n".join(risultato)
"""

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

#unique_words() permette di creare un'elenco in ordine alfabetico o meno a scelta dell'utente eliminando tutte le parole che si ripetono

def unique_words(words=None, min=None, max=None, ord=""):
    if(words==None):
        inp=input("Inserisci le stringhe ")
        min=input("Inserisci il minimo ")
        max=input("Inserisci il massimo ")
        ord=input("Vuoi oridnare il oridne alfabetico le stringhe?Y/n ")
        words=inp.replace(","," ").split()
    ì=0
    Lis=[]
    if(min!=None and max!=None and min!="" and max!=""):
        for w in words:
            if(len(w)>=int(min) and len(w)<=int(max) and (w in Lis)==False):
                Lis.append(w)
                ì+=1
    else:
        for w in words:
            if(w in Lis)==False:
                Lis.append(w)
                ì+=1
    if(ì==0):
        print("Errore nessuna stringa in Lis")
        return "Errore"
    #Uso ord per chiedere all'utente se vuole elencare o meno le stringhe in ordine alfabetico
    if(ord=="y"):
        elencationUnique=sorted(Lis)
        print(elencationUnique)
        return elencationUnique
    else:
        print(Lis)
        return Lis

#Seconda funzione scritta senza AI unique_words()



#Questo codice è scritto maggiormente con AI ma non per molto ancora. :)

