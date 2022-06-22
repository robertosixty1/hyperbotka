#!/bin/sh

if [ ! -f "pyvenv.cfg" ]; then
    python -m venv .
fi

source ./bin/activate
./bin/pip3 install -r requirements.txt
