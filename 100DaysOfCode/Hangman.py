import random

parole = ["python","java","programmazione","udemy","nara","potentissimo","frank","lavoro"]



scelta_parola = random.choice(parole)

display = ["_" for lettera in scelta_parola]
set_lettere_usate = set()
vita = 5
sconfitta = False
while True:
    guess_letter = input("Inserisci la lettera da indovinare: ").lower()
    if guess_letter in set_lettere_usate:
        print(f"Lettere già usate | {set_lettere_usate}")
        continue
    set_lettere_usate.add(guess_letter)
    for index, lettera in enumerate(scelta_parola):
        if guess_letter == lettera:
            display[index] = guess_letter
    if guess_letter not in scelta_parola:
        vita -= 1
    print(f"Hai {vita} vita/e rimanenti")
    print("".join(display))
    if vita == 0:
        sconfitta = True
        print("Hai 0 vite rimanenti")
        print("Hai perso la partita")
        print(f"La parola da indovinare era {scelta_parola}")
        print("ARRIVEDERCI")
        break
    if "".join(display) == scelta_parola:
        print("Hai vinto")
        break




























