str=input('enter date month year')
print(str)
str2=str.split('/')
first_sl=str.find('/')
sec_sl=str.rfind('/',1)
#print(first_sl)
#print(sec_sl)
day=str[0:first_sl:]
month=str[first_sl+1:sec_sl:]
year=str[sec_sl+1::]
print('Day= '+day)
print('Month= '+month)
print('Year= '+year)
print(str2)

anagram1=input('enter 1')
anagram2=input('enter 2')
anagram3=sorted(anagram1)
anagram4=sorted(anagram2)
str=''
str2=''

if len(anagram1)!=len(anagram2):
    print('No Anagram')

else:

 for i in anagram3:
    str=str+i

 for j in anagram3:
    str2=str2+j

 if str==str2:
    print('Anagram')
 else:
    print('nope')

 for x in anagram1:
     if x not in anagram2:
         print('check fail')
         break
 else:
     print('pass')

