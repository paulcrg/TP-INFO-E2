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
    

ex02()