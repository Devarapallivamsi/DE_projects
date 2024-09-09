**Overview**
-> This project automates the process of incremental data ingestion.
-> AWS Glue's built-in feature **job bookmarking** is used to ingestion only the latest data
-> Ingested data is tested against data quality rules to ensure only quality data is ingested and are dumped into a redshift warehouse.
-> Records that fail the quality check are dumped into an S3 bucket that need to be cleaned or further dealt with.
-> Using Eventbridge bridge pattern, SNS is leveraged to notify the user about bad records.

**Tech stack**
1. AWS account
2. AWS glue crawlers
3. AWS data catlog
4. Glue low code ETL
5. AWS S3 (as data lake)
6. Amazon SNS (for notificaiton)
7. AWS Eventbridge (for pattern matching and publishing messages in SNS topic)
8. AWS IAM (for permissions)
9. Email subscription for SNS

Steps followed:
1. Sample dataset is stored in S3 (as historical data) to run data quality checks.
2. 

