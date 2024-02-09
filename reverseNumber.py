a=int(input("enter your number"))
string=str(a)
length =len(str(a))
string2=[]
b=''
print("length=",length)
while length >0:
    print(string[length-1])
    b=b+string[length-1]
    length=length-1

print(b)
