import time

sum=0
i: int
for i in range(1,11):
    print(f"square of {i}",i*i)
    if i%2==0:
       sum=sum+i

print("sum of all even=",sum)

a= int(input("enter first number"))
b= int(input("enter second number"))
c= int(input("enter third number"))
val=0
time.sleep(3)
for i in range(100,1000):

    if a ==i:
        val=val+1
    if b==i:
        val = val + 1
    if c==i:
        val = val + 1

print(val)
