#Escribe una funcion para tomar el valor de celcius comoargumento y devolver el valor de farenheit crrespondiente
#La siguiente ecuacion se utiliza para calcular el valor de farentheit 9/5*celcius+32
celsius=int(input('Introduce el valor de celcius para convertir a farenheit: '))
def convertir(c):
 res= 9/5*c+32
 return res
fahrenheit=convertir(celsius)
print(fahrenheit)
