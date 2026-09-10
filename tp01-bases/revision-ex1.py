#Exercice 06 - TP 01
#Paul Crémoux Guiblain
print(chr(65))
etat = 1
while etat == 1:
    op = input("type d'opération souhaité : (a)ddition, (s)oustraction, (m)ultiplication et (d)ivision :")
    op = op.lower()
    if op not in ['a','s','m','d']:
        print("calcul non compris !!")
    x = float(input("x = "))
    y = float(input("y = "))
    if op == 'a':
        print(f"{x} + {y} = {x+y}")
    elif op =='s':
        print(f"{x} - {y} = {x-y}")
    elif op == 'm':
        print(f"{x} * {y} = {x*y}")
    elif op == 'd':
        print(f"{x} / {y} = {x/y}")
    res = input("Un autre calcul ? o/n : ")
    res = res.lower
    if res in ['o','n']:
        etat = 1
    else:
        etat = 0
        break