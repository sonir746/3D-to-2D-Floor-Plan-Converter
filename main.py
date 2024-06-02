# main.py
import sys
import os
import stl_to_pointcloud
import projection
import matplotlib.pyplot as plt

def main(stl_file, save_dir=None, together=False):
    # Convert STL to point cloud
    point_cloud = stl_to_pointcloud.stl_to_point_cloud(stl_file)

    # Project to 2D for different views
    views = ['front', 'back', 'left', 'right', 'top', 'bottom']
    fig = None
    if together:
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    for idx, view in enumerate(views):
        points_2d = projection.project_to_2d(point_cloud, view)
        if together:
            ax = axes[idx//3, idx%3]
            ax.scatter(points_2d[:, 0], points_2d[:, 1], s=0.5)
            ax.set_title(f'{view.capitalize()} View')
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.axis('equal')
        else:
            plt.figure(figsize=(5, 5))
            plt.scatter(points_2d[:, 0], points_2d[:, 1], s=0.5)
            plt.title(f'{view.capitalize()} View')
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.axis('equal')
            if save_dir:
                save_path = os.path.join(save_dir, f'{view}.png')
                plt.savefig(save_path)
                print(f'Saved {view} view to {save_path}')
            plt.show()

    if together:
        plt.tight_layout()
        if save_dir:
            save_path = os.path.join(save_dir, 'all_views_together.png')
            plt.savefig(save_path)
            print(f'Saved all views together to {save_path}')
        plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <stl_file> [-s/--save save_dir] [-t/--together]")
        sys.exit(1)
    
    stl_file = sys.argv[1]
    save_dir = None
    together = False

    if len(sys.argv) > 2:
        idx = 2
        while idx < len(sys.argv):
            arg = sys.argv[idx]
            if arg in ['-s', '--save'] and idx + 1 < len(sys.argv):
                save_dir = sys.argv[idx + 1]
                idx += 2
            elif arg in ['-t', '--together']:
                together = True
                idx += 1
            else:
                print("Invalid argument. Usage: python main.py <stl_file> [-s/--save save_dir] [-t/--together]")
                sys.exit(1)
    
    main(stl_file, save_dir, together)
