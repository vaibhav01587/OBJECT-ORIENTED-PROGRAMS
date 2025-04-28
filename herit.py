# class Employee:
#     bonus =2000
#     def display(self):
#         print("this is employer method")
# class Manager(Employee):
#     bonus1=4000
#     def show(self):
#         print("this is manager method")
# e1=Employee()
# m1=Manager()
# e1.display()
# m1.show()
# print(m1.bonus)
# print(e1.bonus1)# parent class will not access child class 

# #hierachal inheritance - one parents and multiple child class

# class Employee:
#     def __init__(self,nm,ag): # call constructor
#         self.name = nm
#         self.age=ag
#     def display(self): # call method
#         print("this is display method")
        

# class Person(Employee):
#     def __init__(self,sal):
#         self.salary=sal
# class Student(Employee):
#     def __init__(self,nm,ag,m):
#         super().__init__(nm,ag)
#         self.marks=m
# s1=Student('vaibhav',38,80000)
# print(s1.__dict__)
# Multiple Inheritance
# class is derived from multiple base class
class Parent_1:

    def __init__(self):
        self.salary=2000
        print("first constructor called")
class Parent_2:
    
    def __init__(self):
        super().__init__()
        self.salary=5000
        print("second constructor called")
class Child(Parent_1,Parent_2):
    def __init__(self):
        super().__init__()
        self.salary=1000
        print("third constructor called")
c= Child()
print(c.__dict__)        