import trimesh
import numpy as np
import pandas as pd
from scipy.interpolate import Rbf
import matplotlib.pyplot as plt

from scipy.interpolate import griddata
from scipy.interpolate import interp2d
from scipy.interpolate import CloughTocher2DInterpolator


mesh = trimesh.load_mesh('Surf.stl')

# num_points = 1000000
# point_cloud, _ = trimesh.sample.sample_surface_even(mesh, num_points)
# x = []
# y = []
# z = []
#
#
# for point in point_cloud:
#     x.append(point[0])
#     y.append(point[1])
#     z.append(point[2])
# x = np.array(x)
# y = np.array(y)
# z = np.array(z)

vertices = mesh.vertices

x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

x_range = np.linspace(min(x), max(x), 25)
y_range = np.linspace(min(y), max(y), 70)


X, Y = np.meshgrid(x_range, y_range)

# rbf = Rbf(x, y, z, function='cubic', smooth=10)
# rbf = RBFInterpolator((x, y), z, kernel='cubic')

# Z = rbf(X, Y)

Z = griddata((x, y), z, (X, Y), method='cubic')

# interp_func = interp2d(x, y, z, kind='cubic')
# interp_func = CloughTocher2DInterpolator(points=(x, y), values=z)
# Z = interp_func(x_range, y_range)

fig1 = plt.figure(dpi=600)
ax = fig1.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='r', marker='o', s=2, label='Point Cloud', alpha=0.2)
# ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, label='Cubic Interpolation')
ax.scatter(X, Y, Z, c='b', marker='^', s=2, alpha=1)
ax.set_title('Comparison: Point Cloud vs. Cubic Interpolation')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
