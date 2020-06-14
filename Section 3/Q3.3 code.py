from math import sqrt
from numpy import array, arange
import pylab
E = 1212.5
nE = 4208.6
const = 14670000.0
w = 2*sqrt((const/nE) - (E - 1232)**2)
f = open('data1.txt', 'r')
ea = []; na = []; dn = []
for line in f:
    estr, nstr, errstr = line.split()
    ea.append(float(estr))
    na.append(float(nstr))
    dn.append(float(errstr))
f.close()
ea = array(ea)
na = array(na)
dn = array(dn)
thn = []
for i in range(0, 22):
    th = const/(((w/2)**2) + (ea[i] - 1232)**2)
    thn.append(th)
ea = array(ea)
thn = array(thn)
pylab.errorbar(ea,na,dn)
pylab.plot(ea, na, 'ro', linestyle = 'None', markersize = 3)
pylab.plot(ea, thn, 'go', linestyle = 'solid', markersize = 0)
pylab.xlabel('E')
pylab.ylabel('n(E)')
pylab.title('n(E) against E')
pylab.show()
print 'w = ', w