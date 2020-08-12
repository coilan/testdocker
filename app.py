#!/usr/bin/env python
# *-*coding:utf-8*-*
"""
@Version : Python3.6.5
@Author  : Coilan
@Date    : 2020-08-12
@Ide    : Pycharm
@Desc    ：
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9876,debug=True)
