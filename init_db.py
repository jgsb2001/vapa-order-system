from app import app, db, User

with app.app_context():
    db.create_all()
    
    admin = User.query.filter_by(username='admin').first()
    
    if not admin:
        admin = User(
            username='admin',
            full_name='Administrator',
            is_admin=True,
            is_active=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()
        print('Admin user created successfully!')
    else:
        print('Admin already exists')
