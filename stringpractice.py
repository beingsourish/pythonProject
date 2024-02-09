s='efcdba'
rr=''
#print(sorted(s))
ss=sorted(s)
for r in ss:
    rr=rr+r

#print(rr.lstrip())

dish_name=input('dish_name')
#print('dish name :  ' + dish_name)
price_name=input('price')
#print('price_name : '  +price_name)
total_length = len(dish_name)+len(price_name)
length_starts=0
if total_length<=25:
 length_starts=(25-total_length)
else:
    pass
starts='*' * length_starts

#print(dish_name+starts+price_name)


password_name=input('password')
print('pass name :  ' + password_name)
confirm_password=input('password_name_confirm')
print('price_name : '  +confirm_password)

if password_name==confirm_password:
    print('matched_successful')
elif password_name.casefold()==confirm_password.casefold():
    print('cases are incorrect but password is ok')
else:
    print('incorrect')