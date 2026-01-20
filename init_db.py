from app import app, db, User, Settings, BudgetHistory

with app.app_context():
    # Create all tables
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
        print('✅ Admin user created successfully!')
        print('Username: admin')
        print('Password: admin123')
    else:
        print('⚠️ Admin user already exists')
    
    # Check if budget setting exists
    budget_setting = Settings.query.filter_by(key='total_budget').first()
    
    if not budget_setting:
        # Create default budget setting
        budget_setting = Settings(
            key='total_budget',
            value='50128',
            updated_by='System'
        )
        db.session.add(budget_setting)
        print('✅ Default budget setting created: $50,128')
    else:
        print(f'⚠️ Budget setting already exists: ${budget_setting.value}')
    
    # Commit all changes
    db.session.commit()
    print('✅ Database initialization complete!')
