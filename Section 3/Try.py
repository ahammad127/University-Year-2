from numpy import array, arange, cos, exp, pi
import pylab
'''f = open('data1.txt', 'r')
ea = []; na = []; dn = []
for line in f:
    estr, nstr, errstr = line.split()
    ea.append(float(estr))
    na.append(float(nstr))
    dn.append(float(errstr))
f.close()
ea = array(ea)
na = array(na)
dn = array(dn)'''
x = arange(0 ,8* pi ,0.05* pi)
pylab.plot(x, cos(x))
pylab.plot(x, cos(x)*exp(-x/20.0))
pylab.xlabel('x')
pylab.title('Oscillation and damped oscillation')
pylab.show()