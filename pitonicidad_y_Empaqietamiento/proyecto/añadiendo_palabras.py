def concatenate(txt_arg,*args):
 cadena = txt_arg 
 for i in args:
  cadena = cadena+"-"+i
 return cadena

print(concatenate("I", "love", "Python", "!"))

