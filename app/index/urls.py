#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:16:13 (CST)
# Last Update:星期四 2016-11-24 15:7:16 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import IndexView

site = Blueprint('index', __name__)

index_view = IndexView.as_view('index')
site.add_url_rule('/', view_func=index_view)
