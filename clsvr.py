#CLASS VARIABLE AND CLASS METHODS
class Employee:
    company_name="infoys" # CLASS VARIABLE
    def __init__(self,nm,id):
        self.name=nm
        self.emp_id=id


e1=Employee('Akanksha',40)
e2=Employee('vaibhav',30)
print(Employee.company_name)
print(e1.company_name)
print(e1)

#HOW TO MODIFY CLASS VARIABLE
class Employee:
    company_name="TCS"
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
e1 = Employee('Akash',30000)
e2 = Employee('Vanu',50000)
print(e1.company_name)
Employee.company_name='Wipro'# we assign new name of company by using class variable
print(e1.company_name)

# Class Method :- Class method is method present in class to work on class variable
# instance method is for instance variable
class Employee:
    company_name='PWC'#class variable
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    @classmethod # class decorator
    def get_company_name(cls):
        cls.company_name='Wipro' # we have done modification tcs into wipro
        print(cls.company_name)
        print(f"Company name is :",cls.company_name)
e1= Employee('Jay',30000)
e2=Employee('Neema',20000)
print(e1.company_name)
print(e1.get_company_name)
Employee.get_company_name()#to access class method we have to give class reference

class Employee:
    company_name='PWC'#class variable
    def __init__(self,nm,sal):
        self.name=nm
        self.salary=sal
    @classmethod # class decorator
    def get_company_name(cls):
        
        print(f"Company name is :",cls.company_name)
e1= Employee('Jay',30000)
e2=Employee('Neema',20000)
Employee.get_company_name()