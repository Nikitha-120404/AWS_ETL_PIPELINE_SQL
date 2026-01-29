# 🌦️ AWS Weather ETL Pipeline (SQL + PySpark)

## 📌 Project Overview
This project demonstrates a **complete end-to-end ETL (Extract, Transform, Load) pipeline on AWS** using real-time weather data.

The pipeline automatically extracts live weather data from an external API, stores it in **Amazon RDS (MySQL)**, transforms the data using **AWS Glue (SQL + PySpark)**, and outputs the cleaned and enriched data into **Amazon S3** and MySQL for analytics.

This project reflects **real-world data engineering practices**, including automation, cloud orchestration, and scalable data processing.

---

## 🎯 Project Objective
To build a **fully automated cloud ETL pipeline** that:
- Ingests live API data using serverless services
- Cleans and enriches raw data
- Applies business logic using SQL and PySpark
- Stores analytics-ready data
- Uses AWS services end to end

---

## 🏗️ Architecture Overview

### ETL Workflow
1. **AWS Lambda**
   - Fetches live weather data from the OpenWeather API
   - Triggered automatically every hour using Amazon CloudWatch
   - Inserts raw weather data into Amazon RDS (MySQL)

2. **Amazon RDS (MySQL)**
   - Stores raw weather data (`usa_weather`)
   - Stores transformed weather data (`usa_weather_transformed`)

3. **AWS Glue**
   - Reads data from MySQL
   - Applies transformations using:
     - SQL (casting, filtering, categorization)
     - PySpark (business logic using Spark)
   - Writes transformed data back to MySQL and S3

4. **Amazon S3**
   - Stores transformed weather data in Parquet format
   - Enables analytics and reporting use cases

---

## 🧠 Key Concepts

- Serverless data ingestion using **AWS Lambda**
- ETL orchestration with **AWS Glue (SQL + PySpark)**
- Relational data storage using **Amazon RDS (MySQL)**
- Data lake storage using **Amazon S3**
- Job monitoring and logging using **Amazon CloudWatch**
- Secure access using **IAM Roles & Policies**

---

## 🧩 Tech Stack

| Category | Tools & Services |
|--------|------------------|
| **Languages** | Python, SQL |
| **AWS Services** | Lambda, RDS (MySQL), Glue, S3, EC2, CloudWatch |
| **Libraries** | `requests`, `pymysql`, `boto3` |
| **Data Format** | JSON → CSV → Parquet |
| **Transformations** | SQL + PySpark |
| **Visualization** | AWS Console & MySQL Workbench |
| **Version Control** | Git & GitHub |

---

## 📂 Project Structure

AWS_ETL_PIPELINE_SQL/
│
├── Glue/
│ └── aws_glue_visual_etl.png
│
├── outputs/
│ ├── Mysql_weather_data_transform.png
│ ├── S3_parquet.png
│ └── transformed_weather_data.csv
│
├── src/
│ ├── lambda_function.py
│ ├── glue_weather_pyspark.py
│ └── glue_weather_transform.sql
│
└── README.md
---

## 🔄 ETL Process Explanation

### 🔹 Extract (Lambda)
- AWS Lambda fetches weather data for multiple US cities
- Extracted fields include temperature, humidity, wind speed, and timestamp
- Lambda is triggered every hour using CloudWatch

### 🔹 Transform (AWS Glue)
- SQL transformations:
  - Cast columns to correct data types
  - Categorize temperature (`Hot`, `Warm`, `Cool`, `Cold`)
  - Categorize humidity (`Humid`, `Normal`, `Dry`)
  - Filter out invalid records
- PySpark transformations:
  - Apply business rules
  - Enrich data using Spark DataFrames

### 🔹 Load (MySQL & S3)
- Transformed data written to:
  - MySQL table: `usa_weather_transformed`
  - Amazon S3 as Parquet files
- CSV output also generated for reference

---

## 📊 Outputs & Results

The `outputs/` folder contains proof of successful execution:
- **MySQL transformed data screenshot**
- **S3 Parquet file output**
- **CSV transformed dataset**

These outputs confirm that the ETL pipeline executed successfully end to end.

---

## ⏱️ Automation & Monitoring
- Lambda scheduled using **Amazon CloudWatch**
- Glue jobs run automatically
- Logs monitored through **CloudWatch Logs**
- No manual intervention required

---

## 📚 What I Learned
- Building serverless ingestion pipelines using AWS Lambda
- Writing SQL and PySpark transformations in AWS Glue
- Integrating relational databases with big data tools
- Designing scalable ETL workflows on AWS
- Managing IAM roles and secure cloud access
- Structuring production-ready data engineering projects

---

## 🚀 Future Enhancements
- Query data using Amazon Athena
- Build dashboards using Amazon QuickSight
- Add alerting and error notifications
- Expand dataset to include global cities

---

## ✅ Final Outcome
✔ Fully automated AWS ETL pipeline  
✔ Real-time weather data ingestion  
✔ Clean, enriched analytics-ready data  
✔ Strong portfolio project for data engineering roles  

---

💡 *This project demonstrates hands-on data engineering skills using AWS services, automation, and scalable data processing.*
