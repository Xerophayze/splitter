#!/bin/bash

echo "Image Splitter - Setup Script for Linux/macOS"
echo "==========================================="
echo ""

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is installed."
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    # Check if it's Python 3
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}' | cut -d. -f1)
    if [ "$PYTHON_VERSION" -eq 3 ]; then
        echo "Python 3 is installed."
        PYTHON_CMD="python"
    else
        echo "Python 3 is not installed. Please install Python 3.x from your package manager."
        echo "For example:"
        echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
        echo "  Fedora: sudo dnf install python3 python3-pip"
        echo "  macOS: brew install python3"
        exit 1
    fi
else
    echo "Python is not installed. Please install Python 3.x from your package manager."
    echo "For example:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  macOS: brew install python3"
    exit 1
fi

echo ""
echo "Installing required packages..."
$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo ""
    echo "Error installing packages. Please check your internet connection and try again."
    exit 1
fi

# Make the script executable
chmod +x splitter.py

echo ""
echo "Setup completed successfully!"
echo "You can now run the application using: $PYTHON_CMD splitter.py"
echo ""

# Set executable permissions for the script itself
chmod +x "$0"
