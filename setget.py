class Employee:
    def setName(self,nm):
        self.name=nm
    def getName(self):
        print("The Name is:",self.name) #to fetch the data
e1=Employee()
e2=Employee()
e1.setName(input("Enter the name : "))
e2.setName(input("Enter the name :"))
print("e1 object is:",e1.__dict__) # return the value in dictionary
print("e2 object is :",e2.__dict__)
e1.getName()
        