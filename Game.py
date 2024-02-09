import random
import time
###hiii merge conflict####
print("Enter your choiGoce ""\n" "1: Sourish ""\n"
      "2: Salman ""\n"
      "3: Mahesh babu ""\n")
a= int(input("Enter here:    "))
if a==1 :
    print("Your choice is Sourish")
elif a==2 :
    print("Your choice is Salman")
elif a==3 :
    print("Your choice is Mahesh Babu")
else:
    print("wrong choice out of Game")

print("let Computer decides................")
time.sleep(5)
b= random.randint(1,3)
if a==1 and b==2 :
    print("Sourish looks like  Salman")
if a==2 and b==1 :
    print("Sourish is fan of mahesh babu")
else:
    print("Sorryyy....")