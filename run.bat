@echo off
echo Starting Image Splitter...

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please run setup.bat first to install dependencies.
    pause
    exit /b 1
)

REM Check if required packages are installed
python -c "import PIL; import tkinterdnd2" >nul 2>&1
if %errorlevel% neq 0 (
    echo Required packages are not installed.
    echo Please run setup.bat first to install dependencies.
    pause
    exit /b 1
)

REM Run the application with any provided arguments
python splitter.pyw %*

exit /b 0
