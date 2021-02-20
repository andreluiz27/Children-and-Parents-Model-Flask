import json

from flask import Response, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from main import app, bcrypt, db

 @app.route('/login', methods=['GET', 'POST'])
 def login():
      form = LoginForm()

     if form.validate_on_submit():
         user = User.query.filter_by(username=form.username.data).first()
         if user and bcrypt.check_password_hash(user.password, form.password.data):
             login_user(user)
             return redirect(url_for('home'))
         else:
             flash('Login Unsuccessful. Please check email and password', 'danger')
     return render_template('login.html', title='Login', form=form)


 @app.route("/logout")
 def logout():
     logout_user()
     return redirect(url_for('home'))



