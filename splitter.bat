@echo off
setlocal

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    
    REM Define Python download URL and installer name
    set "PYTHON_URL=https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe"
    set "PYTHON_INSTALLER=python-installer.exe"
    
    REM Download Python installer
    powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %PYTHON_INSTALLER%"
    
    REM Install Python silently
    %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
    
    REM Clean up installer
    del %PYTHON_INSTALLER%
    
    REM Verify installation
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python installation failed. Please install Python manually and try again.
        exit /b 1
    ) else (
        echo Python installed successfully.
    )
) else (
    echo Python is already installed.
)

REM Run the Python script with the provided argument
python splitter.pyw %1

endlocal
