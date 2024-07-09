#!/bin/bash

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR/backend"

echo "Don't forget to install postgresql from: https://www.postgresql.org/download/"
echo "
      CREATE DATABASE induction_database;
      CREATE USER induction_curtin WITH ENCRYPTED PASSWORD 'mango';
      GRANT ALL PRIVILEGES ON DATABASE induction_database TO induction_curtin;
      GRANT ALL PRIVILEGES ON SCHEMA public TO induction_curtin;
      GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO induction_curtin;

echo "Creating a virtual environment..."
python3 -m venv venv

echo "Activating the virtual environment..."
source ./venv/bin/activate

echo "Installing Django and psycopg2..."
pip install django psycopg2-binary django-cors-headers

pip install XlsxWriter

echo "Running Django migrations..."
python manage.py migrate

echo "Setup complete."