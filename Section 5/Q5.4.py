import pylab
from numpy import zeros, random, arange
import os #Imports the modules and functions required

m = zeros(10, float) #Sets up an array of zeros, but as floats instead of integers
for i in range(1000): #Iterates the code 1000 times - chooses 1000 random floatss from 0 - 1
    x = random.random() #Randomly generates a float between 0 and 1
    if 0.0 <= x and x < 0.1: m[0]= m[0] + 1
    if 0.1 <= x and x < 0.2: m[1]= m[1] + 1
    if 0.2 <= x and x < 0.3: m[2]= m[2] + 1
    if 0.3 <= x and x < 0.4: m[3]= m[3] + 1
    if 0.4 <= x and x < 0.5: m[4]= m[4] + 1
    if 0.5 <= x and x < 0.6: m[5]= m[5] + 1
    if 0.6 <= x and x < 0.7: m[6]= m[6] + 1
    if 0.7 <= x and x < 0.8: m[7]= m[7] + 1
    if 0.8 <= x and x < 0.9: m[8]= m[8] + 1
    if 0.9 <= x and x < 1.0: m[9]= m[9] + 1 #IF statements check which limits the float fits in and adds 1 to the value in the appropriate element in the array

print m #Prints the array full of values of the count of each bin

pylab.bar(arange(0, 1, 0.1), m, width = 0.1) #Plots the bars

pylab.xlabel('Bin Number')
pylab.ylabel('Count') #Axis labels

pylab.title('Count of each Bin Number') #Title of graph

pylab.savefig('Distribution.png') #Graph saved with the name in the brackets
curdir = os.getcwd() #Location of graph
print 'Plot saved in : ', curdir #Prints the location of the graph