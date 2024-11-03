
# SCD (Type 1) Data ingestion using Databricks and PySpark on AWS

## Objective
This project is designed to automate a data pipeline that processes the daily-data files to maintain the latest and updated state of records ensuring efficient processing, loading, and updating of a target table while maintaining data integrity. It includes steps like staging, archiving, and configuring of alerting mechanism.

## Overview
Data Ingestion: A Databricks workflow is configured to trigger upon daily data arrival (in AWS S3).
Task 1:
    Load the data from the input file into a staging table.
    Move the input file to the archive zone. (preserving historical records)
Task 2:
    Merge the data from the staging table into the target table to model SCD Type 1 data.

SCD Type 1 Merge: This operation updates existing records with new data and inserts new records.
Email Alerting: An email alerting system is configured within Databricks to notify users of the pipeline status, as this is a production-critical pipeline.

## Tech stack
**Databricks**: For managing Spark clusters.
**PySpark**: For scripting the tasks involving procesing, transformation of data etc.
**Databricks Unity Catalog**: Used as a schema metastore.
**Databricks Workflow**: Orchestrating the pipeline and configuring dependencies.
**AWS S3**: For storage and creation of Databricks root storage.
**Linux Shell Scripting**: For moving files from the staging (or input) zone to the archive zone.

## Steps Followed
-> **Storage Setup**:
    Configured an AWS S3 bucket to receive daily data files. 
-> **Data Processing and Archiving**:
    _stage_delta_archive_load_ notebook: PySpark script to load the input file into a delta table and move the file to archive.
    _stage_ingest_SCD_merge_ notebook: PySpark script to merge the staged data and target table modeling SCD (Type 1) data.

-> **Automating the pipeline**:
    A Databricks workflow is configured to trigger upon file arrival that conatains two tasks, one for each notebook and a run looks as follows:

-> **Alerting**:
    Set up an email alerting system within Databricks to notify users upon the completion of the workflow. This ensures prompt attention to the pipeline's status, which is crucial for production environments.

**Conclusion**
This project demonstrates the implementation of a robust data pipeline using Databricks and AWS leveraging the power of PySpark for data processing. The configured email alerting mechanism ensures that stakeholders are promptly informed of the pipeline's status, maintaining the reliability and efficiency of the production environment.













