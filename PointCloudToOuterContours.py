import trimesh
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.cluster import KMeans

filename = 'model1.stl'
mesh = trimesh.load_mesh(filename)
number_of_sampled_points = 50000
pointcloud, _ = trimesh.sample.sample_surface_even(mesh, number_of_sampled_points)

global_selected_points = []

x = np.asarray(pointcloud[:, 0])
y = np.asarray(pointcloud[:, 1])
z = np.asarray(pointcloud[:, 2])

x_s, y_s, z_s = [], [], []
height_each_layer = 5
number_of_layers = (max(z) - min(z))/height_each_layer

z_int = np.linspace(min(z), max(z), math.ceil(number_of_layers))

for z_lay in z_int:
    x_r, y_r, z_r = [], [], []
    for i in range(len(x)):
        if z[i] - 1 < z_lay < z[i] + 1:
            x_r.append(x[i])
            y_r.append(y[i])
            z_r.append(z_lay)
    data = np.vstack((x_r, y_r)).T
    num_resampled_points = 50
    kmeans = KMeans(n_clusters=num_resampled_points, random_state=0, n_init='auto', algorithm='lloyd')
    kmeans.fit(data)
    resampled = kmeans.cluster_centers_

    x_resampled, y_resampled = resampled[:, 0], resampled[:, 1]
    z_resampled = np.full((num_resampled_points, 1), z_lay)
    selected_points2 = np.column_stack((x_resampled, y_resampled, z_resampled))
    global_selected_points.extend(selected_points2)

    x_s.append(x_resampled)
    y_s.append(y_resampled)
    z_s.append(np.asarray(z_lay))


common_array = np.asarray(global_selected_points)

fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
ax = plt.axes(projection='3d')
ax.scatter(common_array[:, 0], common_array[:, 1], common_array[:, 2], marker='o')
plt.show()
