#!/bin/bash

# ending.sh - Project wrap-up and handover preparation

echo "=== Ending Development Session ==="

# 1. Update tasks.md status
echo "Checking OpenSpec status..."
openspec status

# 2. Find the active change
ACTIVE_CHANGE=$(ls -d openspec/changes/*/ 2>/dev/null | head -n 1)
if [ -n "$ACTIVE_CHANGE" ]; then
    CHANGE_NAME=$(basename "$ACTIVE_CHANGE")
    echo "Active change detected: $CHANGE_NAME"
    
    # Check if complete (logic: checking status for completion)
    STATUS_OUTPUT=$(openspec status --change "$CHANGE_NAME" --json)
    IS_READY=$(echo "$STATUS_OUTPUT" | grep -i '"isReady": true' || echo "false")
    
    # 3. Archive the change if complete (interactive check or based on status)
    # Since we can't easily auto-archive without risk, we suggest it
    echo "If this change is complete, you should run: openspec archive $CHANGE_NAME"
else
    echo "No active change found to archive."
fi

# 4. Write handover document
echo "Generating HANDOVER.md..."
cat <<EOF > HANDOVER.md
# Handover Notes - $(date '+%Y-%m-%d %H:%M:%S')

## Summary of Work
- Developer session ended. 
$(if [ -n "$CHANGE_NAME" ]; then echo "- Active work in change: $CHANGE_NAME"; fi)

## Next Steps
- [ ] Review current progress in openspec/changes/
- [ ] Continue with the next task in the workflow
EOF
echo "HANDOVER.md updated."

# 5. Push code to GitHub
if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Committing and pushing changes..."
    git add .
    git commit -m "Dev session wrap-up $(date '+%Y-%m-%d %H:%M')" || echo "Nothing new to commit."
    git push origin main || echo "Warning: git push failed."
else
    echo "Not a git repository. Skipping push."
fi

echo -e "\n=== Session Ended Successfully ==="
