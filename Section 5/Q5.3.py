from numpy import zeros, random
import pylab
import os #Import all the modules and functions that I need 

m = zeros(10, int) #Sets up an array of integer zeros
for i in range(1000): #Iterates the code 1000 times - randomly generates 1000 numbers from 0-9
    n = random.randint(10) #Randomly generates a number between 0 and 9
    m[n] = m[n] + 1 #Adds 1 to the value in the randomly generated element
print m #Prints the array full of values of the count of each bin

pylab.bar(range(10), m, width = 0.9, align = 'center') #Plots the bars
pylab.xticks(range(10)) #Shows all the numbers between 0 and 9 on the x axis

pylab.xlabel('Bin Number')
pylab.ylabel('Count') #Axis labels

pylab.title('Count of each Bin Number') #Title of graph

pylab.savefig('Count against Bin Number.png') #Graph saved with the name in the brackets
curdir = os.getcwd() #Location of graph
print 'Plot saved in : ', curdir #Prints the location of the graph