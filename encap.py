# class Finance:
#     def __init__(self):
#         self.revenue=30000
#         self.number_of_sales=114
# f1=Finance()
# class HR:
#     def __init__(self):
#         self.number_of_emp=32
       
#         print(f1.revenue)
# h1= HR()

#ENCAPUSLATIION 

# class Finance:
#     def __init__(self):
#         self.revenue=30000 # revenue is public variable acessible everywhere
#         self.number_of_sales=114
# f1=Finance()
# print(f1.__dict__)# before modify

# class HR:
#     def __init__(self):
#         self.number_of_emp=32
#         f1.revenue=1
# h1= HR()
# print(f1.__dict__) # after modify

# modification in encapsulation
# class Finance:
#     def __init__(self):
#         self.__revenue=30000 # PRIVATE REVENUE
#         self.number_of_sales=114
# f1=Finance()
# print(f1.__dict__)

# class HR:
#     def __init__(self):
#         self.number_of_emp=32
#         f1.__revenue=2000
# h1= HR()
# print(f1.__dict__) # after modify


class Finance:
    def __init__(self):
        self.__revenue=30000 # PRIVATE REVENUE
        self.__number_of_sales=114
        print(f"finance revenue is {self.__revenue}and number of sales is {self.__number_of_sales}")
    def display(self):
        self.__revenue=500000
        self.__number_of_sales=300
        print(f"finance revenue is {self.__revenue}and number of sales is {self.__number_of_sales}")

f1=Finance()
print(f1._Finance__revenue)
print(f1.__dict__)


