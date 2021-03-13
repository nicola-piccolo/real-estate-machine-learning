#!/bin/bash
if [ "${1,,}" != '--development' ] && [ "${1,,}" != '--production' ] || [ "${2,,}" != 'up' ] && [ "${2,,}" != 'down' ] 
then
    echo "Usage:  real-estate-ml-compose options COMMAND
    
    options:
        --development   runs the application in development mode
        --production    runs the application in production mode

    COMMAND:
        up      bootstrap the whole cluster
        down    tear down the cluster"
    exit 1
fi
if [ "${1,,}" == '--production' ]
then
    export APPLICATION_ENVIRONMENT=production
else
    export APPLICATION_ENVIRONMENT=development
fi
if [ "${2,,}" == 'up' ]
then
    exec docker-compose --file ./docker/docker-compose.yml up --detach
    exit 0
fi
if [ "${2,,}" == 'down' ]
then
    exec docker-compose --file ./docker/docker-compose.yml down
    exit 0
fi