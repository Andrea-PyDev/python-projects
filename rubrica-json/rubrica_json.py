import json
print("---RUBRICA JSON||")

#Aggiungi contatto
def aggiungi_contatto():
    with open("rubrica.json","r",encoding="utf-8") as file:
        contatti = json.load(file)
    nome = input("Inserisci nome.\n")
    telefono = (input("Inserisci numero di telefono\n"))
    email = input("Inserisci email.\n")
    nuovo_contatto = {
        "Nome": nome,
        "Telefono": telefono,
        "Email": email
    }
    contatti.append(nuovo_contatto)

    with open("rubrica.json","w",encoding="utf-8") as file:
        json.dump(contatti,file,indent = 4,ensure_ascii=False)

        
#mostra contatto
def mostra_contatto():
    with open("rubrica.json","r",encoding="utf-8") as file:
        contatti = json.load(file)
        for riga in contatti:
            print(f"Nome: {riga['Nome']}| Telefono: {riga['Telefono']} | Email: {riga['Email']}")
                  

#cerca un contatto
def cerca_contatto():
    with open("rubrica.json","r",encoding="utf-8") as file:
        contatti = json.load(file)
    utente = input("Inserisci il nome nella barra di ricerca: ").lower()
    trovato = False
    for riga in contatti:
        if utente == riga["Nome"].lower():
            print(f"Nome: {riga['Nome']}| Telefono: {riga['Telefono']} | Email: {riga['Email']}")
            trovato = True
            break
    if not trovato:
        print("Utente non trovato")

#elimina contatto

def elimina_contatto():
    with open("rubrica.json","r",encoding="utf-8") as file:
        contatti = json.load(file)
    nome_da_eliminare = input("Quale contatto vuoi eliminare?")
    trovato = False
    for riga in contatti:
        if nome_da_eliminare == riga["Nome"]:
            contatti.remove(riga)
            trovato = True
            break
    if not trovato:
        print("Contatto non trovato")
    with open("rubrica.json","w", encoding="utf-8") as file:
        json.dump(contatti,file,indent=4,ensure_ascii=False)

def menu():
    print("----BENVENUTI NELLA RUBRICA DI JSON----\n")
    print("Scegli un opzione...\n")
    while True:
        scelta = input("Scegli '1' per Aggiungere contatto\n" \
    "Scegli '2' per mostrare tutti i contatti\n" \
    "Scegli '3' per cercare un contatto specifico\n" \
    "Scegli '4' per eliminare un contatto specifico\n" \
    "Scegli '5' per uscire dal programma\n")
        if scelta == "1":
            aggiungi_contatto()
        elif scelta == "2":
            mostra_contatto()
        elif scelta == "3":
            cerca_contatto()
        elif scelta == "4":
            elimina_contatto()
        elif scelta == "5":
            print("Arrivederci")
            break
        else:
            print("Opzione non valida..riprovare")
            continue

menu()

    


