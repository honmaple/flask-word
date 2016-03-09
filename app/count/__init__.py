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

site = Blueprint('count', __name__,template_folder='templates')

from . import views
