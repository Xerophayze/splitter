# Image Splitter and Resizer
![python_sSZbYKqzIa](https://github.com/user-attachments/assets/7c70a711-db13-456a-8772-0f40cc45545e)


I created this tool to provide an easy way to split images, particularly for those preparing large datasets of images for AI training. This script is especially useful for splitting images generated from a grid of AI images.

## 🎉 NEW: Per-Image Settings Version Available!

**`splitter_with_per_image.py`** - Enhanced version with:
- ✨ **Image Preview** - See thumbnails before processing
- ⚙️ **Per-Image Settings** - Configure each image individually
- 🎨 **Modern Dual-Panel UI** - Resizable split view
- 📊 **Visual Indicators** - See which images have custom settings
- 🔄 **Global Defaults** - Set base settings for all images

**Launch with:** `run_per_image.bat` or see `COMPLETED.md` for full details!

## Versions

| Version | File | Features |
|---------|------|----------|
| **Original** | `splitter.py` | Basic functionality, simple UI |
| **Modern** | `splitter_modern.py` | Modern UI, threading, validation |
| **Per-Image** ⭐ | `splitter_with_per_image.py` | All modern features + per-image settings & preview |

## Features

### All Versions
- Select multiple image files (jpg, jpeg, png, bmp, webp) to process, even from multiple locations
- Split each selected image into a customizable number of smaller images
- Resize the smaller images to one of several selectable sizes: 512, 768, 1024, 2048, or 4096, or a custom size
- Save the smaller images in a specified output folder, or create a new folder based on the original file name
- Always create a subfolder for each image file using the source file name, even when a custom folder is specified
- If width and height are both 1, create a folder with the date and time as the folder name
- Option to maintain the source image format (e.g., JPG, BMP, PNG)
- Option to run the script via command line with all options configurable through arguments
- Cross-platform support with setup and run scripts for both Windows and Linux/macOS

### Modern & Per-Image Versions
- 🎨 Modern dark theme UI with sv-ttk
- ⚡ Background threading for responsive interface
- 📊 Real-time progress bar
- ✅ Input validation with visual feedback
- 💡 Tooltips on all controls
- 🎯 Better error handling

### Per-Image Version Only
- 🖼️ **Image preview** with dimensions and file size
- ⚙️ **Per-image custom settings** - different split/size for each image
- 📋 **Settings summary** displayed next to each filename
- 🔄 **Global defaults** for images without custom settings
- ✨ **Visual indicators** (⚙ icon) show which images have custom settings
- 🗑️ **Remove selected** image from list
- 📐 **Dual-panel layout** with resizable sections

## Project Files

### Python Scripts
- `splitter.py` - Original version (basic functionality)
- `splitter_modern.py` - Modern UI version (threading, validation)
- `splitter_with_per_image.py` ⭐ - **NEW!** Per-image settings with preview
- `splitter.pyw` - Windows-specific version (runs without console window)

### Launch Scripts
- `run.bat` - Run original version (Windows)
- `run_modern.bat` - Run modern version (Windows)
- `run_per_image.bat` ⭐ - **Run per-image version (Windows)**
- `run.sh` - Run original version (Linux/macOS)
- `splitter.bat` - Original Windows launcher (checks for Python installation)

### Setup & Dependencies
- `requirements.txt` - Python package dependencies (includes sv-ttk for modern UI)
- `install.bat` - Install all dependencies (Windows)
- `setup.bat` - Windows setup script
- `setup.sh` - Linux/macOS setup script

### Documentation
- `README.md` - This file
- `COMPLETED.md` ⭐ - **Per-image version complete guide**
- `IMPROVEMENTS.md` - All improvements documented
- `PER_IMAGE_SETTINGS.md` - Feature documentation
- `IMPLEMENTATION_GUIDE.md` - Technical implementation details
- `QUICK_REFERENCE.md` - Quick lookup reference

## Prerequisites

- Python 3.x
- Required packages: Pillow and tkinterdnd2 (automatically installed by setup scripts)

## Installation

### Windows - Quick Start (Recommended)

**Just double-click to run!** No separate setup needed.

```
run_per_image.bat    ← Per-Image Settings (Recommended)
run_modern.bat       ← Modern Version
run.bat              ← Original Version
```

The launcher will automatically:
- Check if Python is installed
- Install missing dependencies
- Launch the application

**First time users:** If you don't have Python, install it from https://www.python.org/downloads/ (check "Add Python to PATH")

### Manual Installation (Optional)

If you prefer to install dependencies separately:
```
setup.bat    ← Checks Python + installs dependencies
install.bat  ← Installs dependencies only
```

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
