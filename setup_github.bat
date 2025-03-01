@echo off
echo Portfolio GitHub Setup Script

REM Check if git is installed
where git >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Git is not installed. Please install git first.
    exit /b 1
)

REM Check if the repository is already initialized
if exist .git\ (
    echo Git repository is already initialized.
) else (
    echo Initializing git repository...
    git init
)

REM Prompt for GitHub username and repository name
set /p username=Enter your GitHub username: 
set /p repo_name=Enter your repository name: 

REM Check if remote origin already exists
git remote | findstr "^origin$" >nul
if %ERRORLEVEL% equ 0 (
    echo Remote 'origin' already exists. Updating URL...
    git remote set-url origin "https://github.com/%username%/%repo_name%.git"
) else (
    echo Adding remote 'origin'...
    git remote add origin "https://github.com/%username%/%repo_name%.git"
)

REM Add all files to git
echo Adding files to git...
git add .

REM Commit changes
echo Committing changes...
set /p commit_message=Enter commit message (default: 'Initial commit'): 
if "%commit_message%"=="" set commit_message=Initial commit
git commit -m "%commit_message%"

REM Push to GitHub
echo Pushing to GitHub...
echo Note: You may be prompted for your GitHub credentials.
git push -u origin main || git push -u origin master

echo Setup complete! Your code has been pushed to https://github.com/%username%/%repo_name%
pause 