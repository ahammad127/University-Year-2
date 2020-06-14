from numpy import pi, fabs, exp
def f(x):
    y = (1/(2*pi)**0.5)*exp((-x**2)/2)
    return y
def trap0(f, a, b, n):
    h = float(b - a)/n
    s = 0.5*(f(a) + f(b))
    for i in range (1 , n):
        s = s + f(a + i*h)
    return s*h
def trap1(f, a, b, delta, maxtraps = 9000):
    n = 10
    inew = trap0(f, a, b, n)
    iold = -inew
    while(fabs(inew - iold) > delta*fabs(inew)):
        iold = inew
        n = 2*n
        if n > maxtraps:
            print "Cannot reach requested accuracy with", \
            maxtraps, " trapezia"
            return
        inew = trap0(f, a, b, n)
    return inew
r = trap1(f, -2, 2, 1e-7)
p = 1 - r
print r
print p