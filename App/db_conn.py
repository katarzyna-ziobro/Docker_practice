import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = int(os.environ.get("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


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
                cursor.execute(
                    """
                    INSERT INTO lucky_numbers (number)
                    VALUES (%s)
                    """,
                    (number,)
                )
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
                cursor.execute(
                    """
                    SELECT number
                    FROM lucky_numbers
                    ORDER BY created_at DESC
                    LIMIT 10
                    """
                )

                rows = cursor.fetchall()
                return [row[0] for row in rows]

        finally:
            self.connection_pool.putconn(conn)