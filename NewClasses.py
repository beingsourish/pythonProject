a= int(input("Enter your number"))
b= int(input("Enter your number"))
c=a+b
average=c/2
d=a*b
print("AVERAGE is",average)
print("addition is {0} +{1}={2}".format(a,b,c))
print("multiplication is {0} *{1}={2}".format(a,b,d))

if a>b:
    if a==50:
      print("a is grater and value is 50",a)
    print("a is greater")
elif b>a:
    print("b is greater",b)
else:
    print("b is equal to a")

print("end")