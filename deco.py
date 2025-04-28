
def decor(func):
    def addition():
        result =addition
        num3 = int(input("enter then number :"))
        result = result +num3
        return result
    return addition



@decor
def addition():
    
        num1=int(input("enter the number :"))
        num2 =int (input("enter the number :"))
        result =num1 + num2
        return result
addition=decor(10)
print("addtion is:",addition)