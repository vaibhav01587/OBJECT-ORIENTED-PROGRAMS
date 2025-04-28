# what is constructor?
# special method used for intializing objects with attributes.
#default deconstructor
# class Emp:
#     def __init__(self): # self is variable which containn memory address of current object is calls is self
#         self.name='vaibhav'
#         self.age=39
# e1=Emp()#  e1 is object without object there is no use of class 
# print(e1)# it will tell the memory location
# print(e1.__dict__)#dot notation is used to access to any particular object

# class Employee:
#     def __init__(self,nm,ag):
#         self.name=nm
#         self.age=ag
        
# e1=Employee('vaibhav',38)
# print(e1.__dict__)

#Accessing class members
class Employee:
    def __init__(self,sal,ag):
        self.salary=sal
        self.age=ag
    def display(self):
         print(f"salary is{self.salary} and age is{self.age}")
        
e1=Employee(19000,20)
print(e1.salary)
print(e1.age)
e2=Employee(26000,40)
print(e1.salary)
e1.salary=30000
print(e1.salary)
print(e1.__dict__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)


