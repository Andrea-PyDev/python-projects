class Persona:
    def __init__(self,nome,età):
        self.nome = nome
        self.età = età

    def saluta(self):
        print(f"Ciao mi chiamo {self.nome} e ho {self.età} anni")

    def __str__(self):
        return f"{self.nome}: {self.età} anni"



class Studente(Persona):
    def __init__(self,nome,età, università):
        super().__init__(nome,età)
        self.università = università
        self.voti = []

    def aggiungi_voto(self,voto):
        self.voti.append(voto)


class Professore(Persona):
    def __init__(self,nome,età,università,materia,stipendio):
        super().__init__(nome,età)
        self.università = università
        self.materia = materia
        self.stipendio = stipendio
    
    def stipendio_maggiore(self):
        if self.materia == "Storia":
            self.stipendio += 200

andrea = Studente("Andrea", 32, "Università Federico II")
frank = Professore("Frank", 32, "Università Federico II", "Storia", 1200)


andrea.saluta()
frank.saluta()
print(andrea)
print(frank)
print(frank.stipendio)
frank.stipendio_maggiore()
print(frank.stipendio)