class Product:
    def __init__(self, code, name, priceET = 0.2):
        self.code = code
        self.name = name
        self.priceET = priceET

    def __str__(self):
        return f"Code Produit : {self.code} - NomProduit : {self.name} - PrixTTC : {self.priceET}"

    def get_price_it(self):
        return self.priceET

p = Product(55554, 'Peluche')
print(p)
print(p.get_price_it())