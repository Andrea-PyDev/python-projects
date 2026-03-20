# Crea una classe TODO con file "todo.txt"

class TodoList:
    def __init__(self):
        pass
#Aggiungi(descrizione)
    def aggiungi(self,descrizione):
        try:
            with open("todo.txt", "a") as file:
                for index,riga in enumerate(descrizione):
                    file.write = f"{index} - TODO|{riga}"
        except FileNotFoundError:
            print("File non trovato")

            
#Completa(numero)

#Rimuovi(numero)

#mostra()

#mostra_completati()

#mostra_pendenti()