#*************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: run.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-12-20 18:13:59
#*************************************************************************
#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# from app import app
from flask import Flask,request,make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    if 'count' in request.cookies:
        count = int(request.cookies['count']) + 1
    else:
        count = 0
    response = make_response(str(count))
    response.set_cookie('count',value=str(count),max_age=1800)
    return response
if __name__ == '__main__':
    app.run()

