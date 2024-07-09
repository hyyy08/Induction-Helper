#!/bin/bash

set -e

source ./venv/bin/activate

echo "Running backend server..."
python manage.py runserver