#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-05-26 22:44:55 (CST)
# Last Update:星期四 2016-11-24 15:15:3 (CST)
#          By:
# Description:
# **************************************************************************
from flask.views import MethodView
from flask import render_template, request
from .models import Topic


class PageListView(MethodView):
    def get(self):
        page = request.args.get('page', 1, type=int)
        topics = Topic.query.paginate(page, 3, True)
        return render_template('page/page.html', topics=topics)
