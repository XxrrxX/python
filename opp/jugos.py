class jugo:
 def __init__(self,n,c):
  self.n=n
  self.c=c
 def __add__(self,otro):
  return(self.n+'&'+otro.n+' ('+str(self.c+otro.c))+'L)'

f1=str(input('fruta1: '))
cf1=float(input('capacidad fruta 1: '))
f2=str(input('fruta2: '))
cf2=float(input('capacidad fruta 2: '))

a=jugo(f1,cf1)
b=jugo(f2,cf2)

result=a+b
print(result)


