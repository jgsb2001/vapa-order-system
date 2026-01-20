from app import app, db, User

with app.app_context():
    # Find your user by username
    user = User.query.filter_by(username='jongibson').first()  # Change to YOUR username
    
    if user:
        user.is_admin = True
        db.session.commit()
        print(f'✅ {user.full_name} is now an admin!')
    else:
        print('❌ User not found. Check the username.')
```

4. **Commit the file**
5. **Update your Render Build Command** to:
```
   pip install -r requirements.txt && python init_db.py && python make_admin.py
