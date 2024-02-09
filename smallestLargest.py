listofelements=[]

numofelements=int(input("input elements"))

for i in range(numofelements):
    elem=int(input(f"elements:{i}"))
    listofelements.append(elem)

print("largest is",max(listofelements))
print("minimum is",min(listofelements))

