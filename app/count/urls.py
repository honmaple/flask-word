#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:27:56 (CST)
# Last Update:星期四 2016-11-24 14:1:19 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import CountListView

site = Blueprint(
    'count', __name__, template_folder='templates', url_prefix='/count')

countlist_view = CountListView.as_view('countlist')

site.add_url_rule('/', view_func=countlist_view)
