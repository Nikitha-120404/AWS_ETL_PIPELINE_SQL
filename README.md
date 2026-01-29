🌦️ AWS Weather ETL Pipeline (SQL + PySpark)
📌 Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline on AWS using real-time weather data.
The pipeline automatically collects weather data from an external API, stores it in a MySQL database, applies transformations using AWS Glue (SQL and PySpark), and saves the cleaned data for analytics.

This project demonstrates real-world data engineering skills including automation, cloud databases, and distributed data processing.

🎯 Project Goal

To build an automated and scalable cloud ETL pipeline that:

Ingests live API data

Cleans and enriches the data

Stores analytics-ready output

Uses AWS managed services end to end

🏗️ Architecture Overview

Pipeline Flow:

AWS Lambda

Fetches live weather data from the OpenWeather API

Triggered automatically every hour using CloudWatch

Inserts raw data into AWS RDS (MySQL)

AWS RDS (MySQL)

Stores structured raw weather data

Acts as the source for transformations

AWS Glue

Reads data from MySQL

Applies transformations using:

SQL (data cleaning & categorization)

PySpark (business logic)

Writes transformed data back to MySQL or to S3

Amazon S3

Stores transformed data (Parquet format)

Ready for analytics and reporting

🛠️ Technologies Used
Programming & Query Languages

Python

SQL

PySpark

AWS Services

AWS Lambda

Amazon RDS (MySQL)

AWS Glue

Amazon S3

Amazon CloudWatch

Amazon EC2 (for testing & connectivity)

Libraries

requests

pymysql

boto3

📂 Project Structure
AWS_ETL_PIPELINE_SQL/
│
├── src/
│   ├── lambda_function.py
│   ├── glue_weather_pyspark.py
│   └── glue_weather_transform.sql
│
├── outputs/
│   ├── mysql_weather_transformed_output.png
│   ├── s3_parquet_weather_output.png
│   └── glue_job_success.png
│
├── .gitignore
└── README.md

🔄 ETL Workflow Explained
🔹 Extract

AWS Lambda pulls weather data for multiple US cities

Data includes temperature, humidity, wind speed, and timestamp

Data is fetched every hour automatically

🔹 Transform

AWS Glue applies transformations:

Casts columns to correct data types

Categorizes temperature (Hot, Warm, Cool, Cold)

Categorizes humidity (Humid, Normal, Dry)

Filters out invalid or null records

🔹 Load

Transformed data is stored in:

MySQL (usa_weather_transformed)

Amazon S3 as Parquet files (optional)

📊 Sample Output
MySQL (Transformed Data)

Cleaned weather records

Categorized temperature & humidity

Ready for analytics queries

S3 (Parquet Output)

Column-optimized format

Efficient for tools like Athena or BI platforms

(See screenshots in the outputs/ folder)

⏱️ Automation

Lambda scheduled using CloudWatch

Glue jobs run automatically

Logs monitored through CloudWatch Logs

No manual intervention required

📚 What I Learned

Designing cloud-based ETL pipelines

Using AWS Lambda for serverless ingestion

Working with AWS Glue (SQL + PySpark)

Integrating relational databases with big data tools

Writing production-style data transformations

Managing AWS resources securely

🚀 Future Improvements

Query data using Amazon Athena

Build dashboards with Amazon QuickSight

Add error handling & alerting

Expand to global weather datasets

✅ Final Outcome

✔ Fully automated AWS ETL pipeline
✔ Real-time API data ingestion
✔ Clean, categorized analytics data
✔ Strong hands-on data engineering project

💡 This project demonstrates practical data engineering skills using AWS services, automation, and scalable data processing.
