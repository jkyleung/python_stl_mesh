import numpy as np
from stl import mesh
from cylinder import Cylinder

def make_cylinder(pt1, pt2, radius, details=50):
    c = Cylinder(pt1, pt2, radius, details)
    faces = []
    v_base = c.base_circle.vertices
    for i in range(details):
        faces.append(np.array([c.base_circle.center, v_base[i], v_base[(i+1)%details]]))
    v_top = c.top_circle.vertices
    for i in range(details):
        faces.append([c.top_circle.center, v_top[i], v_top[(i+1)%details]])

    for i in range(details):
        faces.append([v_base[i], v_base[(i+1)%details], v_top[i]])
        faces.append([v_base[(i+1)%details], v_top[(i+1)%details], v_top[i]])

    f = np.array(faces)
    cylinder = mesh.Mesh(np.zeros(f.shape[0], dtype=mesh.Mesh.dtype))
    for i in range(f.shape[0]):
        cylinder.vectors[i] = faces[i]
    cylinder.save('cylinder.stl')

if __name__ == '__main__':
    make_cylinder([0,0,0], [1,1,1], 1)