# import trimesh
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Load the STL file
# mesh = trimesh.load_mesh('Surf.stl')
#
# # Extract the coordinates
# vertices = mesh.vertices
#
# # Split the coordinates into x, y, and z components
# x_values = vertices[:, 0]
# y_values = vertices[:, 1]
# z_values = vertices[:, 2]
#
# # Define your TensorFlow model
# model = tf.keras.Sequential([
#    tf.keras.layers.Input(shape=(2,)),  # Input layer for x and y values
#    tf.keras.layers.Dense(64, activation='relu'),
#    tf.keras.layers.Dense(64, activation='relu'),
#    tf.keras.layers.Dense(1)  # Output layer for z value prediction
# ])
#
# # Prepare the training data
# training_data = np.column_stack((x_values, y_values))
# z_targets = z_values
#
# # Compile and train the model
# model.compile(optimizer='adam', loss='mean_squared_error')
# model.fit(training_data, z_targets, epochs=100, batch_size=32)
#
# # Define the x-y values for prediction
# x_test = np.linspace(min(x_values), max(x_values), 100)
# y_test = np.linspace(min(y_values), max(y_values), 100)
# x_test, y_test = np.meshgrid(x_test, y_test)
# x_test = x_test.flatten()
# y_test = y_test.flatten()
#
# # Combine x-y values for prediction
# xy_test = np.column_stack((x_test, y_test))
#
# # Predict z values
# z_pred = model.predict(xy_test)
#
# # Create a scatter plot of the point cloud
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x_values, y_values, z_values, c='b', marker='o', label='Actual Points', s=0.5, alpha=0.5)
#
# # Plot the predicted z values
# ax.scatter(x_test, y_test, z_pred, c='r', marker='x', label='Predicted Points', s=1)
#
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.legend()
# plt.show()

import trimesh
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load the STL file
mesh = trimesh.load_mesh('Surf.stl')

# Extract the coordinates
vertices = mesh.vertices

# Split the coordinates into x, y, and z components
x_values = vertices[:, 0]
y_values = vertices[:, 1]
z_values = vertices[:, 2]

# Define your TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),  # Input layer for x and y values
    tf.keras.layers.Dense(4096, activation='relu'),
    tf.keras.layers.Dense(2048, activation='relu'),
    tf.keras.layers.Dense(1024, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)  # Output layer for z value prediction
])

# Prepare the training data
training_data = np.column_stack((x_values, y_values))
z_targets = z_values

# Compile and train the model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(training_data, z_targets, epochs=10, batch_size=32)

# Generate equidistant points for x and y
n_points = 20  # Adjust this as needed
x_min, x_max = min(x_values), max(x_values)
y_min, y_max = min(y_values), max(y_values)
x_test = np.linspace(x_min, x_max, n_points)
y_test = np.linspace(y_min, y_max, n_points)
x_test, y_test = np.meshgrid(x_test, y_test)
x_test = x_test.flatten()
y_test = y_test.flatten()

# Combine x-y values for prediction
xy_test = np.column_stack((x_test, y_test))

# Predict z values
z_pred = model.predict(xy_test)

# Create a scatter plot of the point cloud
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_values, y_values, z_values, c='b', marker='o', label='Actual Points', s=1, alpha=0.3)

# Plot the predicted z values
ax.scatter(x_test, y_test, z_pred, c='r', marker='x', label='Predicted Points', s=2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
