#!/bin/bash
if [ "${1,,}" != 'up' ] && [ "${1,,}" != 'down' ]
then
    echo "Usage:  real-estate-ml-compose COMMAND
    
    COMMAND:
        up      bootstrap the whole cluster
        down    tear down the cluster"
    exit 1
fi
if [ "${1,,}" == 'up' ]
then
    exec docker-compose --file ./docker/docker-compose.yml up --detach
    exit 0
fi
if [ "${1,,}" == 'down' ]
then
    exec docker-compose --file ./docker/docker-compose.yml down
    exit 0
fi