class Email:
    pass

e1=Email()
e2= Email()
print(type(e1))

class Employee:
    def __init__(self):
        self.salary=22000
        self.age=21
    
e1=Employee()
print(e1.__dict__)