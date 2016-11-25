#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:17:23 (CST)
# Last Update:星期四 2016-11-24 13:18:15 (CST)
#          By:
# Description:
# **************************************************************************
from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):
    def get(self):
        return render_template('index.html')
