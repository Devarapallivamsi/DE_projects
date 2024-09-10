### Automated pipeline for quality data ingestion ### 

**event driven or time driven?**

## Overview
1. This project automates the process of incremental data ingestion.
2. AWS Glue's built-in feature **job bookmarking** is used to ingestion only the latest data
3. Ingested data is tested against data quality rules to ensure only quality data is ingested and are dumped into a redshift warehouse.
4. Records that fail the quality check are dumped into an S3 bucket that need to be cleaned or further dealt with.
5. Using Eventbridge bridge pattern, SNS is leveraged to notify the user about bad records.


## Tech stack
1. AWS account
2. AWS glue crawlers
3. AWS Redshift (as a data warehouse platform)
4. AWS data catlog (~ centralised metstore containing schema BUT NOT THE ACTUAL DATA)
5. Glue low code ETL 
6. AWS S3 (as data lake)
7. Amazon SNS (for nitifying the user about data quality checks)
8. AWS Eventbridge (for pattern matching and publishing messages in SNS topic)
9. AWS IAM (for permissions)


## Steps followed:
1. Sample dataset is stored in S3 (as historical data) to run data quality checks.
2. Glue crawler is used to automatically identify and store the schema in catalog tables
3. S3 bucket is organised to store **_bad records/_**, 














