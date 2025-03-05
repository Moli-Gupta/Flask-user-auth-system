Flask Authentication System
A simple Flask-based user authentication system using PostgreSQL. 
Features:
✔ User Registration (with password hashing)
✔ Login & Logout (session-based authentication)
✔ Protected Dashboard (only accessible after login)

Installation
1. Clone the Repository

git clone https://github.com/Moli-Gupta/Flask-user-auth-system.git
cd Flask-user-auth
cd source

2. Setup Virtual Environment & Install Dependencies

python -m venv .venv
.venv\Scripts\activate.ps1     # Windows  
pip install -r Requirements.txt


Tech Stack

✔ Flask (Backend)
✔ PostgreSQL (Database)
✔ Flask-WTF (Forms & Validation)
✔ Flask-Login (Authentication)
✔ Flask-Bcrypt (Password Hashing)
✔ SQLAlchemy (ORM for database management)

File Structure

/source
│
├── __pycache__/               # Compiled Python files (auto-generated)
├── .venv/                     # Virtual environment files
│
├── templates/                 # HTML templates folder
│   ├── dashboard.html         # Dashboard page
│   ├── index.html             # Home or welcome page
│   ├── layout.html            # Base layout template
│   ├── login.html             # Login page
│   └── register.html          # Registration page
│
├── app.py                     # Main Flask application
├── forms.py                   # Flask-WTF form classes for login/registration
├── models.py                  # Database models (e.g., User model)
│
├── README.txt                 # Documentation or setup instructions
├── Requirements.txt           # Python dependencies file (requirements.txt)
├── schema.sql                 # SQL schema file for database creation
