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
from random import *
nombre_ligne = 0
liste = []
with open('dic.txt', 'r+', encoding ='utf8') as f:
    for lignes in f:
        liste.append(lignes.upper())
        nombre_ligne += 1
print(liste[3])
def pendu():
    nbre = randint(0,nombre_ligne)
print(pendu())