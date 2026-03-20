class ContoCorrente:
    def __init__(self,intestatario,saldo = 0,saldo_minimo = 0):
        self.intestatario = intestatario
        self.saldo = saldo
        self.storico = []
        self.saldo_minimo = saldo_minimo

    def deposita(self,importo):
         self.saldo += importo
         self.storico.append(f"Deposito: + {importo}€ | Saldo: {self.saldo}€")


    def preleva(self,importo):
        if self.saldo - importo  < self.saldo_minimo:
            print("Saldo insufficiente")
        else:
            self.saldo -= importo
            self.storico.append(f"Prelievo: -{importo}€ | Saldo: {self.saldo}€")


    def imposta_saldo_minimo(self,importo):
        self.saldo_minimo = importo
    
    def mostra_storico(self):
        for operazione in self.storico:
            print(operazione)


    def trasferisci(self, importo, altro_conto):
        if self.saldo - importo < self.saldo_minimo:
            print("Saldo insufficiente per il trasferimento")
        else:
            self.preleva(importo)
            altro_conto.deposita(importo)

    def __str__(self):
        return f"Conto di {self.intestatario}: {self.saldo}€ (minimo: {self.saldo_minimo}€)"

        
conto1 = ContoCorrente("Andrea", 1000)
conto2 = ContoCorrente("Frank", 500)

conto1.imposta_saldo_minimo(100)
conto1.deposita(500)
conto1.preleva(200)
conto1.trasferisci(300, conto2)

conto1.mostra_storico()
print(conto1)
print(conto2)