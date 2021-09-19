#Dado un texto comoentrada , encuentra y saca la palabra mas larga
#Entrada 'this is an awesome text'
#Salida 'awesome'
#Llama al metodo split() que devuelve una lista de palabras de cadena
txt='this is an awesome text'
r =  txt.split()
max=0
for i in r:
 l = len(i)
 if max < l:
  max = l
  maxs = i
 else:
  continue
print(maxs) 
