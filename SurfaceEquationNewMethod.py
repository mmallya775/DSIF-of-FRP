import trimesh
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


mesh = trimesh.load_mesh('Surf.stl')

# ## Uncomment the below lines if you want to train the interpolator on more number of points and adjust num_points
# num_points = 10000
# point_cloud, _ = trimesh.sample.sample_surface_even(mesh, num_points)
# x = []
# y = []
# z = []
#
# for point in point_cloud:
#     x.append(point[0])
#     y.append(point[1])
#     z.append(point[2])
# x = np.array(x)
# y = np.array(y)
# z = np.array(z)

vertices = mesh.vertices  # Converts the mesh object to an array of vertices [[x1,x2,x2....][y1,y2,y3...][z1,z2,z3....]]
# splits the Array into three x,y and z
x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

# Creates equidistant points of x(min) to x(max) and y(min) to y(max). 20 x 60 grid
x_range = np.linspace(min(x), max(x), 20)
y_range = np.linspace(min(y), max(y), 60)

# Creates a 2D grid of points of equidistant x and y points created above

X, Y = np.meshgrid(x_range, y_range)

# Griddata interpolator uses the pointcloud data (x,y) and calculates the Z coordinate value of created meshgrid above
Z = griddata((x, y), z, (X, Y), method='cubic')

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='r', marker='o', s=2, label='Point Cloud', alpha=0.2)
# ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, label='Cubic Interpolation')
ax.scatter(X, Y, Z, c='b', marker='^', s=2, alpha=1)
# ax.set_title('Dense Point Cloud')
ax.set_title('Comparison: Point Cloud vs. Cubic Interpolation')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
