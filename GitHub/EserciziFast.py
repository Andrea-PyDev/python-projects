
import csv

with open("studenti.csv", "r", encoding="utf-8") as file:
    lettore = csv.DictReader(file)
    for riga in lettore:
        print(f"{riga['nome']} viene da {riga['città']} e ha preso {riga['voto']}")

            



        