#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: filters.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 14:54:33 (CST)
# Last Update:星期四 2016-11-24 15:19:44 (CST)
#          By:
# Description:
# **************************************************************************


def vote_count(name):
    from app.extension import redis_data
    counts = redis_data.zscore('vote', name)
    return counts


def get_word(time, name):
    from app.extension import redis_data
    time = str(time, 'utf-8')
    word = redis_data.hget(name, time)
    from datetime import datetime
    time = datetime.utcfromtimestamp(int(time))
    return str(word, 'utf-8'), name + ' 于 ' + str(time) + ' 留言:'


def register_jinja2(app):
    app.jinja_env.filters['get_word'] = get_word
    app.jinja_env.filters['vote_count'] = vote_count
