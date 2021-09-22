class Animal:
 def __init__(self,name,color):
  self.name=name
  self.color=color
class cat(Animal):
 def purr(self):
  print("purr")
class dog(Animal):
 def bark(self):
  print("wof wof")
fido = dog("fido","brown")
print(fido.color)
fido.bark()
minino = cat("minino","black")
print(minino.color)
minino.purr()
