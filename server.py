#!/usr/bin/env python3
# coding=utf-8 

import os
from flask import Flask  
from config import APP_MODE, get_conf

conf = get_conf()
app_name = conf.get('app', 'name')
app_host = conf.get('app', 'host')
app_port = conf.get('app', 'port')

is_debug = True if APP_MODE == 'dev' or APP_MODE == None else False

app = Flask(app_name)


@app.route('/')
def home():
  return 'welcome to tac!'


@app.route('/get-series')
def get_series():
  return 'get series'


app.run(host = app_host, port = app_port, debug = is_debug)  