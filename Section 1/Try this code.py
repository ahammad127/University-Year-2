from math import sqrt
def a(x):
    return x - sqrt (x*x - 1)
def b(x):
    return 1/(x + sqrt (x*x - 1))
print a(100), b(100)
'''for x in range (150000, 150010):
    print x, a(x), b(x)'''
