from flask import Flask, request
from uuid import uuid4
from copy import deepcopy
app = Flask(__name__)

index_html = open('front/index.html').read()

events = {}
constructor = {
    'mouse': {
        'x': 0.0, 'y': 0.0, 'z': 0.0
    },
    'keyboard': {
       'queue': []
    },
    'first': True
}
events['TEST'] = deepcopy(constructor)

@app.route('/')
def root():
    return index_html

@app.route('/read/<code>/')
def read(code):
    if(code not in events):
        return 'fail', 404
    # clear built up data on first connection
    if events[code]['first']:
        events[code] = deepcopy(constructor)
        events[code]['first'] = False
    return events[code]

@app.route('/write/<code>/')
def write(code):
    if(code not in events):
        return 'fail', 404
    events[code]['mouse']['x'] += float(request.args.get('x'))
    events[code]['mouse']['y'] += float(request.args.get('y'))
    events[code]['mouse']['z'] += float(request.args.get('z'))
    return 'ok'

@app.route('/reset/<code>')
def reset():
    if(code not in events):
        return 'fail', 404
    events[code] = deepcopy(constructor)
    return 'ok'

@app.route('/getcode/')
def make_code():
    code = uuid4().hex[0:5]
    events[code] = deepcopy(constructor)
    return code
