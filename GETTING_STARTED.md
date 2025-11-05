# Getting Started - Image Splitter

## Quick Start (Windows)

**Just double-click the launcher!** No separate installation needed.

### For Per-Image Settings Version (Recommended)
```
run_per_image.bat
```

### For Modern Version
```
run_modern.bat
```

### For Original Version
```
run.bat
```

## What Happens Automatically

When you run any launcher for the first time:

1. ✓ Checks if Python is installed
2. ✓ Checks if dependencies are installed
3. ✓ Auto-installs missing dependencies
4. ✓ Launches the application

**No manual setup required!**

## First Time Setup

### If You Don't Have Python

1. Download Python from: https://www.python.org/downloads/
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Complete the installation
4. Run any launcher (e.g., `run_per_image.bat`)

### If You Have Python

Just run the launcher! Dependencies will install automatically on first run.

## Which Version Should I Use?

| Version | File | Best For |
|---------|------|----------|
| **Per-Image Settings** ⭐ | `run_per_image.bat` | Different settings per image, preview needed |
| **Modern** | `run_modern.bat` | Same settings for all images, modern UI |
| **Original** | `run.bat` | Basic functionality, simple interface |

## Manual Installation (Optional)

If you prefer to install dependencies manually:

```bash
# Option 1: Use setup.bat (checks Python, installs deps)
setup.bat

# Option 2: Use install.bat (installs deps only)
install.bat

# Option 3: Manual pip install
python -m pip install -r requirements.txt
```

## Troubleshooting

### "Python is not installed or not in PATH"

**Solution:** 
1. Install Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Restart your command prompt
4. Try running the launcher again

### "Failed to install dependencies"

**Solution:**
1. Check your internet connection
2. Try running as administrator (right-click → Run as administrator)
3. Manually install: `python -m pip install -r requirements.txt`

### Dependencies keep reinstalling

**Solution:** This means the import check is failing. Verify installation:
```bash
python -c "import PIL, tkinterdnd2, sv_ttk"
```

If this shows an error, manually reinstall:
```bash
python -m pip uninstall Pillow tkinterdnd2 sv-ttk -y
python -m pip install -r requirements.txt
```

## What's Installed

The launchers automatically install these packages:
- **Pillow** - Image processing
- **tkinterdnd2** - Drag and drop support
- **sv-ttk** - Modern dark theme (for modern/per-image versions)

## Files You Can Delete

Now that launchers handle everything, these are **optional**:

- `install.bat` - Redundant (launchers auto-install)
- `setup.bat` - Redundant (launchers check Python)

**Keep these:**
- `run_per_image.bat` ⭐ - Main launcher
- `run_modern.bat` - Modern version launcher
- `run.bat` - Original version launcher
- `requirements.txt` - Needed by launchers
- `splitter_with_per_image.py` - The actual program
- All `.py` files - The programs themselves

## Advanced Usage

### Command Line

You can still run directly with Python:

```bash
# Per-image version
python splitter_with_per_image.py

# Modern version
python splitter_modern.py

# Original version (with CLI args)
python splitter.py image1.jpg --across 2 --high 2 --size 1024
```

### Virtual Environment (Optional)

If you want isolated dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python splitter_with_per_image.py
```

## Summary

**Old Way (Multiple Steps):**
1. Run `setup.bat` or `install.bat`
2. Wait for installation
3. Run `run_per_image.bat`

**New Way (One Step):**
1. Run `run_per_image.bat` ✓

Everything else happens automatically! 🎉
