class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def get_model(self):
        return self.model

    def get_price(self):
        return self.price


class Benz(Car):
    pass


Benz1 = Benz("C-Class", 250000)
Benz2 = Benz("G-Class", 300000)
Benz3 = Benz("S-Class", 400000)


class BMW(Car):
    pass


BMW1 = BMW("X3", 250000)
BMW2 = BMW("X5", 300000)
BMW3 = BMW("X6", 400000)


class Audi(Car):
    pass


Audi1 = Audi("A4", 250000)
Audi2 = Audi("A5",300000)
Audi3 = Audi("A7",400000)
