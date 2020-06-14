from numpy import zeros, random, arange
import pylab
import os #Import all the modules and functions that I need 

m = zeros(25, int)
n = zeros(25, int)
o = zeros(25, int)
p = zeros(25, int) #Sets up an array of integer zeros
for i in range(1000): #Iterates the code 1000 times - randomly generates 1000 numbers from 0-9
    a = random.poisson(2) #Randomly generates a number between 0 and 9
    m[a] = m[a] + 1 #Adds 1 to the value in the randomly generated element
    b = random.poisson(4) #Randomly generates a number between 0 and 9
    n[b] = n[b] + 1 #Adds 1 to the value in the randomly generated element
    c = random.poisson(6) #Randomly generates a number between 0 and 9
    o[c] = o[c] + 1 #Adds 1 to the value in the randomly generated element
    d = random.poisson(8) #Randomly generates a number between 0 and 9
    p[d] = p[d] + 1 #Adds 1 to the value in the randomly generated element
print m #Prints the array full of values of the count of each bin

pylab.subplot(2, 2, 1)
pylab.bar(arange(0, 25), m, width = 1)
pylab.ylabel('Count')
pylab.subplot(2, 2, 2)
pylab.bar(arange(0, 25), n, width = 1)
pylab.subplot(2, 2, 3)
pylab.bar(arange(0, 25), o, width = 1)
pylab.xlabel('Bin Number')
pylab.ylabel('Count')
pylab.subplot(2, 2, 4)
pylab.bar(arange(0, 25), p, width = 1)
pylab.xlabel('Bin Number')
'''Subplot() allows me to put more than one graph on one page while bar() plots
   each graph and the x/ylabel() puts a heading on the appropriate axis'''

pylab.savefig('Poisson Distributions.png') #Graph saved with the name in the brackets
curdir = os.getcwd() #Location of graph
print 'Plot saved in : ', curdir #Prints the location of the graph