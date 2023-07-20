#!/bin/bash


PID=$(ps -ef | grep 'python app2.py' | grep -v grep | awk '{print $2}')
if ! [[ -z ${PID} ]]; then
    echo "killing ${PID}"
    kill ${PID}
else
    echo "no process"
fi


python app2.py
