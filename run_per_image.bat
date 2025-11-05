@echo off
echo ========================================
echo Image Splitter - Per-Image Settings
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH.
    echo.
    echo Please install Python 3.x from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM Check if dependencies are installed by trying to import them
python -c "import PIL, tkinterdnd2, sv_ttk" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Dependencies not found. Installing required packages...
    echo.
    python -m pip install --upgrade pip --quiet
    python -m pip install -r requirements.txt
    
    if %errorlevel% neq 0 (
        echo.
        echo ERROR: Failed to install dependencies.
        echo Please check your internet connection and try again.
        echo.
        pause
        exit /b 1
    )
    
    echo.
    echo Dependencies installed successfully!
    echo.
)

echo Starting Image Splitter...
echo.
python splitter_with_per_image.py
pause
