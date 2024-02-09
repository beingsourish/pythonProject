s='sourish'
#print(s[0])
#print(s[-1])

for r in range(1,len(s)+1,2):
    print(s[-r])
    if s[-r] in 's':
        print('charcter found')

print(s[0:len(s):])
print(s[:len(s):])
print(s[-1:-(len(s)+1):-1])