# AWS Kinesis near-real time streaming data pipeline


## Overview
This project is created to transform and ingest the streaming data.

## Tech stack and AWS services
1. Python
2. S3
3. DynamoDB
3. Kinesis
4. Lambda
5. Athena
6. Glue


## Steps followed

1. Authored `mock_data_generator_for_dynamodb.py` script to generate mock stream of records.
2. Created a table in `AWS DynamoDB` to receive the streaming records
3. Configured `DynamoDB Streams` to facilitate Change Data Capture(CDC).
4. Created `Kinesis streams` to receive the data from `DynamoDB stream`
5. Created an `eventbridge pipe` to connect DynamoDB stream with Kinesis stream
6. Leveraged `Kinesis firehose` to make a batch of records received from the `kinesis streams`.
7. Authored `lambda` script that tranforms the set of records it receives when it is invoked.
7. The batches of records (from step 6) will be sent to lambda to be transformed before dumping into S3.
8. Created a database and table in Glue to define the schema of the data.
9. Used `Athena` to analyse the data.



































