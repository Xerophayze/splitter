# Image Splitter and Resizer

I created this tool to provide an easy way to split images, particularly for those preparing large datasets of images for AI training. This script is especially useful for splitting images generated from a grid of AI images.

## Features

- Select multiple image files (jpg, jpeg, png, bmp) to process.
- Split each selected image into 15 smaller images.
- Resize the smaller images to one of three selectable sizes: 512x512, 768x768, or 1024x1024.
- Save the smaller images in a specified output folder, or create a new folder based on the original file name.

## Prerequisites

- Python 3.x
- The script will automatically check for and install the `Pillow` library if it is not already installed.

## How to Use

1. **Download the Script**: Save the `split_image_gui.py` script to your local machine.

2. **Run the Script**: Open your terminal or command prompt and navigate to the directory where the script is saved. Run the script using Python:
    ```sh
    python split_image_gui.py
    ```

3. **Using the GUI**:
    - **Select Image Files**: Click the "Browse" button to open a file dialog and select multiple image files you wish to process. The selected file names will be displayed in a list within the GUI.
    - **Select Output Image Size**: Choose the desired output image size (512x512, 768x768, or 1024x1024) from the dropdown menu.
    - **Enter Destination Folder Name (Optional)**: Optionally, enter a name for the destination folder. If left blank, the folder will be named after each image file.
    - **Start Processing**: Click the "Start Processing" button to split and resize the images. The processed images will be saved in the specified output folder.

## Script Details

The script includes the following key functionalities:

- **Dependency Check**: The script checks for the `Pillow` library and installs it if necessary.
- **Image Splitting and Resizing**: Each selected image is split into 15 smaller images, resized to the chosen dimensions, and saved in the specified output folder.
- **File Handling**: If the specified output folder already exists, the user is prompted to confirm whether to overwrite existing files or add new images to the folder.

## Example

Here is an example of how to run the script and use the GUI:

1. Run the script:
    ```sh
    python split_image_gui.py
    ```

2. In the GUI:
    - Click "Browse" and select the images you want to process.
    - Select the desired output image size from the dropdown menu.
    - Optionally, enter a name for the destination folder.
    - Click "Start Processing" to split and resize the images.

3. The processed images will be saved in the specified folder, with each image split into 15 smaller images resized to the chosen dimensions.

## Troubleshooting

- **Dependency Issues**: Ensure you have an active internet connection when running the script for the first time so that it can install the necessary dependencies.
- **File Dialog Issues**: Make sure you are selecting valid image files (jpg, jpeg, png, bmp).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- The `Pillow` library for image processing capabilities.
- The Python Software Foundation for maintaining the Python programming language.
