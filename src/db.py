from dotenv import load_dotenv
import os
import psycopg2

class DBConfig:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            print("Loading environment variables...")
            print("Connecting to the database...")
            print("Database Name:", os.getenv('DB_NAME'))
            print("Database Host:", os.getenv('DB_HOST'))
            print("Database User:", os.getenv('DB_USER'))
            print("Database Password:", os.getenv('DB_PASSWORD'))
            print("Database Port:", os.getenv('DB_PORT'))


            cls._instance = super(DBConfig, cls).__new__(cls)
            cls._instance.conn = psycopg2.connect(
                database=os.getenv('DB_NAME'),
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                port=os.getenv('DB_PORT'),
            )
            cls._instance.cursor = cls._instance.conn.cursor()
            print("Database connection established.")
        return cls._instance.cursor