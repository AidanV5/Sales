class Furniture:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Table(Furniture):
    pass


Table1 = Table("Glass Table", 2500)
Table2 = Table("Wooden Table", 2000)
Table3 = Table("Marble Table", 3500)


class Chair(Furniture):
    pass


Chair1 = Chair("Glass Chair", 2500)
Chair2 = Chair("Wooden Chair", 2500)
Chair3 = Chair("Marble Chair", 2500)


class Wardrobe(Furniture):
    pass


Wardrobe1 = Wardrobe("Brown Wood Wardrobe", 2500)
Wardrobe2 = Wardrobe("Yellow Wood Wardrobe", 2500)
Wardrobe3 = Wardrobe("Black Wardrobe", 2500)

