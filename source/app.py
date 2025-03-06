from flask import Flask, render_template, flash, redirect, url_for, session
from forms import RegisterForm, LoginForm
from models import db, User
from flask_bcrypt import Bcrypt
from functools import wraps
from sqlalchemy.exc import IntegrityError
from flask import abort

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MYSECRETKEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/flask_auth_db' #database connection

    bcrypt = Bcrypt()

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            return f(*args, **kwargs)
        return decorated_function


    @app.route('/')
    def index():
        return render_template("index.html")
    
    @app.route('/login', methods = ['GET','POST'])
    def login():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password,form.password.data): #password hashing
                session['user_id'] = user.id
                session['username'] = user.username
                flash("You have been logged in successfully..", 'success')            #flash messages
                return redirect(url_for('dashboard'))
            else:
                flash('Login unsuccessful.. Please check your credentials','danger')

        return render_template("login.html", form=form)
    
    @app.route('/register', methods = ['GET','POST'])
    def register():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        form = RegisterForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(
                username =  form.username.data,
                email = form.email.data,
                password = hashed_password,
            )

            try:
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created. You can login now.', 'success')
                return redirect(url_for('login'))
            except IntegrityError:
                db.session.rollback()
                flash('Email already exists. Please choose a different one.', 'danger')
            except Exception as e:
                db.session.rollback()
                flash('An unexpected error occurred. Please try again later.', 'danger')
                abort(500)
        return render_template("register.html",form=form)
    
    @app.route('/dashboard')
    @login_required
    def dashboard():
        # if 'user_id' not in session:
        #     return redirect(url_for('login'))
        return render_template("dashboard.html")

    @app.route('/logout')
    def logout():
        session.pop('user_id')
        session.pop('username')
        flash("You have been logged out successfully.. See you soon", 'success')
        return redirect(url_for('index'))


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,port=5001)