def function(named_arg, *args):
 print(named_arg)
 print(args)
function(1,2,3,4,5)

def function(x,y,food="spam"):
 print(food)
function(1,2)
function(3,4,"eggs")
def my_func(x,y=7,*args,**kwargs):
 print(kwargs)
my_func(2,3,4,5,6,a=7,b=8)
