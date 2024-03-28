import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import json
from kafka import KafkaProducer
import time
import logging

# Default arguments for the Airflow DAG
default_args = {
    'owner': 'saffat',
    'start_date': datetime(2024, 3, 26, 10, 00)
}

# Function to fetch user data from a random user API endpoint
def fetch_data():
    """Fetches user data from the randomuser.me/api endpoint and returns it as a dictionary."""
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

# Function to process user data into the desired format
def process_data(res):
    """Takes raw user data as input and returns it in a processed format."""
    data = {}
    location = res['location']
    data['id'] = uuid.uuid4()
    data['firstname'] = res['name']['first']
    data['lastname'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

# Function to send processed user data to a Kafka topic
def send_data():
    """Produces messages containing processed user data to the 'user_list' Kafka topic."""
    # Create a Kafka producer instance
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    
    # Set the start time for the loop
    curr_time = time.time()
    
    # Send messages to Kafka until 120 seconds have elapsed
    while True:
        if time.time() > curr_time + 120:
            break
        
        try:
            # Fetch raw user data from the API endpoint
            res = fetch_data()
            
            # Process the raw data into the desired format
            res = process_data(res)
            
            # Send the processed data as a JSON message to Kafka
            producer.send('user_list', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'Error occured: {e}')
            continue
    
    # Close the producer connection
    producer.close()

# Create an Airflow DAG with a daily schedule
with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    # Define the streaming task to send user data to Kafka
    streaming_task = PythonOperator(
                        task_id='stream_data_from_api',
                        python_callable=send_data
                    )
