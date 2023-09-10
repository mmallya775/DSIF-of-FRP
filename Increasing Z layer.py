import trimesh
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Load the STL file of the hemisphere
hemisphere_mesh = trimesh.load_mesh('Surf.stl')

# Specify the Z value for interpolation
z_value = 80  # Adjust this value as needed

# Get the vertices of the hemisphere mesh
hemisphere_vertices = hemisphere_mesh.vertices

# Extract the vertices with the specified Z value
selected_vertices = hemisphere_vertices
# Interpolate (x, y) points on the Z plane
x = selected_vertices[:, 0]
y = selected_vertices[:, 1]

x_min, x_max = np.min(x), np.max(x)
y_min, y_max = np.min(y), np.max(y)

num_points = 10  # Adjust this as needed
xi = np.linspace(x_min, x_max, num_points)
yi = np.linspace(y_min, y_max, num_points)
xi, yi = np.meshgrid(xi, yi)

zi = griddata((x, y), selected_vertices[:, 2], (xi, yi), method='linear')

# Create subplots for comparison
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the interpolated points
ax.scatter(xi, yi, zi, s=1, label=f'Interpolated Points at Z = {z_value}', c='b')

# Plot the original point cloud
ax.scatter(hemisphere_vertices[:, 0], hemisphere_vertices[:, 1], hemisphere_vertices[:, 2], s=1, label='Original Point Cloud', c='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Comparison of Interpolated Points and Original Point Cloud')
ax.legend()

plt.show()
