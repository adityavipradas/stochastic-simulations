"""
Created on Thu Feb 14 22:41:19 2013

@author: adityavipradas
"""
import time
start = time.time()
import random
import math
import matplotlib.pyplot as plt

def estimate_pi(points, radius):
    x = []
    y = []
    circle = 0.0
    square = 0.0
    for i in xrange(points):
        x.append(round(random.uniform(0, radius), 2))
        y.append(round(random.uniform(0, radius), 2))
        dist = math.sqrt((x[i]**2) + (y[i]**2))
        if (dist <= radius):
            circle = circle + 1
        square = square + 1
    #print "Value of pi for", points, "points is: ", 4*(circle/square)
    return 4*(circle/square)

def plot(points, radius, trials):
    val = []
    pt = []
    pi = []
    for i in xrange(trials):
        value = estimate_pi(points, radius)
        val.append(value)
        pt.append(points)
        pi.append(math.pi)
        points = points + 100
    plt.plot(pt, pi)
    plt.scatter(pt, val)
    plt.title("pi estimate")
    plt.xlabel("number of points")
    plt.ylabel("pi value")
    print "Execution time: ", time.time() - start, "seconds"
    plt.show()

plot(1000, 3, 200)
