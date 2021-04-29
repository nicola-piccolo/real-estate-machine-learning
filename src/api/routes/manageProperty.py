from flask import request, jsonify
from flask_expects_json import expects_json
from . import realEstateMl
from .ResponseBuilder import ResponseBuilder
from .jsonschema.propertyJsonSchema import schema
from .requestmappers.PropertyRequestMapper import PropertyRequestMapper
from api.modules.property.PropertySaver import PropertySaver
from api.modules.property.PropertyLoader import PropertyLoader

@realEstateMl.route('/property', methods=['POST'])
@expects_json(schema)
def store_property():
    newProperty = PropertyRequestMapper.mapRequestIntoProperty(request.json)
    PropertySaver.saveNewProperty(newProperty)
    
    return ResponseBuilder.buildCreated({ 'id': newProperty.id })

@realEstateMl.route('/property', methods=['GET'])
def get_all_property():
    properties = PropertyLoader.getAllProperties()
    
    return ResponseBuilder.buildCreated({
        'data': [currentProperty.serialized for currentProperty in properties]
    })