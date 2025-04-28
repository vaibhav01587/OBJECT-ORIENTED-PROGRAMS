# class Bank:
#     bank_name = 'BOI' # class variable or static variable
#     rate_of_interest= 12.25
#     @staticmethod
#     def simple_interest(principle,n,roi):
#         si=(principle*n*roi)/100
#         print(si)
# Bank.simple_interest(2000,3,2)# decorator call static method we use class reference

# how constructor work in inheritance 
class Father:
    def __init__(self):
        self.name='bajaj'
        self.model='chetak'
        
        print("father constructor called ")
        
# class Son(Father):
#     def __init__(self):
#         super().__init__() # super function is called
#         self.model_car='clx'
#         print("Son Constructor called")
#         self.vehicle="BMW"

# s1=Son()

# print(s1.__dict__)

# HOW TO USE SUPER FUNCTION without postional argument
class Computer():
    def __init__(self):
        self.name='hp'
        self.model='dell'
        print("computer constructor are called")
class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.name_mobile= 'iphone'
        print("mobile constructor are called")
m1=Mobile()

print(m1.__dict__)


# SECOND WAY TO USE SUPER FUNCTION with positonal argument

class Computer():
    def __init__(self,hp,dell): # postional argument
        self.name=hp
        self.model=dell
        print("computer constructor are called")
class Mobile(Computer):
    def __init__(self,hp,dell):
        super().__init__(hp,dell)
        self.name_mobile= 'iphone'
        print("mobile constructor are called")
m1=Mobile('senso','inspiron') # this work like positional argument

print(m1.__dict__)