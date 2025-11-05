#!/bin/bash

echo "========================================"
echo "Image Splitter - Per-Image Settings"
echo "========================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed."
    echo
    echo "Please install Python 3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  macOS: brew install python3"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo
    read -p "Press Enter to exit..."
    exit 1
fi

# Check if dependencies are installed
python3 -c "import PIL, tkinterdnd2, sv_ttk" &> /dev/null
if [ $? -ne 0 ]; then
    echo
    echo "Dependencies not found. Installing required packages..."
    echo
    python3 -m pip install --upgrade pip --quiet
    python3 -m pip install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo
        echo "ERROR: Failed to install dependencies."
        echo "Please check your internet connection and try again."
        echo "You may need to run: sudo python3 -m pip install -r requirements.txt"
        echo
        read -p "Press Enter to exit..."
        exit 1
    fi
    
    echo
    echo "Dependencies installed successfully!"
    echo
fi

echo "Starting Image Splitter..."
echo
python3 splitter_with_per_image.py

# Keep terminal open on error
if [ $? -ne 0 ]; then
    echo
    echo "Application exited with an error."
    read -p "Press Enter to exit..."
fi
