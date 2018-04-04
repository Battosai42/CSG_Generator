import numpy as np
import matplotlib.pyplot as plt

n=100
r1=20
r2=50
alpha = 360/n

x1=[]
y1=[]
x1.append(r1)
y1.append(0)
for m in range(1, n+1, 1):
    x1.append(r1 * np.cos(2 * np.pi * m / n))
    y1.append(r1 * np.sin(2 * np.pi * m / n))

x2=[]
y2=[]
x2.append(r2)
y2.append(0)
for m in range(1, n+1, 1):
    x2.append(r2 * np.cos(2 * np.pi * m / n))
    y2.append(r2 * np.sin(2 * np.pi * m / n))

x=[]
y=[]
k=0
for i in list(range(0, int(n), 2)):
    for k in list(range(4)):
        print(i, k)
        if k == 0:
            x.append(x2[i])
            y.append(y2[i])
        elif k == 1:
            x.append(x2[i + k])
            y.append(y2[i + k])
        elif k == 2:
            x.append(x1[i + k - 1])
            y.append(y1[i + k - 1])
        elif k == 3:
            x.append(x1[i + k - 1])
            y.append(y1[i + k - 1])
x.append(x2[0])
y.append(y2[0])

print(alpha)
print(x1)
print(y1)

#plt.plot(x1, y1)
#plt.plot(x2, y2)
plt.plot(x, y)
plt.show()