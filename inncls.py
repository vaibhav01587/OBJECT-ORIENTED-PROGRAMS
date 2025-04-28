# class Outer:
#     def __init__(self):
#         print("outer constructor callled")
#     def display(self):
#         print("outer display method called")
#     class Inner:
#         def __init__(self):
#             print("Inner constructor called")
#         def show(self):
#             print("Inner constructor method")
            
# ob=Outer()
# iin=ob.Inner()
# iin.show()

# NESTED CLASS OR INNER  CLASS 
class Student:
    def __init__(self,name,roll,dd,mm,yy):
        self.name=name
        self.roll=roll
        self.Dob=self.Dob(dd,mm,yy)
    def display(self):
        print(f" name is {self.name} roll is {self.roll}")
        self.dob.display()
    class Dob:
        def __init__(self,dd,mm,yy):
            self.date=dd
            self.month=mm
            self.year=yy
        def show(self):
            print(f"data of birth iss {self.date}month is {self.month} year is {self.year}")
s1 =Student('vaibhav',45,1987,5,1)
s1.display()
