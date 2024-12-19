from flask import Blueprint, render_template, request
from fireBase_config import db

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def home_view():
    category = request.args.get('category', '').strip()
    platform = request.args.get('platform', '').strip()
    format = request.args.get('format', '').strip()
    tags = request.args.getlist('tag')

    events_ref = db.collection('public_events')
    query = events_ref

    if category:
        query = query.where('category', '==', category)
    if platform:
        query = query.where('platform', '==', platform)
    if format:
        query = query.where('format', '==', format)
    if tags:
        for tag in tags:
            query = query.where('tags', 'array_contains', tag)

    events = [event.to_dict() | {'id': event.id} for event in query.stream()]


    all_tags = {tag for event in events if 'tags' in event for tag in event['tags']}

    return render_template('home.html', events=events, all_tags=all_tags)