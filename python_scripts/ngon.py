# author: Battosai42

# imports
import math as ma
import matplotlib.pyplot as plt
#import pcbnew

# definitions
def createNgon(n, r, xoffset=0, yoffset=0):   # create regular n-gon nith n sides and a circumference of r
    x=[r + xoffset]
    y=[0 + yoffset]
    for m in range(1, n, 1):
        x.append(r * ma.cos(2 * ma.pi * m / n) + xoffset)
        y.append(r * ma.sin(2 * ma.pi * m / n) + yoffset)
    length = ma.sqrt(abs(x[1]-x[0])**2+abs(y[1]-y[0])**2) # calculate the segment length
    return x, y, length
    
def createCirMeander(n, r1, r2, shift=0, xoffset=0, yoffset=0):    # create circular meander using 2 regular n-gons (n has to be even)
    x1, y1, l1 = createNgon(n, r1, xoffset, yoffset)
    x2, y2, l2 = createNgon(n, r2, xoffset, yoffset)
    x=[]
    y=[]
    j=shift+1
    for i in list(range(0, int(n), 2)):
        for k in list(range(4)):
            if k == 0:
                x.append(x2[i])
                y.append(y2[i])
            elif k == 1:
                x.append(x2[i + k])
                y.append(y2[i + k])
            elif k == 2 or k == 3:
                if i + k - j < n:       # if the shift is not 0
                    x.append(x1[i + k - j])
                    y.append(y1[i + k - j])
                else:                   # if the shift is 0
                    x.append(x1[0])
                    y.append(y1[0])
    x.append(x2[0])
    y.append(y2[0])
    return x, y, [l1, l2]
    
def calcN(r, wire_width, clearance):
    lmin = wire_width + clearance
    n=2
    while True:
        x, y, l =createNgon(n, r)
        if l > lmin:
            n = n+2
        else:
            break
    return n-2
    
def createTracks(x, y):
    pcb = pcbnew.GetBoard()
    for i in range(len(x)):
        t = pcbnew.TRACK(pcb)
        pcb.Add(t)
        t.SetStart(pcbnew.wxPointMM(round(x[i],2), round(y[i],2)))
        t.SetEnd(pcbnew.wxPointMM(round(x[i+1],2), round(y[i+1],2)))
        t.SetNetCode(i)
        t.SetLayer(31)
        
def plot(x, y): # plot meander using pyplot
    plt.figure(num=1, figsize=(8, 8), dpi=127, facecolor='w', edgecolor='k')
    plt.grid(True, which='both')
    plt.plot(x, y, linewidth=1)
    plt.show()

# main()
wire_width = 0.2    # Track width
clearance = 0.2     # min. clearance between Tracks
#n=100   # n has to be even
r1=20   # circumference of inner ngon
r2=50   # circumference of outer ngon

# create circular meander
n = calcN(r1, wire_width, clearance)    # calculate max n to comply wire with and clearance
x, y, l = createCirMeander(n, r1, r2, shift=0, xoffset=20, yoffset=20)
plot(x,y)
