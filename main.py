import trimesh
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


def make_data_set(x, y, z):
    d = {
        'x': x,
        'y': y,
        'z': z
    }
    df = pd.DataFrame(data=d)

    return df


def plot3d_mesh(x, y, z):
    df = make_data_set(x, y, z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fig = px.scatter_3d(data_frame=df, x='x', y='y', z='z')
    fig.update_layout(scene=dict(zaxis=dict(range=[0, 200])))
    fig.show(renderer='browser')


def points_on_symmetric_plane1(x, y, z):

    xs_1, ys_1, zs_1 = [], [], []

    x_middle = (max(x) + min(x))/2

    for i in range(0, len(x)):
        if -10 + x_middle < x[i] < 10 + x_middle:
            xs_1.append(x[i])
            ys_1.append(y[i])
            zs_1.append(z[i])

    return xs_1, ys_1, zs_1


def points_on_symmetric_plane2(x, y, z):
    xs_2, ys_2, zs_2 = [], [], []

    for i in range(0, len(y)):
        if -20 < y[i] < 20:
            xs_2.append(x[i])
            ys_2.append(y[i])
            zs_2.append(z[i])

    return xs_2, ys_2, zs_2


if __name__ == '__main__':
    stl_file_name = 'NewSurface.stl'
    mesh = trimesh.load_mesh(file_obj=stl_file_name)
    vertices = mesh.vertices
    x = []
    y = []
    z = []

    for i, vertex in enumerate(vertices[:]):
        x.append(vertex[0])
        y.append(vertex[1])
        z.append(vertex[2])

    plot3d_mesh(x=x, y=y, z=z)
    xs1, ys1, zs1 = points_on_symmetric_plane1(x, y, z)
    plot3d_mesh(x=xs1, y=ys1, z=zs1)
    xs2, ys2, zs2 = points_on_symmetric_plane2(x, y, z)
    plot3d_mesh(x=xs2, y=ys2, z=zs2)
