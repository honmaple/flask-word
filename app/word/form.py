#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: form.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:27:21
# *************************************************************************
from flask_wtf import Form
from wtforms import TextAreaField, StringField
from wtforms.validators import Required, Email, Length


class WordsForm(Form):
    content = TextAreaField(
        '留言板',
        [Required(message=u"留言不能为空"), Length(
            min=4, message=u"留言不能少于4个字符")])
    email = StringField(
        '邮箱',
        [Required(message=u"邮箱不能为空"), Email(message=u"邮箱格式错误，请输入正确的邮箱地址")])
    name = StringField(
        '昵称', [
            Required(message=u"昵称不能为空"), Length(
                min=4, max=20, message=u"昵称长度在4到20个字符之间")
        ])
