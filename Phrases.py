import time

correctString="Salman Khan is bhai"
missingphrase="Salman Khan is ...."
correctanswer="bhai"
missingword=int(1)
numOfChances=int(missingword) +1
print(missingphrase)
for i in range(1,numOfChances+1):
    time.sleep(2)
    a=input("please enter your guess: ")
    if (a == correctanswer):
        print("SUCCESSS")

        break
    elif(i==1 and a!= correctanswer):
        print("You have one more chance wait ......")
    else:
        print("You have  lost SORRYYY")
