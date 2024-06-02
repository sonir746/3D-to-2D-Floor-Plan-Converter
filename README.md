# 3D to 2D Floor Plan Converter

3D to 2D Floor Plan Converter is a tool for converting STL files of 3D models into 2D floor plan projections. The tool generates various views, including front, back, left, right, top, and bottom views, and can display them individually or all together. It also offers an option to save the generated views.

## Features

- Convert 3D models from STL files to point clouds.
- Generate 2D projections (floor plans) from point clouds.
- Provide different views: front, back, left, right, top, and bottom.
- Display views individually or all together.
- Save the generated views as images.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required dependencies:

   ```
   pip install open3d matplotlib
   ```

## Usage

Run the script `main.py` with the STL file path as an argument. You can also specify options to save the views and to display all views together.

```
python main.py <path/to/your/file.stl> [-s/--save <save_dir>] [-t/--together]
```

### Arguments

- `<path/to/your/file.stl>`: Path to the STL file of the 3D model.
- `-s` or `--save <save_dir>`: Optional argument to specify the directory where images will be saved.
- `-t` or `--together`: Optional argument to display all views together in a single figure.

### Examples

1. Display all views together without saving:
   ```
   python main.py model.stl -t
   ```

2. Save individual views to the `saved_views` directory:
   ```
   python main.py model.stl -s saved_views
   ```

3. Save all views together in a single figure and save it:
   ```
   python main.py model.stl -s saved_views -t
   ```

## Project Structure

- `main.py`: Main script to execute the program.
- `stl_to_pointcloud.py`: Module for converting an STL file to a point cloud.
- `projection.py`: Module for projecting the 3D point cloud to 2D for different views.

## Modules

### `main.py`

Handles command-line arguments, coordinates the conversion and projection processes, and manages the display and saving of views.

### `stl_to_pointcloud.py`

Contains the function for converting an STL file into a point cloud using Open3D.

### `projection.py`

Contains functions for projecting the point cloud to 2D for different views and for plotting the floor plans.

## Requirements

- Python 3.x
- open3d
- matplotlib

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## Acknowledgements

This tool is built using the Open3D library for 3D data processing and the Matplotlib library for plotting.

---

Feel free to reach out if you have any questions or suggestions!
