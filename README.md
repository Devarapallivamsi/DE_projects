# Automated pipeline for quality data ingestion with AWS Glue


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

### 1. Sample parquet file as historical data to run data quality checks
A sample parquet file containing 200k transaction records is stored in S3 bucket to run data quality checks.

### 2. create the ruleset in the catalog table to run the checks against current data
Glue Data quality ruleset is created to test the quality of historical (already existing data) records.

### 3. Transaction files arrival in S3 buckets
Files arrive in S3 bucket on daily basis which will be batch-ingested by glue job bookmark feature triggering the pipeline to 
process only the new records.

### 3.  Setup S3 bucket
create a bucket named `financial_trans_bucket`

### 3.  Setup SNS topic
3.1 Create an SNS topic for sending processing notifications.
3.2 Subscribe an email to the topic for receiving notifications.

### 4.  Create IAM role
Create IAM roles for redshift and glue to provision working of crawlers, JDBC connection of redshift with glue, publishing a message in SNS topic

### 5.  Create and configure the pipeline
Create a pipeline and configure it as shown in the image below connecting appropriate source and sink location(s).
The pipeline works as follows:
* Glue job bookmarking feature automatically identifies the newly arrived files
* Runs data quality checks
* Schema will be changed (dropping per-row result of checks) to match the input file schema.
* Each record is routed to either redshift table (if it succesfully passes the checks) or to the S3 bucket (created above).
* The results of the data quality checks will trigger the publishing of a message in SNS topic.

### 6. Testing and Verification
* Upload the sample parquet file to financial_trans_bucket and verify that the pipeline gets triggered.
* Query the redshift table for the records and confirm the columns do not contain any null values.
* Ensure an email notification is received upon completion of the pipeline run.













