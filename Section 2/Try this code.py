'''import pylab
from numpy import *
x = arange(0, 8*pi, 0.01)
pylab.plot(x, sin(x))
pylab.plot(x, cos(x/2))
pylab.xlabel('x')
pylab.title('Oscillation and damped oscillation')
pylab.savefig('pylabplot.png')
import os
curdir = os.getcwd()
print 'Plot saved in : ', curdir
from math import cos , fabs , pi
def g(x):
    n = 1; total = term = cos(x) # First term
    while fabs(term) > (1.0e-7*fabs(total)+1.0e-13):
        n += 2 # Advance to next term
        term = cos(n*x)/(n*n)
        total += term # Add term to total
    return total
x = arange(1,10)
y = g(x) 
print x
print y'''

'''pylab.plot(x, g(x))
pylab.xlabel('x')
pylab.ylabel('g(x)')
pylab.title('g(x) against x')
pylab.savefig('Fourier Series.png')
curdir = os.getcwd()
print 'Plot saved in : ', curdir'''
import pylab
r = 100.0
s = 10000.0
n = 50
a = [r+s]
for i in range(n-1):
    a.append (r+s*a[-1]/(s+a[-1]))
pylab.plot(a)
pylab.show()