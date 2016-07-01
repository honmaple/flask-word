#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-13 21:58:12 (CST)
# Last Update:星期五 2016-7-1 21:19:26 (CST)
#          By:
# Description:
# **************************************************************************
from flask import (Blueprint, render_template, session, redirect, url_for,
                   request)
from .forms import LoginForm

site = Blueprint('chat',
                 __name__,
                 template_folder='templates',
                 static_folder='static')


@site.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        session['username'] = form.username.data
        session['room'] = form.room.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.username.data = session.get('username', '')
        form.room.data = session.get('room', '')
    return render_template('chat/index.html', form=form)


@site.route('/chat')
def chat():
    username = session.get('username', '')
    room = session.get('room', '')
    if username == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat/chat.html', username=username, room=room)


from . import events
