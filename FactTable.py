a=int(input("input your number you want table: "))
start =1
end =10
fact=1
print("Table below:")
####table calculation of the input number######
for i in range(start,end+1):
    print(f"{a}* {i} =",a*i)

####factorial calculation of the input number######
print("factorial below:")
for i in range(start,a+1):
    fact=fact*i
######output reset#########
print("fact=",fact)