from math import *

class Fraction:
    def __init__(self, numerateur, denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __str__(self):
        return f"{self.numerateur}\n{'-'*len(str(self.numerateur))}\n{self.denominateur}"

    def __add__(self, autre):  # +
        ppcm = lcm(self.denominateur, autre.denominateur)

        resn = self.numerateur * (ppcm // self.denominateur) + autre.numerateur * (ppcm // autre.denominateur)

        return Fraction(resn, ppcm)

    def __sub__(self, autre):  # -
        resn = self.numerateur * autre.denominateur - autre.numerateur * self.denominateur
        resd = self.denominateur * autre.denominateur
        return Fraction(resn, resd)

    def __mul__(self, autre):  # *
        resn = self.numerateur * autre.numerateur
        resd = self.denominateur * autre.denominateur
        return Fraction(resn, resd)

    def __truediv__(self, autre):  # /
        resn = self.numerateur * autre.denominateur
        resd = self.denominateur * autre.numerateur
        return Fraction(resn, resd)

    def __gt__(self, autre):  # >
        return self.numerateur/self.denominateur > autre.numerateur/autre.denominateur

    def __lt__(self, autre):  # <
        return self.numerateur/self.denominateur < autre.numerateur/autre.denominateur

    def __le__(self, autre):  # <=
        return self.numerateur/self.denominateur <= autre.numerateur/autre.denominateur

    def __ge__(self, autre):  # >=
        return self.numerateur/self.denominateur >= autre.numerateur/autre.denominateur

    def __eq__(self, autre):  # ==
        return self.numerateur/self.denominateur == autre.numerateur/autre.denominateur

    def __ne__(self, autre):  # !=
        return self.numerateur/self.denominateur != autre.numerateur/autre.denominateur

p = Fraction(1, 2)
q = Fraction(1, 4)

print(p)
print(p + q)