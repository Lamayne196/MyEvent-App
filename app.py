from flask import Flask
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from authRoute import auth
from dashboardRoute import dashboard
from eventRoute import event
from home import home


app = Flask(__name__)

# Session-Konfiguration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key'  # Geheimer Schlüssel für CSRF-Schutz
Session(app)

# CSRF-Schutz aktivieren
csrf = CSRFProtect(app)

# Blueprints registrieren
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(event, url_prefix='/event')
app.register_blueprint(home)


if __name__ == '__main__':
    app.run(debug=True)