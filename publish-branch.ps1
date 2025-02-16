# Get current branch name
$currentBranch = git rev-parse --abbrev-ref HEAD

# Add all changes
git add .

# Commit changes
git commit -m "Publishing branch $currentBranch"

# Push to remote
git push -u origin $currentBranch

Write-Host "Successfully published branch $currentBranch to GitHub" 