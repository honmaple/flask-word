#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-13 21:58:12 (CST)
# Last Update:星期五 2016-11-25 15:21:4 (CST)
#          By:
# Description:
# **************************************************************************
from flask import (render_template, session, redirect, url_for)
from flask.views import MethodView
from .forms import LoginForm


class ChatListView(MethodView):
    def get(self):
        form = LoginForm()
        username = session.get('username')
        room = session.get('room')
        if username and room:
            return render_template(
                'chat/chat.html', username=username, room=room)
        return render_template('chat/index.html', form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            session['username'] = form.username.data
            session['room'] = form.room.data
        return redirect(url_for('chat.chatlist'))


class ChatClearView(MethodView):
    def get(self):
        session.clear()
        return redirect(url_for('chat.chatlist'))


from . import events
