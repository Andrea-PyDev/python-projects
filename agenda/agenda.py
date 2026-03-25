from datetime import datetime

class Evento:
    def __init__(self,titolo,data,ora,descrizione):
        self.titolo = titolo
        self.data = data
        self.ora = ora
        self.descrizione = descrizione

    def __str__(self):
        return f"{self.titolo} : {self.data} | {self.ora} -- {self.descrizione}"
    

class Agenda:
    def __init__(self):
        self.eventi = []

    def aggiungi_evento(self,evento):
        self.eventi.append(evento)
    
    def rimuovi_evento(self,titolo):
            self.eventi = [e for e in self.eventi if e.titolo != titolo]

    def eventi_per_data(self,data):
        risultati = []
        for evento in self.eventi:
            if evento.data == data:
                risultati.append(evento)
        return risultati

    def prossimi_eventi(self,n):
        ordinati = sorted(self.eventi,key = lambda e: datetime.strptime(e.data + " " + e.ora,"%d/%m/%Y %H:%M"))
        return ordinati[:n]

    def salva_su_file(self,nome_file):
        with open(nome_file, "w") as file:
                for evento in self.eventi:
                    file.write(f"{evento.titolo}|{evento.data}|{evento.ora}|{evento.descrizione}\n")
    
    def carica_da_file(self, nome_file):
        try:
            with open(nome_file, "r") as file:
                for riga in file.readlines():
                    riga = riga.strip()
                    if not riga:
                        continue
                    parti = riga.split("|")
                    if len(parti) != 4:
                        print(f"Riga non valida ignorata: '{riga}'")
                        continue
                    evento = Evento(parti[0], parti[1], parti[2], parti[3])
                    self.eventi.append(evento)
        except FileNotFoundError:
            print("File non trovato")

        
if __name__ == "__main__":
    agenda = Agenda()


    e1 = Evento("Studiare Python", "20/03/2026", "09:00", "Fase 2 del roadmap")
    e2 = Evento("Colloquio", "25/03/2026", "14:30", "Azienda tech Roma")
    e3 = Evento("Dentista", "20/03/2026", "11:00", "Controllo annuale")

    agenda.aggiungi_evento(e1)
    agenda.aggiungi_evento(e2)
    agenda.aggiungi_evento(e3)

    print("--- TUTTI GLI EVENTI ---")
    for e in agenda.eventi:
        print(e)

    print("\n--- EVENTI DEL 20/03 ---")
    for e in agenda.eventi_per_data("20/03/2026"):
        print(e)

    print("\n--- PROSSIMI 2 EVENTI ---")
    for e in agenda.prossimi_eventi(2):
        print(e)

    agenda.salva_su_file("agenda.txt")

    agenda2 = Agenda()
    agenda2.carica_da_file("agenda.txt")
    print("\n--- CARICATI DA FILE ---")
    for e in agenda2.eventi:
        print(e)


                




