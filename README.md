# Dr. Lala Kounta — Personal Website

Academic website for Dr. Lala Kounta, Ocean & Climate Scientist.

**Live site:** https://YOUR-USERNAME.github.io/

---

## File structure

```
website/
├── index.html          ← Main website (edit to update content)
├── files/
│   └── CV_Dr_Lala_Kounta.pdf   ← CV PDF (replace to update)
└── README.md
```

---

## How to update your CV

1. Open your CV in Word, export as PDF → **Save as `CV_Dr_Lala_Kounta.pdf`**
2. Copy the new PDF into the `files/` folder (replace the old one)
3. Open Terminal, navigate here:
   ```bash
   cd ~/Documents/Personal/website
   ```
4. Commit and push:
   ```bash
   git add files/CV_Dr_Lala_Kounta.pdf
   git commit -m "Update CV - March 2026"
   git push
   ```
5. Wait ~60 seconds → your site at `https://YOUR-USERNAME.github.io/` is live ✓

---

## How to update website content

Edit `index.html` directly, then:
```bash
git add index.html
git commit -m "Update website content"
git push
```

---

## First-time GitHub Pages setup

1. Create a repo on GitHub named `YOUR-USERNAME.github.io`
2. Connect this folder to it:
   ```bash
   cd ~/Documents/Personal/website
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-USERNAME.github.io.git
   git push -u origin main
   ```
3. Go to the repo on GitHub → **Settings → Pages → Source: Deploy from a branch → main / root → Save**
4. Your site will be live at `https://YOUR-USERNAME.github.io/` within a minute.
