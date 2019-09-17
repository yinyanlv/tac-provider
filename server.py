#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, jsonify
from config import APP_MODE, conf
from db import read_series

app_name = conf.get('app', 'name')
app_host = conf.get('app', 'host')
app_port = conf.get('app', 'port')

is_debug = True if APP_MODE == 'dev' or APP_MODE == None else False

app = Flask(app_name)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def home():
    return 'welcome to tac-provider!'


@app.route('/get-series')
def get_series():
    list = read_series()
    return jsonify(list)


app.run(host=app_host, port=app_port, debug=is_debug)
