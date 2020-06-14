from numpy import abs
def f(x):
   y = ((x**4)*(1-x)**4)/(1+x**2)
   return y

def trap0(f, a, b, n):
    h = float(b - a)/n
    s = 0.5*(f(a) + f(b))
    for i in range (1 , n):
        s = s + f(a + i*h)
    return s*h
n = 1

a = trap0(f, 0, 1, n)
b = trap0(f, 0, 1, n + 1)

while abs(b-a)/a > 0.000001:
    n = n + 1
    a = trap0(f, 0, 1, n)
    b = trap0(f, 0, 1, n + 1)
    print n
    print a