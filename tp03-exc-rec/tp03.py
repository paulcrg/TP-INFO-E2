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

print(syra(89))