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

#Exercice 04

def ex04(n):
    if n > 0:
        pi = 3
        for i in range(1, n+1):
            if i%2==1:
                pi += 4/((2*i)*(2*i+1)*(2*i+2))
            else:
                pi -=4/((2*i)*(2*i+1)*(2*i+2))
        return pi
    else:
        raise ValueError("Nombre négatif ou nul")


#Exercice 05

def ex05():
    n = int(input("Saisir le nombre décimal que vous souhaitez convertir : "))
    q = n
    res = ''
    while q!=0:
        r = q%2
        res+= str(r)
        q = q//2
    print(f"Le nombre décimal {n} est égal à {res[::-1]} en binaire")

#Exercice 07

from random import *

def ex07():
    milieu = randint(1,999)
    m = ''
    if milieu < 10:
        m += '00' + str(milieu)
    elif milieu < 100:
        m += '0' + str(milieu)
    else:
        m+= str(milieu)

    n = randint(65,90)
    l1 = chr(n)
    while l1 in ['I','O', 'U']:
        n = randint(65,90)
        l1 = chr(n)

    n = randint(65,90)
    l2 = chr(n)
    while l2 in ['I','O', 'U']:
        n = randint(65,90)
        l2 = chr(n)

    d = '' + str(l1) + str(l2)

    while d in ['SS']:
        n = randint(65,90)
        l2 = chr(n)
        d = '' + str(l1) + str(l2)

    n = randint(65,90)
    l3 = chr(n)
    while l3 in ['I','O', 'U']:
        n = randint(65,90)
        l3 = chr(n)

    n = randint(65,90)
    l4 = chr(n)
    while l4 in ['I','O', 'U']:
        n = randint(65,90)
        l4 = chr(n)
    
    f = '' + str(l3) + str(l4)
    
    while f in ['SS']:
        n = randint(65,90)
        l4 = chr(n)
        f = '' + str(l3) + str(l4)

    resultat = d + '-' + m + '-' + f
    print(f"Voici votre plaque d'immatriculation : {resultat}")

ex07()