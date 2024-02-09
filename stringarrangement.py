str=input("enter string")
print(str)
str2=''
str3=''
for r in str:
    if r.islower():
        str2=str2+r
    else:
        str3=str3+r
print(str2+str3)