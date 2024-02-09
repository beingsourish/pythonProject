enter_string_1=input('string_1')
enter_string_2=enter_string_1[::-1]
print(enter_string_1)
print(enter_string_2)

if enter_string_1==enter_string_2:
    print('palindrome')

elif enter_string_1.casefold()==enter_string_2.casefold():
    print('palindrome')

else:
    print('Not a palindrome')