for i in range(1,6):
   for j in range(1,i):
       print('*',end='')
   print('\n')

m=1
for i in range(1,5):
   for j in range(m,5-i):
       print('*',end='')
       m=+1
   print('\n')