from flask import Blueprint

realEstateMl = Blueprint('realEstateMl', __name__)

from . import errors, predictPrice, manageProperty