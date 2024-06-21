Image Splitter and Resizer
<img width="463" alt="python_irHbV8Pp75" src="https://github.com/Xerophayze/splitter/assets/113407496/6cec060c-4e33-42c2-a487-8ddb8e2b8569">
I created this tool to provide an easy way to split images, particularly for those preparing large datasets of images for AI training. This script is especially useful for splitting images generated from a grid of AI images.

Features
Select multiple image files (jpg, jpeg, png, bmp, webp) to process.
Split each selected image into a customizable number of smaller images.
Resize the smaller images to one of several selectable sizes: 512x512, 768x768, 1024x1024, 2048x2048, or 4096x4096, or a custom size.
Save the smaller images in a specified output folder, or create a new folder based on the original file name.
Option to run the script via command line with all options configurable through arguments.
Prerequisites
Python 3.x
The script will automatically check for and install the Pillow and tkinterdnd2 libraries if they are not already installed.
How to Use
Command-Line Mode
Download the Script: Save the split_image_gui.py script to your local machine.

Run the Script with Command-Line Arguments:

sh
Copy code
python split_image_gui.py <source_files> [--size SIZE] [--custom_size CUSTOM_SIZE] [--across ACROSS] [--high HIGH] [--folder FOLDER]
<source_files>: Space-separated list of image files to process.
--size SIZE: Base size for resizing (default: 512).
--custom_size CUSTOM_SIZE: Custom size for resizing.
--across ACROSS: Number of images across (default: 1).
--high HIGH: Number of images high (default: 1).
--folder FOLDER: Custom output folder name (optional).
Examples:
Basic Usage:
sh
Copy code
python split_image_gui.py image1.jpg image2.jpg
With Optional Arguments:
sh
Copy code
python split_image_gui.py image1.jpg image2.jpg --size 512 --custom_size 800 --across 2 --high 3 --folder custom_folder
GUI Mode
Download the Script: Save the split_image_gui.py script to your local machine.

Run the Script: Open your terminal or command prompt and navigate to the directory where the script is saved. Run the script using Python:

sh
Copy code
python split_image_gui.py
Using the GUI:

Click the "Browse" button to select multiple image files (jpg, jpeg, png, bmp, webp).
The selected file names will be displayed in a list format within the GUI.
Choose the desired output image size from the dropdown menu.
Enter a custom size if needed.
Enter the number of images across and high.
Optionally, enter a name for the destination folder. If left blank, the folder will be named after each image file.
Click the "Start Processing" button to split and resize the images.
Script Details
The script includes the following key functionalities:

Dependency Check: The script checks for the Pillow and tkinterdnd2 libraries and installs them if necessary.
Image Splitting and Resizing: Each selected image is split into a customizable number of smaller images, resized to the chosen dimensions, and saved in the specified output folder.
File Handling: If the specified output folder already exists, the user is prompted to confirm whether to overwrite existing files or add new images to the folder.
Example
GUI Mode:
Run the script:

sh
Copy code
python split_image_gui.py
In the GUI:

Click "Browse" and select the images you want to process.
Select the desired output image size from the dropdown menu.
Optionally, enter a custom size.
Enter the number of images across and high.
Optionally, enter a name for the destination folder.
Click "Start Processing" to split and resize the images.
The processed images will be saved in the specified folder, with each image split into smaller images resized to the chosen dimensions.

Troubleshooting
Dependency Issues: Ensure you have an active internet connection when running the script for the first time so that it can install the necessary dependencies.
File Dialog Issues: Make sure you are selecting valid image files (jpg, jpeg, png, bmp, webp).
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
The Pillow library for image processing capabilities.
The tkinterdnd2 library for drag-and-drop functionality.
The Python Software Foundation for maintaining the Python programming language.
This updated README includes details about the command-line functionality, the options available, and how to use the script both from the command line and the GUI.

Please update the selectable image sizes to just the one number. For example 512, 768, 1024... They don't need to include XY sizes. The number they select is just the base size that the image will be resized to while maintaining aspect ratio, so the slides they select will be the long side of the image. you dont need to show the updated code again.

2/2

ChatGPT
Here's the updated README reflecting the change in selectable image sizes to just the base size:

Image Splitter and Resizer
<img width="463" alt="python_irHbV8Pp75" src="https://github.com/Xerophayze/splitter/assets/113407496/6cec060c-4e33-42c2-a487-8ddb8e2b8569">
I created this tool to provide an easy way to split images, particularly for those preparing large datasets of images for AI training. This script is especially useful for splitting images generated from a grid of AI images.

Features
Select multiple image files (jpg, jpeg, png, bmp, webp) to process.
Split each selected image into a customizable number of smaller images.
Resize the smaller images to one of several selectable sizes: 512, 768, 1024, 2048, or 4096, or a custom size.
Save the smaller images in a specified output folder, or create a new folder based on the original file name.
Option to run the script via command line with all options configurable through arguments.
Prerequisites
Python 3.x
The script will automatically check for and install the Pillow and tkinterdnd2 libraries if they are not already installed.
How to Use
Command-Line Mode
Download the Script: Save the split_image_gui.py script to your local machine.

Run the Script with Command-Line Arguments:

sh
Copy code
python split_image_gui.py <source_files> [--size SIZE] [--custom_size CUSTOM_SIZE] [--across ACROSS] [--high HIGH] [--folder FOLDER]
<source_files>: Space-separated list of image files to process.
--size SIZE: Base size for resizing (default: 512).
--custom_size CUSTOM_SIZE: Custom size for resizing.
--across ACROSS: Number of images across (default: 1).
--high HIGH: Number of images high (default: 1).
--folder FOLDER: Custom output folder name (optional).
Examples:
Basic Usage:
sh
Copy code
python split_image_gui.py image1.jpg image2.jpg
With Optional Arguments:
sh
Copy code
python split_image_gui.py image1.jpg image2.jpg --size 512 --custom_size 800 --across 2 --high 3 --folder custom_folder
GUI Mode
Download the Script: Save the split_image_gui.py script to your local machine.

Run the Script: Open your terminal or command prompt and navigate to the directory where the script is saved. Run the script using Python:

sh
Copy code
python split_image_gui.py
Using the GUI:

Click the "Browse" button to select multiple image files (jpg, jpeg, png, bmp, webp).
The selected file names will be displayed in a list format within the GUI.
Choose the desired output image size from the dropdown menu.
Enter a custom size if needed.
Enter the number of images across and high.
Optionally, enter a name for the destination folder. If left blank, the folder will be named after each image file.
Click the "Start Processing" button to split and resize the images.
Script Details
The script includes the following key functionalities:

Dependency Check: The script checks for the Pillow and tkinterdnd2 libraries and installs them if necessary.
Image Splitting and Resizing: Each selected image is split into a customizable number of smaller images, resized to the chosen dimensions, and saved in the specified output folder.
File Handling: If the specified output folder already exists, the user is prompted to confirm whether to overwrite existing files or add new images to the folder.
Example
GUI Mode:
Run the script:

sh
Copy code
python split_image_gui.py
In the GUI:

Click "Browse" and select the images you want to process.
Select the desired output image size from the dropdown menu.
Optionally, enter a custom size.
Enter the number of images across and high.
Optionally, enter a name for the destination folder.
Click "Start Processing" to split and resize the images.
The processed images will be saved in the specified folder, with each image split into smaller images resized to the chosen dimensions.

Troubleshooting
Dependency Issues: Ensure you have an active internet connection when running the script for the first time so that it can install the necessary dependencies.
File Dialog Issues: Make sure you are selecting valid image files (jpg, jpeg, png, bmp, webp).
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
The Pillow library for image processing capabilities.
The tkinterdnd2 library for drag-and-drop functionality.
The Python Software Foundation for maintaining the Python programming language.
