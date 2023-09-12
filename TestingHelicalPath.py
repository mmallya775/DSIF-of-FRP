import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the radii of the two circles
radius_large = 17.5  # 35 mm diameter / 2
radius_small = 12.5  # 25 mm diameter / 2
separation_z = 1  # 5 mm separation in Z-direction

# Calculate the pitch (a) to connect the two circles with separation in Z-direction
a = separation_z / (2 * np.pi)

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create theta values for plotting circles
theta_circle = np.linspace(0, 2 * np.pi, 1000)

# Points for the smaller circle
x_small = radius_small * np.cos(theta_circle)
y_small = radius_small * np.sin(theta_circle)
z_small = np.zeros_like(theta_circle)  # All points are at Z = 0

# Points for the larger circle with an offset in the Z-direction
x_large = radius_large * np.cos(theta_circle)
y_large = radius_large * np.sin(theta_circle)
z_large = np.full_like(theta_circle, separation_z)  # All points are at Z = separation_z

# Plot the smaller circle
ax.plot(x_small, y_small, z_small, label='Small Circle', color='red')

# Plot the larger circle
ax.plot(x_large, y_large, z_large, label='Large Circle', color='blue')

# Create points for the helical path
theta_helix = np.linspace(0, 2 * np.pi, 1000)
x_helix = (radius_small + (radius_large - radius_small) * theta_helix / (2 * np.pi)) * np.cos(theta_helix)
y_helix = (radius_small + (radius_large - radius_small) * theta_helix / (2 * np.pi)) * np.sin(theta_helix)
z_helix = a * theta_helix

# Plot the helical path
ax.plot(x_helix, y_helix, z_helix, label='Helical Path', color='green', linewidth=2)

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Set axis limits
ax.set_xlim(-radius_large - 2, radius_large + 2)
ax.set_ylim(-radius_large - 2, radius_large + 2)
ax.set_zlim(0, separation_z + 2)

# Show the 3D plot
plt.show()
