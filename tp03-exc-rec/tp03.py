#Crémoux Guiblain Paul - E2
#TP N°03 Files - Exception - Récursivité

#Exercice 01
def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n-1)

#Exercice 02
def syra(n):
    assert n >= 0
    if n %2 ==0:
        n//=2
    else:
        n = n*3 + 1
    if n !=1:
        return syra(n)
    return n

#Exercice 04
from random import randint
from exceptions import LettreDejaSoumiseError

with open('dic.txt', 'r', encoding='utf8') as f:
    liste = [ligne.strip().upper() for ligne in f]

def pendu():
    mot = liste[randint(0, len(liste) - 1)]
    vies = 7
    soumis = []
    lettres_trouvees = set()

    while vies > 0:
        masque = ''.join(lettre if lettre in lettres_trouvees else '_' for lettre in mot)
        print(masque, f"(vies restantes : {vies})")

        if set(mot) <= lettres_trouvees:
            print("Bravo, vous avez gagné !")
            return

        choix = input("Proposez une lettre : ").strip().upper()

        try:
            if choix in soumis:
                raise LettreDejaSoumiseError(f"Vous avez déjà proposé '{choix}' !")
            soumis.append(choix)

            if choix in mot:
                lettres_trouvees.add(choix)
            else:
                vies -= 1
                print(f"Raté, il vous reste {vies} vie(s).")
        except LettreDejaSoumiseError as e:
            print(e)

    print(f"Perdu ! Le mot était : {mot}")

pendu()