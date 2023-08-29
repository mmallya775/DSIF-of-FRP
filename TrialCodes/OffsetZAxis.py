import trimesh
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


mesh = trimesh.load_mesh('Surf.stl')
vertices = mesh.vertices

x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]


x_range = np.linspace(min(x), max(x), 25)
y_range = np.linspace(min(y), max(y), 25)

X, Y = np.meshgrid(x_range, y_range)

Z = griddata((x, y), z, (X, Y), method='cubic')

offset_value = 10
Z_offset1, Z_offset2 = Z + offset_value, Z - offset_value

fig = plt.figure(dpi=1200)
ax1 = fig.add_subplot(111, projection='3d')


ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('Original 3D Surface vs Offset 3D Surface')

ax1.plot_surface(X, Y, Z_offset1, cmap='inferno')
ax1.plot_surface(X, Y, Z_offset2, cmap='coolwarm')


plt.show()
