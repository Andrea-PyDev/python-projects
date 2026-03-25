from datetime import date
import os

def scrivi_note():
    nota = input("Cosa hai studiato oggi? ")
    oggi = date.today()

    with open("diario.txt", "a") as file:
        file.write(f"{oggi}: {nota}\n")

    print("Nota salvata!")

def leggi_diario():
    try:
        with open("diario.txt", "r") as file:
            contenuto = file.read()
            if contenuto:
                print("\n--- IL TUO DIARIO---")
                print(contenuto)
            else:
                print("Il diario è vuoto")
    except FileNotFoundError:
        print("Nessun diario trovato, Scrivi la prima nota!")

def cancella_note():
    try:
        os.remove("diario.txt")
        print("Note cancellate")
    except FileNotFoundError:
        print("Il file non esiste")


def menu():
    while True:
        print("\n1. Scrivi nota")
        print("2. Leggi diario")
        print("3. Cancellare le note?")
        print("4. Esci")

        scelta = input("Scegli: ")

        if scelta == "1":
            scrivi_note()
        elif scelta == "2":
            leggi_diario()
        elif scelta == "3":
            cancellare = input("Sei sicuro di voler cancellare le note? (s/n)").lower()
            if cancellare == "s":
                cancella_note()
            else:
                print("Cancellazione annullata")
        elif scelta == "4":
            print("A domani")
            break
        else:
            print("Scelta non valida")


if __name__ == "__main__":
    menu()