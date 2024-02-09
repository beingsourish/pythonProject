
myfirstlist=['a','p','p','l','e','j','i','o','o','o','o']
myfirstlist2=['o','r','a','n','e','a','j','j']
mylist3=[]
lentha =len(myfirstlist)
lenthb =len(myfirstlist2)

if lentha >lenthb:
 for i in range(0,lentha):
    for j in range(0,lenthb):
        if myfirstlist[i]==myfirstlist2[j] and (mylist3.count(myfirstlist[i])==0):
            mylist3.append(myfirstlist[i])
else:
    for i in range(0, lenthb):
        for j in range(0, lentha):
            if myfirstlist2[i] == myfirstlist[j] :
                       if (mylist3.count(myfirstlist2[i])==0):
                         mylist3.append(myfirstlist2[i])
print(mylist3)