# # operator oerloading
# num1=10
# num2=50
# print(int.__add__(num1,num2))# addditon of two number by operator overloading
# print(num1.__add__(num2))
# print(dir(int))

# str1 = "hello"
# str2="world"
# print(str1.__add__(str2)) # string concatenation
# print(str.__add__(str1,str2)) # string concatenation
# print(dir(str))

# more about operator overloading
# class Book:
#     def __init__(self,title,page):
#         self.title=title
#         self.page=page
        
#     def __add__(self,other):
#         total=self.page+other.page
#         return total
# b1= Book("one indian girl",400)
# b2 =Book("tinytoe",450)
# print("total number of page is :",b1+b2)

# comparsion operator overloading
# class Hotel:
#     def __init__(self,name,fare):
#         self.name=name
#         self.fare=fare
#     def __gt__(self,other):
#         total=self.fare>other.fare
#         return total
# h1=Hotel('Taj',20000)
# h2=Hotel('Fern',15000)
# print(h1>h2)

# achieving method overloading
# class Calci:
#     def add(self,num1=None,num2=None,num3=None):
#         if num1!=None and num2!=None and num3!=None:
#             print("Addition is :", num1+num2+num3)
#         elif num1!=None and num2!=None:
#             print("Addition is :", num1+num2)
#         else:
#             pass
# c1 = Calci()
# c1.add(10,20)
# c1.add(10,20,30)

# calculate area # it will not work
# class Area:
#     def area(self,l):
#         print("area of square is :",l*l)
#     def area(self,l,b):
#         print("area of rectangle is :",l*b)
# a=Area()
# a.area(10)
# a.area(10,20)

# calculate by overloading
class Area:
    def area(self,l=0,b=0):
        if (l >0 and b>0):
            print('area of rectangle:',l*b)
        elif  (l>0 and b==0):
            print("Area of square:",l*l)
a =Area()
a.area(10,20)
a.area(10)