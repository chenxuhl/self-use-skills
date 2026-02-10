#!/bin/bash
# Claude Code Skills Uninstallation Script for macOS/Linux
# This script removes the skills link from your Claude Code configuration

set -e

# Claude Code config path
CLAUDE_CONFIG_PATH="$HOME/.claude"
SKILLS_TARGET="$CLAUDE_CONFIG_PATH/skills"

echo "========================================"
echo "Claude Code Skills Uninstallation"
echo "========================================"
echo ""

# Check if skills target exists
if [ ! -e "$SKILLS_TARGET" ]; then
    echo "No skills installation found."
    exit 0
fi

# Show what will be removed
echo "Found:"
if [ -L "$SKILLS_TARGET" ]; then
    echo "  Type: Symbolic Link"
    echo "  Target: $(readlink "$SKILLS_TARGET")"
elif [ -d "$SKILLS_TARGET/.git" ]; then
    echo "  Type: Git Repository"
    echo "  This appears to be a git repo, not removing for safety."
    exit 1
else
    echo "  Type: Directory"
fi

echo ""
read -p "Remove this? (y/N) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf "$SKILLS_TARGET"
    echo ""
    echo "SUCCESS: Skills removed from Claude Code configuration."
else
    echo "Uninstallation cancelled."
fi
