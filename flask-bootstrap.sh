#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=realEstateMl
export REAL_ESTATE_ML_DATABASE_HOSTNAME=127.0.0.1
export REAL_ESTATE_ML_DATABASE_NAME=real_estate_ml
export REAL_ESTATE_ML_DATABASE_USER=real_estate_ml_agent
export REAL_ESTATE_ML_DATABASE_PASSWORD=SuPeRsEcReTpWd
cd ./src
flask run