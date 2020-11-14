#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:40:33 2020

@author: kerstin
"""

from bottle import Bottle, HTTPResponse, run, request, response, json_dumps
from ModbusData import ModbusData

#dataMod = ModbusData(period=2)
#data = dataMod.addData()
#print(data)

app = Bottle()

@app.get("/")
def index():
    return "OK"

@app.hook('after_request')
def enable_cors():
    print("after_request hook")
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Accept, Content-Type'

@app.post('/search')
def search():
    return HTTPResponse(body=json_dumps(['series A', 'series B']),
                            headers={'Content-Type': 'application/json'})
    
@app.post('/query')
def query():
    if request.json['targets'][0]['type'] == 'table':
        series = request.json['targets'][0]['target']
        bodies = {'series A': [{
        "columns":[
          {"text":"Time","type":"time"},
          {"text":"Country","type":"string"},
          {"text":"Number","type":"number"}
        ],
        "rows":[
          [1234567,"SE",123],
          [1234567,"DE",231],
          [1234567,"US",321]
        ],
        "type":"table"
        }], 'series B': [{
        "columns":[
          {"text":"Time","type":"time"},
          {"text":"Country","type":"string"},
          {"text":"Number","type":"number"}
        ],
        "rows":[
          [1234567,"BE",123],
          [1234567,"GE",231],
          [1234567,"PS",321]
        ],
        "type":"table"
        }]}

        series = request.json['targets'][0]['target']
        body = json_dumps(bodies[series])
        return HTTPResponse(body=body,
                            headers={'Content-Type': 'application/json'})

if __name__ == '__main__':
    run(app=app, host='localhost', port=8085)