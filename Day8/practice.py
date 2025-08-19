class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

tanjiro = Programmer("Tanjiro", 1000000, 380089)
print(tanjiro.name, tanjiro.salary, tanjiro.pincode)
Yorichi = Programmer("Yorichi", 9990000, 380034)
print(Yorichi.name, Yorichi.salary, Yorichi.pincode)