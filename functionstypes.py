#with parameter and return
def sum(a,b):
    return a+b

#with parameter without return
def multiply(a,b):
    result=a*b
    print("product of",a,'&',b,"is",result)

#without parameter and return
def divide():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: ")) 
    return a/b

#with return without parameter
def power():
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    result=a**b
    print("Exponential of",a,"by",b,"is",result)

#default parameter        
def greet(name='user')
    print(f"welcome {name}")