import numpy as np
import matplotlib.pyplot as plt

# basic definitions
n=100
r1=20
r2=50

# definitions
def createNgon(n, r):
    x=[r]
    y=[0]
    for m in range(1, n+1, 1):
        x.append(r * np.cos(2 * np.pi * m / n))
        y.append(r * np.sin(2 * np.pi * m / n))
    return x, y
    
def createCirMeander(n, r1, r2):
    x1, y1 = createNgon(n, r1)
    x2, y2 = createNgon(n, r2)
    x=[]
    y=[]
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
    return x, y

# main
x, y = createCirMeander(n, r1, r2)

plt.figure(num=1, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.plot(x, y)
plt.show()