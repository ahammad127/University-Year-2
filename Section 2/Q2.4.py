r = 100.0
s = 10000.0 #Define r and s
rn = r #Make a new term so that r can stay constant but rn can change with iterations
rn2 = r + s*rn/(s+rn) #Get the first value of rn2 using the formula
while rn2 != rn:
    rn = rn2
    rn2 = r + s*rn/(s+rn)
    print rn, rn2    #While loop keeps iterating the formula until the constant value is found
print "When n = infinity, R = ", rn2 #prints the constant