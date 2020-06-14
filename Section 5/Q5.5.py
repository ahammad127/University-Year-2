import pylab
from numpy import zeros, random, arange
import os #Imports the modules and functions required

m = zeros(10, float) 
n = zeros(10, float)
o = zeros(10, float)
p = zeros(10, float) #Sets up an array of zeros, but as floats instead of integers
for i in range(1000): #Iterates the code 1000 times - chooses 1000 random floatss from 0 - 1
    w = random.random() #Randomly generates a float between 0 and 1
    x = (w + random.random())/2
    y = (2*x + random.random())/3
    z = (3*y + random.random())/4 #Also produce random numbers, then take an average
    if 0.0 <= w and w < 0.1: m[0] = m[0] + 1
    if 0.1 <= w and w < 0.2: m[1] = m[1] + 1
    if 0.2 <= w and w < 0.3: m[2] = m[2] + 1
    if 0.3 <= w and w < 0.4: m[3] = m[3] + 1
    if 0.4 <= w and w < 0.5: m[4] = m[4] + 1
    if 0.5 <= w and w < 0.6: m[5] = m[5] + 1
    if 0.6 <= w and w < 0.7: m[6] = m[6] + 1
    if 0.7 <= w and w < 0.8: m[7] = m[7] + 1
    if 0.8 <= w and w < 0.9: m[8] = m[8] + 1
    if 0.9 <= w and w < 1.0: m[9] = m[9] + 1 
    if 0.0 <= x and x < 0.1: n[0] = n[0] + 1
    if 0.1 <= x and x < 0.2: n[1] = n[1] + 1
    if 0.2 <= x and x < 0.3: n[2] = n[2] + 1
    if 0.3 <= x and x < 0.4: n[3] = n[3] + 1
    if 0.4 <= x and x < 0.5: n[4] = n[4] + 1
    if 0.5 <= x and x < 0.6: n[5] = n[5] + 1
    if 0.6 <= x and x < 0.7: n[6] = n[6] + 1
    if 0.7 <= x and x < 0.8: n[7] = n[7] + 1
    if 0.8 <= x and x < 0.9: n[8] = n[8] + 1
    if 0.9 <= x and x < 1.0: n[9] = n[9] + 1
    if 0.0 <= y and y < 0.1: o[0] = o[0] + 1
    if 0.1 <= y and y < 0.2: o[1] = o[1] + 1
    if 0.2 <= y and y < 0.3: o[2] = o[2] + 1
    if 0.3 <= y and y < 0.4: o[3] = o[3] + 1
    if 0.4 <= y and y < 0.5: o[4] = o[4] + 1
    if 0.5 <= y and y < 0.6: o[5] = o[5] + 1
    if 0.6 <= y and y < 0.7: o[6] = o[6] + 1
    if 0.7 <= y and y < 0.8: o[7] = o[7] + 1
    if 0.8 <= y and y < 0.9: o[8] = o[8] + 1
    if 0.9 <= y and y < 1.0: o[9] = o[9] + 1 
    if 0.0 <= z and z < 0.1: p[0] = p[0] + 1
    if 0.1 <= z and z < 0.2: p[1] = p[1] + 1
    if 0.2 <= z and z < 0.3: p[2] = p[2] + 1
    if 0.3 <= z and z < 0.4: p[3] = p[3] + 1
    if 0.4 <= z and z < 0.5: p[4] = p[4] + 1
    if 0.5 <= z and z < 0.6: p[5] = p[5] + 1
    if 0.6 <= z and z < 0.7: p[6] = p[6] + 1
    if 0.7 <= z and z < 0.8: p[7] = p[7] + 1
    if 0.8 <= z and z < 0.9: p[8] = p[8] + 1
    if 0.9 <= z and z < 1.0: p[9] = p[9] + 1 #IF statements check which limits the float fits in and adds 1 to the value in the appropriate element in the array

pylab.subplot(2, 2, 1)
pylab.bar(arange(0, 1, 0.1), m, width = 0.1)
pylab.ylabel('Count')
pylab.subplot(2, 2, 2)
pylab.bar(arange(0, 1, 0.1), n, width = 0.1)
pylab.subplot(2, 2, 3)
pylab.bar(arange(0, 1, 0.1), o, width = 0.1)
pylab.xlabel('Bin Number')
pylab.ylabel('Count')
pylab.subplot(2, 2, 4)
pylab.bar(arange(0, 1, 0.1), p, width = 0.1)
pylab.xlabel('Bin Number')
'''Subplot() allows me to put more than one graph on one page while bar() plots
   each graph and the x/ylabel() puts a heading on the appropriate axis'''

pylab.savefig('Distributions of Averages.png') #Graph saved with the name in the brackets
curdir = os.getcwd() #Location of graph
print 'Plot saved in : ', curdir #Prints the location of the graph