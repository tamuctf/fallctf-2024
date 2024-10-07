from src.__init__ import db

from src.util.db_schema import Submission
from src.util.bot import view_message

from flask import Blueprint, render_template, request, make_response, current_app, jsonify

import uuid


pages = Blueprint('pages', __name__)


@pages.route('/', methods=['GET'])
def index():
    resp = make_response(render_template('index.html'))
    session = request.cookies.get('session')

    if(session == None):
        resp.set_cookie('session', uuid.uuid4().hex)

    return resp


@pages.route('/botview/<id>', methods=['GET'])
def bot_view(id):
    if request.cookies.get('session') != current_app.config['ADMIN_SESSION']:
        return 'no'

    payload = Submission.get_submission(id)
    return render_template('submission.html', payload=payload)


@pages.route('/api/submit', methods=['POST'])
def submit():
    try:
        if request.json['comment'] != '':
            if len(request.json['comment']) > 256:
                return jsonify({"message": "Comment too long"})

            if '<' not in request.json['comment']:
                return jsonify({"message": "Comment submitted to admin for review"})

            if '<script>' in request.json['comment']:
                return jsonify({"message": "<script> tags not allowed"})

            submission = Submission(message=request.json['comment'])
            db.session.add(submission)
            db.session.commit()
            view_message(submission.id)

            return jsonify({"message": "Comment submitted to admin for review"})
        return jsonify({"message": "An error occured please try again"})
    except Exception as e:
        print(e, flush=True)
        return jsonify({"message": "An error occured please try again"})


@pages.route('/flag', methods=['GET'])
def flag():
    if request.cookies.get('session') != current_app.config['ADMIN_SESSION']:
        return 'no'
    
    return render_template('flag.html', flag=current_app.config['FLAG'])
