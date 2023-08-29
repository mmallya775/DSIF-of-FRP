import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import trimesh
import plotly.express as px

part = trimesh.load_mesh('Surf.stl')
point_cloud = np.asarray(part.vertices)
np.set_printoptions(threshold=np.inf)
print(point_cloud)
print('===============================================')
print('===============================================')
print('===============================================')

sorted_indices_x = np.argsort(point_cloud[:, 0])
sorted_pointcloud_x = point_cloud[sorted_indices_x]
print(sorted_pointcloud_x)


print('===============================================')
print('===============================================')
print('===============================================')

sorted_indices_y = np.argsort(point_cloud[:, 1])
sorted_pointcloud_y = point_cloud[sorted_indices_y]
sorted_pointcloud_y[:, 1] = np.round(sorted_pointcloud_y[:, 1], 0)
print(sorted_pointcloud_y)


def plot3d_mesh(x, y, z):
    df = make_data_set(x, y, z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig = px.scatter_3d(data_frame=df, x='x', y='y', z='z')
    fig.update_layout(scene=dict(zaxis=dict(range=[0, 200])))
    fig.show(renderer='browser')


def make_data_set(x, y, z):
    d = {
        'x': x,
        'y': y,
        'z': z
    }
    df = pd.DataFrame(data=d)

    return df


# plot3d_mesh(sorted_pointcloud_x[:, 0], sorted_pointcloud_x[:, 1], sorted_pointcloud_x[:, 2])
plot3d_mesh(sorted_pointcloud_y[:, 0], sorted_pointcloud_y[:, 1], sorted_pointcloud_y[:, 2])
