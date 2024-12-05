import os
import firebase_admin
from firebase_admin import credentials, firestore, storage

# Finde den Pfad zur MyEventDB.json automatisch
script_dir = os.path.dirname(os.path.abspath(__file__))
service_account_path = os.path.join(script_dir, 'MyEventDbKey.json')

# Firebase Admin initialisieren
cred = credentials.Certificate(service_account_path)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mydataevent.firebasestorage.app'  # Hier den tatsächlichen Bucket-Namen angeben
})

# Firebase Firestore und Storage initialisieren
db = firestore.client()
bucket = storage.bucket()

