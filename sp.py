# HOW CONSTRUCTOR WORKS
class Human_being:
    def __init__(self):
        self.name=input("Enter your name")
        print("First constructor called")
class Employee(Human_being):
    def __init__(self):
        super().__init__()
        self.salary=float(input("enter your salary"))
        print("second constructor is called")
e1=Employee()
print(e1.__dict__)