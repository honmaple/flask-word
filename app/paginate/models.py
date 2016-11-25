#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: modesl.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-11-24 13:43:31 (CST)
# Last Update:星期四 2016-11-24 15:14:5 (CST)
#          By:
# Description:
# **************************************************************************
from flask_maple.models import ModelMixin
from app.extension import db


class Topic(db.Model, ModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(120))

    def __repr__(self):
        return '<Topic %r>' % str(self.id)
