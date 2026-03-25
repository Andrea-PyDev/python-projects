# Meteo Logger

Applicazione Python che recupera dati meteo in tempo reale tramite API
e salva uno storico delle consultazioni su file di testo.

## Funzionalità
- Recupero dati meteo tramite API REST (wttr.in)
- Visualizzazione di temperatura, descrizione e umidità
- Salvataggio automatico dello storico con data

## Tecnologie utilizzate
- Python 3
- `requests` — chiamate HTTP verso API esterna
- `datetime` — gestione date
- File I/O — persistenza dati su file .txt

## Come avviare il progetto

1. Clona il repository
2. Installa le dipendenze:
   pip install requests
3. Avvia il programma:
   python meteo_logger.py

## Esempio di output

2026-03-25 - Napoli: 18°C, Partly cloudy, umidità 65%
2026-03-25 - Roma: 15°C, Sunny, umidità 50%