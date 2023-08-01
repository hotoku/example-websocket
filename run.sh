#!/bin/bash


PID=$(ps -ef | grep 'python app.py' | grep -v grep | awk '{print $2}')
if ! [[ -z "${PID}" ]]; then
    echo "killing ${PID}"
    kill ${PID}
else
    echo "no process"
fi


python app.py
