# SCD data (type2) merge ingestion on databricks using PySpark
![image](https://github.com/user-attachments/assets/fb778bdc-e593-40d5-8031-32a30309ccd4) <br><br>
## [draw.io pipeline flow visualisation](https://app.diagrams.net/#G10UyFN__m84G239hEkaDJhKhJ8dhcFXwh#%7B%22pageId%22%3A%220%22%7D)

## Overview
1. A databricks workflow is scheduled to trigger the spark notebook.<br>
2. PySpark script in the notebook programmatically fetches the date of execution using python's `datetime` module.<br>
3. The date string is used to read the corresponding day's input files from dbfs (S3 bucket).<br>
4. The input files are read into spark dataframe and quality checks are run against them.<br>
5. If the data quality checks are failed, pipeline run halts.Otherwise, bookings data in ingested into delta (fact) table and customer data to delta (dimension) table.<br>

## Tech Stack
1. AWS S3
2. AWS IAM 
3. Databricks
4. PySpark
5. Python

## Steps followed
1. Setup AWS CSP as the storage and compute provider for databricks.
2. Authored PySpark script on databricks notebook containing the logic to process the data.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.1) Get the date<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.2) Fetch the input files corresponding to the date.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.3) Run data quality checks (defined using Pydeequ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.4) Ingest the data if quality checks are succeeded else halt the run.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.5) Implemented incremental ingestion of bookings data (into fact table).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.6) Implemented SCD2 merge of customer data (into dimension table).<br>
3. Created and configured the workflow to trigger the processing everyday at 11:00 A.M.(scheduled).<br>

## Conclusion
This project effectively demonstrates the automated merge ingestion of SCD2 data on **databricks** platform using **PySpark**.
