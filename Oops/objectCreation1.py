class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Kishor", 900000)
print(e1.name)
print(e1.salary)
print("Changing the Name!!!")

e1.name = "Kishor Gowda o k"
print(e1.name)
print("Adding age variable !!!")
e1.age = 21
print(e1.age) 
print(id(e1.age))
print(id(e1))

e2 = Employee("Rajath", 400000)
print(e2.name)
print(e2.salary)

