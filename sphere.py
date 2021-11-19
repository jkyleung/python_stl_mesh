from circle import Circle
import numpy as np
from stl import mesh
import math

class Sphere():
    def __init__(self, center=[0,0,0], radius=1, details=20):
        if details < 3:
            details = 3
            print("Warning: details < 3, cannot initialize sphere, set details to 3")
        self.center = center
        self.radius = radius
        self.top = np.array(center) + np.array([0,0,radius])
        self.base = np.array(center) - np.array([0,0,radius])
        self.circle_list = []
        # self.vertices = []
        step = radius * 2 / (details - 1)
        for i in range(details - 2):
            temp_center = [self.center[0],self.center[1],self.top[2]-((i+1)*step)]
            temp_height = (i+1)*step if (i+1)*step < self.radius else 2 * self.radius - (i+1)*step
            temp_height = self.radius - temp_height
            temp_radius = math.sqrt(math.pow(self.radius,2) - math.pow(temp_height,2))
            self.circle_list.append(Circle(temp_center, temp_radius, details))
            # self.vertices.append(self.circle_list[i].vertices)
        # self.vertices = np.array(self.vertices).reshape(-1,3)