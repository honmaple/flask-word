#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:39:09 (CST)
# Last Update:星期四 2016-11-24 15:7:53 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import PageListView

site = Blueprint(
    'paginate', __name__, template_folder='templates', url_prefix='/paginate')
pagelist_view = PageListView.as_view('pagelist')

site.add_url_rule('/', view_func=pagelist_view)
