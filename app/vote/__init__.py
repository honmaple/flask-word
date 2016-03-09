#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:16:40
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import Blueprint
from app import app,redis_data

site = Blueprint('vote', __name__,template_folder='templates')


def register(site):
    register_jinja2()

def register_jinja2():
    def vote_count(name):
        counts = redis_data.zscore('vote',name)
        return counts
    app.jinja_env.filters['vote_count'] = vote_count

register(site)

from . import views
