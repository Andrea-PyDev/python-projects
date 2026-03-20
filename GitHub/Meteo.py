import requests

città = input("Inserisci una città: ")
risposta = requests.get(f"https://wttr.in/{città}?format=j1")
dati = risposta.json()

temperatura = dati["current_condition"][0]["temp_C"]
descrizione = dati["current_condition"][0]["weatherDesc"][0]["value"]
umidità = dati["current_condition"][0]["humidity"]
print(f"Temperatura a {città}: {temperatura}°C")
print(f"Condizione: {descrizione}")
print(f"Umidità a {città}: {umidità}% ")