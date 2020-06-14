from numpy import array
import pylab
import os #Import the modules and functions that I need

f = open('data1.txt', 'r') #Opens the data file to read it
ea = []; na = []; dn = [] #Empty listss which will have data and uncertainties appended to them

for line in f: #Runs the code in the loop for each line in the data file
    estr, nstr, errstr = line.split() #Splits each line of the file into the separate corresponding data points and uncertainties
    
    ea.append(float(estr))
    na.append(float(nstr))
    dn.append(float(errstr)) #Append data points to empty arrays
    
f.close() #Closes the data file now that it isn't needed anymore

ea = array(ea)
na = array(na)
dn = array(dn) #Convert the lists into arrays

pylab.errorbar(ea,na,dn) #Produces Error bars
pylab.plot(ea, na, 'ro', linestyle = 'None', markersize = 3) #Plots the data

pylab.xlabel('E')
pylab.ylabel('n(E)') #Label the axis
pylab.grid()

pylab.title('n(E) against E') #Gives the graph a title
pylab.savefig('pylabplot.png') #Saves the graph as a png file
curdir = os.getcwd() #Location of graph file 
print 'Plot saved in : ', curdir