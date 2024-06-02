# stl_to_pointcloud.py
import open3d as o3d

def stl_to_point_cloud(file_path):
    mesh = o3d.io.read_triangle_mesh(file_path)
    point_cloud = mesh.sample_points_poisson_disk(number_of_points=50000)
    return point_cloud
