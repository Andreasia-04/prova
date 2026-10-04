import sys # serve per leggere quello che arriva da input

dispensa={} #dizionario vuoto
            #all'inizio non abbiamo nulla nella dispensa della pizzeria

#IDEA: dopo che viene chiamato il comando RESTOCK aggiungiamo coppie ingrediente quantità
#ad esempio RESTOCK flour 10 , dentro dispensa abbiamo la coppia{ "flour":10 }
#poi ad esempio arriva RESTOCK tomato 5, e dentro dispensa abbiamo 
# { "flour":10 , "tomato":5}

ricette={} #dizionario per defìpositare ricette
ordini={} #dizionario per gestire ordini : dtruttura del tipo "nomePizza:[lista ingredienti pizza]"

for line in sys.stdin: #per ogni riga che arriva in input

    words=line.split() # trasforma line in un array in cui ogni elemento della riga viene separato
                       # es: line= "RESTOCK flour 10" words = ["RESTOCK", "flour", "10"]
                       #in questo modo posso prendere ogni parola facendo tipo words[2] prendo 10
    if not words:
        continue #se line è vuoto passa alla line successiva, questa riga viene ignora(chiesto dalla traccia)

    comando=words[0] #la prima lettera è un comando

    if comando == "RESTOCK": #Se il comando è RESTOCK devo aggiungere la quantità specificata nell'
                             #ingrediente presente nel dizionario
        
        
        if len(words) != 3 or not words[1].isalpha() or not words[2].isdigit() or int (words[2])<=0:
            print("ERROR invalid command")
            continue

        #isalpha() serve per controllare se c'è una stringa
        #is digit() serve per contrllare se c'è un numero


        ingrediente=words[1]
        quantità=int(words[2]) #riocrda che da stringa deve passare intero sennò non la legge

        dispensa[ingrediente]=dispensa.get(ingrediente,0)+quantità 
        #dispensa.get(ingrediente,0):se ingrediente è in dispensa ottengo la quantità , se non c'è prende zero
        #e crea la coppia "ingrediente":quantità nella dispensa

        print("OK")

    elif comando=="STOCK": #se il comando è stock riotrna la quantità dell'ingrediente oppure 0 se non c'è 

        if len(words) !=2 or not words[1].isalpha():
             print("ERROR invalid command")
             continue
        
        ingrediente=words[1]
        print(dispensa.get(ingrediente,0))

    
    elif comando=="TRASH": #qua invece bisogna eleminare la quanittà specificata nella riga
        
        if len(words) != 3 or not words[1].isalpha() or not words[2].isdigit() or int (words[2])<=0:
                    print("ERROR invalid command")
                    continue
        ingrediente=words[1]
        quantità=int(words[2])

        if dispensa.get(ingrediente,0)<quantità:
            print("Errore non c'è abbastanza ingrediente",ingrediente)
        else:
            dispensa[ingrediente]=dispensa.get(ingrediente,0)-quantità
            print("OK")

    elif comando=="RECIPE":
        if len(words) < 3 or not words[1].isalpha() or any(not w.isalpha() for w in words[2:]):
                    print("ERROR invalid command")
                    continue
        
        pizza=words[1]
        ingredienti=words[2:] #prende come ingrediente tutto ciò che viene dopo la posizione 2 (compresa) 
                              #e la mette dentro un array, ottenendo lista degli ingredienti
    
        ricette[pizza] =ingredienti
        print("OK")

    elif comando=="ORDER":
        if len(words) != 2 or not words[1].isalpha():
                    print("ERROR invalid command")
                    continue
        pizza=words[1]
    
        if pizza not in ricette:
            print("Errore, pizza sconosciuta")
            continue
        else:
            possibileOrdine=True
            necessari={}# metto in un dizionario gli ingredienti che mi servono e il loro numero per quella pizza
            for ingredinte in ricette[pizza]:
                    necessari[ingrediente]=necessari.get(ingrediente,0)+1 
            
            for ingrediente in necessari:
                 if dispensa.get(ingrediente,0)< necessari[ingrediente]:
                      print("Errore, non c'è abbastanza quantità di:", ingrediente)
                      #se nella dispensa non bho abbastanza ingredienti non posso fare la pizza
                      possibileOrdine=False
                      break
                 

            if possibileOrdine==True:
                    for ingrediente in necessari:
                         dispensa[ingrediente]-=necessari[ingrediente]
                    print("OK")
    
    elif comando=="SALES": 
        if len(words)!=1:
            print("ERROR invalid command")
            continue
        
        if not ordini:
              print("none")
              continue
        else:
             coppie=ordini.items() #ritorna un set in cui sono presenti coppia pizza, numero di ordini

             ordinate=sorted(coppie, key=lambda coppia:(-coppia[1], coppia[0]))
            #sorted:prende quello che ha sentro e lo ordina secondo un criterio specificato in key. 
            #il primo criterio per la traccia è il numero di ordini e quindi all'inzio metto quello
            #(si trova nel secondo elemento della coppia): mette - davetni per l'ordine decrescente
            # poi mette come secondo criterio coppia[0] perchè a parità di ordine si fa per lettera 
             risultato=""
             for coppia in ordinate:
                  risultato+=coppia[0]+""+str(coppia[1])

             print(risultato)

    elif comando=="CAN":
        if len(words) != 2 or not words[1].isalpha():
            print("ERROR invalid command")
            continue
        pizza=words[1]

        if pizza not in ricette:
              print("Errore pizza sconosciuta")
              continue
        else:
             necessari={}
             for ingrediente in ricette[pizza]:
                  necessari[ingrediente]=necessari.get(ingrediente,0)+1

             massimoPizze=float("inf")
             for ingrediente in necessari:
                  possibili=dispensa.get(ingrediente,0) //necessari[ingrediente]
                  massimoPizze=min(massimoPizze,possibili)

             print(massimoPizze)
    


        

                



    

    




                    

