from flask import Blueprint, render_template, session, redirect, url_for, flash
from fireBase_config import db
from functools import wraps

dashboard = Blueprint('dashboard', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Bitte loggen Sie sich ein, um fortzufahren.', 'danger')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@dashboard.route('/')
@login_required
def dashboard_view():
    user_email = session.get('user')
    username = session.get('username')

    if not user_email:
        flash('Fehler: Keine Benutzersitzung gefunden. Bitte erneut einloggen.', 'danger')
        return redirect(url_for('auth.login'))

    user_ref = db.collection('users').where('email', '==', user_email).get()
    if not user_ref:
        flash('Benutzer nicht gefunden.', 'danger')
        return redirect(url_for('auth.login'))

    user_doc = user_ref[0]
    events = [{'id': event.id, **event.to_dict()} for event in user_doc.reference.collection('events').stream()]

    if not username:
        username = user_doc.get('username')
        session['username'] = username

    return render_template('dashboard.html', events=events, username=username)