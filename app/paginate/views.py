#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-05-26 22:44:55 (CST)
# Last Update:星期五 2016-5-27 0:12:8 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint, render_template, abort, request
from app import app, db

site = Blueprint('paginate', __name__, template_folder='templates')


def is_num(num):
    if num is not None:
        try:
            num = int(num)
            if num > 0:
                return num
            else:
                abort(404)
        except ValueError:
            abort(404)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(120))

    def __repr__(self):
        return '<Topic %r>' % self.id


@site.route('')
def index():
    app.config['PER_PAGE'] = 3
    page = is_num(request.args.get('page'))
    topics = Topic.query.paginate(page, app.config['PER_PAGE'], error_out=True)
    return render_template('page/page.html', topics=topics)
