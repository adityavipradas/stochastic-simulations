from __future__ import division
"""
Created on Fri Feb 15 10:52:18 2013

@author: adityavipradas
"""
import random
import sympy
import bimin
import bimax
import matplotlib.pyplot as plt

def estimate_integral(points):
    x,y = [],[]
    plotx,ploty = [],[]
    func,domain = 0.0, 0.0
    area = (bimin.bk-bimin.ak)*(bimax.equation(bimax.xstar) - bimin.equation(bimin.xstar))
    for i in xrange(points):
        x.append(random.uniform(bimin.ak, bimin.bk))
        y.append(random.uniform(bimin.equation(bimin.xstar), bimax.equation(bimax.xstar)))        
        if (y[i] >= bimin.equation(x[i])):
            func = func + 1
        domain = domain + 1
    print "Estimated integral: ",area*(func/domain)
    z = sympy.Symbol('z')
    print "Actual integral: ", float(bimin.equation(z).integrate((z, 3, 7)))
    for i in range(bimin.ak*10, bimin.bk*10, 1):
        plotx.append(i/10)
        ploty.append(bimin.equation(i/10))
    plt.scatter(x,y)
    plt.plot(plotx, ploty,'red')
    plt
    plt.show()  

estimate_integral(10000)
