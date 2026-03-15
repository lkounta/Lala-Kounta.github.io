#!/bin/bash
# ─────────────────────────────────────────────────────────────
# update-cv.sh  —  Drop a new CV PDF and push to GitHub
#
# Usage:
#   ./update-cv.sh /path/to/new-cv.pdf
#
# What it does:
#   1. Copies the PDF to files/CV_Dr_Lala_Kounta.pdf
#   2. Updates CV_UPDATED date in cv.py
#   3. Rebuilds index.html via build.py
#   4. Commits and pushes everything to GitHub
# ─────────────────────────────────────────────────────────────

set -e

PDF="${1}"
DEST="files/CV_Dr_Lala_Kounta.pdf"
DATE=$(date "+%B %Y")

if [ -z "$PDF" ]; then
  echo "Usage: ./update-cv.sh /path/to/new-cv.pdf"
  exit 1
fi

if [ ! -f "$PDF" ]; then
  echo "Error: file not found: $PDF"
  exit 1
fi

cd "$(dirname "$0")"

# 1. Copy the PDF
cp "$PDF" "$DEST"
echo "✓  Copied to $DEST"

# 2. Update the date in cv.py
sed -i '' "s/^CV_UPDATED = .*/CV_UPDATED = \"$DATE\"/" cv.py
echo "✓  Updated CV_UPDATED to $DATE in cv.py"

# 3. Rebuild index.html
python3 build.py

# 4. Commit and push
git add "$DEST" cv.py index.html
git commit -m "Update CV — $DATE"
echo "✓  Committed"

git push
echo "✓  Pushed to GitHub"
echo ""
echo "Your site will refresh in ~60 seconds."
