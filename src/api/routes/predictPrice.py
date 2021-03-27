from flask import request, jsonify
from flask_expects_json import expects_json
from . import realEstateMl
from .responseBuilder import ResponseBuilder
from .jsonschema.predictPriceJsonSchema import schema
from api.modules.pricePredictor.PricePredictor import PricePredictor

@realEstateMl.route('/predict-price', methods=['POST'])
@expects_json(schema)
def predict_price():
    predictor = PricePredictor()
    prediction = predictor.predict([request.json])
    return ResponseBuilder.buildCreated({ 'prediction': prediction[0] })