# Image Splitter with Per-Image Settings

<img width="474" alt="python_wwAG0YSEKo" src="https://github.com/Xerophayze/splitter/assets/113407496/89501363-f6eb-4456-ae36-d140471544bc">

An advanced image splitting tool with per-image settings, preview functionality, and a modern dual-panel interface. Perfect for preparing large datasets of images for AI training.

## 🚀 Quick Start

### Windows
```bash
run_per_image.bat
```

### Linux/macOS
```bash
chmod +x run_per_image.sh
./run_per_image.sh
```

**That's it!** The launcher will:
- ✓ Check if Python is installed
- ✓ Auto-install dependencies if needed
- ✓ Launch the application

**First time?** Install Python from https://www.python.org/downloads/ (check "Add Python to PATH")

---

## ✨ Features

### Core Functionality
- 🖼️ **Image Preview** - See thumbnails with dimensions and file size
- ⚙️ **Per-Image Settings** - Configure each image individually
- 🎨 **Modern Dual-Panel UI** - Resizable split view
- 📊 **Visual Indicators** - ⚙ icon shows which images have custom settings
- 🔄 **Global Defaults** - Set base settings for all images
- 📋 **Settings Summary** - See configuration at a glance
- 🗑️ **Remove Selected** - Delete individual images from list

### Image Processing
- Split images into customizable grids (1×1 to 10×10)
- Resize to standard sizes: 512, 768, 1024, 2048, 4096, or custom
- Maintain source format (JPG, PNG, BMP, WEBP) or convert to JPEG
- Custom output folder names
- Drag and drop support
- Batch processing with progress tracking

### Modern UI
- Dark theme with sv-ttk
- Background threading for responsive interface
- Real-time progress bar
- Input validation with visual feedback
- Tooltips on all controls
- Better error handling

---

## 📖 How to Use

### Basic Workflow
1. **Add Images**
   - Click "📁 Browse Images" OR drag and drop files

2. **Set Global Defaults** (optional)
   - Configure base settings in left panel
   - These apply to all images without custom settings

3. **Configure Individual Images** (optional)
   - Click an image to see preview
   - Check "Use custom settings for this image"
   - Adjust settings as needed
   - Click "Apply to Image"
   - Image shows ⚙ icon

4. **Process**
   - Click "▶ Process All Images"
   - Each image uses its own settings

### Example Scenarios

#### Scenario 1: All Same Settings
```
1. Add 10 images
2. Set global defaults: Size 1024, Grid 2×2
3. Click Process
→ All 10 images split into 4 parts at 1024px
```

#### Scenario 2: Mixed Settings
```
1. Add 3 images
2. Set global: Size 512, Grid 1×1

3. Select image1.jpg
   - Enable custom settings
   - Set Size: 2048, Grid: 3×3
   - Apply

4. Leave image2.jpg at defaults

5. Select image3.jpg
   - Enable custom settings
   - Set Grid: 1×4 (horizontal strip)
   - Apply

6. Process

Result:
  - image1.jpg → 9 parts at 2048px (3×3 grid)
  - image2.jpg → 1 part at 512px (no split)
  - image3.jpg → 4 parts at 512px (1×4 horizontal)
```

---

## 📁 Project Files

### Essential Files
- `splitter_with_per_image.py` - Main application
- `requirements.txt` - Python dependencies
- `run_per_image.bat` - Windows launcher
- `run_per_image.sh` - Linux/macOS launcher

### Documentation
- `README.md` - This file
- `COMPLETED.md` - Complete usage guide
- `GETTING_STARTED.md` - Quick start guide
- `PER_IMAGE_SETTINGS.md` - Feature documentation

---

## 🔧 Requirements

- **Python 3.x**
- **Pillow** - Image processing (auto-installed)
- **tkinterdnd2** - Drag and drop support (auto-installed)
- **sv-ttk** - Modern dark theme (auto-installed)

All dependencies install automatically on first run!

---

## 🎯 Visual Indicators

| Symbol | Meaning |
|--------|---------|
| ⚙ | Image has custom settings |
| (no icon) | Using global defaults |
| ✓ | Success message |
| ✗ | Error message |
| ▶ | Process/Start |
| ⏹ | Stop/Cancel |
| 📁 | Browse files |

---

## 💡 Tips

1. **Set Global Defaults First** - Most images will use these
2. **Use Preview** - Verify you're configuring the right image
3. **Check ⚙ Icon** - Quick way to see which images have custom settings
4. **Settings Summary** - Shows key settings without selecting
5. **Reset if Unsure** - "Reset to Defaults" is always safe

---

## 🐛 Troubleshooting

### "Python is not installed or not in PATH"
**Solution:** 
1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart terminal and try again

### "Failed to install dependencies"
**Solution:**
1. Check internet connection
2. Run as administrator (Windows) or with sudo (Linux/macOS)
3. Manual install: `python -m pip install -r requirements.txt`

### Preview not showing
**Solution:**
- Verify file path is valid
- Ensure image format is supported (JPG, PNG, BMP, WEBP)
- Try removing and re-adding the image

### Settings not applying
**Solution:**
- Make sure "Use custom settings" is checked
- Click "Apply to Image" button
- Verify ⚙ icon appears next to filename

---

## ⌨️ Keyboard Shortcuts

- **Up/Down Arrow** - Navigate image list
- **Delete** - Remove selected image
- **Enter** - Apply settings (when in settings panel)

---

## 🎨 UI Layout

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

---

## 📚 Additional Documentation

- **COMPLETED.md** - Comprehensive feature guide with examples
- **GETTING_STARTED.md** - Detailed installation and setup
- **PER_IMAGE_SETTINGS.md** - In-depth feature documentation
- **FILES_TO_DELETE.md** - Cleanup guide for old files

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **Pillow** - Image processing capabilities
- **tkinterdnd2** - Drag-and-drop functionality
- **sv-ttk** - Modern dark theme
- **Python Software Foundation** - Python programming language

---

## 🎉 Summary

**One-Click Launch:**
```
Windows: run_per_image.bat
Linux/macOS: ./run_per_image.sh
```

**Features:**
- ✓ Per-image custom settings
- ✓ Image preview
- ✓ Modern dual-panel UI
- ✓ Auto-install dependencies
- ✓ Batch processing
- ✓ Progress tracking

**Result:** Professional image splitting with maximum flexibility! 🚀
