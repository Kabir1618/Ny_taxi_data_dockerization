# Ny Taxi Data Dockerization

This project is aimed at setting up a Docker environment for ingesting CSV data into a PostgreSQL database using Python.

## Overview

The project consists of two Docker services:

1. **pgdatabase**:
   - PostgreSQL database container with version 13.
   - Environment variables for database configuration (user, password, database name).
   - Volume mapping for persistent data storage.
   - Exposes port 5432 for database access.

2. **pgadmin**:
   - pgAdmin 4 container for managing PostgreSQL databases.
   - Environment variables for default login credentials.
   - Exposes port 8080 for web access to pgAdmin.

## Prerequisites

Before running the project, ensure you have the following installed:

- Docker
- Python 3

## Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/Ny_taxi_data_dockerization.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Ny_taxi_data_dockerization
    ```

3. Run the Docker containers:

    ```bash
    docker-compose up -d
    ```

4. Execute the Python script to ingest CSV data into PostgreSQL:

    ```bash
    python ingest_csv_to_postgres.py --user <username> --password <password> --host pgdatabase --port 5432 --db ny_taxi --table_name <table_name> --url <csv_url>
    ```

   Replace `<username>`, `<password>`, `<table_name>`, and `<csv_url>` with appropriate values.

## Notes

- The `ingest_csv_to_postgres.py` script downloads a CSV file specified by the `<csv_url>` argument and ingests its data into the PostgreSQL database.
- Adjust the PostgreSQL connection parameters (`--user`, `--password`, `--host`, `--port`, `--db`) according to your database configuration.
- Ensure the `ny_taxi_postgres_data` directory exists in the project directory for volume mapping.
- Visit [localhost:8080](http://localhost:8080) to access pgAdmin and manage the PostgreSQL database.
