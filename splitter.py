import os
import sys
import hashlib
import subprocess
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, IntVar, messagebox, Listbox, Scrollbar, OptionMenu
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image

def install_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def check_and_install_dependencies():
    required_packages = ["Pillow", "tkinterdnd2"]
    for package in required_packages:
        install_package(package)

check_and_install_dependencies()

def get_image_hash(image_path):
    with open(image_path, 'rb') as f:
        img_hash = hashlib.md5(f.read()).hexdigest()
    return img_hash

def resize_image_keep_aspect_ratio(image, target_size):
    original_width, original_height = image.size
    if original_width > original_height:
        new_width = target_size
        new_height = int(target_size * original_height / original_width)
    else:
        new_height = target_size
        new_width = int(target_size * original_width / original_height)
    return image.resize((new_width, new_height))

def split_and_resize_image(image_path, images_across, images_high, output_size, custom_folder):
    # Get the base name and directory of the file without extension
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    source_directory = os.path.dirname(image_path)
    output_folder = os.path.join(source_directory, custom_folder or base_name)
    
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
        img_width, img_height = img.size
        small_width = img_width // images_across
        small_height = img_height // images_high

        # Split the image into the specified number of smaller images
        count = 1
        for row in range(images_high):
            for col in range(images_across):
                # Calculate the coordinates of the current small image
                left = col * small_width
                upper = row * small_height
                right = left + small_width
                lower = upper + small_height

                # Crop the image
                small_img = img.crop((left, upper, right, lower))
                # Resize the image to the specified output size while keeping aspect ratio
                small_img = resize_image_keep_aspect_ratio(small_img, output_size)

                # Save the small image as a jpg file
                small_img.save(os.path.join(output_folder, f"{base_name}_part_{count}.jpg"), "JPEG")
                count += 1

def browse_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")])
    if file_paths:
        image_paths.set("\n".join(file_paths))
        listbox.delete(0, 'end')
        for file_path in file_paths:
            listbox.insert('end', file_path)

def drop(event):
    files = root.tk.splitlist(event.data)
    current_files = listbox.get(0, 'end')
    for file in files:
        if os.path.splitext(file)[1].lower() in [".jpg", ".jpeg", ".png", ".bmp", ".webp"]:
            if file not in current_files:
                listbox.insert('end', file)
                current_files += (file,)
    image_paths.set("\n".join(listbox.get(0, 'end')))

def start_processing():
    processing_label.config(text="")
    file_paths = image_paths.get().split("\n")
    images_across = images_across_var.get()
    images_high = images_high_var.get()
    custom_folder = folder_name_var.get()
    if file_paths:
        output_size = int(size_var.get())

        for file_path in file_paths:
            split_and_resize_image(file_path, images_across, images_high, output_size, custom_folder)
        
        processing_label.config(text="Processing completed!")

# Set up the GUI
root = TkinterDnD.Tk()
root.title("Image Splitter and Resizer")

image_paths = StringVar()
size_var = StringVar(value="512")
folder_name_var = StringVar()
images_across_var = IntVar(value=4)
images_high_var = IntVar(value=2)

Label(root, text="Select image files:").pack(pady=5)
Button(root, text="Browse", command=browse_images).pack(pady=5)

# Create a listbox with a scrollbar to display selected file names
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

listbox = Listbox(root, yscrollcommand=scrollbar.set, width=100, height=10)
listbox.pack(pady=5)
scrollbar.config(command=listbox.yview)

# Enable drag and drop
listbox.drop_target_register(DND_FILES)
listbox.dnd_bind('<<Drop>>', drop)

Label(root, text="Select output image size:").pack(pady=5)
OptionMenu(root, size_var, "512", "768", "1024").pack(pady=5)

Label(root, text="Enter number of images across:").pack(pady=5)
Entry(root, textvariable=images_across_var).pack(pady=5)

Label(root, text="Enter number of images high:").pack(pady=5)
Entry(root, textvariable=images_high_var).pack(pady=5)

Label(root, text="Enter destination folder name (optional):").pack(pady=5)
Entry(root, textvariable=folder_name_var).pack(pady=5)

Button(root, text="Start Processing", command=start_processing).pack(pady=20)

processing_label = Label(root, text="")
processing_label.pack(pady=5)

root.mainloop()
