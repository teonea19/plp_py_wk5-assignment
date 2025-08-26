class Phone:
    def __init__(self, name, model,amount):
        self.name = name
        self.model = model
        self._amount = amount

    def getAmount(self):
        return self._amount

    def setAmount(self, new_amount):
        if new_amount >= 0:
            self._amount = new_amount
        else:
            print("Amount can't be zero")

    def identify(self):
        print(f"My phone is {self.name} {self.model}")
    def ring(self):
        print(f"{self.name} {self.model} is ringing")

    def buy(self):
        print(f"I bought {self.name} for {self._amount}")

class Ios(Phone):
    def __init__(self, name, model, amount, year):
        super().__init__(name, model, amount)
        self.year = year

    def identify(self):
        print(f"My iOS device is {self.name} {self.model}, released in {self.year}")


class Android(Phone):
    def __init__(self, name, model, amount, year):
        super().__init__(name, model, amount)
        self.year = year

    def identify(self):
        print(f"My Android device is {self.name} {self.model}, released in {self.year}")


myPhone1 = Phone("Samsung Galaxy", "S16", 2500)
myPhone2 = Phone("Iphone16", "Pro Max", 3000)

ios = Ios("Iphone20", "Premium", 2800, 2025 )
android = Android("Samsung Galaxy", "S23", 1800, 2024)


myPhone1.buy()
myPhone1.identify()
myPhone1.ring()

myPhone2.buy()
myPhone2.identify()
myPhone2.ring()

ios.identify()
android.identify()