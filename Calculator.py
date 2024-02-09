print("Please select your operation")
print("     1:Addition")
print("     2:Subtraction")
print("     3:Multiplicator")
print("     4:Division")

a=int(input("enter your choice     "))

if a==1:
    print("you chosen addition")
    a=int(input("enter your first number   "))
    b=int(input("enter your second number    "))
    add=a+b
    print(F"addition=",add)

elif a==2:
    print("you chosen subtraction")
    a=int(input("enter your first number  "))
    b=int(input("enter your second number  "))
    sub=a-b
    print("subtraction=",sub)

elif a==3:
    print("you chosen multiplication")
    a=int(input("enter your first number   "))
    b=int(input("enter your second number  "))
    mul=a*b
    print("multiplication=",mul)

elif a==4:
    print("you chosen division")
    a=int(input("enter your first number   "))
    b=int(input("enter your second number  "))
    div=a/b
    print("division=",div)

else:
    print("invalid choice")