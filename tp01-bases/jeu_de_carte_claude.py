import random

NB_MANCHES = 10
ORDRE_VALEURS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "V", "C", "D", "R", "A"]
COULEURS = ["s", "c", "d", "h"]


def creer_paquet():
    """Construit un paquet complet : toutes les combinaisons valeur/couleur."""
    paquet = []
    for valeur in ORDRE_VALEURS:
        for couleur in COULEURS:
            paquet.append((valeur, couleur))
    return paquet


def melanger_paquet(paquet):
    """Mélange le paquet en place."""
    random.shuffle(paquet)


def piocher_carte(paquet):
    """Retire et renvoie la carte du dessus du paquet."""
    return paquet.pop()


def afficher_carte(carte):
    """Renvoie une chaîne lisible pour une carte, ex: '[A h]'."""
    valeur, couleur = carte
    return f"[{valeur}{couleur}]"


def demander_prediction():
    """Demande au joueur sa prédiction : renvoie 'S' ou 'I'."""
    while True:
        reponse = input("Votre prediction pour la prochaine carte (S = superieur / I = inferieur) : ").strip().upper()
        if reponse in ("S", "I"):
            return reponse
        print("Reponse invalide, tapez S ou I.")


def comparer_cartes(ancienne, nouvelle):
    """
    Compare deux cartes selon leur valeur.
    Renvoie  1 si la nouvelle carte est superieure
    Renvoie -1 si la nouvelle carte est inferieure
    Renvoie  0 en cas d'egalite
    """
    rang_ancienne = ORDRE_VALEURS.index(ancienne[0])
    rang_nouvelle = ORDRE_VALEURS.index(nouvelle[0])

    if rang_nouvelle > rang_ancienne:
        return 1
    elif rang_nouvelle < rang_ancienne:
        return -1
    else:
        return 0


def jouer_manche(paquet, numero_manche):
    """
    Joue une manche complete.
    Renvoie  1 si le joueur marque le point
    Renvoie  0 si l'ordinateur marque le point
    Renvoie -1 en cas d'egalite (aucun point distribue)
    """
    print(f"\n--- Manche {numero_manche} ---")

    carte_actuelle = piocher_carte(paquet)
    print("Carte tiree :", afficher_carte(carte_actuelle))

    prediction = demander_prediction()

    carte_suivante = piocher_carte(paquet)
    print("Nouvelle carte :", afficher_carte(carte_suivante))

    resultat = comparer_cartes(carte_actuelle, carte_suivante)

    if resultat == 0:
        print("Egalite ! Personne ne marque de point.")
        return -1

    if (resultat == 1 and prediction == "S") or (resultat == -1 and prediction == "I"):
        print("Bonne prediction ! Vous marquez un point.")
        return 1
    else:
        print("Mauvaise prediction. L'ordinateur marque un point.")
        return 0


def jouer_partie():
    """Joue une partie complete en NB_MANCHES manches et affiche le resultat."""
    paquet = creer_paquet()
    melanger_paquet(paquet)

    score_joueur = 0
    score_ordinateur = 0

    for manche in range(1, NB_MANCHES + 1):
        # Il faut 2 cartes par manche, on remelange si le paquet est presque vide
        if len(paquet) < 2:
            paquet = creer_paquet()
            melanger_paquet(paquet)

        resultat = jouer_manche(paquet, manche)
        if resultat == 1:
            score_joueur += 1
        elif resultat == 0:
            score_ordinateur += 1

        print(f"Score actuel -> Vous : {score_joueur} | Ordinateur : {score_ordinateur}")

    print("\n===== Fin de la partie =====")
    print(f"Score final -> Vous : {score_joueur} | Ordinateur : {score_ordinateur}")

    if score_joueur > score_ordinateur:
        print("Vous avez gagne la partie !")
    elif score_joueur < score_ordinateur:
        print("L'ordinateur a gagne la partie.")
    else:
        print("Match nul !")


def main():
    rejouer = "o"
    while rejouer == "o":
        jouer_partie()
        rejouer = input("\nVoulez-vous rejouer une partie ? (o/n) : ").strip().lower()

    print("Merci d'avoir joue !")


if __name__ == "__main__":
    main()