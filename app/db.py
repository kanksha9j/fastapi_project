#psycopg2 is a PostgreSQL database adapter for python that allows Python programs
# to connect to a PostgreSQL database, execute SQL queries and handle results.
import psycopg2  #pip install psycopg2-binary
from psycopg2.extras import RealDictCursor
from psycopg2 import OperationalError
import time

from app.config import settings
#never put db environment variables directly here.
#to configure environment variables safely use 

def get_db_connection():
    while True:
        try:     
            conn = psycopg2.connect(
                host=settings.db_host,
                port=settings.db_port,
                dbname=settings.db_name,
                user=settings.db_user,
                password=settings.db_password,
                cursor_factory=RealDictCursor
            )
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            print("Database connection established")
            break
        except Exception as error:
            print(f"Error connecting to the database: {error}")
            time.sleep(2)

    return conn, cursor