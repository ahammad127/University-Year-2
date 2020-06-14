from numpy import cos, pi, arange
import pylab, os
def f(theta):
    y = 1/(cos(theta)-cos(pi/4))**0.5
    return y
theta = arange(0, pi/4, 0.001)
y = f(theta)
pylab.plot(theta, y)
pylab.xlabel('Theta')
pylab.ylabel('f(theta)') 
pylab.title('f(theta) against theta')
pylab.savefig('Intgrand')
curdir = os.getcwd()
print 'Plot saved in : ', curdir