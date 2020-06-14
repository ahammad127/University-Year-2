from math import sqrt
from numpy import array, arange
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
def theoretical(thn):
    for i in range(0, 22):
        a = const/(((w/2)**2) + (ea[i] - 1232)**2)
        thn.append(a)
    thn = array(thn)
    return thn
th = theoretical(thn)
r = na - th
print r
def discrepancy(a, b):
    x = (a/(b))
    y = x**2
    z = sum(y)
    return z
d = discrepancy(r, dn)
print d