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

site = Blueprint('word', __name__,template_folder='templates')

def register(site):
    register_jinja2()


def register_jinja2():
    def get_word(time, name):
        time = str(time, 'utf-8')
        word = redis_data.hget(name, time)
        from datetime import datetime
        time = datetime.utcfromtimestamp(int(time))
        return str(word, 'utf-8'), name + ' 于 ' + str(time) + ' 留言:'
    app.jinja_env.filters['get_word'] = get_word

register(site)

from . import views
