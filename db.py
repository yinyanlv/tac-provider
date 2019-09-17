#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pyodbc
from config import conf

server = conf.get('db', 'server')
username = conf.get('db', 'username')
password = conf.get('db', 'password')
database = conf.get('db', 'database')
driver = conf.get('db', 'driver')


def get_connect_str():
    return 'DRIVER={{{0}}};SERVER={1};DATABASE={2};UID={3};PWD={4}'.format(driver, server, database, username, password)


def read_series():
    list = []
    cursor.execute('SELECT Code, Description FROM dbo.Catalog')
    for row in cursor:
        item = {}
        item['id'] = row[0]
        item['name'] = row[1]
        list.append(item)
    return list


conn = pyodbc.connect(get_connect_str())
cursor = conn.cursor()
