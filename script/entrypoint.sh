#!/bin/bash 

# Set the environment to exit on errors (if any)
set -e

# Check if there is a requirements file available to install
if [  -e "/opt/airflow/requirements.txt" ]; then
  $(command python) pip install --upgrade pip
  $(command -v pip) install --user -r requirements.txt
fi

# Check if  the Airflow database exists
if [ ! -f "/opt/airflow/airflow.db" ]; then
  # Initialize an Airflow database if it doesn't exist
  airflow db init
  # Create the initial admin user
  airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin
fi

# Upgrade the database (if needed)
$(command -v airflow) db upgrade

# Start the Airflow webserver
exec  airflow webserver
