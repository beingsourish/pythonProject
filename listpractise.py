'''
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

Over1 = [1,0,2,0,0,4]
Over2 = [6,6,2,2,0,6]
print("Dot balls",Over1.count(0))
boundariesOver1=Over1.count(4)+Over1.count(6)
boundariesOver2=Over2.count(4)+Over2.count(6)
totalBoundary=boundariesOver1+boundariesOver2
print("Total boundary",totalBoundary)
SumOver1=sum(Over1)
SumOver2=sum(Over2)
totalSum=SumOver1+SumOver2
print("Total Runs",totalSum)
combineOver=Over1+Over2
print(combineOver)
updList=Over1.remove(4)
print("Over without boundary",Over1)
item = 6
for x in range(len(Over2)):
 if Over2[x]==item:
     print(item, "is hit at ball",x)

item_0 = 0
for x in range(len(Over1)):
 if Over1[x]==item_0:
     Over1[x]=6

print(Over1)





