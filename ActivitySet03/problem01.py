import math

class point:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
def inp():
   x = float(input('enter the cordinate'))
   return math.floor(x)

def length(a1,a2):
    prod = ((a1.x-a2.x)**2) + ((a1.y-a2.y)**2)
    dis = math.sqrt(prod)
    return dis

def area(l,b):
    a=l*b
    print(a)
    
def cond(p1,p2,p3):
    l1 = length(p1,p2)
    l2 = length(p2,p3)
    l3 = length(p3,p1)
    if (l1**2 + l2**2 == l3**2):
         area(l1,l2)
    elif (l2**2 + l3**2 == l1**2):
         area(l2,l3)
    elif (l3**2 + l1**2 == l2**2):
         area(l1,l3)
    else:
        print('not valid')
p1=point(inp(),inp())
p2=point(inp(),inp())
p3=point(inp(),inp())
cond(p1,p2,p3)
