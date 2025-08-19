class Employee:
    salary = 1200000
    language = "python"

    def __init__(self, name, salary, language): #Dunder method which is called Automatically
        self.name = name
        self.salary = salary
        self.language = language
        print("Hi i am yorichi")
    
    # def __init__(Kuch_bhi, name, salary, language): #Dunder method which is called Automatically
    #     Kuch_bhi.name = name
    #     Kuch_bhi.salary = salary
    #     Kuch_bhi.language = language

    def greet(self):
        print("Good Morning")

    @staticmethod
    def Greet():
        print("Good Morning")

harry = Employee("yorichi", 1200000, "python")
print(harry.name, harry.salary, harry.language)
# harry.greet()

# rohan = Employee("rohan", 1300000, "java")