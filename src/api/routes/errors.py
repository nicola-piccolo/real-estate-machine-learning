from flask import jsonify, make_response
from . import realEstateMl

@realEstateMl.errorhandler(400)
def bad_request_handler():
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@realEstateMl.app_errorhandler(404)
def not_found_handler(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@realEstateMl.errorhandler(500)
def internal_server_error_handler():
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)