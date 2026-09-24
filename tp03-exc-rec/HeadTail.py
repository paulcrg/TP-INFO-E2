import sys

try:
    choix = sys.argv[1]
    nombre_str = sys.argv[2]
    chemin = sys.argv[3]

    if choix not in ('head', 'tail'):
        raise ValueError(f"Premier paramètre invalide : '{choix}' (attendu 'head' ou 'tail')")

    nombre = int(nombre_str)
    if nombre < 0:
        raise ValueError(f"Le nombre de lignes doit être positif, reçu : {nombre}")

    try:
        with open(chemin, 'r', encoding='utf8') as fichier:
            lignes = fichier.readlines()
    except IOError:
        raise IOError(f"Impossible de trouver ou d'ouvrir le fichier : '{chemin}'")

    if choix == 'head':
        selection = lignes[:nombre]
    else:
        selection = lignes[-nombre:] if nombre > 0 else []

    for ligne in selection:
        print(ligne, end='')

except IndexError:
    print("Usage : ./HeadTail.py head/tail nombre chemin_fichier")
except ValueError as e:
    print(f"Erreur de valeur : {e}")
except IOError as e:
    print(f"Erreur de fichier : {e}")