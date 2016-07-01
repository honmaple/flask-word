#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: extensions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-13 22:07:08 (CST)
# Last Update:星期五 2016-7-1 21:34:16 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple import Bootstrap, Error
from flask_wtf.csrf import CsrfProtect

# from celery import Celery


def register_maple(app):
    # maple = Bootstrap(css=('chat/chat.css', ), js=('chat/chat.js', ))
    maple = Bootstrap(css=('chat/chat.css', ))
    maple.init_app(app)
    Error(app)


def register_form(app):
    csrf = CsrfProtect()
    csrf.init_app(app)

# def register_socketio(app):
#     socketio.init_app(app)
#     return app

# def register_celery(app):
#     celery = Celery(app.import_name,
#                     backend=app.config['CELERY_RESULT_BACKEND'],
#                     broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
#     TaskBase = celery.Task

#     class ContextTask(TaskBase):
#         abstract = True

#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)

#     celery.Task = ContextTask
#     return celery
