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
- Cross-platform support with setup and run scripts for both Windows and Linux/macOS.

## Project Files

- `splitter.py` - Main Python script (runs with console window in background)
- `splitter.pyw` - Windows-specific version (runs without console window)
- `requirements.txt` - Lists all Python package dependencies
- `setup.bat` - Windows setup script to install dependencies
- `setup.sh` - Linux/macOS setup script to install dependencies
- `run.bat` - Windows script to run the application
- `run.sh` - Linux/macOS script to run the application
- `splitter.bat` - Original Windows launcher (checks for Python installation)

## Prerequisites

- Python 3.x
- Required packages: Pillow and tkinterdnd2 (automatically installed by setup scripts)

## Installation

### Windows
1. Run `setup.bat` to install all required dependencies
   ```
   setup.bat
   ```
2. After setup is complete, you can run the application using:
   ```
   run.bat
   ```
   
   Alternatively, you can use the original `splitter.bat` which also checks for Python installation.

### Linux/macOS
1. Make the setup script executable:
   ```sh
   chmod +x setup.sh
   ```
2. Run the setup script to install dependencies:
   ```sh
   ./setup.sh
   ```
3. Run the application:
   ```sh
   ./run.sh
   ```

## How to Use

### Command-Line Mode

1. **Install Dependencies**: First, run the appropriate setup script for your operating system:
   - Windows: `setup.bat`
   - Linux/macOS: `./setup.sh`

2. **Run the Application with Command-Line Arguments**:
   
   On Windows:
   ```
   run.bat [image1.jpg image2.jpg] [options]
   ```
   
   On Linux/macOS:
   ```sh
   ./run.sh [image1.jpg image2.jpg] [options]
   ```
   
   Available options:
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
    ./run.sh image1.jpg image2.jpg
    ```
- **With Optional Arguments**:
    ```sh
    ./run.sh image1.jpg image2.jpg --size 512 --custom_size 800 --across 2 --high 3 --folder custom_folder --maintain_format
    ```

### GUI Mode

1. **Install Dependencies**: First, run the appropriate setup script for your operating system:
   - Windows: `setup.bat`
   - Linux/macOS: `./setup.sh`

2. **Launch the Application**:
   
   On Windows:
   ```
   run.bat
   ```
   
   On Linux/macOS:
   ```sh
   ./run.sh
   ```
   
   Alternatively on Windows, you can use the original `splitter.bat` file which will check for and install Python if needed.

3. **Using the GUI**:
    - Click the "Browse" button to select multiple image files (jpg, jpeg, png, bmp, webp).
    - The selected file names will be displayed in a list format within the GUI.
    - Choose the desired output image size from the dropdown menu.
    - Enter a custom size if needed.
    - Enter the number of images across and high.
    - Optionally, enter a name for the destination folder. If left blank, the folder will be named after each image file.
    - Check the "Maintain source image format" checkbox to keep the original format of the source images.
    - Click the "Process" button to split and resize the images.

## Script Details

The script includes the following key functionalities:

- **Dependency Check**: The script checks for the `Pillow` and `tkinterdnd2` libraries and installs them if necessary.
- **Image Splitting and Resizing**: Each selected image is split into a customizable number of smaller images, resized to the chosen dimensions, and saved in the specified output folder.
- **File Handling**: If the specified output folder already exists, the user is prompted to confirm whether to overwrite existing files or add new images to the folder.

## Example

### GUI Mode:

1. Install dependencies:
   
   On Windows:
   ```
   setup.bat
   ```
   
   On Linux/macOS:
   ```sh
   ./setup.sh
   ```

2. Run the application:
   
   On Windows:
   ```
   run.bat
   ```
   
   On Linux/macOS:
   ```sh
   ./run.sh
   ```

3. In the GUI:
    - Click "Browse" and select the images you want to process.
    - Select the desired output image size from the dropdown menu.
    - Optionally, enter a custom size.
    - Enter the number of images across and high.
    - Optionally, enter a name for the destination folder.
    - Check the "Maintain source image format" checkbox if desired.
    - Click "Process" to split and resize the images.

4. The processed images will be saved in the specified folder, with each image split into smaller images resized to the chosen dimensions.

## Troubleshooting

- **Installation Issues**: If you encounter problems during setup, make sure you have an active internet connection so that the setup scripts can download and install the necessary dependencies.
- **Python Not Found**: Ensure Python 3.x is installed and added to your system PATH. On Windows, the `splitter.bat` file will attempt to install Python if it's not found.
- **Dependency Issues**: If the application fails to start after setup, try running the setup script again. If problems persist, you can manually install the dependencies using `pip install -r requirements.txt`.
- **File Dialog Issues**: Make sure you are selecting valid image files (jpg, jpeg, png, bmp, webp).
- **Permission Issues on Linux/macOS**: If you can't run the shell scripts, make sure they have executable permissions with `chmod +x setup.sh run.sh`.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- The `Pillow` library for image processing capabilities.
- The `tkinterdnd2` library for drag-and-drop functionality.
- The Python Software Foundation for maintaining the Python programming language.
