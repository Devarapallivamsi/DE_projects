# SCD data (type2) merge ingestion on databricks using PySpark
![image](https://github.com/user-attachments/assets/fb778bdc-e593-40d5-8031-32a30309ccd4)
![image](https://github.com/user-attachments/assets/90ba543d-891b-4862-88ca-015512532d77)

## Overview
1. A databricks workflow is scheduled to trigger the spark notebook.
2. PySpark script in the notebook programmatically fetches the date of execution using python's `datetime` module.
3. The date string is used to read the corresponding day's input files from dbfs (S3 bucket).
4. The input files are read into spark dataframe and quality checks are run against them. 
5. If the data quality checks are failed, pipeline run halts.Otherwise, bookings data in ingested into delta (fact) table and customer data to delta (dimension) table.

## Tech Stack
1. AWS S3
2. AWS IAM 
3. Databricks
4. PySpark
5. Python

## Steps followed
1. Setup AWS CSP as the storage and compute provider for databricks.
2. Authored PySpark script on databricks notebook containing the logic to process the data.
     2.1) Get the date
     2.2) Fetch the input files corresponding to the date.
     2.3) Run data quality checks (defined using Pydeequ)
     2.4) Ingest the data if quality checks are succeeded.
     2.5) Implement incremental ingestion of bookings data (into fact table).
     2.6) Implement SCD2 merge of customer data (into dimension table).
3. Created and configured the workflow to trigger the processing everyday at 11:00 A.M.(scheduled).

## Conclusion
This project effectively demonstrates the automated merge ingestion of SCD2 data.
