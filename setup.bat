@echo off
echo Image Splitter - Setup Script for Windows
echo =======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.x from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
) else (
    echo Python is installed. Checking version...
    for /f "tokens=2" %%V in ('python --version 2^>^&1') do (
        echo Detected Python version: %%V
    )
)

echo.
echo Installing required packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo Error installing packages. Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo Setup completed successfully!
echo You can now run the application using splitter.bat or directly with splitter.pyw
echo.
pause
