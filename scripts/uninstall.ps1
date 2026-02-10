# Claude Code Skills Uninstallation Script for Windows
# This script removes the skills link from your Claude Code configuration

$ErrorActionPreference = "Stop"

# Claude Code config path
$ClaudeConfigPath = "$env:USERPROFILE\.claude"
$SkillsTarget = Join-Path $ClaudeConfigPath "skills"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Claude Code Skills Uninstallation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if skills target exists
if (!(Test-Path $SkillsTarget)) {
    Write-Host "No skills installation found." -ForegroundColor Yellow
    exit 0
}

$item = Get-Item $SkillsTarget

# Show what will be removed
Write-Host "Found:" -ForegroundColor Yellow
if ($item.LinkType -eq "SymbolicLink") {
    Write-Host "  Type: Symbolic Link" -ForegroundColor White
    Write-Host "  Target: $($item.Target)" -ForegroundColor White
} elseif (Test-Path (Join-Path $SkillsTarget ".git")) {
    Write-Host "  Type: Git Repository" -ForegroundColor White
    Write-Host "  This appears to be a git repo, not removing for safety." -ForegroundColor Red
    exit 1
} else {
    Write-Host "  Type: Directory" -ForegroundColor White
}

Write-Host ""
$choice = Read-Host "Remove this? (y/N)"

if ($choice -eq "y" -or $choice -eq "Y") {
    Remove-Item $SkillsTarget -Force -Recurse
    Write-Host ""
    Write-Host "SUCCESS: Skills removed from Claude Code configuration." -ForegroundColor Green
} else {
    Write-Host "Uninstallation cancelled." -ForegroundColor Yellow
}
