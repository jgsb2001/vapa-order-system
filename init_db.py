from app import app, db, User

with app.app_context():
    # Create tables
    db.create_all()
    
    # Check if admin exists
    admin = User.query.filter_by(username='admin').first()
    
    if not admin:
        # Create admin user
        admin = User(
            username='admin',
            full_name='Administrator',
            is_admin=True,
            is_active=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('✅ Admin user created successfully!')
        print('Username: admin')
        print('Password: admin123')
    else:
        print('⚠️ Admin user already exists')
```

5. **Click "Commit changes"**

### Update Render Build Command

6. **Go to Render Dashboard → Your Service → Settings**
7. **Find "Build Command"**
8. **Change it to:**
```
   pip install -r requirements.txt && python init_db.py
