#!/bin/bash


python -m http.server > /tmp/web.log 2>&1 &
python app.py > /tmp/app.log 2>&1 &
