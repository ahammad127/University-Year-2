def discrepancy(w):
    th=[]
    for i in range(len(ea)):
        th.append(theory(ea[i], w))
    th= array(th)
    ri = na- th
    weighted_ri= ri/ dn
    weighted_ri_sq= weighted_ri**2
    discrep= sum(weighted_ri_sq)
    return discrep

from minimise import gmin
from numpy import exp

def func(x):
    y= exp(x) + 1.0/x
    return y

gmin = gmin(discrepancy, 110.0, 115.0)
w_acc= gmin[0]
print w_acc