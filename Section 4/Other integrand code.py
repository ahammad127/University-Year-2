from numpy import sin, pi, arange
import pylab
def f(phi):
    y = 1/(1-(sin(pi/8)*sin(phi))**2)**0.5
    return y
phi = arange(-10, 10, 0.001)
y = f(phi)
pylab.plot(phi, y)
pylab.xlabel('Phi')
pylab.ylabel('f(phi)') 
pylab.title('f(phi) against phi')