# Per-Image Settings Implementation Guide

## Summary
This guide shows how to add per-image settings to the modernized splitter. The base classes (ImageItem, updated ImageSplitterConfig) have been added to `splitter_with_per_image.py`.

## What's Already Done ✓

1. **ImageItem class** - Stores per-image settings
2. **Updated ImageSplitterConfig** - Now uses image_items list
3. **ImageTk import** - Added for preview functionality

## What Needs To Be Added

### 1. Update GUI __init__ and setup_variables

Add preview image storage and per-image variables:

```python
def __init__(self, root):
    # ... existing code ...
    self.preview_image = None  # ADD THIS
    self.config = ImageSplitterConfig()
    self.setup_variables()
    self.setup_ui()
    self.validate_inputs()

def setup_variables(self):
    """Initialize tkinter variables."""
    # Global defaults (rename existing vars)
    self.global_size_var = StringVar(value="512")
    self.global_custom_size_var = StringVar()
    self.global_folder_name_var = StringVar()
    self.global_images_across_var = IntVar(value=1)
    self.global_images_high_var = IntVar(value=1)
    self.global_maintain_format_var = BooleanVar()
    
    # Per-image settings (NEW)
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
```

### 2. Update setup_ui to use PanedWindow

```python
def setup_ui(self):
    """Create the user interface."""
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
    
    # Setup panels
    self.create_file_section(left_panel)
    self.create_global_settings_section(left_panel)  # RENAMED
    self.create_preview_section(right_panel)  # NEW
    self.create_per_image_settings_section(right_panel)  # NEW
    
    # Action buttons and status at bottom
    self.create_action_buttons(main_frame)
    self.create_status_section(main_frame)
```

### 3. Update Listbox to Show Settings

In `create_file_section`, change the Treeview to have columns:

```python
# Use Treeview with columns for better display
self.listbox = ttk.Treeview(list_frame, yscrollcommand=scrollbar.set, 
                            columns=('settings',), show='tree', height=10)
self.listbox.grid(row=0, column=0, sticky='nsew')
self.listbox.column('#0', width=300)
self.listbox.column('settings', width=200)
scrollbar.config(command=self.listbox.yview)

# Bind selection event
self.listbox.bind('<<TreeviewSelect>>', self.on_image_select)

# ... existing drag and drop code ...

# Add Remove button
btn_frame2 = ttk.Frame(file_frame)
btn_frame2.grid(row=2, column=0, sticky='ew', pady=(5, 0))

self.clear_btn = ttk.Button(btn_frame2, text="Clear List", command=self.clear_list)
self.clear_btn.pack(side='left', padx=(0, 5))

self.remove_btn = ttk.Button(btn_frame2, text="Remove Selected", command=self.remove_selected)
self.remove_btn.pack(side='left')
```

### 4. Add New Methods

#### Preview Section
```python
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
```

#### Per-Image Settings Section
```python
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
    
    # Settings container
    self.settings_container = ttk.Frame(settings_frame)
    self.settings_container.grid(row=1, column=0, columnspan=2, sticky='nsew')
    self.settings_container.grid_columnconfigure(1, weight=1)
    
    # Add all the settings controls (size, grid, folder, format)
    # ... (see full implementation in PER_IMAGE_SETTINGS.md)
    
    # Apply/Reset buttons
    btn_frame = ttk.Frame(self.settings_container)
    btn_frame.grid(row=6, column=0, columnspan=2, sticky='ew', pady=(10, 0))
    
    self.apply_btn = ttk.Button(btn_frame, text="Apply to Image", command=self.apply_settings)
    self.apply_btn.pack(side='left', padx=(0, 5))
    
    self.reset_btn = ttk.Button(btn_frame, text="Reset to Defaults", command=self.reset_to_defaults)
    self.reset_btn.pack(side='left')
    
    # Initially disable settings
    self.toggle_settings_state(False)
```

#### Event Handlers
```python
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
            
            img.thumbnail((300, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            self.preview_image = photo
            self.preview_label.config(image=photo, text="")
    except Exception as e:
        self.preview_label.config(image='', text=f"Error loading preview:\n{str(e)}")

def apply_settings(self):
    """Apply current settings to selected image."""
    if not self.config.selected_item:
        return
        
    if self.use_custom_settings_var.get():
        img_item = self.config.selected_item
        img_item.base_size = int(self.size_var.get())
        
        custom_size = self.custom_size_var.get().strip()
        img_item.custom_size = int(custom_size) if custom_size.isdigit() else None
        
        img_item.images_across = self.images_across_var.get()
        img_item.images_high = self.images_high_var.get()
        img_item.maintain_format = self.maintain_format_var.get()
        img_item.custom_folder = self.folder_name_var.get()
        
        self.update_listbox_item(img_item)
        self.status_var.set(f"✓ Applied custom settings to {img_item.file_path.name}")

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
```

### 5. Update browse_images and on_drop

Change to use ImageItem objects:

```python
def browse_images(self):
    """Open file dialog to select images."""
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.webp")]
    )
    if file_paths:
        for file_path in file_paths:
            # Check if already in list
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
```

### 6. Update Processing Logic

Modify `process_images` to use per-image settings:

```python
def process_images(self, file_paths, images_across, images_high, output_size, 
                  custom_folder, maintain_format):
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
```

### 7. Update validate_inputs

```python
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
```

## Testing Steps

1. Run `install.bat` to ensure all dependencies are installed
2. Run `python splitter_with_per_image.py`
3. Add multiple images
4. Click on an image - should see preview
5. Enable "Use custom settings"
6. Change settings and click "Apply"
7. Image should show ⚙ icon
8. Process all images - each should use its settings

## Quick Start

The file `splitter_with_per_image.py` has the base classes ready. You need to:

1. Update the GUI class methods as shown above
2. Test the functionality
3. Adjust UI layout as needed

## Files

- `splitter.py` - Original version
- `splitter_modern.py` - Modernized version (no per-image settings)
- `splitter_with_per_image.py` - Base for per-image settings (needs GUI updates)
- `PER_IMAGE_SETTINGS.md` - Feature documentation
- `IMPLEMENTATION_GUIDE.md` - This file

## Next Steps

Due to the size of the changes, I recommend:

1. Review the implementation guide
2. Test each section as you add it
3. Start with preview functionality
4. Then add per-image settings UI
5. Finally update processing logic

The core architecture (ImageItem class) is already in place!
