mydict = {"name": 'sourish', "wife": 'ananya'}
print(mydict)
mydict["place"]="Kolkata"
print(mydict)



for i in mydict.keys():
    if i=="wife" :
          print("wife key exists")
          print(mydict[i])