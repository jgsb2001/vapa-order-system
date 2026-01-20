from app import app, db, User

with app.app_context():
    # Find the admin user
    admin = User.query.filter_by(username='admin').first()
    
    if admin:
        # Change password here (replace with YOUR password)
        admin.set_password('YourNewSecurePassword123')
        db.session.commit()
        print('✅ Admin password changed successfully!')
        print('New password set')
    else:
        print('❌ Admin user not found')
```

5. **IMPORTANT:** Replace `YourNewSecurePassword123` with **your actual new password**
6. **Commit the file**

**Step 2: Run it on Render**

1. **Go to Render → Your service → Settings**
2. **Find "Build Command"**
3. **Update it to:**
```
   pip install -r requirements.txt && python init_db.py && python change_admin_password.py
```
4. **Save Changes**
5. Render will auto-deploy

**Step 3: Check the Logs**

1. **Go to Logs tab**
2. **Look for:** `✅ Admin password changed successfully!`

**Step 4: Test the New Password**

1. **Logout**
2. **Login with:**
   - Username: `admin`
   - Password: `[your new password]`

**Step 5: Clean Up (Optional)**

After it works:
1. **Go back to GitHub**
2. **Delete `change_admin_password.py`** (you don't need it anymore)
3. **Update Build Command back to:**
```
   pip install -r requirements.txt && python init_db.py
