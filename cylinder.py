from circle import Circle
import numpy as np
from stl import mesh
import math

import matplotlib.pyplot as plt

# define cylinder by 2 pts
class Cylinder():
    def __init__(self, center1=[0,0,0], center2=[0,0,1], radius=1, details=10):
        self.base_circle = Circle(center1, radius, details)
        self.top_circle = Circle(center2, radius, details)
        # by Pyth. thm. 
        self.height = math.sqrt(math.pow(center1[0]-center2[0],2) + math.pow(center1[1]-center2[1],2) + math.pow(center1[2]-center2[2],2))
        # rotate the circles to match the shapes of cylinder (when two center is not on the z-axis)
        # a_angle = math.atan((center2[0]-center1[0])/(center2[2]-center1[2]))   # x/z
        # b_angle = math.atan((center2[1]-center1[1])/math.sqrt(math.pow(center1[0]-center2[0],2) + math.pow(center1[2]-center2[2],2)))   # y/sqrt(x^2+z^2)
        angle = math.atan(math.sqrt(math.pow(center1[0]-center2[0],2) + math.pow(center1[2]-center2[2],2))/(center2[2]-center1[2]))

        # Rodrigues rotation matrix
        # unit vector: vector parallel to intersection of two planes
        v = np.array(center2) - np.array(center1)
        n = [0,0,1]
        unit_v = np.cross(v, n)
        unit_v = unit_v / (math.sqrt(math.pow(unit_v[0],2)+math.pow(unit_v[1],2)+math.pow(unit_v[2],2)))
        W = np.array([[0, -unit_v[2], unit_v[1]],
                    [unit_v[2], 0, -unit_v[0]],
                    [-unit_v[1], unit_v[0], 0]])
        # rotation matrix
        R = np.array(np.array([[1,0,0],[0,1,0],[0,0,1]]) + W * math.sin(angle) + np.dot(W, W) * (1 - math.cos(angle)))

        # base circle
        self.base_circle.vertices = self.base_circle.vertices - np.array(self.base_circle.center)
        self.base_circle.vertices = np.dot(self.base_circle.vertices, R)
        self.base_circle.vertices = self.base_circle.vertices + np.array(self.base_circle.center)
        # top circle
        self.top_circle.vertices = self.top_circle.vertices - np.array(self.top_circle.center)
        self.top_circle.vertices = np.dot(self.top_circle.vertices, R)
        self.top_circle.vertices = self.top_circle.vertices + np.array(self.top_circle.center)


        '''
        # rotate along with y-axis
        R = np.array([[math.cos(a_angle), 0, -math.sin(a_angle)],
                        [0, 1, 0],
                        [math.sin(a_angle), 0, math.cos(a_angle)]])
        # base circle
        self.base_circle.vertices = self.base_circle.vertices - np.array(self.base_circle.center)
        self.base_circle.vertices = np.dot(self.base_circle.vertices, R)
        self.base_circle.vertices = self.base_circle.vertices + np.array(self.base_circle.center)
        # top circle
        self.top_circle.vertices = self.top_circle.vertices - np.array(self.top_circle.center)
        self.top_circle.vertices = np.dot(self.top_circle.vertices, R)
        self.top_circle.vertices = self.top_circle.vertices + np.array(self.top_circle.center)
        
        # rotate along with x-axis
        R = np.array([[1, 0, 0],
                        [0, math.cos(b_angle), -math.sin(b_angle)],
                        [0, math.sin(b_angle), math.cos(b_angle)]])
        # base circle
        self.base_circle.vertices = self.base_circle.vertices - np.array(self.base_circle.center)
        self.base_circle.vertices = np.dot(self.base_circle.vertices, R)
        self.base_circle.vertices = self.base_circle.vertices + np.array(self.base_circle.center)
        # top circle
        self.top_circle.vertices = self.top_circle.vertices - np.array(self.top_circle.center)
        self.top_circle.vertices = np.dot(self.top_circle.vertices, R)
        self.top_circle.vertices = self.top_circle.vertices + np.array(self.top_circle.center)
        '''

# define cylinder by height
# class Cylinder_h(Cylinder):
