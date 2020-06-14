from math import fabs
from numpy import zeros, arange

def sweep(v,p,q,r,s):
    a = 1
    for i in range(1,len(v)-1):
        for j in range(1,len(v)-1):
            c=0.0
            if i==p and j==q: c=1.0
            if i==r and j==s: c=-1.0
            v[i,j] = (v[i - 1, j] + v[i + 1, j] + v[i , j - 1] + v[i, j + 1] + c - a*v[i, j])/(4 - a)

N=22
v=zeros((N,N),float)
p=q=(len(v)-1)/2
r=s=p+1

dv=1.0e10
lastdv=0
count=0
while (fabs(dv-lastdv)>1.0e-7*fabs(dv)):
  lastdv=dv
  sweep(v,p,q,r,s)
  dv=v[p,q]-v[r,s]
  count+=1
  print count, dv