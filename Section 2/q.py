import numpy
import pylab
import math as m
Rinf = 1051.24921973
r =100.0
s =10000.0
n=50
a=[r+s]
for i in range (n-1):
    a.append(r+s*a[-1]/(s+a[-1]))

a = numpy.asarray(a)
print a
a = a - Rinf
print a

b = numpy.array([])

for i in a:
    b = numpy.append(b, m.log(i))

pylab.plot(b)