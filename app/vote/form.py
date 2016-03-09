#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: form.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:27:21
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
from flask_wtf import Form
from wtforms import RadioField
from wtforms.validators import Required


class VoteForm(Form):
    vote = RadioField('投票',
                      validators=[Required(message=u"投票不能为空")])
