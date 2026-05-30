import matplotlib.pyplot as plt
import math

x = []
y = []

def sctan(a,b,c,d,q1,q2,q):
    for i in range(-360 + (q1 * 360),361 + (q2 * 360)):
        rad = math.radians(i)
        if q == "tan":
            if i % 180 == 90:
                x.append(None)
                y.append(None)
                continue
        if q == "sin":
            x.append((rad-c)/b)
            y.append((math.sin(rad))*a+d)
        elif q == "cos":
            x.append((rad-c)/b)
            y.append((math.cos(rad))*a+d)
        elif q == "tan":
            x.append((rad-c)/b)
            y.append((math.sin(rad)/math.cos(rad))*a+d)
   
q = input("sin,cos,tan중 어떤 그래프: ")

a = int(input(f"a{q}(bx + c) + d 의 a값: "))
b = int(input(f"a{q}(bx + c) + d 의 b값: "))
c = int(input(f"a{q}(bx + c) + d 의 c값: "))
d = int(input(f"a{q}(bx + c) + d 의 d값: "))

if c>0:
    q2 = c//4
    q1 = q2//3
elif c<0:
    q1 = c//4
    q2 = q1//3
else:
    q1 = q2 = 0

sctan(a,b,c,d,q1,q2,q)
    
plt.plot(x,y)
plt.axhline(0, color='red', linewidth=1) #x축
plt.axvline(0, color='red', linewidth=1) #y축
plt.grid()
plt.show()
