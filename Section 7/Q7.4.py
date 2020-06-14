from math import fabs
from numpy import zeros, arange, array
import pylab
import os

def sweep(v,p,q,r,s):
  for i in range(1,len(v)-1):
    for j in range(1,len(v)-1):
      c=0.0
      if i==p and j==q: c=1.0
      if i==r and j==s: c=-1.0
      v[i,j]=0.25*(v[i-1,j]+v[i+1,j]+v[i,j-1]+v[i,j+1]+c)

N=22
v=zeros((N,N),float)
p=q=1
s = q

r1 = []
r2 = []

for i in range(1, 21):
    r = p + i
    dv=1.0e10
    lastdv=0
    count=0
    while (fabs(dv-lastdv)>1.0e-7*fabs(dv)):
        lastdv=dv
        sweep(v,p,q,r,s)
        dv=v[p,q]-v[r,s]
        count+=1
    r1.append(dv)

for i in range(1, 21):
    r = p + i
    s = q + i
    dv=1.0e10
    lastdv=0
    count=0
    while (fabs(dv-lastdv)>1.0e-7*fabs(dv)):
        lastdv=dv
        sweep(v,p,q,r,s)
        dv=v[p,q]-v[r,s]
        count+=1
    r2.append(dv)
    
print r1
print r2
R1 = array(r1)
R2 = array(r2)
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
pylab.plot(x, R1, label = 'Parallel')
pylab.plot(x, R2, linestyle = "--", label = 'Diagonal')
pylab.legend(loc='upper right')
pylab.xlabel("'Distance' between nodes (Arbitrary units)")
pylab.ylabel("Resistance (Ohms)")
pylab.title("Resistance against distance between nodes")
pylab.savefig("Resistance graph for Q4.png")
curdir = os.getcwd()
print 'Plot saved in: ', curdir