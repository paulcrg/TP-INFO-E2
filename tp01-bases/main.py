from tp01 import ex01, ex02, ex03, ex04, ex05, ex06, ex07

def choix():
    print("Quel exercice voulez-vous voir ?")
    print("1 : IMC")
    print("2 : Programme nombre")
    print("3 : Années Chien")
    print("4 : Calcul de Pi")
    print("5 : Conversion décimal -> binaire")
    print("6 : Calculatrice")
    print("7 : Générateur de plaque d'immatriculation")
    choix = int(input("Choix utilisateur : "))
    if choix == 1:
        ex01()
    elif choix == 2:
        ex02()
    elif choix == 3:
        ex03()
    elif choix == 4:
        ex04()
    elif choix == 5:
        ex05()
    elif choix == 6:
        ex06()
    elif choix == 7:
        ex07()
    else:
        print("Choix invalide")