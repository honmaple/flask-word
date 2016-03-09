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
from config import load_config

def create_app():
    app = Flask(__name__, static_folder='static')
    config = load_config()
    app.config.from_object(config)
    return app

def register(app):
    register_assets(app)
    register_form(app)
    register_blueprint(app)

def register_form(app):
    from flask_wtf.csrf import CsrfProtect
    csrf = CsrfProtect()
    csrf.init_app(app)

def register_blueprint(app):
    from .index import site
    app.register_blueprint(site,url_prefix='')
    from .vote import site
    app.register_blueprint(site,url_prefix='/vote')
    from .word import site
    app.register_blueprint(site,url_prefix='/word')
    from .count import site
    app.register_blueprint(site,url_prefix='/count')

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

app = create_app()
config = app.config
redis_data = StrictRedis(db=config['REDIS_DB'],
                            password=config['REDIS_PASSWORD'])
register(app)


