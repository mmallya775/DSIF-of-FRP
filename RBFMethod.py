import numpy as np
import trimesh
from scipy.interpolate import RBFInterpolator
import matplotlib.pyplot as plt


mesh = trimesh.load_mesh('Surf.stl')
# ## Uncomment the below lines if you want to train the interpolator on more number of points and adjust num_points
# num_points = 25000
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


vertices = mesh.vertices # Converts the mesh object to an array of vertices [[x1,x2,x2....][y1,y2,y3...][z1,z2,z3....]]
# splits the Array into three x,y and z
x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

num_points = 35     # The RBF Interpolator uses a n x n grid of equal points in x and y direction
xi = np.linspace(min(x), max(x), num_points)
yi = np.linspace(min(y), max(y), num_points)
XI, YI = np.meshgrid(xi, yi)

# Radial Basis Function interpolation The x and y arrays need to be flattened using the ravel() function to be used
# in RBFInterpolator and the interpolation object
measured_points = np.stack([x.ravel(), y.ravel()], -1)
interpolated_points = np.stack([XI.ravel(), YI.ravel()], -1)

interpolation_rbf = RBFInterpolator(y=measured_points, d=z.ravel(), smoothing=0, kernel='cubic', degree=2)
Z_rbf = interpolation_rbf(interpolated_points).reshape(num_points, num_points)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='r', marker='o', s=3, label='Point Cloud', alpha=0.25)
# ax.plot_surface(XI, YI, Z_rbf, cmap='viridis', alpha=0.7, label='Cubic Interpolation')
ax.scatter(XI, YI, Z_rbf, c='b', marker='^', s=2, alpha=1)
ax.set_title('Comparison: Point Cloud vs. RBF Interpolation')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
