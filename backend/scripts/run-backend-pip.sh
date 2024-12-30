#!/bin/bash

# create virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the app
python3 app.py