import os
import trimesh

mesh = trimesh.load('obj_files/chair_001_24.obj')
print(mesh.vertices)