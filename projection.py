# projection.py
import numpy as np

def project_to_2d(point_cloud, view):
    points = np.asarray(point_cloud.points)
    if view == 'front':
        points_2d = points[:, [0, 1]]  # XY plane
    elif view == 'back':
        points_2d = points[:, [0, 1]]  # XY plane, flipped X axis
        points_2d[:, 0] = -points_2d[:, 0]
    elif view == 'left':
        points_2d = points[:, [2, 1]]  # ZY plane
    elif view == 'right':
        points_2d = points[:, [2, 1]]  # ZY plane, flipped Z axis
        points_2d[:, 0] = -points_2d[:, 0]
    elif view == 'top':
        points_2d = points[:, [0, 2]]  # XZ plane
    elif view == 'bottom':
        points_2d = points[:, [0, 2]]  # XZ plane, flipped X axis
        points_2d[:, 1] = -points_2d[:, 1]
    else:
        raise ValueError("Invalid view specified")
    return points_2d
