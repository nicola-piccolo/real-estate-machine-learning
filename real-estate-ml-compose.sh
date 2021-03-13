#!/bin/bash
servers_number=1
if [ "${1,,}" == '--scale' ]
then
    shift
    servers_number="$1"
    shift
fi
if [ "${1,,}" != 'up' ] && [ "${1,,}" != 'down' ] 
then
    echo "Usage:  real-estate-ml-compose [options] COMMAND
    
    options:
        --scale sets the number of servers for the real estate ML application

    COMMAND:
        up      bootstrap the whole cluster
        down    tear down the cluster"
    exit 1
fi
if [ "${1,,}" == 'up' ]
then
    exec docker-compose --file ./docker/docker-compose.yml up --detach --scale real-estate-ml=$servers_number
    exit 0
fi
if [ "${1,,}" == 'down' ]
then
    exec docker-compose --file ./docker/docker-compose.yml down
    exit 0
fi