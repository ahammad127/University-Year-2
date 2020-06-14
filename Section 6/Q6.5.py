def f(y, t):
    return -y + 1.0 #Function to calculate the slope at a point
def odestep(f, y, t, dt):
    '''Uses slope at A to calculate B' (denoted as Bp), then calculates slope at B', 
       then takes the average of the slopes to use as the linear slope to calculate 
       B from A'''
    Aslope = f(y,t)
    Bp = y + Aslope*dt
    Bpslope = f(Bp, t)
    B  = y + 0.5*dt*(Aslope + Bpslope)
    return B
a = []; b = []
t = 0; y = 0; dt = 0.2 #Initial values of y and t (voltage and time), dt is the time interval
tf = 2.0; nsteps = int(tf/dt) #tf is the range of time, nsteps is the number of steps
print t, y #Prints initial t and y
for i in range(nsteps):
    '''Calculates a value for B from A, sets the new A to be this value of B
       for each iteration. It also sets each new value of time to be the 
       the initial time + time interval and prints these values. It iterates
       the code as many times as there are steps.'''
    y = odestep(f, y, t, dt)
    t = (i + 1)*dt
    a.append(y)
    print t, y 

dt2 = dt/2
nsteps2 = int(tf/dt2)
t = 0; y = 0
for i in range(nsteps2):
    '''Calculates a value for B from A, sets the new A to be this value of B
       for each iteration. It also sets each new value of time to be the 
       the initial time + time interval and prints these values. It iterates
       the code as many times as there are steps.'''
    y = odestep(f, y, t, dt2)
    t = (i + 1)*dt2
    b.append(y)
    print t, y 
while (b[nsteps2 - 1] - a[nsteps - 1])/a[nsteps - 1] > 0.000001:
    a = []; b = []
    dt2 = dt2/2
    dt = dt/2
    nsteps2 = int(tf/dt2)
    nsteps = int(tf/dt)
    t = 0; y = 0
    tf = 2.0; nsteps = int(tf/dt) #tf is the range of time, nsteps is the number of steps
    print t, y #Prints initial t and y
    for i in range(nsteps):
        '''Calculates a value for B from A, sets the new A to be this value of B
           for each iteration. It also sets each new value of time to be the 
           the initial time + time interval and prints these values. It iterates
           the code as many times as there are steps.'''
        y = odestep(f, y, t, dt)
        t = (i + 1)*dt
        a.append(y)
        print t, y 
    t = 0; y = 0
    for i in range(nsteps2):
        '''Calculates a value for B from A, sets the new A to be this value of B
           for each iteration. It also sets each new value of time to be the 
           the initial time + time interval and prints these values. It iterates
           the code as many times as there are steps.'''
        y = odestep(f, y, t, dt2)
        t = (i + 1)*dt2
        b.append(y)
        print t, y 
print ""
print a[nsteps - 1], a[int((nsteps - 1)/2)]
print b[nsteps2 - 1], b[int((nsteps2 - 1)/2)]
print dt2