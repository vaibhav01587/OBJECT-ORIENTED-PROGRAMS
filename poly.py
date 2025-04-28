# # polymorphism
# class Veh:
#     def __init__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#     def display(self):
#         print("name is :",self.name)
#         print("color is :",self.color)
#         print("price is :",self.price)
#     def max_speed(self):
#         print("maximum speed limit is 100")
#     def gear(self):
#         print("hear change os 5")
# class Car(Veh):
#     def max_speed(self):
#         print("maximum speed limit is 140")
#     def gear(self):
#         print("hear change os 7")
# v1=Veh('Truck','Red',2000000)
# c1=Car('Car','White',500000)
# v1.display()
# c1.display()
# v1.max_speed()
# c1.max_speed()

#polymorphism with inheritance
# class Cart:
#     def __str__(self):
#         print("this is cart class")
# c1 = Cart()
# print(c1.__dict__)    
class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.clothes=basket1
        self.electronics=basket2
        self.other=basket3
    def __len__(self):
        print("total number of items in cart :")
        return len(self.clothes)+len(self.electronics)+len(self.other)
vaibhav=Cart(['pant','shirt','T-shirt'],['Tv','earphone'],['chair'])
print(len(vaibhav))