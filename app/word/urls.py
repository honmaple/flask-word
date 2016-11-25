#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:30:41 (CST)
# Last Update:星期四 2016-11-24 14:0:54 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import WordListView

site = Blueprint(
    'word', __name__, template_folder='templates', url_prefix='/word')

wordlist_view = WordListView.as_view('wordlist')
site.add_url_rule('/', view_func=wordlist_view)
