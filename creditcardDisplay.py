credit_card_number=input('Enter Credit card Number')
print(credit_card_number)
last_four_digit=credit_card_number[15:19:1]
print(last_four_digit)
string_to_replace=credit_card_number[0:14:1]
print(string_to_replace)
string_new=''
for i in string_to_replace:
    if i.isdigit():
        string_to_replace=string_to_replace.replace(i,'*')

print(string_to_replace+' '+last_four_digit)
#7777 7777 7777 0008