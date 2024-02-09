numbers_count=int(input('enter count of numbers='))
enter_sign=str(input('enter sign='))


def calc(numbers_count):
    result=0
    result_mul = 1
    while numbers_count>0:
        numbers = int(input('enter the number='+str(numbers_count)))
        if enter_sign == '+':
            result=result+numbers
        if enter_sign == '-':
            result=numbers - result
        if enter_sign == '*':
            result_mul=result_mul * numbers
        if enter_sign == '/':
            result = 1
            result=numbers
        numbers_count-=1
        if enter_sign=='*' or enter_sign=='/' :
           print(result_mul)
        else:
            print(result)

def max(numbers_count):
    result_max=0
    while numbers_count>0:
        numbers = int(input('enter the number=' + str(numbers_count)+':  '))
        if result_max>numbers:
            result_max=numbers
            print(numbers)
        else:
            result_max = numbers
        numbers_count-=1
    print('f max number=',{result_max})

max(numbers_count)










