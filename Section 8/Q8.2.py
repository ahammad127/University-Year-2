from numpy import random #Import the required function

a = 1.7
b = 21.0 
R = (2.0*a*b)**0.5
L = 20
fiscount = 0 #Count of secondary fissions
'''Set the variables as given, but I set my own value of L'''

def neutrons():
    """Number of secondary neutrons produced in each fission.
    Returns an integer number of neutrons, with average 2.5."""
    i=int(random.normal()+3.0)
    if (i<0): return 0
    else: return i
    
for i in range(100):
    x = L*random.random(1) #Position of initial fission
    k = neutrons() #Number of neutrons produced from initial fission
    for j in range(k): #Iterates as many times for as many neutrons produced
        d = random.random(1) #Direction variable
        if d > 0.5:
            y = x + R #Neutron's position moved right
        else:
            y = x - R ##Neutron's position moved left
        if 0.0 <= y <= L:
            fiscount += 1 #Counts the number of secondary fissions
'''First loop represents the 100 initial fissions releasing k neutrons (secondary loop). 
   This loop moves each neutron to its new position - if it is still in the Uranium 
   we assume it causes a secondary fission.'''
print fiscount #Prints the number of secondary fissions