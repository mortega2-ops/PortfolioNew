#!/bin/bash

# This script helps set up your GitHub repository for this project

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install git first."
    exit 1
fi

# Check if the repository is already initialized
if [ -d .git ]; then
    echo "Git repository is already initialized."
else
    echo "Initializing git repository..."
    git init
fi

# Prompt for GitHub username and repository name
read -p "Enter your GitHub username: " username
read -p "Enter your repository name: " repo_name

# Check if remote origin already exists
if git remote | grep -q "^origin$"; then
    echo "Remote 'origin' already exists. Updating URL..."
    git remote set-url origin "https://github.com/$username/$repo_name.git"
else
    echo "Adding remote 'origin'..."
    git remote add origin "https://github.com/$username/$repo_name.git"
fi

# Add all files to git
echo "Adding files to git..."
git add .

# Commit changes
echo "Committing changes..."
read -p "Enter commit message (default: 'Initial commit'): " commit_message
commit_message=${commit_message:-"Initial commit"}
git commit -m "$commit_message"

# Push to GitHub
echo "Pushing to GitHub..."
echo "Note: You may be prompted for your GitHub credentials."
git push -u origin main || git push -u origin master

echo "Setup complete! Your code has been pushed to https://github.com/$username/$repo_name" 