#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: views.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:17:57
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from app import redis_data
from . import site
from flask import render_template, request, jsonify, redirect,url_for,flash
from .form import VoteForm


choices = ['走进荒野', '荒野求生','学好人']
_vote = {
    'title': '请选择你最喜欢的电影:',
    'total':38,
    'list': [(str(x+1),y) for x,y in enumerate(choices)]
}



@site.route('')
def index():
    form = VoteForm()
    form.vote.choices = _vote['list']
    form.process()
    return render_template('vote/index.html', vote=_vote, form=form)

@site.route('/hello')
def hello():
    form = VoteForm()
    form.vote.choices = [('1','hello'),('2','world'),('3','hello world')]
    form.process()
    return render_template('vote/index.html', vote=_vote, form=form)


@site.route('/index', methods=['GET', 'POST'])
def vote():
    form = VoteForm()
    error = None
    form.vote.choices = _vote['list']
    if form.validate_on_submit() and request.method == "POST":
        if request.remote_addr.encode() in list(redis_data.smembers('vote:user')):
            error = u'你已投票，不能重复投票'
            return jsonify(judge=False, error=error)
        else:
            vote = int(form.vote.data) - 1
            name = _vote['list'][vote][1]
            redis_data.zincrby('vote',name,1)
            redis_data.sadd('vote:user',request.remote_addr)
            flash("投票成功")
            return jsonify(judge=True, error=error)
    else:
        if form.vote.errors:
            error = form.vote.errors
            return jsonify(judge=False, error=error)
        else:
            pass
        return redirect(url_for('vote.index'))
