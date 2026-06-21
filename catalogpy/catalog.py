#Copyright (C) 2026 Gabriele Ristori

#La documentazione è un po pigra scusate cercherò di risolvere in futuro :)
#I try to explain my code in english but I'm not so good and I'm so busy with school actualy I've got some summer recovery exame at school in summer so I've to study 

#Funzione elencation() ordina in ordine alfabetico le stringhe e facoltativamente può filtrare anche per lunghezza le parole la uso anche come base per alcune delle altre funzioni
#This function elencation() reorder some string in alphabetich order and actualy some of the other function are based on elencation()

def elencation(words=None, min=None, max=None, text=None):
    #words is the only parameter that's not optional
    if(words==None):
        #Puoi effettivamente personalizzare le frasi di input ma il parametro text deve essere tassativamente di 3 elementi sennò partiranno le frasi di default in italiano

        #if you want you can personalize the input text but if the len() of text parameter is not 3 then will go the default input texts that are in italian 
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

#Prima funzione senza AI elencation() aggiornata e riscritta completamente bhe l'aggiornamento risale a qualche mese fa ma ho davvero poco tempo e sono pigro ma sono cosi fiero del mio lavoro :)
#The first function whitout AI elencation() all updated and rewritted well the update is of some moths ago but I'm so lazy and I don't have so much time but I'm so proud of my work :)

#ordination() serve ad ordinare in ordine alfabetico le stringhe numerandole
#ordination() is a usefull function similar to elencation but it can numerate all the word in the list

def ordination(start=1, words=None, min=None, max=None, text=None):
    inp=elencation(words, min, max, text)
    List=[]
    for numero, parola in enumerate(inp, start=start):
        List.append(f"{numero}. {parola}")
    return List
    #finalmente terza funzione fatta senza AI ordination() un'altro passo verso il grande aggiornamento!(21/06/2025):)
    #finally the third function whitout AI another step to the big update 2.0 is coming!(21/06/2025) :)

#Codice con le ore contate
#Some code with the counted hours.
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
#uique_words() you can create a list in alphabetich order or not erasing al the multiple words

def unique_words(ord=False, words=None, min=None, max=None, text=None):
    
    if(ord==True):
        inp=elencation(words, min, max, text)
        List=[]
        i=0
        for w in inp:
            if((w in inp)==False):
                List.append(w)
                i+=1
        if(i==0):
            return "Nessuna stringa soddisfa i parametri"
    else:
        if(words==None):
            if(text==None or len(text)!=3):
                inp=input("Inserisci le stringhe ")
                min=input("Inserisci il minimo ")
                max=input("Inserisci il massimo ")
            else:
                inp=input(text[0]+" ")
                min=input(text[1]+" ")
                max=input(text[2]+" ")
            words=inp.replace(","," "),split()

        ì=0
        Lis=[]
        if(min!=None and max!=None and min!="" and max!=""):
            for w in words:
                if(len(w)>=int(min) and len(w)<=int(max) and (w in Lis)==False):
                    Lis.append(w)
                    i+=1
        else:
            for w in words:
                if(w in Lis)==False:
                    Lis.append(w)
                    i+=1
        if(i==0):
            print("Errore nessuna stringa in Lis")
            return "Errore"
        else:
            print(Lis)
            return Lis

#Seconda funzione scritta senza AI unique_words() sono cosi felice
#Second function whitout AI unique_words() I'm so happy

#Questo codice è scritto maggiormente con AI ma non per molto ancora. :)
#This code is generated for the most with AI but not for many :)
