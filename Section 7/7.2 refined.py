from math import fabs
from numpy import zeros, arange
import pylab

def sweep(v,p,q,r,s):
  for i in range(1,len(v)-1):
    for j in range(1,len(v)-1):
      c=0.0
      if i==p and j==q: c=1.0
      if i==r and j==s: c=-1.0
      v[i,j]=0.25*(v[i-1,j]+v[i+1,j]+v[i,j-1]+v[i,j+1]+c)

P = 40
N = arange(4, P, 1.0)
dv1 = zeros(len(N))
dv2 = zeros(len(N))

i = 0
while i < (P-4):
    lastdv = -1
    count = 0
    v = zeros((int(N[i]), int(N[i])), float)
    p = q = (len(v) - 1)/2
    r = s = p + 1
    while (fabs(dv1[i] - lastdv)>1.0e-7*fabs(dv1[i])):
        lastdv = dv1[i]
        sweep(v,p,q,r,s)
        dv1[i] = v[p, q] - v[r, s]
        count += 1
    i += 1

i = 0
while i < (P-4):
    lastdv = -1
    count = 0
    v = zeros((int(N[i]), int(N[i])), float)
    p = q = (len(v) - 1)/2
    r = p + 1
    s = q
    while (fabs(dv2[i] - lastdv)>1.0e-7*fabs(dv2[i])):
        lastdv = dv2[i]
        sweep(v,p,q,r,s)
        dv2[i] = v[p, q] - v[r, s]
        count += 1
    i += 1
print dv1
print dv2

pylab.plot((1/(N**2)), dv1, linestyle = "none", marker = "o")
pylab.plot((1/(N**2)), dv2, linestyle = "none", marker = "o")