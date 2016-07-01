#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: forms.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-06-13 21:59:29 (CST)
# Last Update:星期一 2016-6-13 22:1:28 (CST)
#          By:
# Description:
# **************************************************************************
from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms.fields import StringField, SubmitField


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    room = StringField('Room', validators=[DataRequired()])
    submit = SubmitField('Enter Chatroom')
