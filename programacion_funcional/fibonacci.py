#Cada numero de la secuencia es la suma de los dosnumeros que la preceden
#Casobase: n<=1
num=int(input('ingresa un numero: '))
def fibonacci(n):
 a,b,i=0,1,1
 while i<=n:
  print(a)
  a,b,i=b,a+b,i+1
fibonacci(num)
