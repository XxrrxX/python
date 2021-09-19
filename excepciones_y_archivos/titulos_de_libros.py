#Necesitas hacer un programa de categorizacion especial basado en su titulo
#El codigo es igual a la primera letra del libro, seguido del numero de caracteres del titulo
#Ejemplo "HarryPoter" el codigo seria H12 utiliza el metodo read lines() recuerda que tolas las lineas contienen /n al final no debe ser incluidp en el recuento de caractteres
file=open('books.txt','r')

for line in file:
 c=str(line[0])
 if c == 'G':
  n=str(len(line))
  print(c+n)
 else:
  n=str(len(line)-1)
  print(c+n)
file.close()
