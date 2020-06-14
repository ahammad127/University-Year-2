import pylab
from numpy import array
import os

n = array([7.0, 12.0, 17.0, 22.0])
n2 = n**2
x = 1/n2
y1 = array([0.482964218066, 0.495400564657, 0.497829971704, 0.498752996303])
y2 = array([0.603292512873, 0.627517778894, 0.632302019212, 0.634135159455])
pylab.plot(x, y1, linestyle = "none", marker = "o", label='A-B')
pylab.plot(x, y2, linestyle = "none", marker = "o", label='A-C')
pylab.legend(loc='upper right')
pylab.xlabel("1/N^2")
pylab.ylabel("Resistance (Ohms)")
pylab.title("Resistance against 1/N^2")

pylab.savefig("Resistance graph for Q2.png")
curdir = os.getcwd()
print 'Plot saved in: ', curdir