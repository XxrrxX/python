#fizzbuzz es una tarea de programacion muy conocida , preguntada durante las entrevistas de trabajo Elcodigo dado resuelve el problema de fizzbuzz y utiliza las palabras "fizz"y "buzz" toma una entrada n y saca los numeros de 1 a n Por cada multiplo de 3 imprime "fizz" en lugar del numero por cada multiplo de 5  imprime "buzz" en lugar del numero para los numeros multiplos de 5 y 3 imprime "fizzbuzz" omite losnumeros pares
n=int(input('Ingresa un numero: '))
for x in range(1,n):
 if x%2==0:
  continue
 elif x%3==0 and x%5==0:
  print('fizzbuzz')
 elif x%3==0:
  print('fizz')
 elif x%5==0:
  print('buzz')
 else:
  print(x)
