from flask import jsonify, make_response

class ResponseBuilder:
    
    @staticmethod
    def buildBadRequest(errorMessage='Bad Request'):
        return make_response(jsonify({'error': errorMessage}), 400)
    
    @staticmethod
    def buildNotFound(errorMessage='Not found'):
        return make_response(jsonify({'error': errorMessage}), 404)
    
    @staticmethod
    def buildInternalServerError(errorMessage='Internal Server Error'):
        return make_response(jsonify({'error': errorMessage}), 500)

    @staticmethod
    def buildCreated(payload={}):
        return make_response(jsonify(payload), 201)