from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from firebase_admin import storage
from fireBase_config import db
from dashboardRoute import login_required
from forms import CreateEventForm  # Importiere das Formular

event = Blueprint('event', __name__)

@event.route('/<event_id>', methods=['GET', 'POST'])
def eventInfo(event_id):
    user_email = session.get('user')
    events_ref = db.collection('public_events')
    doc_ref = events_ref.document(event_id)
    doc = doc_ref.get()

    if not doc.exists:
        return "Event nicht gefunden", 404

    event_data = doc.to_dict() | {'id': event_id}
    rsvp_status = user_email and doc_ref.collection('participants').document(user_email).get().exists

    if request.method == 'POST':
        if 'update_event' in request.form:
            updated_data = {
                'title': request.form.get('title'),
                'date': request.form.get('date'),
                'location': request.form.get('location'),
                'description': request.form.get('description'),
                'category': request.form.get('category'),
                'max_participants': int(request.form.get('max_participants'))
            }
            doc_ref.update(updated_data)
            flash('Änderungen erfolgreich.', 'success')
            return redirect(url_for('event.eventInfo', event_id=event_id))

        elif 'delete_event' in request.form:
            doc_ref.collection('participants').list_documents()
            doc_ref.delete()
            return redirect(url_for('dashboard.dashboard_view'))

    is_creator = user_email and event_data.get('created_by') == user_email
    template = 'eventInfo.html' if is_creator else 'eventInfoGuest.html'
    return render_template(template, event=event_data, rsvp_status=rsvp_status)

@event.route('/create', methods=['GET', 'POST'])
@login_required
def createEvent():
    form = CreateEventForm()
    if form.validate_on_submit():
        # Konvertiere das Datum in einen String
        date = form.date.data
        date_string = date.isoformat()  # Konvertiere date in einen String

        # Restliche Formulardaten
        title = form.title.data
        description = form.description.data
        location = form.location.data
        category = form.category.data
        max_participants = form.max_participants.data
        format = form.format.data
        platform = form.platform.data
        tags = form.tags.data.split(',') if form.tags.data else []
        image = form.image.data

        # Bild in Firebase hochladen
        bucket = storage.bucket()
        blob = bucket.blob(f'event_images/{image.filename}')
        blob.upload_from_file(image)
        blob.make_public()
        image_url = blob.public_url

        # Event-Daten speichern
        event_data = {
            'title': title,
            'description': description,
            'date': date_string,  # Verwende den konvertierten String
            'location': location,
            'category': category,
            'image_url': image_url,
            'created_by': session.get('user'),
            'max_participants': max_participants,
            'rsvp_count': 0,
            'format': format,
            'platform': platform,
            'tags': tags
        }

        event_ref = db.collection('public_events').add(event_data)
        flash('Event erfolgreich erstellt.', 'success')
        return redirect(url_for('event.eventInfo', event_id=event_ref[1].id))

    return render_template('createEvent.html', form=form)

@event.route('/<event_id>/rsvp', methods=['POST'])
def rsvp(event_id):
    events_ref = db.collection('public_events')
    doc_ref = events_ref.document(event_id)
    doc = doc_ref.get()

    if not doc.exists:
        return "Event nicht gefunden", 404

    event_data = doc.to_dict()
    max_participants = event_data.get('max_participants', 0)
    current_rsvp_count = event_data.get('rsvp_count', 0)
    participants_ref = doc_ref.collection('participants')

    email = request.form.get('email_participant')
    participant_doc = participants_ref.document(email).get()

    if 'cancel_rsvp' in request.form:
        if participant_doc.exists:
            participants_ref.document(email).delete()
            doc_ref.update({'rsvp_count': current_rsvp_count - 1})
            flash('Du hast das Event erfolgreich abgesagt.', 'success')
    else:
        if current_rsvp_count >= max_participants:
            flash('Teilnehmerlimit erreicht.', 'danger')
            return redirect(url_for('event.eventInfo', event_id=event_id))

        if participant_doc.exists:
            flash('Du hast bereits zugesagt.', 'warning')
            return redirect(url_for('event.eventInfo', event_id=event_id))

        participants_ref.document(email).set({
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': email
        })
        doc_ref.update({'rsvp_count': current_rsvp_count + 1})
        flash('Du hast dich erfolgreich für das Event angemeldet.', 'success')

    return redirect(url_for('event.eventInfo', event_id=event_id))

@event.route('/<event_id>/participants', methods=['GET'])
@login_required
def participantList(event_id):
    user_email = session.get('user')
    if not user_email:
        return redirect(url_for('auth.login'))

    events_ref = db.collection('public_events')
    doc_ref = events_ref.document(event_id)
    participants = doc_ref.collection('participants').stream()

    participant_list = [{'first_name': p.get('first_name'), 'last_name': p.get('last_name'), 'email': p.get('email')} for p in participants]

    return render_template('participantList.html', participants=participant_list, event_id=event_id)

@event.route('/<event_id>/delete', methods=['POST'])
@login_required
def deleteEvent(event_id):
    user_email = session.get('user')
    if not user_email:
        return redirect(url_for('auth.login'))

    db.collection('public_events').document(event_id).delete()
    flash('Event erfolgreich gelöscht.', 'success')
    return redirect(url_for('dashboard.dashboard_view'))