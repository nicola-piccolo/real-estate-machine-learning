import jsonschema
from .ResponseBuilder import ResponseBuilder
from . import realEstateMl

@realEstateMl.errorhandler(400)
def bad_request_handler(error):
    if isinstance(error.description, jsonschema.ValidationError):
        return ResponseBuilder.buildBadRequest(str(error.description))
    else:
        return ResponseBuilder.buildBadRequest(error.description)

@realEstateMl.app_errorhandler(404)
def not_found_handler(error):
    return ResponseBuilder.buildNotFound(error.description)

@realEstateMl.errorhandler(500)
def internal_server_error_handler(error):
    return ResponseBuilder.buildInternalServerError(error.description)