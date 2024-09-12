# Automated pipeline for quality data ingestion with AWS Glue


## Overview
1. This project automates the process of **incremental data ingestion**.
2. AWS Glue's built-in feature **job bookmarking** is used to ensure only the latest data gets ingested.
3. Ingested data is tested against **data quality rules** to ensure only quality data is ingested and are dumped into a redshift warehouse.
4. Records that fail the quality check are dumped into an S3 bucket which need to be cleaned or further dealt with.
5. Using Eventbridge pattern, SNS is leveraged to notify the user about data quality results.


## Tech stack
1. AWS account
2. AWS glue crawlers
3. AWS Redshift (as data warehouse platform)
4.AWS Virtual Private Cloud (to isolate the reources and create endpoints for connectivity)
5. AWS data catlog (~ centralised metstore containing schema BUT NOT THE ACTUAL DATA)
6. Glue visual ETL 
7. AWS S3 (as data lake)
8. Amazon SNS (for notifying the user about data quality checks)
9. AWS Eventbridge (to trigger message publishing in SNS topic)
10. AWS IAM (for permissions and roles)


## Steps followed:

### 1. Sample parquet file as historical data to run data quality checks
A sample parquet file containing 200k transaction records is stored in S3 bucket to run data quality checks.

### 2. create the ruleset in the catalog table to run the checks against current data
Glue Data quality ruleset is created to test the quality of historical (already existing data) records.

### 3. Transaction files arrival in S3 buckets
Numerous files arrive in S3 bucket on daily basis containing transaction records all of which, will be batch-ingested by glue job bookmark feature, triggering the pipeline to 
process only the new records.

### 3.  Setup S3 bucket
create a bucket named `financial_trans_bucket`

### 3.  Setup SNS topic
3.1 Create an SNS topic to send data quality result notifications.
3.2 Subscribe an email to the topic for receiving notifications.

### 4.  Create IAM role
Create IAM roles for redshift and glue to provision working of crawlers, JDBC connection of redshift with glue, publishing a message in SNS topic

### 5.  Create and configure the pipeline
Create a pipeline and configure it as shown in the image below connecting appropriate source and sink location(s).

![image](https://github.com/user-attachments/assets/c614a2de-d299-47b6-aff3-54f04d21bd5a)

The pipeline works as follows:
* Pipeline runs as per schedule everyday.
* Glue job bookmarking feature automatically identifies the newly arrived files in S3.
* Runs data quality checks.
* The results of the data quality checks will trigger the publishing of a message in SNS topic.
* Rule outcomes --description of how much percentage of data passed the quality checks-- will be written into S3 bucket in JSON format.
* Row level outcomes pass through a conditional router so as to dump the records in appropriate sink(s).
* Each record is routed to either redshift table (if it succesfully passes the checks) or to the S3 bucket (in case of failure).
* Schema will be changed (dropping per-row result of checks) to match the input file schema before writing to redshift table.


### 6. Testing and Verification
* Upload the sample parquet file to financial_trans_bucket and verify that the pipeline gets triggered.
* Query the redshift table for the records and confirm the columns do not contain any null values.
* Ensure an email notification is received upon completion of the pipeline run.













