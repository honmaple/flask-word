#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: events.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-13 22:04:25 (CST)
# Last Update:星期五 2016-7-1 21:1:25 (CST)
#          By:
# Description:
# **************************************************************************
from jinja2 import Template
from flask import session
from flask.ext.socketio import emit, join_room, leave_room
from werkzeug.utils import escape
from .. import socketio


def get_html(username, msg):
    template = Template('''
    <div class="text-left" style="margin-bottom:10px">
    <span class="msg">
    {{ username }}
    </span>
    </div>
    <div class="text-left u-infor">
    <span class="bg-info infor">
    {{ msg }}
    </span>
    </div>
    ''')
    return template.render(username=username, msg=msg)


@socketio.on('joined', namespace='/chat')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('username') + ' has entered the room.'},
         room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    username = session.get('username')
    msg = escape(message['msg'])
    html = get_html(username, msg)
    emit('message', {'html': html}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('username') + ' has left the room.'},
         room=room)
