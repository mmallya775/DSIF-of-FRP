import pandas as pd
from scipy.interpolate import griddata
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import numpy as np
import trimesh
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import least_squares


def plot3d_mesh(df):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig = px.scatter_3d(data_frame=df, x='x', y='y', z='z')
    #fig.update_layout(scene=dict(zaxis=dict(range=[0, 200])))
    fig.show(renderer='browser')


def sphere_equation(params, points):
    a, b, c, r = params
    return (points[:, 0] - a) ** 2 + (points[:, 1] - b) ** 2 + (points[:, 2] - c) ** 2 - r**2


def error(params):
    residuals = sphere_equation(params, point_cloud_np_array)
    return np.sum(residuals**2)


mesh = trimesh.load_mesh('NewSurface.stl')

num_points = 25000
point_cloud, _ = trimesh.sample.sample_surface_even(mesh, num_points)

x1 = []
y1 = []
z1 = []


for point in point_cloud:
    x1.append(point[0])
    y1.append(point[1])
    z1.append(point[2])

d = {
    'x': x1,
    'y': y1,
    'z': z1
}

df = pd.DataFrame(data=d)
#plot3d_mesh(df)

point_cloud_np_array = np.array(point_cloud)
print(type(point_cloud_np_array))

initial_params = [0.0, 0.0, 0.0, 1.0]

result = minimize(error, initial_params, method='BFGS')
#result = least_squares(sphere_equation, initial_params, args = (point_cloud,))
# optimal_params = result.x

a, b, c, r = result.x

print('a= ', end=' ')
print(a)
print('b= ', end=' ')
print(b)
print('c= ', end=' ')
print(c)
print('r= ', end=' ')
print(r)

fig = plt.figure(dpi=1000)
ax = fig.add_subplot(111, projection='3d')

ax.scatter(point_cloud_np_array[:, 0], point_cloud_np_array[:, 1], point_cloud_np_array[:, 2], label='Point Cloud', s=1)
u, v = np.mgrid[-np.pi:np.pi:40j, 0:np.pi:40j]
x = r * np.cos(u) * np.sin(v) + a
y = r * np.sin(u) * np.sin(v) + b + 60
z = r * np.cos(v) + c
ax.plot_surface(x, y, z, color='red', alpha=0.2, label='Fitted Sphere')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
