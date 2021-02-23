#!/bin/bash
export ENV APPLICATION_ENVIRONMENT="production"
exec gunicorn -b 0.0.0.0:8000 realEstateMl:application