import random
import time

print("Enter your choiGoce ""\n" "1: Sourish ""\n"
      "2: Ananya ""\n"
      "3: Katrina ""\n")
a= int(input("Enter here:    "))
if a==1 :
    print("Your choice is Sourish")
elif a==2 :
    print("Your choice is Ananya")
elif a==3 :
    print("Your choice is Katrina")
else:
    print("wrong choice out of Game")

print("let Computer decides................")
time.sleep(5)
b= random.randint(1,3)
if a==1 and b==2 :
    print("Sourish weds Ananya")
if a==2 and b==1 :
    print("Sourish weds Ananya")
else:
    print("Sorryyy....")