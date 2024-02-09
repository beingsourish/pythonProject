'''
list1=["a","e","i","o","u"]
list1.append("1")
list1.insert(0,2)
print(list1.index("a"))
print(list1[0:2])

Assignment 1
1. Ask user to provide his email ID.
2. print how long long the user ID is ?
3. print , What is the user ID , domain name is ?
4. replace the "@" in email id with "-"
5. print new email id , where the domain name is changed from gmail to yahoo




#List
even  = [2,4,6,8]
numbers = [10,20,30]

#Score.sort() # sorts the list in increasing order
#Score.reverse() # reverses the order of the list
#print(Score.count(16))  # counts the occurence of data in list
#Score.clear() #Clears the whole list
#print(Score.index(78))
#Score.append(200)
#Score.insert(2 , 350)
#Score.remove(96)
#Score.pop(2)

Over1 = [1,0,2,0,0,4]
Over2 = [4,6,2,2,0,4]


1. How many dot balls were delivered in Over1 ?
2. How many boundries were hit in both Overs.
3. what is the total runs scored in both overs ?
4. print a combined list of all the deliveries in both overs ?
5. Remove the boundry-score of Over1 , and print the updated list ?
6. In which delivery of ball , was 6 hit ?
7. For the over 1 , update all dot balls with non-zero score and print.

'''

emailId=input("plesae enter a valid email id:")
print("length of email id:",len(emailId))
userID=emailId.partition("@")[0]
domainName=emailId.partition("@")[2]
print("user_id:",userID)
print("Donam_name:",domainName.partition(".")[0])
print("New Email with -",emailId.replace("@","-"))
print("New Email with yahoo",emailId.replace("gmail","yahoo"))



listEvenNum=[2,4,6,8,10,12]
listEvenNum.append("1")
listEvenNum.insert(0,2)
print(listEvenNum.index("a"))
print(listEvenNum[0:2])