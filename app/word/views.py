#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: views.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:17:57
# *************************************************************************
from app.extension import redis_data
from flask.views import MethodView
from flask import render_template, request, jsonify
from .form import WordsForm
from time import time


class WordListView(MethodView):
    def get(self):
        form = WordsForm()
        all_users = redis_data.hkeys("users")
        all_words = {}
        for user in all_users:
            user = str(user, 'utf-8')
            user_words_time = redis_data.hkeys(user)
            for user_word_time in user_words_time:
                all_words[user_word_time] = user
        return render_template(
            'word/index.html', form=form, all_words=all_words)

    def post(self):
        form = WordsForm()
        '''得到所有用户'''
        all_users = redis_data.hkeys("users")
        all_words = {}
        if form.validate_on_submit() and request.method == "POST":
            email = form.email.data
            name = form.name.data
            content = form.content.data
            if name.encode() in all_users:
                if str(redis_data.hget("users", name.encode()),
                       'utf-8') != email:
                    error = u'昵称已被占用'
                    return jsonify(judge=False, error=error)
            pipe = redis_data.pipeline()
            pipe.hset("users", name, email)
            word_time = int(time()) + 28800
            pipe.hset(name, word_time, content)
            pipe.execute()
            error = u"谢谢你的留言!"
            return jsonify(judge=True, error=error)
        else:
            if form.content.errors:
                error = form.content.errors
                return jsonify(judge=False, error=error)
            elif form.email.errors:
                error = form.email.errors
                return jsonify(judge=False, error=error)
            elif form.name.errors:
                error = form.name.errors
                return jsonify(judge=False, error=error)
            else:
                pass
            return render_template(
                'word/index.html', form=form, all_words=all_words)
