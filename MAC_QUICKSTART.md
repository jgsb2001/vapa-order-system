# QUICK START FOR MAC USERS 🍎

## Option 1: Easy Way (One Command)

1. **Open Terminal** (Applications → Utilities → Terminal)

2. **Navigate to the folder:**
   ```bash
   cd ~/Downloads/vapa_order_system
   ```
   (Adjust path if you put it somewhere else)

3. **Run the startup script:**
   ```bash
   chmod +x START_HERE.sh
   ./START_HERE.sh
   ```

4. **Open your browser** to: http://localhost:5000

5. **Login:**
   - Username: `admin`
   - Password: `admin123`

---

## Option 2: Manual Commands

If the script doesn't work, run these commands one by one:

```bash
# Navigate to the folder
cd ~/Downloads/vapa_order_system

# Install Python dependencies
pip3 install -r requirements.txt

# Run the application
python3 app.py
```

Then open your browser to: http://localhost:5000

---

## Troubleshooting

### "pip3: command not found"

Install Python 3:
1. Go to https://www.python.org/downloads/
2. Download and install Python 3.11 or higher
3. Try the commands again

OR use Homebrew:
```bash
brew install python3
```

### "Permission denied"

Make the script executable:
```bash
chmod +x START_HERE.sh
```

### Port already in use

If port 5000 is busy, edit `app.py` at the bottom:
```python
app.run(debug=True, port=5001)  # Change 5000 to 5001
```

Then use: http://localhost:5001

---

## First Time Setup

After logging in as admin:

1. **Change your password** (very important!)
2. **Add teachers:**
   - Click "Manage Teachers"
   - Click "+ Add Teacher"
   - Add: Angelina, Jenn, Maricel, Jon, Scot, Sean

3. **Create a test order** to verify everything works

4. **Export to Excel** to test that feature

---

## Deploy Online (Recommended)

For production use, deploy to Render.com:
- See **QUICK_START.md** for full instructions
- 100% free
- 15 minutes to deploy
- Works from anywhere

---

## Stop the Server

When running locally:
- Press **Ctrl+C** in Terminal
- Or just close the Terminal window

---

## Need Help?

- Read: **README.md** for full documentation
- Read: **PROJECT_SUMMARY.md** for overview
- Read: **QUICK_START.md** for online deployment

---

**You're all set! Enjoy your new order management system! 🎨**
