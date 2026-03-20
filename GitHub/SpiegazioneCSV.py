import csv

#Aggiungi studente con voto

def aggiungi_studente():
    nome = input("Inserisci il nome:\n")
    età = int(input("Inserisci l'età:\n"))
    città = input("Inserisci la città:\n")
    voto = int(input("Inserisci il voto:\n"))
    with open("studenti.csv", "a", encoding="utf-8",newline="") as file:
        file.write("\n")
        studente_aggiunto = csv.DictWriter(file,fieldnames=["nome","età","città","voto"])
        studente_aggiunto.writerow({"nome": nome,"età": età,"città": città,"voto": voto})

#Mostra tutti gli studenti
def mostra_studenti():
    with open("studenti.csv", "r",encoding="utf-8",newline="") as file:
        studenti = csv.DictReader(file)
        for riga in studenti:
            print(f"Nome: {riga['nome']}| Età: {riga['età']}| Città: {riga['città']}| Voto: {riga['voto']}.")
              

#Calcola la media dei voti
def media_voti():
    with open("studenti.csv","r",encoding="utf-8",newline="") as file:
        voti = csv.reader(file)
        lista_voti = []
        next(voti)
        for riga in voti:
            if riga and riga[3]:
                lista_voti.append(int(riga[3]))
        media_dei_voti = sum(lista_voti) / len(lista_voti)
        return media_dei_voti


#trova lo studente con il voto più alto
def trova_studente():
    cerca_studente = input("Nome dello studente?\n").lower()
    with open("studenti.csv","r",encoding="utf-8") as file:
        cercare = csv.DictReader(file)
        for riga in cercare:
            if cerca_studente == riga["nome"].lower():
                print(f"Nome: {riga['nome']}| Età: {riga['età']}| Città: {riga['città']}| Voto: {riga['voto']}.")
                break
        else:
            print("Studente non trovato")

        

def menu():
    print("----BENVENUTI NEL REGISTRO STUDENTI DI NARA----\n")
    print("Scegli un opzione...\n")
    while True:
        scelta = input("Scegli '1' per Aggiungere studente\n" \
    "Scegli '2' per mostrare tutti gli studenti\n" \
    "Scegli '3' per visualizzare la media voti\n" \
    "Scegli '4' per trovare uno studente specifico\n" \
    "Scegli '5' per uscire dal programma\n")
        if scelta == "1":
            aggiungi_studente()

        elif scelta == "2":
            mostra_studenti()

        elif scelta == "3":
            print(f"Media voti: {media_voti()}")

        elif scelta == "4":
            trova_studente()

        elif scelta == "5":
            print("Arrivederci")
            break
        else:
            print("Opzione non valida")


menu()


    


