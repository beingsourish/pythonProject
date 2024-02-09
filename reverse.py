num=int(input("your num"))
num_buff=num
counter=0
num2=0
str2=''
while(num>0):
    r=num%2
    str2 = str2 + str(r)
    #print(str2)
    num=num//2
    counter+=1
    num2=r+num2


#print(num2)
#print(counter)
print(int(str2))
'''print(num_buff)
if (int(str2) ==num_buff):
    print('you got palindrome')
'''