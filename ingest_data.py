import pandas as pd
from sqlalchemy import create_engine
import argparse
import os
def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db 
    table_name = params.table_name
    url = params.url

    csv_name = 'output.csv'

    #download the csv
    os.system(f"curl {url} -o {csv_name}")

    engine = create_engine(f'postgresql://{args.user}:{args.password}@{args.host}:{args.port}/{args.db}')
    engine.connect()
    csv_name2 = 'yellow_tripdata_2021-01.csv.gz'
    df_iter = pd.read_csv(csv_name2,  iterator=True, chunksize=100000)

    while True:
        try:
            df = next(df_iter)
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.to_sql(table_name, con=engine, if_exists='append')
        except StopIteration:
            print("Finished")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV to postgres')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='db for postgres')
    parser.add_argument('--table_name', help='table for postgres')
    parser.add_argument('--url', help='url of csv')

    args = parser.parse_args()
    main(args)