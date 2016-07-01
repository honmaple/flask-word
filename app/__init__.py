#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:16:40
# *************************************************************************
from flask import Flask, render_template
from redis import StrictRedis
from config import load_config
from flask import send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from .extensions import register_form, register_maple


def create_app():
    app = Flask(__name__)
    config = load_config()
    app.config.from_object(config)
    return app


def register(app):
    register_form(app)
    register_maple(app)
    register_blueprint(app)


def register_blueprint(app):
    from .vote import site
    app.register_blueprint(site, url_prefix='/vote')
    from .word import site
    app.register_blueprint(site, url_prefix='/word')
    from .count import site
    app.register_blueprint(site, url_prefix='/count')
    from .paginate.views import site
    app.register_blueprint(site, url_prefix='/paginate')
    from .chat.views import site as chat_site
    app.register_blueprint(chat_site, url_prefix='/chat')


app = create_app()
socketio = SocketIO(app)
db = SQLAlchemy(app)
# celery = register_celery(app)
config = app.config
redis_data = StrictRedis(db=config['REDIS_DB'],
                         password=config['REDIS_PASSWORD'])
register(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/robots.txt')
@app.route('/favicon.ico')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
