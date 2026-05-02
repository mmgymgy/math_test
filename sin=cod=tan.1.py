import matplotlib.pyplot as plt
import math


def sin(a,b):
    x = []
    y = []
   
    for i in range(0,361):
        rad = math.radians(i)
        x.append(rad/b)
        y.append((math.sin(rad))*a)
   
    plt.plot(x,y)
    plt.grid()
    plt.show()


"""def cos(a,b,c,d):

   
def tan(a,b,c,d):


q = input("sin,cos,tan중 어떤 그래프: ")

a = int(input(f"a {q}(bx + c) + d 의 a값: "))
b = int(input(f"a {q}(bx + c) + d 의 b값: "))
c = int(input(f"a {q}(bx + c) + d 의 c값: "))
d = int(input(f"a {q}(bx + c) + d 의 d값: "))

if q == sin:
    sin(a,b,c,d)
elif q == cos:
    cos(a,b,c,d)
elif q == tan:
    tan(a,b,c,d)"""
sin(2,2)
