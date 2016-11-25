#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:19:22 (CST)
# Last Update:星期四 2016-11-24 13:26:22 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import VoteListView

site = Blueprint(
    'vote', __name__, template_folder='templates', url_prefix='/vote')

votelist_view = VoteListView.as_view('votelist')

site.add_url_rule('/', view_func=votelist_view)
