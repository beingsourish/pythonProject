text=input("Please enter a statement:").lower()
countA=int(text.count("a") or text.count("A"))
countE=int(text.count("e") or  text.count("E"))
countI=int(text.count("i") or text.count("I"))
countO=int(text.count("o") or text.count("O"))
countU=int(text.count("u") or text.count("U"))
length=-int(len(text))
subs=text[length:-5]

TotalVowel=countA+countE+countI+countO+countU
try:
 print(subs)
 print(TotalVowel)
 pos=text.index("hitlike")
 print(pos)

except:
 print("string not found")


