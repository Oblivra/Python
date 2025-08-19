class Employee:
    salary = 1200000
    language = "python"

harry = Employee()
harry.language = "Javascript" # instance attribute preference is higher
print(harry.salary, harry.language)