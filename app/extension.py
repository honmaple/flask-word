#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: extensions.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-13 22:07:08 (CST)
# Last Update:星期五 2016-11-25 14:56:2 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple import Bootstrap, Error
from flask_wtf.csrf import CsrfProtect
from flask_maple.app import App
from flask_maple.json import CustomJSONEncoder
from flask_socketio import SocketIO
from flask_maple.models import db
from flask_maple.redis import Redis
from flask_maple.middleware import Middleware


db = db
socketio = SocketIO()
bootstrap = Bootstrap()
error = Error()
csrf = CsrfProtect()
maple_app = App(json=CustomJSONEncoder)
redis_data = Redis()
middleware = Middleware()
