from flask import Flask, jsonify, render_template, request
import requests
import csv
from io import StringIO

app = Flask(__name__)

API_URL = 'https://api.premiumy.net/v1.0'
API_KEY = 'Ca_PJ88mRmGfhAzXGFmFfw'


import datetime
import time
@app.route('/', methods=['GET'])
def index():
                key = request.args.get('key', None)
                number = request.args.get('number', None)
                start0 = datetime.datetime.now(datetime.timezone.utc)
                time.sleep(40)
            
                start = start0.strftime("%Y-%M-%dT%H:00:00")
                end = start0.strftime("%Y-%M-%dT%H:60:60")
                headers = {
                    'Content-Type': 'application/json',
                    'Api-Key': key,
                }

                json_data = {
                    'id': None,
                    'jsonrpc': '2.0',
                    'method': 'sms.mdr_full:get_list',
                    'params': {
                        'filter': {
                            'start_date': str(start),          
                            'end_date': str(end),
                            'senderid': 'Microsoft',
                            'phone': number,
                        },
                        'page': 1,
                        'per_page': 1,
                    },
                }

                response = requests.post('https://api.premiumy.net/v1.0/csv', headers=headers, json=json_data)
                return response.text
                #code = response.json()['result']['mdr_full_list'][len(response.json()['result']['mdr_full_list'])-1]['message']
