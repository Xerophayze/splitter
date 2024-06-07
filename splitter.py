import os
import sys
import hashlib
import subprocess
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, OptionMenu, messagebox, Listbox, Scrollbar
from PIL import Image

def install_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def check_and_install_dependencies():
    required_packages = ["Pillow"]
    for package in required_packages:
        install_package(package)

check_and_install_dependencies()

def get_image_hash(image_path):
    with open(image_path, 'rb') as f:
        img_hash = hashlib.md5(f.read()).hexdigest()
    return img_hash

def split_and_resize_image(image_path, output_size, output_folder):
    # Get the base name of the file without extension
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    if not output_folder:
        output_folder = os.path.join(os.getcwd(), base_name)
    else:
        output_folder = os.path.join(os.getcwd(), output_folder)
    
    # Get the hash of the selected image
    selected_image_hash = get_image_hash(image_path)
    
    if os.path.exists(output_folder):
        # Check for existing files and their hashes
        existing_files = [f for f in os.listdir(output_folder) if f.endswith('.jpg')]
        for file in existing_files:
            file_path = os.path.join(output_folder, file)
            try:
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash == selected_image_hash:
                    # Overwrite the existing file if hashes match
                    continue
            except Exception as e:
                messagebox.showerror("Error", f"Error checking file {file}: {str(e)}")
        
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the image file
    with Image.open(image_path) as img:
        # Split the image into 15 smaller images
        count = 1
        for row in range(3):
            for col in range(5):
                # Calculate the coordinates of the current small image
                left = col * img.width // 5
                upper = row * img.height // 3
                right = left + img.width // 5
                lower = upper + img.height // 3

                # Crop the image
                small_img = img.crop((left, upper, right, lower))
                # Resize the image to the specified output size
                small_img = small_img.resize((output_size, output_size))

                # Save the small image as a jpg file
                small_img.save(os.path.join(output_folder, f"{base_name}_part_{count}.jpg"), "JPEG")
                count += 1

def browse_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_paths:
        image_paths.set("\n".join(file_paths))
        listbox.delete(0, 'end')
        for file_path in file_paths:
            listbox.insert('end', os.path.basename(file_path))

def start_processing():
    processing_label.config(text="")
    file_paths = image_paths.get().split("\n")
    output_folder = folder_name_var.get()
    if file_paths:
        output_size = int(size_var.get())

        # Check if the output folder exists and prompt only once
        if output_folder:
            if os.path.exists(output_folder):
                answer = messagebox.askyesno("Folder Exists", 
                                             f"The folder '{os.path.basename(output_folder)}' already exists. Do you want to continue? If any existing images in the folder were created using these images, they will be overwritten. Otherwise, new images will be added to the existing file set.")
                if not answer:
                    return

        for file_path in file_paths:
            split_and_resize_image(file_path, output_size, output_folder)
        
        processing_label.config(text="Processing completed!")

# Set up the GUI
root = Tk()
root.title("Image Splitter and Resizer")

image_paths = StringVar()
size_var = StringVar(value="512")
folder_name_var = StringVar()

Label(root, text="Select image files:").pack(pady=5)
Button(root, text="Browse", command=browse_images).pack(pady=5)

# Create a listbox with a scrollbar to display selected file names
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

listbox = Listbox(root, yscrollcommand=scrollbar.set, width=50, height=10)
listbox.pack(pady=5)
scrollbar.config(command=listbox.yview)

Label(root, text="Select output image size:").pack(pady=5)
OptionMenu(root, size_var, "512", "768", "1024").pack(pady=5)

Label(root, text="Enter destination folder name (optional):").pack(pady=5)
Entry(root, textvariable=folder_name_var).pack(pady=5)

Button(root, text="Start Processing", command=start_processing).pack(pady=20)

processing_label = Label(root, text="")
processing_label.pack(pady=5)

root.mainloop()
