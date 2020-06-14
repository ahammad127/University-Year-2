'''from numpy import exp, arange, fabs
import pylab
def f(x):
    y = exp(-x**2)
    return y
x = arange(-2.5, 2.5, 0.01)
y = f(x)
pylab.plot(x, y)
pylab.xlabel('x')
pylab.ylabel('f(x)') 
pylab.title('f(x) against x')

def trap0(f, a, b, n):
    h = float(b - a)/n
    s = 0.5*(f(a) + f(b))
    for i in range (1 , n):
        s = s + f(a + i*h)
    return s*h

def trap1(f, a, b, delta, maxtraps = 1024):
    n = 10
    inew = trap0(f, a, b, n)
    iold = -inew
    while(fabs(inew - iold) > delta*fabs(inew)):
        iold = inew
        n = 2*n
        if n > maxtraps:
            print "Cannot reach requested accuracy with", \
                maxtraps, " trapezia"
            return
        inew = trap0(f ,a ,b ,n)
    return inew
I = trap1(f, a = -100, b = 100, delta = 1e-7, maxtraps = 10000)
print I'''
from numpy import cos, pi, arange
import pylab
def f(theta):
    y = 1/(cos(theta)-cos(pi/4))**0.5
    return y
theta = arange(-90, 90, 0.001)
y = f(theta)
pylab.plot(theta, y)
pylab.xlabel('Theta')
pylab.ylabel('f(theta)') 
pylab.title('f(theta) against theta')