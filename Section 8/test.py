from math import sin, cos, log, pi, sqrt, acos
from numpy import random, array

a = 1.7
b = 21.0 
r = (2.0*a*b)**0.5
fiscount = 0 #Count of secondary fissions
n = 200
avg = []
'''Set the variables as given, but I set my own value of L'''

def neutrons():
    """Number of secondary neutrons produced in each fission.
    Returns an integer number of neutrons, with average 2.5."""
    i=int(random.normal()+3.0)
    if (i<0): return 0
    else: return i
def diffusion():
    """Distance diffused by a neutron before causing fission.
    Returns a random number with probability density p(s) =
    s^2 exp(-3s^2/R^2). This distribution has a mean of 1, so
    multiply by R to get the physical distance."""
    a=cos(2.0*pi*random.random())
    return sqrt(-0.667*(log(random.random())+log(random.random())*a*a))
def xp(x):
    theta = acos(2.0* random . random () -1.0)
    phi = 2.0* pi * random . random ()
    s = r*diffusion()
    xp = x + s*sin(theta)*cos(phi)
    return xp
def yp(y):
    theta = acos(2.0* random . random () -1.0)
    phi = 2.0* pi * random . random ()
    s = r*diffusion()
    yp = y + s*sin(theta)*sin(phi)
    return yp
def zp(z):
    theta = acos(2.0* random . random () -1.0)
    s = r*diffusion()
    zp = z + s*cos(theta)
    return zp
'''Functions defining each coordinate based on how it's given in the notes'''


for c in range(100):
    L = 10
    fiscount = 0
    while fiscount < n:
        fiscount = 0
        for i in range(100):
            x = L*random.random(1) 
            y = L*random.random(1) 
            z = L*random.random(1) 
            '''Coordinates of initial fission'''
            k = neutrons() #Number of neutrons produced from initial fission
            for j in range(k): #Iterates as many times for as many neutrons produced
                x2 = xp(x)
                y2 = yp(y)
                z2 = zp(z)
                '''Coordinates of neutrons after movement'''
                if 0.0 <= x2 <= L and 0.0 <= y2 <= L and 0.0 <= z2 <= L:
                    fiscount += 1 #Counts the number of secondary fissions
        L += 0.1
    avg.append(L)
    print L
Avg = array(avg)
print Avg
AvgL = sum(Avg)/100
print AvgL
CriticalV = (L**3)/1000000
print CriticalV
CriticalM = 18700*CriticalV
print CriticalM