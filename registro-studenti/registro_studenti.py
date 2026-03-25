from datetime import date


NOME_FILE = "registro_studenti.txt"
#Aggiungi studente e segna presenza/assenza
def studente():
    nome = input("Inserisci nome e cognome studente: ").lower()
    presenza_assenza = input("Lo studente è 'presente' o 'assente'? ").lower()
    oggi = date.today()
    with open(NOME_FILE,"a") as file:
        file.write(f"{oggi}:Studente: {nome} è {presenza_assenza}\n")
    return nome, presenza_assenza

#Vedi storico
def storico():
    try:
        with open(NOME_FILE,"r") as file:
            contenuto = file.read()
            print(contenuto)
    except FileNotFoundError:
        print("Nessun studente inserito")

#Analisi stato dello studente
def conta_stato(stato):
    try:
        nome = input("Di quale studente vuoi vedere le presenze?").lower()
        contatore_stato = 0
        with open(NOME_FILE,"r") as file:
            for riga in file:
                if nome in riga and stato in riga:
                    contatore_stato += 1
            print(f"{nome} è stato {stato} {contatore_stato} volta/e. ")
    except FileNotFoundError:
        print("Il file non esiste")



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
                conta_stato("presente")
            elif scelta == "4":
                conta_stato("assente")
            elif scelta == "5":
                print("Arrivederci")
                break
            else:
                print("Errore")


if __name__ == "__main__":
    menu()




