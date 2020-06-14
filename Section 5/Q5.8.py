from numpy import random #Import required module
s = 0.0 #Sets the beginning sum to zero
for i in range(1000): #Iterates the code 1000 times to get a mean over a large number
    x = random.poisson(15) #Generates a random number around a mean of 15
    s = s + x #Adds each random number together
print s/1000 #Calculates the average random number