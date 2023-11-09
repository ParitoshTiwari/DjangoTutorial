import django

class Shop:
    def __init__(self, totalScooter) -> None:
        self.totalScooter = totalScooter
        self.rates = {'hourly': 10, 'daily': 20, 'weekly': 50}
        self.price = 0
        self.availableScooter = totalScooter

    def calculateRates(self, rates, duration, quantity):
        if quantity > self.availableScooter:
            return 'These many scooters are not available.'
        else:
            self.availableScooter -= quantity
            return self.rates.get(rates, 0) * duration * quantity


if __name__ == '__main__':
    print(django.get_version())
    firstShop = Shop(50)
    print(firstShop.calculateRates('hourly', 5, 40))