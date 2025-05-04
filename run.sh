#!/bin/bash

# Determine Python command
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}' | cut -d. -f1)
    if [ "$PYTHON_VERSION" -eq 3 ]; then
        PYTHON_CMD="python"
    else
        echo "Python 3 is required but not found. Please run setup.sh first."
        exit 1
    fi
else
    echo "Python is not installed. Please run setup.sh first."
    exit 1
fi

# Run the application
$PYTHON_CMD splitter.py "$@"
