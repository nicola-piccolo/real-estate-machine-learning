from flask import jsonify, current_app as application
from . import realEstateMl

@realEstateMl.route('/hello')
def get_comment():
    application.logger.error('Hello World!')
    return jsonify({'message': 'Hello World!'})