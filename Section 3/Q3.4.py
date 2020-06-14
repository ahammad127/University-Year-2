from math import sqrt
from numpy import array
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
dn = array(dn) #lines 1 to 14 serve the same purpose as lines 1 to 19 in the code in Q3.1 

E = 1212.5
nE = 4208.6 #Real values of E and n(E) close to the peak
const = 14670000.0
w =  2*sqrt((const/nE) - (E - 1232)**2) #Calculation to determine w

def theoretical(thn):
    for i in range(0, 22):
        a = const/(((w/2)**2) + (ea[i] - 1232)**2)
        thn.append(a)
    thn = array(thn)
    return thn #This function produces an array of the theoretical values for n(E)

thn = [] #Empty list to have theoretical values appended to it
th = theoretical(thn) #Array of the theoretical values

def discrepancy(a, b):
    x = (a/(b))
    y = x**2
    z = sum(y)
    return z #Function to calculate discrepancy

r = na - th #Calculation to determine the residuals
d = discrepancy(r, dn) #Value for discrepancy determined
print d