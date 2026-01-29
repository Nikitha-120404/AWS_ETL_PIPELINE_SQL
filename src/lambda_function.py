"""
AWS Lambda Function: Weather Data Ingestion
-------------------------------------------
Triggered automatically every 1 hour via AWS CloudWatch.
Fetches live weather data from OpenWeatherMap API and inserts it into
AWS RDS (MySQL) for further ETL processing in AWS Glue.
"""

import os
import pymysql
import requests
from datetime import datetime


def lambda_handler(event, context):
    """
    Lambda entry point function.
    Extracts weather data from OpenWeatherMap API and inserts into AWS RDS.
    """

    # --- AWS RDS (MySQL) Connection Details ---
    host = os.environ["DB_HOST"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]
    port = 3306

    # --- Cities to Collect Weather Data For ---
    cities = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
        "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
        "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington"
    ]

    # --- API Setup ---
    api_key = os.environ["OPENWEATHER_API_KEY"]
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # --- Connect to MySQL Database ---
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=dbname,
            port=port,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conn.cursor()
        print("Connected to RDS successfully.")

    except Exception as e:
        print("Database connection failed:", e)
        return {"statusCode": 500, "body": f"Database connection error: {e}"}

    # --- Fetch Weather Data and Insert into DB ---
    try:
        for city in cities:
            params = {"q": city, "appid": api_key, "units": "metric"}
            response = requests.get(base_url, params=params, timeout=15)
            data = response.json()

            cursor.execute(
                """
                INSERT INTO usa_weather
                    (city, weather_desc, temperature, humidity, wind_speed, recorded_at)
                VALUES
                    (%s, %s, %s, %s, %s, %s)
                """,
                (
                    city,
                    data["weather"][0]["description"],
                    data["main"]["temp"],
                    data["main"]["humidity"],
                    data["wind"]["speed"],
                    datetime.utcnow(),
                ),
            )
            print(f"Inserted weather data for: {city}")

        conn.commit()
        print("All weather data committed to RDS successfully.")

    except Exception as e:
        print("Error inserting data:", e)
        conn.rollback()
        return {"statusCode": 500, "body": f"Data insertion error: {e}"}

    finally:
        cursor.close()
        conn.close()

    # --- Success Response ---
    return {
        "statusCode": 200,
        "body": "Weather data inserted successfully into AWS RDS (MySQL)."
    }

  
