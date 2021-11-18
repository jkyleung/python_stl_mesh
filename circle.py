import numpy as np
from stl import mesh
import math

import matplotlib.pyplot as plt

class Circle():
    def __init__(self, center=[0,0,0], radius=1, details=10):
        self.center = center
        self.radius = radius
        self.details = details
        self.vertices = []
        
        angle = math.pi * 2 / details
        temp_pt = [radius, 0, 0]

        for i in range(details):
            # rotation matrix
            R = np.array([[math.cos(angle*i), math.sin(angle*i), 0],
                        [-math.sin(angle*i), math.cos(angle*i), 0],
                        [0, 0, 1]])
            self.vertices.append(np.dot(temp_pt, R)+center)
    