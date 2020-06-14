from numpy import sin, pi, fabs, sqrt
def f(phi):
    y = 1.0/sqrt(1.0-(sin(pi/4.0)*sin(phi))**2.0)
    return y
def trap0(f, a, b, n):
    h = float(b - a)/n
    s = 0.5*(f(a) + f(b))
    for i in range (1 , n):
        s = s + f(a + i*h)
    return s*h
def trap1(f, a, b, delta, maxtraps = 1024):
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
r = 2*trap1(f, 0, pi/2.0, 1e-7)/pi
print r