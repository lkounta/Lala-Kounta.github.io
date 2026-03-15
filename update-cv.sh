#!/bin/bash
# ─────────────────────────────────────────────────────────────
# update-cv.sh  —  Drop a new PDF here and push to GitHub
# Usage:  ./update-cv.sh /path/to/your/new-cv.pdf
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

cp "$PDF" "$DEST"
echo "✓  Copied to $DEST"

git add "$DEST"
git commit -m "Update CV — $DATE"
echo "✓  Committed"

git push
echo "✓  Pushed to GitHub"
echo ""
echo "Your site will refresh in ~60 seconds."
