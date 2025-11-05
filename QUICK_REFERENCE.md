# Image Splitter - Quick Reference Card

## Files Overview

| File | Description | Status |
|------|-------------|--------|
| `splitter.py` | Original version | ✓ Working |
| `splitter_modern.py` | Modernized UI, no per-image settings | ✓ Complete |
| `splitter_with_per_image.py` | Base with ImageItem class | ⚙ Needs GUI updates |
| `requirements.txt` | Dependencies | ✓ Updated |
| `install.bat` | Dependency installer | ✓ Ready |
| `run_modern.bat` | Launch modern version | ✓ Ready |

## Feature Comparison

| Feature | Original | Modern | Per-Image |
|---------|----------|--------|-----------|
| Basic splitting | ✓ | ✓ | ✓ |
| Drag & drop | ✓ | ✓ | ✓ |
| Modern UI | ✗ | ✓ | ✓ |
| Threading | ✗ | ✓ | ✓ |
| Progress bar | ✗ | ✓ | ✓ |
| Input validation | ✗ | ✓ | ✓ |
| Tooltips | ✗ | ✓ | ✓ |
| Image preview | ✗ | ✗ | ✓ |
| Per-image settings | ✗ | ✗ | ✓ |
| Settings indicator | ✗ | ✗ | ✓ |

## Key Classes

### ImageItem
```python
# Stores per-image settings
img_item = ImageItem(file_path)
img_item.base_size = 1024
img_item.images_across = 2
img_item.images_high = 2
img_item.maintain_format = True

# Check if has custom settings
if img_item.has_custom_settings():
    print(img_item.get_settings_summary())
```

### ImageSplitterConfig
```python
# Manages application state
config = ImageSplitterConfig()
config.image_items = []  # List of ImageItem
config.selected_item = None  # Currently selected
config.processing = False  # Processing flag
```

## UI Layout

```
┌─────────────────────────────────────────┐
│ Left Panel          │ Right Panel       │
├─────────────────────┼───────────────────┤
│ File List           │ Preview           │
│ ⚙ image1.jpg        │ [Thumbnail]       │
│   image2.png        │                   │
│                     │ Per-Image Settings│
│ Global Defaults     │ ☑ Use custom      │
│ Size: 512           │ Size: 1024        │
│ Grid: 1×1           │ Grid: 2×2         │
├─────────────────────┴───────────────────┤
│ ▶ Process All Images    ⏹ Cancel        │
│ ████████░░░░░░░░░░░░░░░░░░░░░░░░░░      │
│ Processing 2/5: image2.png              │
└─────────────────────────────────────────┘
```

## Workflow

### Simple (Global Settings)
1. Add images
2. Set global settings
3. Process

### Advanced (Per-Image)
1. Add images
2. Click image → Preview appears
3. Enable "Use custom settings"
4. Adjust settings
5. Click "Apply to Image"
6. Repeat for other images
7. Process all

## Visual Indicators

| Symbol | Meaning |
|--------|---------|
| ⚙ | Has custom settings |
| ✓ | Success |
| ✗ | Error |
| ▶ | Process/Play |
| ⏹ | Stop/Cancel |
| 📁 | Browse files |

## Settings Priority

```
For each image:
  1. Check if image has custom settings
     → Use custom settings
  2. Else
     → Use global defaults
```

## Code Snippets

### Add Image to List
```python
img_item = ImageItem(file_path)
self.config.image_items.append(img_item)
item_id = str(id(img_item))
self.listbox.insert('', 'end', iid=item_id,
                   text=img_item.get_display_name(),
                   values=(img_item.get_settings_summary(),))
```

### Load Preview
```python
with Image.open(img_item.file_path) as img:
    img.thumbnail((300, 300), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    self.preview_image = photo
    self.preview_label.config(image=photo)
```

### Apply Settings
```python
if self.use_custom_settings_var.get():
    img_item.base_size = int(self.size_var.get())
    img_item.images_across = self.images_across_var.get()
    img_item.images_high = self.images_high_var.get()
    self.update_listbox_item(img_item)
```

### Process with Settings
```python
for img_item in self.config.image_items:
    # Get effective settings
    size = img_item.custom_size or img_item.base_size or global_size
    across = img_item.images_across or global_across
    high = img_item.images_high or global_high
    
    # Process
    split_and_resize_image(img_item.file_path, across, high, size, ...)
```

## Implementation Status

### ✓ Completed
- ImageItem class with settings storage
- ImageSplitterConfig updated
- ImageTk import added
- Base file created (`splitter_with_per_image.py`)
- Documentation written

### ⚙ Needs Implementation
- Update GUI `__init__` and `setup_variables`
- Change `setup_ui` to use PanedWindow
- Update Treeview to show settings column
- Add `create_preview_section` method
- Add `create_per_image_settings_section` method
- Add `create_global_settings_section` method (rename existing)
- Add event handlers (`on_image_select`, `load_preview`, etc.)
- Update `browse_images` and `on_drop` to use ImageItem
- Update `process_images` to use per-image settings
- Update `validate_inputs` for new structure

## Testing Checklist

- [ ] Install dependencies
- [ ] Launch application
- [ ] Add multiple images
- [ ] Click image - preview appears
- [ ] Enable custom settings
- [ ] Change settings
- [ ] Apply to image
- [ ] Verify ⚙ icon appears
- [ ] Add another image
- [ ] Leave it with global defaults
- [ ] Process all images
- [ ] Verify each uses correct settings
- [ ] Check output folders
- [ ] Test drag and drop
- [ ] Test remove selected
- [ ] Test clear list
- [ ] Test cancel during processing

## Troubleshooting

### Preview not showing
- Check ImageTk import
- Verify preview_image reference kept
- Check file path is valid

### Settings not applying
- Verify use_custom_settings_var is True
- Check apply_settings method called
- Verify update_listbox_item updates display

### Processing uses wrong settings
- Check settings priority logic
- Verify None checks for custom settings
- Ensure global defaults used as fallback

## Quick Commands

```bash
# Install
install.bat

# Run modern version (no per-image)
python splitter_modern.py

# Run per-image version (when complete)
python splitter_with_per_image.py

# CLI mode
python splitter_modern.py image.jpg --across 2 --high 2 --size 1024
```

## Documentation Files

- `IMPROVEMENTS.md` - All improvements made to modern version
- `PER_IMAGE_SETTINGS.md` - Feature documentation
- `IMPLEMENTATION_GUIDE.md` - Detailed implementation steps
- `QUICK_REFERENCE.md` - This file

## Support

For issues:
1. Check `IMPLEMENTATION_GUIDE.md` for detailed steps
2. Review `PER_IMAGE_SETTINGS.md` for feature details
3. Compare with `splitter_modern.py` for working examples
4. Test with `splitter_modern.py` first to isolate issues

## Version History

- v1.0 - Original splitter.py
- v2.0 - Modern UI (splitter_modern.py)
- v3.0 - Per-image settings (splitter_with_per_image.py) - IN PROGRESS
