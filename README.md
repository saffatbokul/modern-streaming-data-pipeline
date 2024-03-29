📝 Modern Streaming Data Pipeline 🪐
-----------------------------------

### Overview 🚀

This project demonstrates a data streaming pipeline where Apache Airflow fetches data from an API and sends it the Kafka topic. Apache Spark then reads the user data from Kafka and processes and writes it to a Cassandra NOSQL database. It's like a data highway, with each component playing a crucial role in the smooth flow of information!

### Architecture 🌐

The architecture involves:
-   Apache Airflow: The traffic controller, orchestrating the data streaming process 🚦
-   Apache Kafka: The publisher, pushing user data onto the Kafka topic like a newsfeed 📰
-   Apache Spark: The data wrangler, transforming and preparing the data for storage 🛠️
-   Apache Cassandra: The data vault, storing the processed user data securely 💾


### Components 🧩

-   **kafka_stream.py**: Python functions that fetch, process, and send user data to Kafka. Think of it as the data generator, creating a stream of user information.
-   **entrypoint.sh**: The entrypoint script for the Airflow container, ensuring all the necessary dependencies and database setup. It's like the mechanic, making sure the engine is running smoothly.
-   **docker-compose.yml**: The Docker Compose file that brings all the components together in isolated containers. It's like the architect, designing the overall structure of the system.
-   **spark_stream.py**: Python functions that read data from Kafka, transform it using Spark, and write it to Cassandra. It's the data processor, crunching the numbers and organizing the information.

### Installation and Usage 🚀

-   Install Docker 🐳
-   Clone the repo: `git clone https://github.com/saffatbokul/modern-streaming-data-pipeline`
-   Build and run Docker images: `docker-compose up -d`

### Conclusion 🎉

This project is a data streaming dream team! It showcases how Airflow, Kafka, Spark, and Cassandra work together to automate complex data processing and storage tasks. It's like having a data management superpower, ensuring real-time insights and efficient data handling. 


