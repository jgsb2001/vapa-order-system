#!/bin/bash

echo "========================================"
echo "VAPA Order System - Local Server"
echo "========================================"
echo ""
echo "Installing required packages..."
pip3 install -r requirements.txt
echo ""
echo "Starting server..."
echo ""
echo "Your application will be available at:"
echo "http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
python3 app.py
