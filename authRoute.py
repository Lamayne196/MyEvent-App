from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from fireBase_config import db
from forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        query = db.collection('users').where('email', '==', email).where('password', '==', password).get()
        if query:
            user_data = query[0].to_dict()
            session['user'] = email
            session['username'] = user_data['username']
            flash('Du hast dich erfolgreich angemeldet.', 'success')
            return redirect(url_for('dashboard.dashboard_view'))

        flash('Ungültige Anmeldeinformationen.', 'danger')
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if db.collection('users').where('email', '==', email).get():
            flash('E-Mail bereits vergeben.', 'danger')
            return redirect(url_for('auth.register'))

        db.collection('users').add({'username': username, 'email': email, 'password': password})
        flash('Benutzer erfolgreich registriert.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('username', None)
    flash('Du hast dich erfolgreich abgemeldet.', 'success')
    return redirect(url_for('home.home_view'))