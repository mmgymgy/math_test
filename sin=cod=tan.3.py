import matplotlib.pyplot as plt
import math


def sin(a,b,c,d,q1,q2):
    x = []
    y = []
   
    for i in range(-360 + (q1 * 360),361 + (q2 * 360)):
        rad = math.radians(i)
        x.append(rad/b-c)
        y.append((math.sin(rad))*a+d)
   
    plt.plot(x,y)
    plt.axhline(0, color='red', linewidth=1)
    plt.axvline(0, color='red', linewidth=1)
    plt.grid()
    plt.show()


def cos(a,b,c,d,q1,q2):
    x = []
    y = []
   
    for i in range(-360 + (q1 * 360),361 + (q2 * 360)):
        rad = math.radians(i)
        x.append(rad/b-c)
        y.append((math.cos(rad))*a+d)
   
    plt.plot(x,y)
    plt.axhline(0, color='red', linewidth=1)
    plt.axvline(0, color='red', linewidth=1)
    plt.grid()
    plt.show()

   
def tan(a,b,c,d,q1,q2):
    x = []
    y = []
   
    for i in range(-180 + (q1 * 180),181 + (q2 * 180)):
        rad = math.radians(i)
        x.append(rad/b-c)
        y.append((math.tan(rad))*a+d)
    plt.plot(x,y)
    plt.axhline(0, color='red', linewidth=1)
    plt.axvline(0, color='red', linewidth=1)
    plt.grid()
    plt.ylim(-30,30)
    plt.show()



q = input("sin,cos,tan중 어떤 그래프: ")

a = int(input(f"a{q}(bx + c) + d 의 a값: "))
b = int(input(f"a{q}(bx + c) + d 의 b값: "))
c = int(input(f"a{q}(bx + c) + d 의 c값: "))
d = int(input(f"a{q}(bx + c) + d 의 d값: "))

if c>0:
    q1 = 0
    q2 = c//4
elif c<0:
    q1 = c//4
    q2 = 0
else:
    q1 = q2 = 0

if q == "sin":
    sin(a,b,c,d,q1,q2)
elif q == "cos":
    cos(a,b,c,d,q1,q2)
elif q == "tan":
    tan(a,b,c,d,q1,q2)
