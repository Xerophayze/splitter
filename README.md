# Image Splitter and Resizer
![python_sSZbYKqzIa](https://github.com/user-attachments/assets/7c70a711-db13-456a-8772-0f40cc45545e)


An advanced image splitting tool featuring per-image configuration, live previews, and a modern ttk interface. Purpose-built for preparing large image batches (e.g., AI model training sets) while giving granular control over each source image.

---

## 🚀 Quick Start

> **All you need:** Python 3.x + one launcher. Dependencies install automatically on first run.

### Windows
```bat
run_per_image.bat
```

### Linux / macOS
```bash
chmod +x run_per_image.sh   # first run only
./run_per_image.sh
```

Both launchers automatically:
1. Check that Python is available
2. Install required packages (`Pillow`, `tkinterdnd2`, `sv-ttk`) if missing
3. Start the per-image splitter UI

If Python is not installed, download it from [python.org](https://www.python.org/downloads/) and (on Windows) choose **“Add Python to PATH.”**

---

## ✨ Key Features

### Per-Image Controls
- 🖼️ Thumbnail preview (300×300) with dimensions & file size
- ⚙️ Custom settings per file (size, grid, folder, format)
- 📋 Summary column showing applied overrides
- ✳️ ⚙ icon marks images using custom settings

### Global Defaults
- Configure size, grid, folder, and format once
- Any image without overrides inherits global values

### Modern UI / UX
- sv-ttk dark theme with ttk widgets
- Responsive layout using PanedWindow (resizable split panels)
- Drag-and-drop + multi-file browse
- Background threading for non-blocking processing
- Progress bar with detailed status updates
- Validation feedback + tooltips on every control

---

## 📁 Project Structure

| File | Purpose |
|------|---------|
| `splitter_with_per_image.py` | Main application code |
| `requirements.txt` | Dependency list used by launchers |
| `run_per_image.bat` | Windows launcher (auto setup + run) |
| `run_per_image.sh` | Linux/macOS launcher (auto setup + run) |
| `COMPLETED.md` | Comprehensive feature & usage guide |
| `GETTING_STARTED.md` | Quick start walkthrough |
| `PER_IMAGE_SETTINGS.md` | Detailed feature documentation |
| `README.md` | This overview |

> Removed legacy files: original/modern Python scripts, older launchers, and manual setup batch files. Everything funnels through the per-image version now.

---

## 🛠️ Requirements

- Python 3.8+ (Windows, Linux, or macOS)
- Automatically installed on first run:
  - [Pillow](https://python-pillow.org/)
  - [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)
  - [sv-ttk](https://github.com/rdbende/Sun-Valley-ttk-theme)

Optional but recommended:
- GPU-accelerated image viewing for large previews (handled by Pillow)

---

## 🧭 Usage Overview

### 1. Load Images
- Drag and drop files into the left panel **or** click **📁 Browse Images**
- Supported formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.webp`

### 2. Set Global Defaults (left panel)
- **Base Size** (512–4096) or specify a **Custom Size**
- **Images Across** / **Images High** to define the grid
- **Output Folder** name (optional)
- **Maintain Format** to keep original file type

### 3. Configure Individual Images (right panel)
- Select an image to show its preview
- Check **“Use custom settings for this image”**
- Adjust size / grid / folder / format
- Click **Apply to Image** to store overrides (⚙ icon appears)
- Use **Reset to Defaults** to remove overrides

### 4. Process Images
- Click **▶ Process All Images**
- Each image uses its custom settings; others fall back to global defaults
- Progress bar and status text show real-time updates

---

## ✅ Tips for Best Results

1. **Set global defaults first** to minimize per-image tweaks.
2. Use previews to verify orientation and grid choices before processing.
3. Watch for the ⚙ icon and summary column to confirm custom settings saved.
4. After applying settings, you can switch images without losing changes.
5. The **status bar** confirms actions (applied overrides, resets, processing).

---

## 🧪 Testing Checklist

- Add multiple images via drag-and-drop
- Apply custom grid to one image, default to others
- Verify preview updates when switching selection
- Ensure ⚙ icon appears and summary text reflects overrides
- Run processing and confirm outputs respect per-image vs global settings
- Test failure scenarios (e.g., missing file) to confirm graceful errors

---

## 🧰 Troubleshooting

| Issue | Fix |
|-------|-----|
| **“Python is not installed or not in PATH.”** | Install Python 3.x and ensure it’s on PATH. On Windows, re-run installer with *Add to PATH* checked. |
| **Dependencies fail to install.** | Check internet connection. On Windows, run launcher as Administrator; on Linux/macOS, run `python3 -m pip install -r requirements.txt` manually (prepend `sudo` if needed). |
| **Preview missing or blank.** | Confirm the file exists, is a supported format, and hasn’t been moved. Remove and re-add if necessary. |
| **Custom settings not saving.** | Make sure the checkbox is enabled, click **Apply to Image**, and confirm the ⚙ icon appears. |
| **Permission errors on Linux/macOS.** | Ensure the launcher has execute permission (`chmod +x run_per_image.sh`). |

---

## 📜 License & Credits

- Licensed under the **MIT License** (see `LICENSE`).
- Built with:
  - Pillow for image manipulation
  - tkinterdnd2 for drag-and-drop support
  - sv-ttk for modern themed widgets
- Special thanks to the Python community for the tools that made this project possible.

---

## 📚 Additional Resources

- `COMPLETED.md` – Implementation details and full walkthrough
- `GETTING_STARTED.md` – Step-by-step quick start guide
- `PER_IMAGE_SETTINGS.md` – Deep dive into per-image configuration

If you cloned the full repository history, older files such as `splitter.py`, `splitter_modern.py`, `run_modern.bat`, etc., may still exist in Git history but are no longer part of the supported workflow.

---

### ✨ TL;DR

```
Windows: double-click run_per_image.bat
Linux/macOS: ./run_per_image.sh

Configure global defaults → tweak per-image settings → press ▶
```

Enjoy effortless, fine-grained image splitting! 🎉
