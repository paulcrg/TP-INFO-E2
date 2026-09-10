#TP 01 - Les bases du langages
#Crémoux Guiblain Paul

#Exercice 01
def ex01():
    taille = float(input("Saisir votre taille : "))/100
    poids = int(input("Saisir votre poids : "))
    return round(poids/(taille*taille),1)

#Exercice 02

def ex02():
    liste = []
    somme = 0
    n = int(input("Saisir un nombre entier (nombre négatif -> stop) : "))
    while n >=0:
        liste.append(n)
        somme +=n
        n = int(input("Saisir un nombre entier (nombre négatif -> stop) : "))
    tri = sorted(liste)
    mini = min(liste)
    maxi = max(liste)
    moyenne = somme/len(liste)
    print("Nombres dans l'odre croissant :", tri)
    print("Minimum des nombre saisis :", mini)
    print("Maximum des nombres saisis", maxi)
    print("Moyenne des nombre saisis", moyenne)

#Exercice 03

def ex03():
    age = int(input("Saisir votre âge : "))
    if age >= 2:
        print(f"Vous avez {age*10.5} ans en années canines")
    else:
        deux = 10.5*2
        age = age-2
        print(f"Vous avez {(age*4)+deux} ans en années canines")

print(round(10.0,1))