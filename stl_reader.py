import numpy as np
from stl import mesh
import math

# load the mesh from stl file
mesh_model = mesh.Mesh.from_file('cube.stl')

# value of the mesh: vectors
print(mesh_model.vectors)

# rotate with ref. axis and degree
degree = 45
ref_axis = [0,1,0]
mesh_model.rotate(ref_axis, math.radians(degree))
mesh_model.rotate([1,0,0], math.radians(degree))
print('----------')
print(mesh_model.vectors)

mesh_model.save('new_cube.stl')