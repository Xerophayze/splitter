import sys
import argparse
import datetime
import threading
from pathlib import Path
from tkinter import filedialog, StringVar, IntVar, BooleanVar, messagebox
from tkinter import ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

try:
    import sv_ttk
    THEME_AVAILABLE = True
except ImportError:
    THEME_AVAILABLE = False


class ImageItem:
    """Represents an image with its individual processing settings."""
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        # Individual settings (None means use global defaults)
        self.base_size = None
        self.custom_size = None
        self.images_across = None
        self.images_high = None
        self.maintain_format = None
        self.custom_folder = None
        
    def get_display_name(self):
        """Get display name for the list."""
        name = self.file_path.name
        if self.has_custom_settings():
            name = f"⚙ {name}"
        return name
        
    def has_custom_settings(self):
        """Check if this image has custom settings."""
        return any([
            self.base_size is not None,
            self.custom_size is not None,
            self.images_across is not None,
            self.images_high is not None,
            self.maintain_format is not None,
            self.custom_folder is not None and self.custom_folder != ""
        ])
        
    def get_settings_summary(self):
        """Get a summary of custom settings."""
        if not self.has_custom_settings():
            return "Using global defaults"
        
        parts = []
        if self.custom_size:
            parts.append(f"Size: {self.custom_size}")
        elif self.base_size:
            parts.append(f"Size: {self.base_size}")
            
        if self.images_across or self.images_high:
            across = self.images_across or 1
            high = self.images_high or 1
            parts.append(f"Grid: {across}×{high}")
            
        if self.maintain_format is not None:
            parts.append("Keep format" if self.maintain_format else "Convert to JPEG")
            
        if self.custom_folder and self.custom_folder.strip():
            parts.append(f"Folder: {self.custom_folder}")
            
        return " | ".join(parts) if parts else "Using global defaults"


class ImageSplitterConfig:
    """Configuration and state management for image splitting operations."""
    def __init__(self):
        self.image_items = []  # List of ImageItem objects
        self.selected_item = None
        self.processing = False


def resize_image_keep_aspect_ratio(image, target_size):
    """Resize image maintaining aspect ratio."""
    original_width, original_height = image.size
    if original_width > original_height:
        new_width = target_size
        new_height = int(target_size * original_height / original_width)
    else:
        new_height = target_size
        new_width = int(target_size * original_width / original_height)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)


def create_output_folder(image_path, custom_folder, images_across, images_high, timestamp):
    """Create output folder using pathlib for cross-platform compatibility."""
    image_path = Path(image_path)
    base_name = image_path.stem
    source_directory = image_path.parent

    if images_across == 1 and images_high == 1:
        if custom_folder:
            output_folder = source_directory / custom_folder / timestamp
        else:
            output_folder = source_directory / timestamp
    else:
        if custom_folder:
            output_folder = source_directory / custom_folder / base_name
        else:
            output_folder = source_directory / base_name

    output_folder.mkdir(parents=True, exist_ok=True)
    return output_folder


def split_and_resize_image(image_path, images_across, images_high, output_size, custom_folder, maintain_format, timestamp, progress_callback=None):
    """Split and resize image with optional progress callback."""
    output_folder = create_output_folder(image_path, custom_folder, images_across, images_high, timestamp)
    image_path = Path(image_path)

    with Image.open(image_path) as img:
        img_width, img_height = img.size
        small_width = img_width // images_across
        small_height = img_height // images_high
        img_format = img.format if maintain_format else "JPEG"

        total_parts = images_across * images_high
        count = 1
        
        for row in range(images_high):
            for col in range(images_across):
                left = col * small_width
                upper = row * small_height
                right = left + small_width
                lower = upper + small_height

                small_img = img.crop((left, upper, right, lower))
                small_img = resize_image_keep_aspect_ratio(small_img, output_size)
                
                output_name = f"{image_path.stem}_part_{count}.{img_format.lower()}"
                small_img.save(output_folder / output_name, img_format)
                
                if progress_callback:
                    progress_callback(count, total_parts)
                
                count += 1


class ImageSplitterGUI:
    """Modern GUI for image splitting application."""
    
    VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
    
    PREVIEW_SIZE = 300
    
    def __init__(self, root):
        self.root = root
        self.root.title("Image Splitter and Resizer - Per-Image Settings")
        self.root.minsize(900, 600)
        
        # Apply modern theme
        if THEME_AVAILABLE:
            sv_ttk.set_theme("dark")
        
        self.config = ImageSplitterConfig()
        self.preview_image = None
        self.setup_variables()
        self.setup_ui()
        self.validate_inputs()
        
    def setup_variables(self):
        """Initialize tkinter variables."""
        # Global defaults
        self.global_size_var = StringVar(value="512")
        self.global_custom_size_var = StringVar()
        self.global_folder_name_var = StringVar()
        self.global_images_across_var = IntVar(value=1)
        self.global_images_high_var = IntVar(value=1)
        self.global_maintain_format_var = BooleanVar()
        
        # Per-image settings
        self.size_var = StringVar(value="512")
        self.custom_size_var = StringVar()
        self.folder_name_var = StringVar()
        self.images_across_var = IntVar(value=1)
        self.images_high_var = IntVar(value=1)
        self.maintain_format_var = BooleanVar()
        self.use_custom_settings_var = BooleanVar(value=False)
        
        self.status_var = StringVar(value="Ready")
        
        # Add validation traces
        self.custom_size_var.trace('w', lambda *args: self.validate_inputs())
        self.images_across_var.trace('w', lambda *args: self.validate_inputs())
        self.images_high_var.trace('w', lambda *args: self.validate_inputs())
        self.use_custom_settings_var.trace('w', lambda *args: self.on_custom_settings_toggle())
        
    def setup_ui(self):
        """Create the user interface."""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky='nsew')
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create paned window for resizable sections
        paned = ttk.PanedWindow(main_frame, orient='horizontal')
        paned.grid(row=0, column=0, sticky='nsew')
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Left panel - File list and global settings
        left_panel = ttk.Frame(paned)
        paned.add(left_panel, weight=1)
        
        # Right panel - Preview and per-image settings
        right_panel = ttk.Frame(paned)
        paned.add(right_panel, weight=1)
        
        # Setup left panel
        self.create_file_section(left_panel)
        self.create_global_settings_section(left_panel)
        
        # Setup right panel
        self.create_preview_section(right_panel)
        self.create_per_image_settings_section(right_panel)
        
        # Action buttons and status at bottom
        self.create_action_buttons(main_frame)
        self.create_status_section(main_frame)
        
    def create_file_section(self, parent):
        """Create file selection UI."""
        file_frame = ttk.LabelFrame(parent, text="Image Files", padding="10")
        file_frame.grid(row=0, column=0, sticky='nsew', pady=(0, 10))
        file_frame.grid_rowconfigure(1, weight=1)
        file_frame.grid_columnconfigure(0, weight=1)
        
        # Browse button
        btn_frame = ttk.Frame(file_frame)
        btn_frame.grid(row=0, column=0, sticky='ew', pady=(0, 5))
        
        self.browse_btn = ttk.Button(btn_frame, text="📁 Browse Images", command=self.browse_images)
        self.browse_btn.pack(side='left', padx=(0, 5))
        self.create_tooltip(self.browse_btn, "Select one or more image files to process")
        
        ttk.Label(btn_frame, text="or drag and drop files below", foreground="gray").pack(side='left')
        
        # Listbox with scrollbar
        list_frame = ttk.Frame(file_frame)
        list_frame.grid(row=1, column=0, sticky='nsew')
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # Use Treeview with columns for better display
        self.listbox = ttk.Treeview(list_frame, yscrollcommand=scrollbar.set, 
                                    columns=('settings',), show='tree', height=10)
        self.listbox.grid(row=0, column=0, sticky='nsew')
        self.listbox.column('#0', width=300)
        self.listbox.column('settings', width=200)
        scrollbar.config(command=self.listbox.yview)
        
        # Bind selection event
        self.listbox.bind('<<TreeviewSelect>>', self.on_image_select)
        
        # Enable drag and drop
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind('<<Drop>>', self.on_drop)
        
        # Buttons
        btn_frame2 = ttk.Frame(file_frame)
        btn_frame2.grid(row=2, column=0, sticky='ew', pady=(5, 0))
        
        self.clear_btn = ttk.Button(btn_frame2, text="Clear List", command=self.clear_list)
        self.clear_btn.pack(side='left', padx=(0, 5))
        
        self.remove_btn = ttk.Button(btn_frame2, text="Remove Selected", command=self.remove_selected)
        self.remove_btn.pack(side='left')
        
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
    def create_global_settings_section(self, parent):
        """Create global default settings UI."""
        settings_frame = ttk.LabelFrame(parent, text="Global Default Settings", padding="10")
        settings_frame.grid(row=1, column=0, sticky='ew', pady=(0, 10))
        
        # Size options
        size_frame = ttk.Frame(settings_frame)
        size_frame.grid(row=0, column=0, columnspan=2, sticky='ew', pady=(0, 5))
        
        ttk.Label(size_frame, text="Base Size:").pack(side='left', padx=(0, 5))
        size_combo = ttk.Combobox(size_frame, textvariable=self.global_size_var, 
                                  values=["512", "768", "1024", "2048", "4096"], 
                                  width=10, state='readonly')
        size_combo.pack(side='left', padx=(0, 10))
        self.create_tooltip(size_combo, "Default output size for all images")
        
        ttk.Label(size_frame, text="Custom:").pack(side='left', padx=(0, 5))
        ttk.Entry(size_frame, textvariable=self.global_custom_size_var, width=10).pack(side='left')
        
        # Grid options
        grid_frame = ttk.Frame(settings_frame)
        grid_frame.grid(row=1, column=0, columnspan=2, sticky='ew', pady=(0, 5))
        
        ttk.Label(grid_frame, text="Across:").pack(side='left', padx=(0, 5))
        ttk.Spinbox(grid_frame, from_=1, to=10, textvariable=self.global_images_across_var, width=8).pack(side='left', padx=(0, 10))
        
        ttk.Label(grid_frame, text="High:").pack(side='left', padx=(0, 5))
        ttk.Spinbox(grid_frame, from_=1, to=10, textvariable=self.global_images_high_var, width=8).pack(side='left')
        
        # Other options
        ttk.Checkbutton(settings_frame, text="Maintain source format", 
                       variable=self.global_maintain_format_var).grid(row=2, column=0, columnspan=2, sticky='w')
        
        ttk.Label(settings_frame, text="Output Folder:").grid(row=3, column=0, sticky='w', pady=(5, 0))
        ttk.Entry(settings_frame, textvariable=self.global_folder_name_var).grid(row=3, column=1, sticky='ew', pady=(5, 0))
        settings_frame.grid_columnconfigure(1, weight=1)
        
    def create_preview_section(self, parent):
        """Create image preview UI."""
        preview_frame = ttk.LabelFrame(parent, text="Preview", padding="10")
        preview_frame.grid(row=0, column=0, sticky='nsew', pady=(0, 10))
        preview_frame.grid_rowconfigure(1, weight=1)
        preview_frame.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        # Info label
        self.preview_info_label = ttk.Label(preview_frame, text="Select an image to preview")
        self.preview_info_label.grid(row=0, column=0, sticky='ew', pady=(0, 5))
        
        # Preview canvas
        preview_canvas_frame = ttk.Frame(preview_frame, relief='sunken', borderwidth=2)
        preview_canvas_frame.grid(row=1, column=0, sticky='nsew')
        preview_canvas_frame.grid_rowconfigure(0, weight=1)
        preview_canvas_frame.grid_columnconfigure(0, weight=1)
        
        self.preview_label = ttk.Label(preview_canvas_frame, text="No image selected", 
                                       anchor='center', background='#2b2b2b')
        self.preview_label.grid(row=0, column=0, sticky='nsew')
        
    def create_per_image_settings_section(self, parent):
        """Create per-image settings UI."""
        settings_frame = ttk.LabelFrame(parent, text="Image-Specific Settings", padding="10")
        settings_frame.grid(row=1, column=0, sticky='nsew')
        settings_frame.grid_columnconfigure(0, weight=1)
        
        # Enable custom settings checkbox
        self.use_custom_check = ttk.Checkbutton(settings_frame, 
                                               text="Use custom settings for this image",
                                               variable=self.use_custom_settings_var)
        self.use_custom_check.grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 10))
        self.create_tooltip(self.use_custom_check, "Override global defaults for selected image")
        
        # Settings container
        self.settings_container = ttk.Frame(settings_frame)
        self.settings_container.grid(row=1, column=0, columnspan=2, sticky='nsew')
        self.settings_container.grid_columnconfigure(1, weight=1)
        
        # Size options
        row = 0
        ttk.Label(self.settings_container, text="Base Size:").grid(row=row, column=0, sticky='w', pady=2)
        size_combo = ttk.Combobox(self.settings_container, textvariable=self.size_var, 
                                  values=["512", "768", "1024", "2048", "4096"], 
                                  width=15, state='readonly')
        size_combo.grid(row=row, column=1, sticky='w', pady=2)
        
        row += 1
        ttk.Label(self.settings_container, text="Custom Size:").grid(row=row, column=0, sticky='w', pady=2)
        self.custom_size_entry = ttk.Entry(self.settings_container, textvariable=self.custom_size_var, width=15)
        self.custom_size_entry.grid(row=row, column=1, sticky='w', pady=2)
        
        row += 1
        ttk.Label(self.settings_container, text="Images Across:").grid(row=row, column=0, sticky='w', pady=2)
        self.across_entry = ttk.Spinbox(self.settings_container, from_=1, to=10, 
                                       textvariable=self.images_across_var, width=15)
        self.across_entry.grid(row=row, column=1, sticky='w', pady=2)
        
        row += 1
        ttk.Label(self.settings_container, text="Images High:").grid(row=row, column=0, sticky='w', pady=2)
        self.high_entry = ttk.Spinbox(self.settings_container, from_=1, to=10, 
                                     textvariable=self.images_high_var, width=15)
        self.high_entry.grid(row=row, column=1, sticky='w', pady=2)
        
        row += 1
        ttk.Label(self.settings_container, text="Output Folder:").grid(row=row, column=0, sticky='w', pady=2)
        ttk.Entry(self.settings_container, textvariable=self.folder_name_var).grid(row=row, column=1, sticky='ew', pady=2)
        
        row += 1
        ttk.Checkbutton(self.settings_container, text="Maintain source format", 
                       variable=self.maintain_format_var).grid(row=row, column=0, columnspan=2, sticky='w', pady=5)
        
        # Apply/Reset buttons
        row += 1
        btn_frame = ttk.Frame(self.settings_container)
        btn_frame.grid(row=row, column=0, columnspan=2, sticky='ew', pady=(10, 0))
        
        self.apply_btn = ttk.Button(btn_frame, text="Apply to Image", command=self.apply_settings)
        self.apply_btn.pack(side='left', padx=(0, 5))
        
        self.reset_btn = ttk.Button(btn_frame, text="Reset to Defaults", command=self.reset_to_defaults)
        self.reset_btn.pack(side='left')
        
        # Initially disable settings
        self.toggle_settings_state(False)
        
    def create_action_buttons(self, parent):
        """Create action buttons."""
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=1, column=0, sticky='ew', pady=(10, 0))
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        
        self.process_btn = ttk.Button(button_frame, text="▶ Process All Images", 
                                      command=self.start_processing, style='Accent.TButton')
        self.process_btn.grid(row=0, column=0, sticky='ew', padx=(0, 5))
        
        self.cancel_btn = ttk.Button(button_frame, text="⏹ Cancel", 
                                     command=self.cancel_processing, state='disabled')
        self.cancel_btn.grid(row=0, column=1, sticky='ew')
        
    def create_status_section(self, parent):
        """Create status and progress display."""
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=2, column=0, sticky='ew', pady=(10, 0))
        status_frame.grid_columnconfigure(0, weight=1)
        
        self.progress = ttk.Progressbar(status_frame, mode='determinate')
        self.progress.grid(row=0, column=0, sticky='ew', pady=(0, 5))
        
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var)
        self.status_label.grid(row=1, column=0, sticky='w')
        
    def create_tooltip(self, widget, text):
        """Create tooltip for widget."""
        def on_enter(event):
            tooltip = ttk.Label(self.root, text=text, relief='solid', borderwidth=1, 
                               background='#ffffe0', foreground='#000000', padding=5)
            tooltip.place(x=event.x_root - self.root.winfo_rootx() + 10, 
                         y=event.y_root - self.root.winfo_rooty() + 10)
            widget.tooltip = tooltip
            
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                delattr(widget, 'tooltip')
                
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
        
    def toggle_settings_state(self, enabled):
        """Enable or disable per-image settings widgets."""
        state = 'normal' if enabled else 'disabled'
        for child in self.settings_container.winfo_children():
            if isinstance(child, (ttk.Entry, ttk.Spinbox, ttk.Combobox, ttk.Checkbutton, ttk.Button)):
                child.configure(state=state)
                
    def on_custom_settings_toggle(self):
        """Handle custom settings checkbox toggle."""
        enabled = self.use_custom_settings_var.get()
        print(f"Custom settings toggle: {enabled}")
        self.toggle_settings_state(enabled)
    
    def on_image_select(self, event):
        """Handle image selection in listbox."""
        selection = self.listbox.selection()
        if not selection:
            self.config.selected_item = None
            self.clear_preview()
            return
            
        item_id = selection[0]
        for img_item in self.config.image_items:
            if str(id(img_item)) == item_id:
                self.config.selected_item = img_item
                self.load_preview(img_item)
                self.load_image_settings(img_item)
                break
                
    def load_preview(self, img_item):
        """Load and display image preview."""
        try:
            with Image.open(img_item.file_path) as img:
                width, height = img.size
                file_size = img_item.file_path.stat().st_size / 1024
                
                info_text = f"{img_item.file_path.name} | {width}×{height} | {file_size:.1f} KB"
                self.preview_info_label.config(text=info_text)
                
                img.thumbnail((self.PREVIEW_SIZE, self.PREVIEW_SIZE), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                
                self.preview_image = photo
                self.preview_label.config(image=photo, text="")
        except Exception as e:
            self.preview_label.config(image='', text=f"Error loading preview:\n{str(e)}")
            self.preview_info_label.config(text="Error loading image")
            
    def clear_preview(self):
        """Clear the preview display."""
        self.preview_label.config(image='', text="No image selected")
        self.preview_info_label.config(text="Select an image to preview")
        self.preview_image = None
        self.use_custom_settings_var.set(False)
        self.toggle_settings_state(False)
        
    def load_image_settings(self, img_item):
        """Load settings for selected image."""
        if img_item.has_custom_settings():
            self.use_custom_settings_var.set(True)
            self.size_var.set(str(img_item.base_size or self.global_size_var.get()))
            self.custom_size_var.set(str(img_item.custom_size or ""))
            self.images_across_var.set(img_item.images_across or self.global_images_across_var.get())
            self.images_high_var.set(img_item.images_high or self.global_images_high_var.get())
            self.maintain_format_var.set(img_item.maintain_format if img_item.maintain_format is not None 
                                        else self.global_maintain_format_var.get())
            self.folder_name_var.set(img_item.custom_folder or self.global_folder_name_var.get())
        else:
            self.use_custom_settings_var.set(False)
            self.size_var.set(self.global_size_var.get())
            self.custom_size_var.set(self.global_custom_size_var.get())
            self.images_across_var.set(self.global_images_across_var.get())
            self.images_high_var.set(self.global_images_high_var.get())
            self.maintain_format_var.set(self.global_maintain_format_var.get())
            self.folder_name_var.set(self.global_folder_name_var.get())
            
    def apply_settings(self):
        """Apply current settings to selected image."""
        print(f"\n=== apply_settings called ===")
        print(f"Selected item: {self.config.selected_item}")
        print(f"use_custom_settings_var.get(): {self.use_custom_settings_var.get()}")
        
        if not self.config.selected_item:
            print("No selected item, returning")
            return
            
        if self.use_custom_settings_var.get():
            print("✓ Custom settings enabled, applying...")
            img_item = self.config.selected_item
            img_item.base_size = int(self.size_var.get())
            
            custom_size = self.custom_size_var.get().strip()
            img_item.custom_size = int(custom_size) if custom_size.isdigit() else None
            
            img_item.images_across = self.images_across_var.get()
            img_item.images_high = self.images_high_var.get()
            img_item.maintain_format = self.maintain_format_var.get()
            
            folder = self.folder_name_var.get().strip()
            img_item.custom_folder = folder if folder else None
            
            # Debug: Print what was saved
            print(f"Applied settings to {img_item.file_path.name}:")
            print(f"  base_size: {img_item.base_size}")
            print(f"  custom_size: {img_item.custom_size}")
            print(f"  images_across: {img_item.images_across}")
            print(f"  images_high: {img_item.images_high}")
            print(f"  maintain_format: {img_item.maintain_format}")
            print(f"  custom_folder: {img_item.custom_folder}")
            print(f"  has_custom_settings(): {img_item.has_custom_settings()}")
            
            self.update_listbox_item(img_item)
            self.status_var.set(f"✓ Applied custom settings to {img_item.file_path.name}")
        else:
            print("✗ Custom settings NOT enabled, calling reset_to_defaults()")
            self.reset_to_defaults()
            
    def reset_to_defaults(self):
        """Reset selected image to use global defaults."""
        if not self.config.selected_item:
            return
            
        img_item = self.config.selected_item
        img_item.base_size = None
        img_item.custom_size = None
        img_item.images_across = None
        img_item.images_high = None
        img_item.maintain_format = None
        img_item.custom_folder = None
        
        self.use_custom_settings_var.set(False)
        self.load_image_settings(img_item)
        self.update_listbox_item(img_item)
        self.status_var.set(f"✓ Reset {img_item.file_path.name} to global defaults")
        
    def update_listbox_item(self, img_item):
        """Update listbox display for an image item."""
        item_id = str(id(img_item))
        print(f"Updating listbox for item_id: {item_id}")
        print(f"  Display name: {img_item.get_display_name()}")
        print(f"  Settings summary: {img_item.get_settings_summary()}")
        if self.listbox.exists(item_id):
            self.listbox.item(item_id, text=img_item.get_display_name(), 
                            values=(img_item.get_settings_summary(),))
            print(f"  ✓ Listbox updated")
        else:
            print(f"  ✗ Item ID not found in listbox!")
        
    def validate_inputs(self):
        """Validate user inputs and update UI state."""
        valid = True
        
        # Validate custom size
        custom_size = self.custom_size_var.get().strip()
        if custom_size and not custom_size.isdigit():
            valid = False
            self.custom_size_entry.state(['invalid'])
        else:
            self.custom_size_entry.state(['!invalid'])
            
        # Validate grid dimensions
        try:
            across = self.images_across_var.get()
            high = self.images_high_var.get()
            if across <= 0 or high <= 0:
                valid = False
        except:
            valid = False
            
        # Enable/disable process button
        has_images = len(self.config.image_items) > 0
        if valid and has_images and not self.config.processing:
            self.process_btn.state(['!disabled'])
        else:
            self.process_btn.state(['disabled'])
            
        return valid
        
    def browse_images(self):
        """Open file dialog to select images."""
        file_paths = filedialog.askopenfilenames(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
        )
        if file_paths:
            for file_path in file_paths:
                if not any(item.file_path == Path(file_path) for item in self.config.image_items):
                    img_item = ImageItem(file_path)
                    self.config.image_items.append(img_item)
                    item_id = str(id(img_item))
                    self.listbox.insert('', 'end', iid=item_id, 
                                       text=img_item.get_display_name(),
                                       values=(img_item.get_settings_summary(),))
            self.validate_inputs()
            
    def on_drop(self, event):
        """Handle drag and drop files."""
        files = self.root.tk.splitlist(event.data)
        
        for file in files:
            file_path = Path(file)
            if file_path.suffix.lower() in self.VALID_EXTENSIONS:
                if not any(item.file_path == file_path for item in self.config.image_items):
                    img_item = ImageItem(file_path)
                    self.config.image_items.append(img_item)
                    item_id = str(id(img_item))
                    self.listbox.insert('', 'end', iid=item_id,
                                       text=img_item.get_display_name(),
                                       values=(img_item.get_settings_summary(),))
                    
        self.validate_inputs()
        
    def clear_list(self):
        """Clear the file list."""
        for item in self.listbox.get_children():
            self.listbox.delete(item)
        self.config.image_items.clear()
        self.clear_preview()
        self.validate_inputs()
        
    def remove_selected(self):
        """Remove selected image from list."""
        selection = self.listbox.selection()
        if not selection:
            return
            
        item_id = selection[0]
        # Find and remove from image_items
        for img_item in self.config.image_items[:]:
            if str(id(img_item)) == item_id:
                self.config.image_items.remove(img_item)
                break
                
        # Remove from listbox
        self.listbox.delete(item_id)
        self.clear_preview()
        self.validate_inputs()
        
    def start_processing(self):
        """Start image processing in background thread."""
        if self.config.processing:
            return
            
        if not self.config.image_items:
            messagebox.showwarning("Warning", "No images selected. Please select some images to process.")
            return
        
        # Update UI state
        self.config.processing = True
        self.process_btn.state(['disabled'])
        self.cancel_btn.state(['!disabled'])
        self.progress['value'] = 0
        self.progress['maximum'] = len(self.config.image_items)
        
        # Start processing thread
        thread = threading.Thread(
            target=self.process_images,
            daemon=True
        )
        thread.start()
        
    def process_images(self):
        """Process images in background thread."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        total_files = len(self.config.image_items)
        
        try:
            for idx, img_item in enumerate(self.config.image_items, 1):
                if not self.config.processing:
                    break
                    
                self.update_status(f"Processing {idx}/{total_files}: {img_item.file_path.name}")
                
                # Get effective settings for this image
                custom_size = self.global_custom_size_var.get().strip()
                output_size = img_item.custom_size or (int(custom_size) if custom_size.isdigit() else int(self.global_size_var.get()))
                
                if img_item.base_size and not img_item.custom_size:
                    output_size = img_item.base_size
                    
                across = img_item.images_across or self.global_images_across_var.get()
                high = img_item.images_high or self.global_images_high_var.get()
                folder = img_item.custom_folder or self.global_folder_name_var.get()
                format_setting = img_item.maintain_format if img_item.maintain_format is not None else self.global_maintain_format_var.get()
                
                split_and_resize_image(
                    str(img_item.file_path), across, high, output_size,
                    folder, format_setting, timestamp
                )
                
                self.root.after(0, lambda v=idx: self.progress.configure(value=v))
                
            if self.config.processing:
                self.update_status("✓ Processing completed successfully!")
                messagebox.showinfo("Success", f"Processed {total_files} image(s) successfully!")
        except Exception as e:
            self.update_status(f"✗ Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.config.processing = False
            self.root.after(0, self.reset_ui)
            
    def cancel_processing(self):
        """Cancel ongoing processing."""
        self.config.processing = False
        self.update_status("Processing cancelled")
        
    def update_status(self, message):
        """Update status message (thread-safe)."""
        self.root.after(0, lambda: self.status_var.set(message))
        
    def reset_ui(self):
        """Reset UI to ready state."""
        self.process_btn.state(['!disabled'])
        self.cancel_btn.state(['disabled'])
        self.validate_inputs()


def main():
    """Main entry point for the application."""
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
        # CLI mode
        file_paths = args.files
        custom_folder = args.folder
        images_across = args.across
        images_high = args.high
        output_size = args.custom_size if args.custom_size else args.size
        maintain_format = args.maintain_format
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        print(f"Processing {len(file_paths)} image(s)...")
        for idx, file_path in enumerate(file_paths, 1):
            print(f"  [{idx}/{len(file_paths)}] {Path(file_path).name}")
            split_and_resize_image(file_path, images_across, images_high, output_size, 
                                  custom_folder, maintain_format, timestamp)
        print("✓ Processing completed!")
    else:
        # GUI mode
        root = TkinterDnD.Tk()
        app = ImageSplitterGUI(root)
        root.mainloop()


if __name__ == "__main__":
    main()
