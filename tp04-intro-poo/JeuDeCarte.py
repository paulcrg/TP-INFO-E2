class CardValue:
    def __init__(self, value_txt, value_pts):
        self.value_txt = value_txt
        self.value_pts = value_pts


class CardColor:
    def __init__(self, shade, shade_name, foreground_color, background_color):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def is_equal_value(self, card):
        return self.value.value_pts == card.value.value_pts

    def __eq__(self, card):
        return self.value.value_pts == card.value.value_pts

    def __str__(self):
        return f"{self.value.value_txt}{self.color.shade}"

    def __repr__(self):
        return f"{self.value.value_txt}{self.color.shade}"

from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []
        self.discard_pile = []

    def init52_cards(self):
        # Les 13 valeurs
        valeurs = [
            CardValue("2", 2),
            CardValue("3", 3),
            CardValue("4", 4),
            CardValue("5", 5),
            CardValue("6", 6),
            CardValue("7", 7),
            CardValue("8", 8),
            CardValue("9", 9),
            CardValue("10", 10),
            CardValue("J", 11),
            CardValue("Q", 12),
            CardValue("K", 13),
            CardValue("A", 14)
        ]

        couleurs = [
            CardColor("♠", "pique", "noir", "blanc"),
            CardColor("♣", "trefle", "noir", "blanc"),
            CardColor("♦", "carreau", "rouge", "blanc"),
            CardColor("♥", "coeur", "rouge", "blanc")
        ]

        for couleur in couleurs:
            for valeur in valeurs:
                self.deck.append(Card(valeur, couleur))

    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        if len(self.deck) > 0:
            return self.deck.pop(0)

    def discard(self, card):
        self.discard_pile.append(card)

    def __str__(self):
        return str(self.deck)