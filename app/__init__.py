#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: __init__.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:16:40
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask import Flask
from flask_assets import Environment, Bundle
from redis import StrictRedis
from app import config


def register(app):
    register_assets(app)
    register_form(app)
    register_jinja2(app)

def register_jinja2(app):
    def get_word(time,name):
        time = str(time,'utf-8')
        word = redis_data.hget(name,time)
        from datetime import datetime
        time = datetime.utcfromtimestamp(int(time))
        return str(word,'utf-8'),name + ' 于 ' + str(time) + ' 留言:'
    app.jinja_env.filters['get_word'] = get_word

def register_form(app):
    from flask_wtf.csrf import CsrfProtect
    csrf = CsrfProtect()
    csrf.init_app(app)

def register_assets(app):
    bundles = {

        'home_js': Bundle(
            'style/js/jquery.min.js',      #这里直接写static目录的子目录 ,如static/bootstrap是错误的
            'style/js/bootstrap.min.js',
            output='style/assets/home.js',
            filters='jsmin'),

        'home_css': Bundle(
            'style/css/bootstrap.min.css',
            output='style/assets/home.css',
            filters='cssmin')
        }

    assets = Environment(app)
    assets.register(bundles)

app = Flask(__name__)
app.config.from_object(config)
config = app.config
redis_data = StrictRedis(db=config['REDIS_DB'],
                            password=config['REDIS_PASSWORD'])
register(app)

from app import views
