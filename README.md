# VAPA Order Management System
## Saddleback High School - Visual and Performing Arts Department

A web-based order management system for tracking departmental purchases, budget allocation, and vendor orders.

---

## Features

✅ **Teacher Management**
- Admin panel to add, edit, and manage teacher accounts
- Individual teacher logins with secure authentication
- Active/inactive account status

✅ **Order Management**
- Create orders for different vendors
- Add multiple items per order
- Real-time cost calculations
- Category-based organization (Books & Supplies, Consultants, Repairs, etc.)

✅ **Budget Tracking**
- Department-wide budget overview
- Category breakdowns
- Teacher spending summaries
- Remaining budget calculations

✅ **Export Functionality**
- Export all orders to Excel
- Formatted summary sheets
- Individual teacher sheets

✅ **User-Friendly Interface**
- Clean, modern design
- Mobile-responsive
- Intuitive navigation
- Real-time calculations

---

## Quick Start

### Option 1: Run Locally (Testing)

1. **Install Python** (3.9 or higher)
   - Download from https://python.org

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the System**
   - Open browser to: http://localhost:5000
   - Login: `admin` / `admin123`
   - **IMPORTANT:** Change admin password immediately!

---

### Option 2: Deploy Online (Free Hosting)

## Deployment to Render.com (Recommended - FREE)

### Step 1: Prepare Your Files

1. Download all files from this project
2. Create a free account at https://render.com

### Step 2: Create GitHub Repository

1. Go to https://github.com and create a new repository
2. Upload all project files to the repository
3. Make sure these files are included:
   - app.py
   - requirements.txt
   - Procfile (create this - see below)
   - All templates and static folders

### Step 3: Create Procfile

Create a file named `Procfile` (no extension) with this content:
```
web: gunicorn app:app
```

### Step 4: Deploy on Render

1. Log into Render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name:** vapa-orders (or your choice)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

5. Click "Create Web Service"
6. Wait 5-10 minutes for deployment
7. Your app will be live at: `https://your-app-name.onrender.com`

### Step 5: Security Setup

⚠️ **CRITICAL SECURITY STEPS:**

1. **Change Secret Key**
   In `app.py`, line 11:
   ```python
   app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
   ```
   Generate a random key:
   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

2. **Change Admin Password**
   - Log in as admin
   - Create yourself a new admin account
   - Delete the default admin account

3. **Update Database Path** (for production)
   Consider using PostgreSQL for production (Render provides free PostgreSQL)

---

## Alternative Deployment Options

### Heroku (Free Tier Removed - Paid Only)
### Railway.app (Free Tier Available)
### PythonAnywhere (Free Tier Available)

Instructions for these platforms available in DEPLOYMENT_GUIDE.md

---

## User Guide

### For Administrators

#### Initial Setup

1. **Login**
   - Default credentials: `admin` / `admin123`
   - **Change immediately!**

2. **Add Teachers**
   - Go to "Manage Teachers"
   - Click "+ Add Teacher"
   - Enter:
     - Full Name (e.g., "Angelina DeLoch")
     - Username (e.g., "angelina")
     - Temporary Password
   - Teacher can change password after first login

3. **Set Budget**
   - Budget is currently hardcoded in `app.py` line 131
   - Edit the line: `total_budget = 50128`
   - Restart the application

#### Monitoring Orders

- **Dashboard** shows:
  - Total budget vs allocated
  - Category breakdowns
  - Teacher spending summaries

- **Export to Excel**
  - Click "Export to Excel" button
  - Downloads complete order data
  - Includes summary and individual teacher sheets

### For Teachers

#### Creating an Order

1. **Login** with credentials provided by admin
2. Click "+ New Order"
3. Enter vendor name (e.g., "Blick Art Materials")
4. Click "Create Order & Add Items"

#### Adding Items

1. Fill in each row:
   - **Catalog #:** Item/product number
   - **Description:** What you're ordering
   - **Quantity:** How many
   - **Unit Cost:** Price per item
   - **Category:** Select from dropdown
   
2. **Total Cost** calculates automatically

3. Click "+ Add Item" for more rows

4. Click "Save Order" when done

#### Viewing Your Totals

- Dashboard shows your category totals
- Each order card displays order total
- View detailed breakdowns in order view

---

## Database Schema

### Users Table
- id (Primary Key)
- username (Unique)
- password_hash
- full_name
- is_admin (Boolean)
- is_active (Boolean)
- created_at

### Orders Table
- id (Primary Key)
- user_id (Foreign Key → Users)
- vendor
- created_at
- updated_at

### OrderItems Table
- id (Primary Key)
- order_id (Foreign Key → Orders)
- catalog_number
- description
- quantity
- unit_cost
- category

---

## Categories

The system tracks spending in these categories:
1. **Books & Supplies** - Art materials, instruments, classroom supplies
2. **Consultants** - Professional development, teaching artists
3. **Repairs** - Instrument repairs, technology maintenance
4. **Software Licensing** - Software subscriptions
5. **Conference/Training** - Professional development events
6. **Field Trips** - Transportation and field trip costs

---

## Security Features

✅ Password hashing (bcrypt)
✅ Session-based authentication
✅ Role-based access control (Admin/Teacher)
✅ CSRF protection (Flask built-in)
✅ Input validation
✅ SQL injection protection (SQLAlchemy ORM)

### Recommended Production Security Enhancements

1. Use HTTPS (Render provides this automatically)
2. Implement rate limiting
3. Add email verification
4. Enable 2FA for admin accounts
5. Regular database backups

---

## Troubleshooting

### "Database locked" error
- SQLite issue with concurrent access
- Solution: Upgrade to PostgreSQL for production

### Items not saving
- Check browser console for JavaScript errors
- Ensure all form fields are filled correctly

### Cannot login
- Verify username and password
- Check if account is marked "Active"
- Contact admin to reset password

### Export not working
- Check openpyxl is installed: `pip install openpyxl`
- Browser should download automatically

---

## Customization

### Change Colors
Edit `/static/css/style.css`:
- Primary color: `#4472C4`
- Dark blue: `#203864`
- Success green: `#28a745`

### Add New Categories
1. Edit `app.py` - update category dictionaries
2. Edit templates - update category dropdowns
3. Edit `_data` sheet in original Excel (for reference)

### Modify Budget
Edit `app.py` line 131:
```python
total_budget = 50128  # Change this number
```

---

## Support

For technical issues or questions:
1. Check this README
2. Review the code comments
3. Contact your IT department
4. Email: [your-contact-email]

---

## License

Developed for Saddleback High School VAPA Department
© 2025 All Rights Reserved

---

## Credits

Built with:
- Flask (Python web framework)
- SQLAlchemy (Database ORM)
- Bootstrap-inspired CSS
- OpenPyXL (Excel export)

Developed for Saddleback High School Visual and Performing Arts Department

---

## Changelog

### Version 1.0 (January 2026)
- Initial release
- Teacher management
- Order entry system
- Budget tracking
- Excel export
