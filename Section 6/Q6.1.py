def f(y, t):
    return -y + 1.0
def odestep(f, y, t, dt):
    return y + dt*f(y, t)
t = 0; y = 0; dt = 0.1
tf = 2.0; nsteps = int(tf/dt)
print t, y
for i in range(nsteps):
    y = odestep(f, y, t, dt)
    t = (i + 1)*dt
    print t, y