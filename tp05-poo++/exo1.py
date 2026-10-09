class Rectangle:
    def __init__(self, nom='rectangle', longueur=5, largeur=3):
        self.nom = nom
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        return f"Nom : {self.nom}, Longueur : {self.longueur}, Largeur : {self.largeur}"

    def surface(self):
        return f"La surface du {self.nom} est {self.longueur * self.largeur}"


class Carre(Rectangle):
    def __init__(self, cote = 5):
        super().__init__("carré", cote, cote)
        self.nom = "carré"


rect = Rectangle()
carr = Carre()

print(rect)
print(carr)

print(rect.surface())
print(carr.surface())