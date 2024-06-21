# Image Splitter and Resizer
<img width="474" alt="python_wwAG0YSEKo" src="https://github.com/Xerophayze/splitter/assets/113407496/89501363-f6eb-4456-ae36-d140471544bc">

I created this tool to provide an easy way to split images, particularly for those preparing large datasets of images for AI training. This script is especially useful for splitting images generated from a grid of AI images.

## Features

- Select multiple image files (jpg, jpeg, png, bmp, webp) to process, even from multiple locations.
- Split each selected image into a customizable number of smaller images.
- Resize the smaller images to one of several selectable sizes: 512, 768, 1024, 2048, or 4096, or a custom size.
- Save the smaller images in a specified output folder, or create a new folder based on the original file name. All done in the source image file location.
- Always create a subfolder for each image file using the source file name, even when a custom folder is specified.
- If width and height are both 1, create a folder with the date and time as the folder name.
- Option to maintain the source image format (e.g., JPG, BMP, PNG).
- Option to run the script via command line with all options configurable through arguments.
- Use `splitter.bat` on Windows to automatically check for and install Python if not installed and open the GUI interface.

## Prerequisites

- Python 3.x
- The script will automatically check for and install the `Pillow` and `tkinterdnd2` libraries if they are not already installed.

## How to Use

### Command-Line Mode

1. **Download the Script**: Save the `splitter.py` script to your local machine.

2. **Run the Script with Command-Line Arguments**:
    ```sh
    python splitter.py <source_files> [--size SIZE] [--custom_size CUSTOM_SIZE] [--across ACROSS] [--high HIGH] [--folder FOLDER] [--maintain_format]
    ```
    - `<source_files>`: Space-separated list of image files to process.
    - `--size SIZE`: Base size for resizing (default: 512).
    - `--custom_size CUSTOM_SIZE`: Custom size for resizing.
    - `--across ACROSS`: Number of images across (default: 1).
    - `--high HIGH`: Number of images high (default: 1).
    - `--folder FOLDER`: Custom output folder name (optional).
    - `--maintain_format`: Maintain source image format.

#### Examples:
- **Basic Usage**:
    ```sh
    python splitter.py image1.jpg image2.jpg
    ```
- **With Optional Arguments**:
    ```sh
    python splitter.py image1.jpg image2.jpg --size 512 --custom_size 800 --across 2 --high 3 --folder custom_folder --maintain_format
    ```

### GUI Mode

1. **Download the Script**: Save the `splitter.py` script to your local machine.

2. **Run the Script**: Open your terminal or command prompt and navigate to the directory where the script is saved. Run the script using Python:
    ```sh
    python splitter.py
    ```

3. **Using `splitter.bat` on Windows**:
    - Double-click the `splitter.bat` file. This batch file will automatically check for and install Python if it is not already installed.
    - The GUI interface will open, allowing you to select and process images.

4. **Using the GUI**:
    - Click the "Browse" button to select multiple image files (jpg, jpeg, png, bmp, webp).
    - The selected file names will be displayed in a list format within the GUI.
    - Choose the desired output image size from the dropdown menu.
    - Enter a custom size if needed.
    - Enter the number of images across and high.
    - Optionally, enter a name for the destination folder. If left blank, the folder will be named after each image file.
    - Check the "Maintain source image format" checkbox to keep the original format of the source images.
    - Click the "Start Processing" button to split and resize the images.

## Script Details

The script includes the following key functionalities:

- **Dependency Check**: The script checks for the `Pillow` and `tkinterdnd2` libraries and installs them if necessary.
- **Image Splitting and Resizing**: Each selected image is split into a customizable number of smaller images, resized to the chosen dimensions, and saved in the specified output folder.
- **File Handling**: If the specified output folder already exists, the user is prompted to confirm whether to overwrite existing files or add new images to the folder.

## Example

### GUI Mode:

1. Run the script:
    ```sh
    python splitter.py
    ```

2. In the GUI:
    - Click "Browse" and select the images you want to process.
    - Select the desired output image size from the dropdown menu.
    - Optionally, enter a custom size.
    - Enter the number of images across and high.
    - Optionally, enter a name for the destination folder.
    - Check the "Maintain source image format" checkbox if desired.
    - Click "Start Processing" to split and resize the images.

3. The processed images will be saved in the specified folder, with each image split into smaller images resized to the chosen dimensions.

## Troubleshooting

- **Dependency Issues**: Ensure you have an active internet connection when running the script for the first time so that it can install the necessary dependencies.
- **File Dialog Issues**: Make sure you are selecting valid image files (jpg, jpeg, png, bmp, webp).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- The `Pillow` library for image processing capabilities.
- The `tkinterdnd2` library for drag-and-drop functionality.
- The Python Software Foundation for maintaining the Python programming language.
