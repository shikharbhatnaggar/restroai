import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("APP_ENV") == "development"

def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )


def fetch_one(query, params=None):

    conn = get_connection()

    try:
        if DEBUG:
            print("\n========== SQL ==========")
            print(query)
            print("PARAMS:", params)
            print("=========================\n")

        with conn.cursor() as cursor:

            cursor.execute(query, params)

            return cursor.fetchone()

    except Exception as e:
        print(f"Database Error: {e}")
        raise

    finally:

        conn.close()


def fetch_all(query, params=None):

    conn = get_connection()

    try:

        if DEBUG:
            print("\n========== SQL ==========")
            print(query)
            print("PARAMS:", params)
            print("=========================\n")

        with conn.cursor() as cursor:

            cursor.execute(query, params)

            return cursor.fetchall()
    
    except Exception as e:
        print(f"Database Error: {e}")
        raise

    finally:

        conn.close()


def execute(query, params=None):

    conn = get_connection()

    try:

        if DEBUG:
            print("\n========== SQL ==========")
            print(query)
            print("PARAMS:", params)
            print("=========================\n")

        with conn.cursor() as cursor:

            cursor.execute(query, params)

            return cursor.lastrowid
    
    except Exception as e:
        print(f"Database Error: {e}")
        raise

    finally:

        conn.close()

