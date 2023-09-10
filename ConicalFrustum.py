import open3d as o3d
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

model_path = 'model1.stl'
mesh = o3d.io.read_triangle_mesh(model_path)

pointcloud = mesh.sample_points_poisson_disk(number_of_points=70000)

points = np.asarray(pointcloud.points)

x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

print(z[np.argsort(z)])
