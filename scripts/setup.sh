#!/bin/bash
echo "Setting up the development environment..."

# Frontend setup
echo "Installing frontend dependencies..."
cd frontend
npm install
npx tailwindcss init
cd ..

echo "Setup completed!"
