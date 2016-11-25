#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 14:15:24 (CST)
# Last Update:星期五 2016-11-25 15:20:18 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import ChatListView, ChatClearView

site = Blueprint(
    'chat',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/chat')

chatlist_view = ChatListView.as_view('chatlist')
chatclear_view = ChatClearView.as_view('chatclear')

site.add_url_rule('/', view_func=chatlist_view)
site.add_url_rule('/clear', view_func=chatclear_view)
