import os
import sys
import hashlib
import subprocess
import argparse
import datetime
from tkinter import Tk, Label, Button, Entry, filedialog, StringVar, IntVar, BooleanVar, messagebox, Listbox, Scrollbar, OptionMenu, Frame, Checkbutton
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, UnidentifiedImageError

def install_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def check_and_install_dependencies():
    required_packages = {
        "Pillow": "PIL",
        "tkinterdnd2": "tkinterdnd2"
    }
    for package, module in required_packages.items():
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

check_and_install_dependencies()

def get_image_hash(image_path):
    try:
        with open(image_path, 'rb') as f:
            img_hash = hashlib.md5(f.read()).hexdigest()
        return img_hash
    except Exception as e:
        messagebox.showerror("Error", f"Error hashing file {image_path}: {e}")
        return None

def resize_image_keep_aspect_ratio(image, target_size):
    original_width, original_height = image.size
    if original_width > original_height:
        new_width = target_size
        new_height = int(target_size * original_height / original_width)
    else:
        new_height = target_size
        new_width = int(target_size * original_width / original_height)
    return image.resize((new_width, new_height))

def create_output_folder(image_path, custom_folder, images_across, images_high, timestamp):
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    source_directory = os.path.dirname(image_path)

    if images_across == 1 and images_high == 1:
        if custom_folder:
            output_folder = os.path.join(source_directory, custom_folder, timestamp)
        else:
            output_folder = os.path.join(source_directory, timestamp)
    else:
        if custom_folder:
            output_folder = os.path.join(source_directory, custom_folder, base_name)
        else:
            output_folder = os.path.join(source_directory, base_name)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    return output_folder

def split_and_resize_image(image_path, images_across, images_high, output_size, custom_folder, maintain_format, timestamp):
    try:
        output_folder = create_output_folder(image_path, custom_folder, images_across, images_high, timestamp)
        selected_image_hash = get_image_hash(image_path)

        if selected_image_hash is None:
            return

        with Image.open(image_path) as img:
            img_width, img_height = img.size
            small_width = img_width // images_across
            small_height = img_height // images_high
            img_format = img.format if maintain_format else "JPEG"

            count = 1
            for row in range(images_high):
                for col in range(images_across):
                    left = col * small_width
                    upper = row * small_height
                    right = left + small_width
                    lower = upper + small_height

                    small_img = img.crop((left, upper, right, lower))
                    small_img = resize_image_keep_aspect_ratio(small_img, output_size)
                    small_img.save(os.path.join(output_folder, "%s_part_%d.%s" % (os.path.splitext(os.path.basename(image_path))[0], count, img_format.lower())), img_format)
                    count += 1
    except UnidentifiedImageError:
        messagebox.showerror("Error", f"Cannot identify image file {image_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error processing file {image_path}: {e}")

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

def clear_listbox():
    listbox.delete(0, 'end')
    image_paths.set("")

def start_processing():
    try:
        processing_label.config(text="")
        file_paths = image_paths.get().split("\n")
        
        if not file_paths or file_paths == ['']:
            messagebox.showwarning("Warning", "No images selected. Please select some images to process.")
            return

        images_across = images_across_var.get()
        images_high = images_high_var.get()
        custom_folder = folder_name_var.get()
        maintain_format = maintain_format_var.get()
        
        custom_size = custom_size_var.get().strip()
        if custom_size.isdigit():
            output_size = int(custom_size)
        else:
            output_size = int(size_var.get())

        if images_across <= 0:
            images_across = 1
        if images_high <= 0:
            images_high = 1

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        for file_path in file_paths:
            split_and_resize_image(file_path, images_across, images_high, output_size, custom_folder, maintain_format, timestamp)
        
        processing_label.config(text="Processing completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def main():
    try:
        parser = argparse.ArgumentParser(description="Image Splitter and Resizer")
        parser.add_argument('files', nargs='*', help="List of image files to process")
        parser.add_argument('--size', type=int, default=512, help="Base size for resizing (default: 512)")
        parser.add_argument('--custom_size', type=int, help="Custom size for resizing")
        parser.add_argument('--across', type=int, default=1, help="Number of images across (default: 1)")
        parser.add_argument('--high', type=int, default=1, help="Number of images high (default: 1)")
        parser.add_argument('--folder', type=str, help="Custom output folder name (optional)")
        parser.add_argument('--maintain_format', action='store_true', help="Maintain source image format")
        args = parser.parse_args()

        if args.files:
            file_paths = args.files
            custom_folder = args.folder
            images_across = args.across
            images_high = args.high
            output_size = args.custom_size if args.custom_size else args.size
            maintain_format = args.maintain_format
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            for file_path in file_paths:
                split_and_resize_image(file_path, images_across, images_high, output_size, custom_folder, maintain_format, timestamp)
        else:
            global root, image_paths, size_var, custom_size_var, folder_name_var, images_across_var, images_high_var, maintain_format_var, processing_label, listbox

            root = TkinterDnD.Tk()
            root.title("Image Splitter and Resizer")

            # Set minimum window size
            root.minsize(500, 420)

            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)

            main_frame = Frame(root)
            main_frame.grid(sticky='nsew')
            main_frame.grid_columnconfigure(0, weight=1)
            main_frame.grid_rowconfigure(0, weight=1)

            image_paths = StringVar()
            size_var = StringVar(value="512")
            custom_size_var = StringVar()
            folder_name_var = StringVar()
            images_across_var = IntVar(value=1)
            images_high_var = IntVar(value=1)
            maintain_format_var = BooleanVar()

            browse_frame = Frame(main_frame)
            browse_frame.grid(row=0, column=0, pady=5, sticky='w')
            browse_frame.grid_columnconfigure(0, weight=1)
            browse_frame.grid_columnconfigure(1, weight=1)

            Label(browse_frame, text="Select image files:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
            Button(browse_frame, text="Browse", command=browse_images).grid(row=0, column=1, padx=5, pady=5, sticky="w")

            scrollbar = Scrollbar(main_frame)
            scrollbar.grid(row=1, column=1, sticky='ns')

            listbox = Listbox(main_frame, yscrollcommand=scrollbar.set, width=100, height=10)
            listbox.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
            scrollbar.config(command=listbox.yview)

            listbox.drop_target_register(DND_FILES)
            listbox.dnd_bind('<<Drop>>', drop)

            buttons_frame = Frame(main_frame)
            buttons_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky='ew')
            buttons_frame.grid_columnconfigure(0, weight=1)
            buttons_frame.grid_columnconfigure(1, weight=1)

            Button(buttons_frame, text="Clear", command=clear_listbox).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
            Button(buttons_frame, text="Process", command=start_processing).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

            options_frame = Frame(main_frame)
            options_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky='ew')
            options_frame.grid_columnconfigure(0, weight=1)
            options_frame.grid_columnconfigure(1, weight=1)
            options_frame.grid_columnconfigure(2, weight=1)
            options_frame.grid_columnconfigure(3, weight=1)
            options_frame.grid_columnconfigure(4, weight=1)

            Label(options_frame, text="Base Size:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
            OptionMenu(options_frame, size_var, "512", "768", "1024", "2048", "4096").grid(row=0, column=1, padx=5, pady=5, sticky="w")

            Label(options_frame, text="Custom size:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
            Entry(options_frame, textvariable=custom_size_var).grid(row=0, column=3, padx=5, pady=5, sticky="w")

            Label(options_frame, text="Images across:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
            Entry(options_frame, textvariable=images_across_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")

            Label(options_frame, text="Images high:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
            Entry(options_frame, textvariable=images_high_var).grid(row=1, column=3, padx=5, pady=5, sticky="w")

            Label(options_frame, text="Output folder name (optional):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
            Entry(options_frame, textvariable=folder_name_var).grid(row=2, column=1, padx=5, pady=5, sticky="w")

            Checkbutton(options_frame, text="Maintain source image format (e.g., JPG, BMP, PNG)", variable=maintain_format_var).grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky="w")

            processing_label = Label(main_frame, text="")
            processing_label.grid(row=4, column=0, columnspan=2, pady=5, sticky="w")

            root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
