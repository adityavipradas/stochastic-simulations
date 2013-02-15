"""
Created on Sun Jan 20 00:43:19 2013

@author: adityavipradas
"""

"""Bisection Method for locating a local minima of a function in a specified closed interval
Function in the closed interval is continuous and unimodal"""

"""import libraries"""
import math

"""define function"""
"""change the function as per requirement"""
def equation(x):
    y = (x+1)*(x+3)*(x)
    return y

"""accept inputs"""  
a = 3
b = 7
ak = a
bk = b
e = 1
iter = 0

"""solve"""
try:
    while (math.fabs(b - a)>(e/100.)):
        
        """increment the iteration count"""
        iter = iter + 1
        
        """calculate the values of new points x1 and x2"""
        x1 = ((a + b)/2.) - ((b - a)/4)
        x2 = ((a + b)/2.) + ((b - a)/4)
        
        """evaluate the values of function at x1 and x2"""
        f1 = equation(x1)
        f2 = equation(x2)
        
        """eliminate the undesired region"""
        if (f1 < f2):
            b = x2
        elif (f2 < f1):
            a = x1

    """store the minima value in xstar"""
    if (f1 < f2):
        xstar = x1
    else:
        xstar = x2
except:
    print "Unable to locate minima"
