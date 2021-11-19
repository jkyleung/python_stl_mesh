from circle import Circle
from cylinder import Cylinder
from sphere import Sphere
import numpy as np
from stl import mesh
import math

import matplotlib.pyplot as plt

if __name__ == '__main__':
    '''
    c = Circle(details=50)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    v = np.transpose(c.vertices)
    ax.scatter(v[0],v[1],v[2])
    plt.show()
    '''
    '''
    c = Cylinder([0,0,0],[1,1,1],details=50)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    v = np.concatenate((np.transpose(c.base_circle.vertices), np.transpose(c.top_circle.vertices)), axis=1)
    ax.scatter(v[0],v[1],v[2])
    ax.set_xlim3d(-1, 2)
    ax.set_ylim3d(-1, 2)
    ax.set_zlim3d(-1, 2)
    plt.show()
    '''
    s = Sphere([0,0,0],1,details=30)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    v = np.concatenate((np.transpose([s.top]), np.transpose(s.vertices), np.transpose([s.base])), axis=1)
    ax.scatter(v[0],v[1],v[2])
    ax.set_xlim3d(-2, 2)
    ax.set_ylim3d(-2, 2)
    ax.set_zlim3d(-1.5, 1.5)
    plt.show()