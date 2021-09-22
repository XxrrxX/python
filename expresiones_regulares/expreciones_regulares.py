import re
pattern=r"spam"
if re.match(pattern,"eggspamsausagespam"):
 print("match")
else:
 print("nomatch")
if re.search(pattern,"eggspamsausagespam"):
 print("match")
else:
 print("nomatch")
print(re.findall(pattern,"eggspamsausagespam"))
print(re.finditer(pattern,"eggspamsausagespam"))
pattern=r"pam"
match=re.search(pattern,"eggspamsauagespam")
if match:
 print(match.group())
 print(match.start())
 print(match.end())
 print(match.span())

str="My name is david hi david"
print("cadena original: "+str)
n=input("Escribe un nombre para remplazarlo en la cadena: ")
pattern=r"david"
newstr=re.sub(pattern,n,str)
print(newstr)
