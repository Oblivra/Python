class Employee:
    salary = 1200000
    language = "python"

    def getInfo(self):
        print(self.salary, self.language)
    
    def greet(self):
        print("Good Morning")

    @staticmethod
    def Greet():
        print("Good Morning")

harry = Employee()
harry.language = "Javascript" # instance attribute preference is higher
harry.getInfo()
# Employee.getInfo(harry)
harry.greet()
# Employee.greet(harry)
harry.Greet() 
# static method can be called without instance 

# self ke alawa bhi kuch bhi likh sakte hai
# it is just a parameter