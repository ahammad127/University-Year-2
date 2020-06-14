from numpy import cos, array
import pylab
import os
y1 = []; y2 = []; y3 = []; g1 = []; g2 = []; g3 = []; t1 = [] 
def f(y, t):
    return -y + cos(w*t)
def odestep(f, y, t, dt):
    Aslope = f(y,t)
    Bp = y + Aslope*dt
    Bpslope = f(Bp, t)
    B  = y + 0.5*dt*(Aslope + Bpslope)
    return B

t = 0; y = 1; dt = 0.0015625
tf = 20.0; nsteps = int(tf/dt)
w = 0.5
for i in range(nsteps):
    y = odestep(f, y, t, dt)
    t = (i + 1)*dt
    y1.append(y)
    g1.append(cos(w*t))
    t1.append(t)
w = 1.0
t = 0; y = 1
for i in range(nsteps):
    y = odestep(f, y, t, dt)
    t = (i + 1)*dt
    y2.append(y)
    g2.append(cos(w*t))
w = 2.0
t = 0; y = 1
for i in range(nsteps):
    y = odestep(f, y, t, dt)
    t = (i + 1)*dt
    y3.append(y)
    g3.append(cos(w*t))

y1 = array(y1)
y2 = array(y2)
y3 = array(y3)
g1 = array(g1)
g2 = array(g2)
g3 = array(g3)
t1 = array(t1)    
    
pylab.subplot(3, 1, 1)
pylab.plot(t1, y1)
pylab.plot(t1, g1)
pylab.ylabel('Voltage')
pylab.xlabel('t')
pylab.title ('Input (orange) and Output (blue) voltages against time')

pylab.subplot(3, 1, 2)
pylab.plot(t1, y2)
pylab.plot(t1, g2)
pylab.ylabel('Voltage')
pylab.xlabel('t')
pylab.title ('Input (orange) and Output (blue) voltages against time')

pylab.subplot(3, 1, 3)
pylab.plot(t1, y3)
pylab.plot(t1, g3)
pylab.ylabel('Voltage')
pylab.xlabel('t')
pylab.title ('Input (orange) and Output (blue) voltages against time')
pylab.subplots_adjust(hspace = 1.0)
pylab.savefig('Input and Output Voltages 2')
curdir = os.getcwd()
print 'Plot saved in: ', curdir