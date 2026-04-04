import matplotlib.pyplot as plt
import math

def cosine_rule(a,b,c):
    a= 3
    b = 5
    c = 30
    c = math.radians(c)
    return math.sqrt(a*a + b*b - 2*a*b*math.cos(c))

x = []
y = []

for i in range(0,360):
    rad = math.radians(i)
    x.append(i)
    y.append(math.cos(rad))

plt.plot(x,y)
plt.grid()
plt.show()
