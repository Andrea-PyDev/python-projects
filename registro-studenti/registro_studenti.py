from datetime import date



#Aggiungi studente e segna presenza/assenza
def studente():
    nome = input("Inserisci nome e cognome studente: ").lower()
    presenza_assenza = input("Lo studente è 'presente' o 'assente'? ").lower()
    oggi = date.today()
    with open("Registrodeglistudenti.txt","a") as file:
        file.write(f"{oggi}:Studente: {nome} è {presenza_assenza}\n")
    return nome, presenza_assenza

#Vedi storico
def storico():
    try:
        with open("registrodeglistudenti.txt","r") as file:
            contenuto = file.read()
            print(contenuto)
    except FileNotFoundError:
        print("Nessun studente inserito")
#Totale presenze per studente
def presenze():
    nome = input("Di quale studente vuoi vedere le presenze?").lower()
    presenze = 0
    with open("registrodeglistudenti.txt","r") as file:
        for riga in file:
            if nome in riga and "presente" in riga:
                presenze += 1
        print(f"{nome} è stato presente {presenze} volta/e. ")

#Totale assenze per studente
def assenze():
    nome = input("Di quale studente vuoi vedere le assenze?").lower()
    assenze = 0 
    with open("registrodeglistudenti.txt","r") as file:
        for riga in file:
            if nome in riga and "assente" in riga:
                assenze += 1
        print(f"{nome} è stato assente {assenze} volta/e. ")

def menu():

    while True:
            print("--- Benvenuti nel Registro studenti---\n")
            print("1- Presenza o Assenza dello studente\n")
            print("2- Storico dei dati del Registro Studenti\n")
            print("3- Totale presenze dello studente\n")
            print("4- Totale assenze dello studente\n")
            print("5- Esci dal programma\n")
            scelta = input("Inserisci la scelta: ")
            if scelta == "1":
                studente()
            elif scelta == "2":
                storico()
            elif scelta == "3":
                presenze()
            elif scelta == "4":
                assenze()
            elif scelta == "5":
                print("Arrivederci")
                break
            else:
                print("Errore")

menu()




