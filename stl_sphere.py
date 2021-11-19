import numpy as np
from stl import mesh
from sphere import Sphere

def make_sphere(pt, radius, details=30):
    s = Sphere(pt, radius, details)
    faces = []
    v_top = s.top
    v_base = s.base

    for i in range(details):
        faces.append(np.array([v_top, s.circle_list[0].vertices[i], s.circle_list[0].vertices[(i+1)%details]]))
    
    for i in range(details):
        faces.append(np.array([v_base, s.circle_list[-1].vertices[i], s.circle_list[-1].vertices[(i+1)%details]]))
    
    if details > 3:
        for i in range(details-3):
            for j in range(details):
                faces.append([s.circle_list[i].vertices[j], s.circle_list[i].vertices[(j+1)%details], s.circle_list[i+1].vertices[j]])
                faces.append([s.circle_list[i].vertices[(j+1)%details], s.circle_list[i+1].vertices[j], s.circle_list[i+1].vertices[(j+1)%details]])

    f = np.array(faces)
    sphere = mesh.Mesh(np.zeros(f.shape[0], dtype=mesh.Mesh.dtype))
    for i in range(f.shape[0]):
        sphere.vectors[i] = faces[i]
    sphere.save('sphere.stl')

if __name__ == '__main__':
    make_sphere([0,0,0], 1)