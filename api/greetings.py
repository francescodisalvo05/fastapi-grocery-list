from flask import make_response, jsonify, request
from flask import current_app as app

import logging

logger = logging.getLogger()

@app.route('/say/hi', methods=['POST'])
def say_hi():

    data = request.json

    if data == '':
        app.logger.info('%s received successfully', data)
        response = make_response(jsonify({'hi' : data}))
        return response
    else:
        app.logger.info('Failed')
        return None

@app.route('/say/hello', methods=['POST'])
def say_hello():

    data = request.json
    response = make_response(jsonify({'hello' : data}))

    return response