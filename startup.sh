#!/bin/bash

# startup.sh - Development environment initialization and handover review

echo "=== Starting Development Session ==="

# 1. Pull code from GitHub
if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Pulling latest changes from GitHub..."
    git pull origin main || echo "Warning: git pull failed. Proceeding anyway."
else
    echo "This is not a git repository. Skipping git pull."
fi

# 2. Read the handover document
if [ -f HANDOVER.md ]; then
    echo -e "\n--- HANDOVER DOCUMENT ---"
    cat HANDOVER.md
    echo -e "\n--------------------------"
else
    echo "No HANDOVER.md found. Starting fresh."
fi

# 3. Initialize OpenSpec
echo "Initializing OpenSpec structure..."
openspec init --tools antigravity --force

# 4. Suggest next actions
echo -e "\n=== Suggested Next Actions ==="
if [ -f HANDOVER.md ]; then
    echo "Based on the handover document:"
    # Very simple logic to find "Next Steps" or "- [ ]" tasks
    grep -A 5 "Next Steps" HANDOVER.md | grep "\- \[ \]" || echo "- Follow the instructions in HANDOVER.md"
else
    echo "- Use /opsx:propose to start a new change."
    echo "- Use openspec status to check current progress."
fi

echo -e "\n=== Startup Complete ==="
