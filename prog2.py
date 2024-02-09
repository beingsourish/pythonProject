'''x = 1

y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

txt = "The best things in life are free!"
print("free" in txt)

b = "heyW"
if len(b) > 0:
    print(b[0])
    print(b.upper())
    print(b.lower())
    print(b.strip())
    print(b.replace("h", "J"))
    print(b.find("W"))
    for x in b:
        if x.find("W")==0:
          print(x)
        else:
         print("no W")
else:
    print('hi')

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
motherName="My mother name is Barna Roy Chowdhury"
x=motherName[motherName.find("Barna"):len(motherName)]
Y=motherName[motherName.find("Roy"):motherName.find("Roy")+3]
print(x,Y)
if "Barna" in motherName:
   print("Yes, 'Barna' is in the name list")
else:
     print("not exists")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
del tropical
print(thislist)
thislist.pop(1)
del thislist[0:3]
print(thislist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
newlist=[x.upper()  for x in fruits if "i" in x]
print(fruits)
print("comprehensive",newlist)
for x in fruits:
  if "i" in x:
    newlist.append(x)

print("new list",newlist)
for y in fruits:
    newlist.append(y)
    print(newlist)
'''


fruit = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = []


def myFunc(x):
     x=x.upper()
     print(x)
     return x.upper()

   # newlist3=[x if x !="banana"  else "sourish" for x in fruit ]
    #print("newlist3",newlist3)



for x in fruit:
    if x != "banana":
        newlist2.append(myFunc(x))
    else:
        newlist2.append( "orange")

print(newlist2)

newlist3=["roy",3]
print(newlist3)