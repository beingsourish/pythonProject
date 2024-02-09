a=input("enter string:")
val=0
for i in a:
   if ((i in 'a') or (i in 'e') or (i in 'i' ) or (i in 'o') or (i in 'u')):
      val=val+1
      print("Total vowels :",i.count('a')+i.count('e')+i.count('i')+i.count('o')+i.count('u'))
   else:
     print(a[::-1])
print(val)