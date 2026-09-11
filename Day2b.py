
operator=input(print("Which arithmetic operation would you like to perform (+,-,*,/,%,//,**) : "))
print( f" You have choosed {operator}")
a=int(input(print("Enter your first number :")))
b=int(input(print("Enter your second number : ")))

def takeinput():
        if (operator== "+"):
            result=a+b
            print(f"{result}")
        elif (operator == "-"):
            result=a-b
            print(f"{result}")
        elif (operator=="*"):
            result=a*b
            print(f"{result}")
        elif(operator=="/"):
            result=a/b
            print(f"{result}")
        elif(operator=="%"):
            result=a%b
            print(f"{result}")
        elif(operator=="//"):
            result=a//b
            print(f"{result}")
        elif(operator=="**"):
            result=a**b
            print(f"{result}")
        else:
            print("Invalid operator")
    
takeinput()


