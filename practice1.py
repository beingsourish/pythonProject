from datetime import datetime
x = 15


def change():
    global x

    x = x + 5

    print("value of x inside a function :", x)


print("value of x outside a function :", x)

change()


now = datetime.now()
print (now)

mytime = now.strftime("%d-%m-%y")

date = now.strftime("%d==%a==%b==%Y")
print (mytime)
print (date)