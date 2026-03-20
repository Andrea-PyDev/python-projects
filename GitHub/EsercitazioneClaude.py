def analizza_stringa(parola):
    analisi_stringa = {}
    analisi_stringa["Lunghezza"] = len(parola)
    contatore_consonante = 0
    contatore_vocale = 0
    for char in parola:
        if char.isalpha():
            if char.lower() in "aeiou":
                contatore_vocale += 1
            else:
                contatore_consonante += 1
    analisi_stringa["Vocali"] = contatore_vocale
    analisi_stringa["Consonante"] = contatore_consonante
    spazi_vuoti = parola.count(" ")
    analisi_stringa["Spazi Vuoti"] = spazi_vuoti
    parole = len(parola.split())
    analisi_stringa["Parole"] = parole
    print(analisi_stringa)

analizza_stringa("Ciao mi chiamo Andrea")

    
