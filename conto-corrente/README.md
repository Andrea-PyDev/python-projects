# Conto Corrente

Simulazione di un conto corrente bancario in Python
tramite programmazione orientata agli oggetti.

## Funzionalità
- Deposito e prelievo con controllo saldo minimo
- Trasferimento fondi tra due conti
- Storico completo delle operazioni
- Saldo minimo configurabile

## Tecnologie utilizzate
- Python 3
- OOP — classe `ContoCorrente`
- `__str__` per rappresentazione leggibile dell'oggetto

## Come avviare il progetto

1. Clona il repository
2. Avvia il programma (nessuna dipendenza esterna):
   python conto_corrente.py

## Esempio di output

Deposito: + 500€ | Saldo: 1500€
Prelievo: -200€ | Saldo: 1300€
Trasferimento: -300€ | Saldo: 1000€
Conto di Andrea: 1000€ (minimo: 100€)