class Calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def greet():
        print("Hello, Kaise ho ?")

    def square(self):
        print(self.n ** 2)

    def cube(self):
        print(self.n ** 3)

    def squareroot(self):
        print(self.n ** (1/2))


a = Calculator(5)
a.greet()
a.square()
a.cube()
a.squareroot()