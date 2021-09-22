import re
#tu código va aquí
n=str(input("ingesa numero: "))
pattern = n
if int(len(pattern)) == 8:
 if re.match("1",pattern) or re.match("8",pattern) or re.match("9",pattern):
  print("valid")
 else:
  print("invalid")
else:
 print("invalid")

