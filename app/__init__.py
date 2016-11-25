#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:16:40
# *************************************************************************
from flask import Flask
from flask_maple.lazy import LazyExtension
from .filters import register_jinja2


def create_app(config=None):
    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
    else:
        app.config.from_object('config.config')
    register(app)
    return app


def register(app):
    register_extension(app)
    register_jinja2(app)


def register_extension(app):
    extension = LazyExtension(
        module='app.extension.',
        extension=[
            'db', 'csrf', 'bootstrap', 'error', 'redis_data', 'maple_app',
            'middleware', 'socketio'
        ])
    extension.init_app(app)
