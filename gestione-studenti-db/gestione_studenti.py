import sqlite3
connessione = sqlite3.connect("studenti.db")
cursore = connessione.cursor()

cursore.execute(""" CREATE TABLE IF NOT EXISTS studenti
                (id_studente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                eta INTEGER NOT NULL,
                citta TEXT,
                voto FLOAT NOT NULL)
            """ )
#Aggiunge studente
def aggiungi_studente():
    nome = input("Inserisci il nome dello studente: ")
    eta = int(input("Inserisci l'età dello studente: "))
    citta = input("Città di provenienza: ")
    voto = float(input("Inserisci il voto dello studente: "))
    cursore.execute("""
                    INSERT INTO studenti (nome,eta,citta,voto)
                    VALUES (?,?,?,?)
                    """, (nome,eta,citta,voto))
    connessione.commit()
    print("Studente aggiunto!")
                    
    
#Mostra studente
def mostra_studenti():
    cursore.execute(""" SELECT * FROM studenti""")
    studenti = cursore.fetchall()
    for studente in studenti:
        print(f"ID|{studente[0]} Nome|{studente[1]}| Età {studente[2]}| Città {studente[3]}| Voto {studente[4]} ")


#Cerca studente
def cerca_studente():
    nome_studente = input("Inserisci il nome dello studente: ")
    cursore.execute("SELECT * FROM studenti WHERE nome = ?",(nome_studente,))
    risultato = cursore.fetchone()
    if risultato:
        print(f"ID|{risultato[0]}| Nome - {risultato[1]}| Età - {risultato[2]}| Città - {risultato[3]}| Voto {risultato[4]}.")
    else:
        print("Studente non trovato!")
        

#Aggiorna voto
def aggiorna_voto():
    nome_studente = input("Inserisci il nome dello studente per aggiornare il voto: ")
    nuovo_voto = float(input("Inserisci il nuovo voto da inserire: "))
    cursore.execute("UPDATE studenti SET voto = ? WHERE nome = ?", (nuovo_voto, nome_studente))
    connessione.commit()
    print(f"Voto di {nome_studente} aggiornato a {nuovo_voto}")


#Elimina studente

def elimina_studente():
    studente_eliminato = input("Inserisci il nome dello studente da cancellare: ")
    cursore.execute("DELETE FROM studenti WHERE nome = ?", (studente_eliminato,))
    connessione.commit()
    print(f"Lo studente {studente_eliminato} è stato cancellato dal Registro di classe")


def menu():

    print("---BENVENUTI NEL NUOVO REGISTRO STUDENTI CON DATABASE INCLUSO---")
    print("Scegli le seguenti opzioni.")
    while True:
        scelta = input("""
                    Scelta '1' - Aggiungi Studente
                    Scelta '2' - Mostri gli Studenti
                    Scelta '3' - Cerca uno Studente
                    Scelta '4' - Aggiorna Voto dello Studente
                    Scelta '5' - Elimina uno Studente
                    Scelta '6' - Esci dal programma..
                                                   \n""") 
        if scelta == "1":
            aggiungi_studente()
        elif scelta == "2":
            mostra_studenti()
        elif scelta == "3":
            cerca_studente()
        elif scelta == "4":
            aggiorna_voto()
        elif scelta == "5":
            elimina_studente()
        elif scelta == "6":
            print("Programma in uscita, arrivederci!")
            connessione.close()
            break
        else:
            print("Errore nella selezione della scelta, si prega di riprovare")
            continue

if __name__ == "__main__":
    menu()