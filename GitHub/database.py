import sqlite3

connessione = sqlite3.connect("scuola.db")
cursore = connessione.cursor()

cursore.execute("""
    CREATE TABLE IF NOT EXISTS studenti (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nome    TEXT    NOT NULL,
        eta     INTEGER NOT NULL,
        citta   TEXT,
        voto    REAL
    )
""")
cursore.execute("DELETE FROM studenti")
studenti = [
    ('Andrea',32,'Caserta',8.0),
    ("Mario",25,"Napoli",7.0),
    ("Sara",22,"Milano",10.0),
    ("Luigi",28,"Roma",9.0)
]

cursore.executemany("""
                    INSERT INTO studenti(nome,eta,citta,voto)
                    VALUES (?,?,?,?)
                    """,studenti)
cursore.execute("SELECT * FROM studenti")
righe = cursore.fetchall()
for riga in righe:
    print(f"ID| {riga[0]} - Nome| {riga[1]} - Anni| {riga[2]} - Città| {riga[3]} - Voto| {riga[4]}.")

cursore.execute("SELECT * FROM studenti WHERE voto >= 9")
migliori = cursore.fetchall()
print("\n--- Studenti con voto >= 9 ---")
for riga in migliori:
    print(f"{riga[1]} - Voto: {riga[4]}")
    
cursore.execute("SELECT * FROM studenti WHERE citta = 'Napoli' OR citta = 'Caserta' ORDER BY voto DESC")
provenienza = cursore.fetchall()
print("---Studenti provenienti da Caserta o Napoli---")
for riga in provenienza:
    print(f"{riga[1]} proviene da {riga[3]}.")

#UPDATE 
cursore.execute("UPDATE studenti SET voto = 9.0 WHERE nome = 'Mario'")
print("\nVoto di Mario aggiornato!")
cursore.execute("SELECT nome, voto FROM studenti WHERE nome = 'Mario'")
print(cursore.fetchone())

#DELETE 
cursore.execute("DELETE FROM studenti WHERE nome = 'Sara'")
print("\n Sara è stata cancellata dalla tabella")
cursore.execute("SELECT nome, voto FROM studenti WHERE nome = 'Sara'")
print(cursore.fetchone())




connessione.commit()
print("Dati inseriti!")
connessione.close()
