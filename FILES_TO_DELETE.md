# Files to Keep vs Delete

## ✅ KEEP THESE FILES (Essential)

### Main Application
- **`splitter_with_per_image.py`** - The per-image settings application
- **`requirements.txt`** - Dependency list (used by launchers)

### Launchers (Choose Your Platform)
- **`run_per_image.bat`** - Windows launcher (auto-installs dependencies)
- **`run_per_image.sh`** - Linux/macOS launcher (auto-installs dependencies)

### Documentation (Recommended)
- **`README.md`** - Main documentation
- **`COMPLETED.md`** - Per-image version guide
- **`GETTING_STARTED.md`** - Quick start guide
- **`PER_IMAGE_SETTINGS.md`** - Feature documentation

---

## ❌ DELETE THESE FILES (Redundant)

### Redundant Launchers
- ❌ `run_modern.bat` - You're only using per-image version
- ❌ `run.bat` - Original version launcher
- ❌ `run.sh` - Original version launcher
- ❌ `splitter.bat` - Old launcher

### Redundant Setup Scripts
- ❌ `setup.bat` - Launchers now check Python automatically
- ❌ `setup.sh` - Launchers now check Python automatically
- ❌ `install.bat` - Launchers now auto-install dependencies

### Redundant Python Files
- ❌ `splitter_modern.py` - You're only using per-image version
- ❌ `splitter.py` - Original version
- ❌ `splitter.pyw` - Windows-specific original version

---

## ⚠️ OPTIONAL (Keep if Useful)

### Documentation
- `IMPROVEMENTS.md` - Details of all improvements made
- `IMPLEMENTATION_GUIDE.md` - Technical implementation details
- `QUICK_REFERENCE.md` - Quick lookup reference
- `LAUNCHER_IMPROVEMENTS.md` - Launcher consolidation details
- `FILES_TO_DELETE.md` - This file

### Backup/Reference
- `splitter_modern.py` - Keep if you want the modern version without per-image settings
- `splitter.py` - Keep if you want the original simple version

---

## 📁 Final Minimal File Structure

After cleanup, you'll have:

```
splitter/
├── splitter_with_per_image.py    ← Main application
├── requirements.txt               ← Dependencies
├── run_per_image.bat             ← Windows launcher
├── run_per_image.sh              ← Linux/macOS launcher
├── README.md                      ← Main docs
├── COMPLETED.md                   ← Usage guide
├── GETTING_STARTED.md             ← Quick start
└── PER_IMAGE_SETTINGS.md          ← Feature docs
```

**Total: 8 essential files**

---

## 🗑️ Deletion Commands

### Windows (PowerShell)
```powershell
# Delete redundant launchers
Remove-Item run_modern.bat, run.bat, run.sh, splitter.bat

# Delete redundant setup scripts
Remove-Item setup.bat, setup.sh, install.bat

# Delete redundant Python files
Remove-Item splitter_modern.py, splitter.py, splitter.pyw

# Delete optional documentation (if you don't need it)
Remove-Item IMPROVEMENTS.md, IMPLEMENTATION_GUIDE.md, QUICK_REFERENCE.md, LAUNCHER_IMPROVEMENTS.md, FILES_TO_DELETE.md
```

### Linux/macOS (Bash)
```bash
# Delete redundant launchers
rm run_modern.bat run.bat run.sh splitter.bat

# Delete redundant setup scripts
rm setup.bat setup.sh install.bat

# Delete redundant Python files
rm splitter_modern.py splitter.py splitter.pyw

# Delete optional documentation (if you don't need it)
rm IMPROVEMENTS.md IMPLEMENTATION_GUIDE.md QUICK_REFERENCE.md LAUNCHER_IMPROVEMENTS.md FILES_TO_DELETE.md
```

### Safe Deletion (One at a Time)
If you want to be cautious, delete files one at a time and test:

1. Delete one redundant file
2. Run `run_per_image.bat` (or `.sh`)
3. Verify it still works
4. Repeat

---

## 📊 File Size Comparison

### Before Cleanup
- ~40+ files
- Multiple versions
- Confusing structure

### After Cleanup
- 8 essential files
- One version
- Clear purpose

---

## ✅ Verification Checklist

After deletion, verify:

- [ ] `run_per_image.bat` (Windows) or `run_per_image.sh` (Linux/macOS) exists
- [ ] `splitter_with_per_image.py` exists
- [ ] `requirements.txt` exists
- [ ] Running the launcher works
- [ ] Dependencies auto-install on first run
- [ ] Application launches successfully

---

## 🔄 If You Need to Restore

If you accidentally delete something important:

1. **From Git:** `git checkout <filename>`
2. **From Backup:** Restore from your backup
3. **Recreate:** The launchers and docs can be recreated from this guide

---

## 📝 Summary

**Keep:**
- Main app: `splitter_with_per_image.py`
- Launcher: `run_per_image.bat` / `run_per_image.sh`
- Dependencies: `requirements.txt`
- Docs: `README.md`, `COMPLETED.md`, `GETTING_STARTED.md`, `PER_IMAGE_SETTINGS.md`

**Delete:**
- All other `.bat`, `.sh` files
- All other `.py`, `.pyw` files
- All setup/install scripts
- Optional: Extra documentation

**Result:** Clean, simple, single-version setup! 🎉
