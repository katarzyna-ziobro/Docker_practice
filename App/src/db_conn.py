from psycopg2 import pool
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))
DB_NAME = os.getenv("APP_DB_NAME")
DB_USER = os.getenv("APP_DB_NPTA")
DB_PASSWORD = os.getenv("APP_DB_NPTA_PASS")
DB_TABLE = os.getenv("APP_DB_TABLE")


class DB_conn:

    def __init__(self):
        self.connection_pool = pool.ThreadedConnectionPool( minconn=1,
            maxconn=10,
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
    

    def insert_lucky_number(self, number: int):
        conn = self.connection_pool.getconn()

        try:
            with conn.cursor() as cursor:
                command = f"INSERT INTO {DB_TABLE} (number) VALUES (%s)"
                cursor.execute(command, (number,))
                conn.commit()
                print("Number entered")

        except Exception as e:
            conn.rollback()
            raise e

        finally:
            self.connection_pool.putconn(conn)


    def get_last_10(self):
        conn = self.connection_pool.getconn()

        try:
            with conn.cursor() as cursor:
                command = f"SELECT number FROM {DB_TABLE} ORDER BY created_at DESC LIMIT 10"
                cursor.execute(command)

                rows = cursor.fetchall()
                return [row[0] for row in rows]

        finally:
            self.connection_pool.putconn(conn)