from numpy import sin, pi, fabs, sqrt #Imports all functions we need
alpha = 0 #Starting value for alpha
r = [] #An empty list to have values of ratios appended to it
while alpha <= 2.0*pi: #Keep looping until alpha is greater than 2pi
    def f(phi):
        y = 1/sqrt(1-(sin(alpha/2)*sin(phi))**2)
        return y #This is the function for the integrand

    def trap0(f, a, b, n):
        '''Basic trapezium rule . Integrate f (x) over the
        interval from a to b using n strips.'''
        h = float(b - a)/n
        s = 0.5*(f(a) + f(b))
        for i in range (1 , n):
            s = s + f(a + i*h)
        return s*h
    
    def trap1(f, a, b, delta, maxtraps = 1024):
        '''Improved trapezium rule . Integrate f (x) over
        interval from a to b , trying to get relative accuracy
        delta . Optional last argument is maximum allowed
        number of trapezia.'''
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
    
    I = trap1(f, 0, pi/2, 1e-7, maxtraps = 1024) #I is the integral of the f() function
    ratio = I*2/pi #Now multiply by 2/pi to compute the ratio
    r.append(ratio) #Each successive value for the ratio is then appended to the list
    alpha = alpha + pi/3 #Changes initial alpha to the next alpha to get the ratio at different amplitudes

print "Amplitude", "Ratio"
print "0        ", r[0]
print "pi/3     ", r[1]
print "2pi/3    ", r[2]
print "pi       ", r[3]
print "4pi/3    ", r[4]
print "5pi/3    ", r[5]
print "2pi      ", r[6] #These lines print the amplitude and corresponding ratio in a table format