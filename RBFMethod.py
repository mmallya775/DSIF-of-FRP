import numpy as np
import trimesh
from scipy.interpolate import RBFInterpolator
import matplotlib.pyplot as plt


mesh = trimesh.load_mesh('Surf.stl')
vertices = mesh.vertices

x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

num_points = 30
xi = np.linspace(min(x), max(x), num_points)
yi = np.linspace(min(y), max(y), num_points)
XI, YI = np.meshgrid(xi, yi)

# Radial Basis Function interpolation
measured_points = np.stack([x.ravel(), y.ravel()], -1)
interpolated_points = np.stack([XI.ravel(), YI.ravel()], -1)

interpolation_rbf = RBFInterpolator(y=measured_points, d=z.ravel(), smoothing=0, kernel='cubic')
Z_rbf = interpolation_rbf(interpolated_points).reshape(num_points, num_points)

fig = plt.figure(dpi=600)
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='r', marker='o', s=3, label='Point Cloud', alpha=0.3)
# ax.plot_surface(XI, YI, Z_rbf, cmap='viridis', alpha=0.7, label='Cubic Interpolation')
ax.scatter(XI, YI, Z_rbf, c='b', marker='^', s=2, alpha=1)
ax.set_title('Comparison: Point Cloud vs. RBF Interpolation')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
