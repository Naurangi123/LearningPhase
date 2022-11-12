from secrets import choice


def add( A,B):
    return A+B
def Subtract( A,B):
    return A-B
def Multiply( A,B):
    return A*B
def Division( A,B):
    return A/B
def Square(A,B):
    return A**B





print("Select the Opretion")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Division")
print("e.Square")
choice=input("Enter your choice(a/ b/ c/ d/ e):")

n1=int(input("enter first number"))
n2=int(input("enter second number"))

if choice=='a':
    print(n1,"+",n2,"=",add(n1,n2))
elif choice=='b':
    print(n1,"-",n2,"=",Subtract(n1,n2))
elif choice=='c':
    print(n1,"*",n2,"=",Multiply(n1,n2))
elif choice=='d':
    print(n1,"/",n2,"=",Division(n1,n2))
elif choice=='e':
    print(n1,"**",n2,"=",Square(n1,n2))
else :
    print("Invalid numbers")
    
