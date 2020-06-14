from math import cos, fabs, pi
import numpy
import os, pylab

x = numpy.arange(0, 4.01*pi, 0.01*pi) #Array of numbers between 0 and 4pi in intervals of 0.01pi

def g(x):
    n = 1; total = term = cos(x) # First term
    while fabs(term) > (1.0e-7*fabs(total)+1.0e-13):
            n += 2 # Advance to next term
            term = cos(n*x)/(n*n)
            total += term # Add term to total
    return total

y = numpy.array([]) #Empty array

for i in x:
    y = numpy.append(y, g(i)) #Appends g() function applied to each number in x to y

pylab.plot(x, y) #Forms the graph

pylab.xlabel('x')
pylab.ylabel('g(x)') #x-axis and y-axis headings

pylab.title('g(x) against x') #Graph title

pylab.savefig('Fourier Series.png') #Name of saved graph

curdir = os.getcwd() #Location of saved graph

print 'Plot saved in : ', curdir