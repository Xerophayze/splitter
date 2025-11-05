# Per-Image Settings Feature

## Overview
Enhanced version of the Image Splitter that allows you to configure individual settings for each image in the list.

## New Features

### 1. Image Item Management
- Each image in the list now has its own settings object
- Visual indicator (⚙) shows which images have custom settings
- Settings summary displayed next to each image

### 2. Preview Panel
- Click any image in the list to see a preview
- Shows image dimensions and file size
- Preview updates automatically when selecting different images
- 300x300 pixel thumbnail with aspect ratio preserved

### 3. Per-Image Settings
- **Use Custom Settings** checkbox to override global defaults
- Individual controls for each image:
  - Base Size (512, 768, 1024, 2048, 4096)
  - Custom Size (any numeric value)
  - Images Across (grid columns)
  - Images High (grid rows)
  - Output Folder name
  - Maintain Format option

### 4. Global Default Settings
- Set defaults that apply to all images without custom settings
- Located in left panel for easy access
- New images automatically use global defaults

### 5. Settings Management
- **Apply to Image** button saves custom settings
- **Reset to Defaults** button removes custom settings
- Settings persist while images are in the list
- Visual feedback when settings are applied

## UI Layout

```
┌─────────────────────────────────────────────────────────┐
│  Image Splitter and Resizer                             │
├──────────────────────────┬──────────────────────────────┤
│ Left Panel               │ Right Panel                  │
│                          │                              │
│ ┌─ Image Files ────────┐ │ ┌─ Preview ──────────────┐  │
│ │ 📁 Browse            │ │ │ image.jpg | 1920×1080  │  │
│ │                      │ │ │ ┌────────────────────┐ │  │
│ │ ⚙ image1.jpg         │ │ │ │                    │ │  │
│ │   image2.png         │ │ │ │   [Thumbnail]      │ │  │
│ │ ⚙ image3.jpg         │ │ │ │                    │ │  │
│ │                      │ │ │ └────────────────────┘ │  │
│ │ Clear | Remove       │ │ └────────────────────────┘  │
│ └──────────────────────┘ │                              │
│                          │ ┌─ Image-Specific Settings ┐ │
│ ┌─ Global Defaults ───┐ │ │ ☑ Use custom settings    │ │
│ │ Base Size: 512      │ │ │                          │ │
│ │ Across: 1  High: 1  │ │ │ Base Size: 1024         │ │
│ │ ☐ Maintain format   │ │ │ Custom Size: 2048       │ │
│ │ Output Folder:      │ │ │ Across: 2  High: 2      │ │
│ └─────────────────────┘ │ │ Output Folder: custom   │ │
│                          │ │ ☑ Maintain format       │ │
│                          │ │                          │ │
│                          │ │ [Apply] [Reset]         │ │
│                          │ └──────────────────────────┘ │
├──────────────────────────┴──────────────────────────────┤
│ ▶ Process All Images              ⏹ Cancel              │
│ ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │
│ Processing 3/5: image3.jpg                              │
└─────────────────────────────────────────────────────────┘
```

## Workflow

### Basic Workflow (Global Settings)
1. Add images to the list
2. Set global default settings
3. Click "Process All Images"
4. All images use the same settings

### Advanced Workflow (Per-Image Settings)
1. Add images to the list
2. Click on an image to select it
3. Preview appears on the right
4. Check "Use custom settings for this image"
5. Adjust settings for that specific image
6. Click "Apply to Image"
7. Image shows ⚙ icon indicating custom settings
8. Repeat for other images as needed
9. Click "Process All Images"
10. Each image processes with its own settings

## Visual Indicators

- **⚙ icon** - Image has custom settings
- **No icon** - Image uses global defaults
- **Settings summary** - Shows key settings next to filename
  - Example: "Size: 2048 | Grid: 2×2 | Keep format"

## Settings Priority

1. **Custom settings** (if enabled for that image)
2. **Global defaults** (if no custom settings)

## Examples

### Example 1: Mixed Processing
```
Images:
  ⚙ photo1.jpg - Size: 2048 | Grid: 1×1
    photo2.jpg - Using global defaults
  ⚙ photo3.jpg - Size: 1024 | Grid: 2×2 | Keep format
  
Global Defaults:
  Size: 512
  Grid: 1×1
  Format: Convert to JPEG
  
Result:
  - photo1.jpg → Split into 1 part at 2048px
  - photo2.jpg → Split into 1 part at 512px (global)
  - photo3.jpg → Split into 4 parts at 1024px, keep PNG format
```

### Example 2: Batch with Variations
```
Scenario: Process multiple images with different split patterns

  ⚙ banner.jpg - Grid: 4×1 (split into 4 horizontal sections)
  ⚙ poster.jpg - Grid: 1×3 (split into 3 vertical sections)
  ⚙ grid.jpg   - Grid: 3×3 (split into 9 tiles)
    normal.jpg - Grid: 1×1 (no split, just resize)
```

## Technical Implementation

### ImageItem Class
```python
class ImageItem:
    - file_path: Path to image file
    - base_size: Base size setting (or None for global)
    - custom_size: Custom size (or None)
    - images_across: Grid columns (or None for global)
    - images_high: Grid rows (or None for global)
    - maintain_format: Format setting (or None for global)
    - custom_folder: Output folder (or None for global)
    
    Methods:
    - has_custom_settings(): Returns True if any custom settings
    - get_display_name(): Returns name with ⚙ if custom
    - get_settings_summary(): Returns human-readable summary
```

### Processing Logic
```python
for each image_item:
    # Get effective settings
    size = image_item.custom_size or image_item.base_size or global_size
    across = image_item.images_across or global_across
    high = image_item.images_high or global_high
    format = image_item.maintain_format if not None else global_format
    folder = image_item.custom_folder or global_folder
    
    # Process with those settings
    split_and_resize_image(image_item.file_path, across, high, size, ...)
```

## Benefits

1. **Flexibility** - Different settings for different images in one batch
2. **Efficiency** - Process all at once instead of multiple runs
3. **Visual Feedback** - See which images have custom settings
4. **Preview** - Verify the right image before adjusting settings
5. **Easy Reset** - One click to return to global defaults
6. **No Mistakes** - Settings saved per image, can't mix them up

## Installation

Same as before - the per-image settings are built into the enhanced version.

```bash
# Install dependencies
install.bat

# Run enhanced version
python splitter_modern_v2.py
```

## Keyboard Shortcuts

- **Up/Down Arrow** - Navigate image list
- **Space** - Toggle custom settings checkbox
- **Enter** - Apply settings (when in settings panel)
- **Delete** - Remove selected image from list

## Tips

1. **Set Global Defaults First** - Most images will use these
2. **Use Preview** - Verify you're adjusting the right image
3. **Check the ⚙ Icon** - Quick way to see which images have custom settings
4. **Settings Summary** - Hover to see full details
5. **Reset if Unsure** - "Reset to Defaults" is always safe

## Future Enhancements

Possible additions for future versions:
- Save/load preset configurations
- Copy settings from one image to another
- Bulk apply settings to multiple selected images
- Settings templates for common scenarios
- Grid overlay on preview showing split lines
- Before/after preview of split results
