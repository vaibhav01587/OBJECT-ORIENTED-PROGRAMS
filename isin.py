# class Employee:
#     """this is employee class for maintaining employee data"""
#     def __init__(self,nm,ag):
#         self.name=nm
#         self.age=ag
#         def display(self):
#             print(f"My name is {name} and age is {age}")
# e1=Employee('jay',23)
# print(isinstance(e1,Employee))
# print(Employee.__base__)
# type of variables
# class Student:
#     def __init__(self,nm,m):
#         self.name=nm
#         self.marks=m
# std1=Student('vaibhav',30)
# std2=Student('vanya',19)
# std3=Student('akki',24)
# print(std1.__dict__)
# print(isinstance(std1,Student))
# std1.name='vaibhavi' # updating the file
# print(std1.__dict__)
# del std1.name # deleted name from std1 name
# print(std1.__dict__)
# instance method
class Student:
    def __init__(self,nm,m): # constructor called
        self.name=nm
        self.marks=m
    def display(self):
            print(self.name,self.marks)
    def change_data(self):
        self.name="tia"
        self.marks=90
         
                
std1= Student('akshay',89)
std2 = Student('raj',99)
std3 = Student('vinay',60)
std1.change_data()
print(std1.__dict__)
