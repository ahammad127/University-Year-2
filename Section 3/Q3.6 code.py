from minimise import gmin
from numpy import exp
def f(x):
    y = exp(x) + 1/x
    return y
minimum = gmin(f, 0, 10, tol = 3.0e-8)
print minimum