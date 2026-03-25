import requests
from datetime import date

# Chiede input all'utente richiesta_utente()
# Fa la chiamata HTTP richiesta_utente()

def richiesta_utente():
    città = input("Inserire città: ")
    richiesta = requests.get(f"https://wttr.in/{città}?format=j1")
    dati = richiesta.json()
    return dati , città
# Estrae temperatura, descrizione, umidità estrai_dati()
def estrai_dati(dati):
    temperatura = dati["current_condition"][0]["temp_C"]
    descrizione = dati["current_condition"][0]["weatherDesc"][0]["value"]
    umidità = dati["current_condition"][0]["humidity"]
    return temperatura, descrizione, umidità
# Salva nel file con data e ora salvataggio_file()
def salvataggio_file(città, temperatura, descrizione, umidità):
    oggi = date.today()
    with open("meteologger.txt", "a") as file:
        file.write(f"{oggi} - {città}: {temperatura}°C, {descrizione}, umidità {umidità}%\n")
# Mostra lo storico storico_dati()

def storico_dati():
    try:
        with open("meteologger.txt", "r") as file:
            contenuto = file.read()
            return contenuto
    except FileNotFoundError:
        print("Il file non esiste.\n")
        
def menu():
     dati, città = richiesta_utente()
     temperatura, descrizione, umidità = estrai_dati(dati)
     salvataggio_file(città, temperatura, descrizione, umidità)
     print(storico_dati())
     
if __name__ == "__main__":
    menu()
