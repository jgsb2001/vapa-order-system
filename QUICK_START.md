# QUICK DEPLOYMENT GUIDE
## Get Your VAPA Order System Online in 15 Minutes

---

## OPTION 1: Render.com (RECOMMENDED - 100% FREE)

### Why Render?
✅ Completely FREE forever
✅ Automatic HTTPS/SSL
✅ Easy GitHub integration
✅ Auto-deploys when you update code
✅ Perfect for school projects

### Steps:

#### 1. Create GitHub Account (if you don't have one)
- Go to https://github.com
- Sign up (free)

#### 2. Upload Your Code
1. Download this entire folder
2. Go to https://github.com/new
3. Name it: `vapa-order-system`
4. Upload all files from this folder

#### 3. Deploy on Render
1. Go to https://render.com
2. Sign up with your GitHub account
3. Click "New +" → "Web Service"
4. Select your `vapa-order-system` repository
5. Settings:
   - **Name:** `saddleback-vapa-orders` (or anything you want)
   - **Region:** Oregon (closest to you)
   - **Branch:** main
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Plan:** Free

6. Click "Create Web Service"
7. Wait 5-10 minutes
8. Done! Your URL: `https://saddleback-vapa-orders.onrender.com`

#### 4. First Login
- URL: `https://your-app-name.onrender.com`
- Username: `admin`
- Password: `admin123`
- **IMMEDIATELY change the password!**

---

## OPTION 2: Run on School Computer (No Internet Required)

### For Testing or Internal Use Only

1. **Install Python**
   - Download: https://python.org
   - Version 3.9 or higher
   - During install: Check "Add Python to PATH"

2. **Run Setup**
   - Double-click: `START_HERE.bat` (Windows)
   - Or in terminal: `python app.py`

3. **Access Locally**
   - Open browser
   - Go to: `http://localhost:5000`
   - Login: `admin` / `admin123`

4. **Access from Other School Computers**
   - Find your computer's IP address
   - Share URL: `http://YOUR-IP:5000`
   - Only works on school network

---

## OPTION 3: Railway.app (Alternative Free Option)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Railway auto-detects Python
6. Wait for deployment
7. Get your URL

---

## LINKING TO YOUR SCHOOL WEBSITE

Since your school uses Finalsite (sausd.us/saddleback), you can:

### Option A: Add a Button/Link
1. Log into Finalsite admin
2. Edit your VAPA department page
3. Add a button/link:
   - Text: "VAPA Order System"
   - URL: `https://your-app-name.onrender.com`

### Option B: Embed in iFrame (if Finalsite allows)
```html
<iframe src="https://your-app-name.onrender.com" width="100%" height="800px"></iframe>
```

### Option C: Add to Navigation
- Contact your district webmaster
- Request link added to navigation menu
- They can add it to the main menu

---

## IMPORTANT: First Steps After Deployment

### 1. Change Admin Password
```
1. Login as admin/admin123
2. Go to Dashboard
3. Click your name
4. Change password (feature to add)
```

### 2. Add Yourself as New Admin
```
1. Go to "Manage Teachers"
2. Add a new teacher with YOUR info
3. Edit that teacher → Make admin
4. Logout and login as yourself
5. Delete the default admin account
```

### 3. Add Your Teachers
Based on your Excel file, add:
- Angelina DeLoch
- Jenn Connell
- Maricel Castellon
- Jon Gibson
- Scot Hansen
- Sean Knight

### 4. Test Everything
- Create a test order
- Add some items
- Check calculations
- Export to Excel
- Delete test data

---

## SECURITY CHECKLIST

Before going live:

☐ Changed admin password
☐ Created personal admin account
☐ Deleted default admin
☐ Changed secret key in app.py (for production)
☐ Tested on mobile device
☐ Verified teachers can login
☐ Tested Excel export
☐ Set correct budget amount

---

## GETTING HELP

### Free Deployment Issues
- Render Docs: https://render.com/docs
- Render Community: https://community.render.com

### Code Issues
- Check README.md
- Review error messages
- Contact IT department

### School Integration
- Contact Finalsite support
- Work with district webmaster
- SAUSD IT Help Desk

---

## MAINTENANCE

### Regular Tasks
- ✅ Backup database monthly (download export)
- ✅ Review teacher spending
- ✅ Update budget at start of year
- ✅ Archive old orders

### Updates
When code updates needed:
1. Edit files on GitHub
2. Render auto-deploys new version
3. Database stays intact

---

## TIPS FOR SUCCESS

💡 **Start Small**
- Add yourself and one teacher first
- Create test orders together
- Fix any issues before rolling out

💡 **Training**
- Show teachers how to use it
- Create a quick video tutorial
- Share screenshot guide

💡 **Backup Plan**
- Keep Excel file as backup
- Export regularly
- Save exports to Google Drive

💡 **Mobile Access**
- System works on phones/tablets
- Teachers can add orders anywhere
- Good for vendor visits

---

## COST: $0

Everything in this guide is **completely free**:
- ✅ GitHub: Free
- ✅ Render: Free tier (plenty for school use)
- ✅ Code/Software: Free
- ✅ Domain: Uses Render's free subdomain

Optional paid upgrades (NOT needed):
- Custom domain: ~$12/year
- Upgraded hosting: ~$7/month
- Database backups: Usually free tier enough

---

## TIMELINE

- ⏱️ **5 min:** Create GitHub account, upload code
- ⏱️ **5 min:** Deploy on Render
- ⏱️ **5 min:** Initial setup, change passwords
- ⏱️ **15 min:** Add teachers, test system
- ⏱️ **30 min:** Total to be fully operational

---

## SUPPORT CONTACTS

**Technical Support:**
- Render Status: https://status.render.com
- GitHub Help: https://docs.github.com

**School Support:**
- SAUSD IT: [contact info]
- District Webmaster: [contact info]
- Your School Tech Coordinator: [contact info]

---

**Ready to deploy? Start with Option 1 - Render.com!**

Questions? Check the full README.md for detailed documentation.
