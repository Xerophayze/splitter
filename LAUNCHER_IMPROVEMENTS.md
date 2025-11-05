# Launcher Improvements - Unified Installation

## What Changed

### Before
Users had to run **two separate files**:
1. `setup.bat` or `install.bat` - Install dependencies
2. `run_per_image.bat` - Run the application

This was confusing and required multiple steps.

### After
Users just run **one file**:
1. `run_per_image.bat` - Does everything automatically!

## How It Works

Each launcher (`run_per_image.bat`, `run_modern.bat`, `run.bat`) now:

1. **Checks for Python**
   - If not found: Shows helpful error message with download link
   - If found: Continues to next step

2. **Checks for Dependencies**
   - Tries to import: `PIL`, `tkinterdnd2`, `sv_ttk`
   - If missing: Automatically installs them
   - If present: Skips installation

3. **Launches Application**
   - Runs the Python script
   - Shows any errors in the console

## Benefits

✅ **One-Click Launch** - No separate setup step
✅ **Auto-Install** - Dependencies install automatically on first run
✅ **Smart Detection** - Only installs if needed
✅ **Error Handling** - Clear messages if something goes wrong
✅ **No Confusion** - Users don't need to know about setup.bat vs install.bat

## File Status

### Active Files (Keep These)
- ✅ `run_per_image.bat` - **Main launcher** (per-image version)
- ✅ `run_modern.bat` - Modern version launcher
- ✅ `run.bat` - Original version launcher
- ✅ `requirements.txt` - Dependency list (used by launchers)

### Optional Files (Can Delete)
- ⚠️ `setup.bat` - Redundant (launchers check Python now)
- ⚠️ `install.bat` - Redundant (launchers auto-install now)

**Note:** Keeping `setup.bat` and `install.bat` won't hurt anything, but they're no longer needed.

## User Experience

### Old Workflow
```
User: "How do I run this?"
Instructions: 
  1. First run setup.bat
  2. Wait for installation
  3. Then run run_per_image.bat
  
Result: 3 steps, potential confusion
```

### New Workflow
```
User: "How do I run this?"
Instructions: 
  1. Double-click run_per_image.bat
  
Result: 1 step, automatic setup
```

## Technical Details

### Dependency Check
```batch
python -c "import PIL, tkinterdnd2, sv_ttk" >nul 2>&1
if %errorlevel% neq 0 (
    REM Dependencies missing, install them
    python -m pip install -r requirements.txt
)
```

This checks if all required packages can be imported. If any fail, it installs from `requirements.txt`.

### Python Check
```batch
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed
    REM Show helpful message
)
```

This verifies Python is installed and in PATH before attempting anything else.

## Error Messages

### Python Not Found
```
ERROR: Python is not installed or not in PATH.

Please install Python 3.x from https://www.python.org/downloads/
Make sure to check "Add Python to PATH" during installation.
```

### Installation Failed
```
ERROR: Failed to install dependencies.
Please check your internet connection and try again.
```

Both errors pause the window so users can read the message.

## First Run Example

```
========================================
Image Splitter - Per-Image Settings
========================================

Dependencies not found. Installing required packages...

[pip installation output]

Dependencies installed successfully!

Starting Image Splitter...

[Application launches]
```

## Subsequent Runs

```
========================================
Image Splitter - Per-Image Settings
========================================

Starting Image Splitter...

[Application launches immediately]
```

No installation messages - it just works!

## Comparison Table

| Feature | Old (setup.bat) | New (run_per_image.bat) |
|---------|----------------|-------------------------|
| Python check | ✓ | ✓ |
| Dependency install | ✓ | ✓ |
| Launch app | ✗ | ✓ |
| Auto-detect installed | ✗ | ✓ |
| One-click operation | ✗ | ✓ |
| Skip if already installed | ✗ | ✓ |

## Migration Guide

### For Users
**No action needed!** Just use the new launchers:
- `run_per_image.bat` instead of running setup first
- Everything else works the same

### For Developers
If you want to clean up:
1. Keep: `run_*.bat`, `requirements.txt`, `*.py`
2. Optional: Delete `setup.bat` and `install.bat`
3. Update documentation to reference new workflow

## Future Improvements

Possible enhancements:
- Add version checking (update if outdated)
- Create virtual environment automatically
- Add `--force-reinstall` flag
- Show progress bar during installation
- Cache dependency check for faster startup

## Testing

Tested scenarios:
- ✓ Fresh install (no Python)
- ✓ Python installed, no dependencies
- ✓ Python + dependencies already installed
- ✓ Missing one dependency (sv-ttk)
- ✓ Internet connection issues
- ✓ Permission issues

All scenarios handled gracefully with clear error messages.

## Summary

The new unified launchers make the Image Splitter much easier to use:

**Before:** "Run setup.bat, wait, then run run_per_image.bat"
**After:** "Run run_per_image.bat"

Simple, automatic, and user-friendly! 🎉
