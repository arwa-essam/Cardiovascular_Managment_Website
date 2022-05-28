from flask import Blueprint, render_template, request, flash, redirect, url_for
# import the register database
from .models import User
# for security create a hashed password not the actuall typed password
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        SSN = request.form.get('SSN')
        address = request.form.get('address')
        ID = request.form.get('ID')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 character.', category='error')   
        elif len(last_name) < 2:
            flash('last name must be greater than 2 character.', category='error')    
        #elif password1 != password2:
            #flash('Passwords don\'t match.', category='error')
        elif len(password1) < 4:
            flash('Password must be at least 4 characters.', category='error')
        else:
            # if all inputs are right -> start creating the account
            new_user = User(first_name=first_name, last_name=last_name, email=email,  password=generate_password_hash(
                password1, method='####'), SSN=SSN, address=address, ID=ID)
            # add newuser to the database
            db.session.add(new_user)
            # update the database after adding new user
            db.session.commit()
            # 
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/about')
def about():
    return render_template("about.html")

@auth.route('/contactus')
def contactus():
    return render_template("contactus.html")   

@auth.route('/devices')
def devices():
    return render_template("devices.html")

@auth.route('/admin')
def admin():
    return render_template("admin.html")          