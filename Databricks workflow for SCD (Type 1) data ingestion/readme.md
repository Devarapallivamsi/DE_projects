
# SCD (Type 1) Data ingestion using Databricks and PySpark on AWS

## Objective
This project is designed to automate a data pipeline that processes the daily-data files to maintain the latest and updated state of records ensuring efficient processing, loading, and updating of a target table while maintaining data integrity. It includes steps like staging, archiving, and configuring the alerting mechanism.

## Overview
**Data Ingestion**: A Databricks workflow is configured to trigger upon daily data arrival (in AWS S3).<br/>
&emsp;> Load the data from the input file into a staging table.<br/>
&emsp;> Move the input file to the archive zone. (preserving historical records)<br/>
**SCD Type 1 Merge**: Merge the data from the staging table into the target table to model SCD Type 1 data.This operation updates existing records with new data and inserts new records.
    
**Email Alerting**: An email alerting system is configured within Databricks the pipeline status to the users as this is a production-critical pipeline.

## Tech stack<br/>
1. **Databricks**: To manage Spark cluster.<br/>
2. **PySpark**: To define the tasks involving procesing, transformation, and loading of data.<br/>
3. **Databricks Unity Catalog**: To manage the metadata like schema of the tables and adding external storage location for enabling event based pipeline triggering.<br/>
4. **Databricks Workflow**: To Orchestrate the pipeline and define the dependencies between tasks.<br/>
5. **AWS S3**: To store the files and as a root storage for Databricks (dbfs).<br/>
6.  **Shell Scripting**: To moving files from the staging (or input) zone to the archive zone.<br/>

## Steps Followed<br/>
1. **Storage Setup**: Configured an AWS S3 bucket to receive daily data files.
2. **Data Processing and Archiving**:
_stage_delta_archive_load_ notebook: PySpark script to load the input file into a delta table and move the file to archive.<br/>
_stage_ingest_SCD_merge_ notebook: PySpark script to merge the data in stage table with the target table modeling SCD (Type 1) data.<br/>

3. **Automating the pipeline**:
A Databricks workflow is configured to trigger upon file arrival that conatains two tasks, one for each notebook.
    <br/>
    ![pipeline run](https://github.com/user-attachments/assets/c81a0ce2-b307-4b67-9ef3-deb80501b474)
    <br/>
5. **Alerting**:
Set up an email alerting system within Databricks to notify users upon the completion of the workflow. This ensures prompt attention to the pipeline's status, which is crucial for production environments.
    <br/>
    ![databricks_email_alert](https://github.com/user-attachments/assets/fc2e15ce-6c5b-4b5b-9b16-12cef25d42e7)
    <br/>
6. **Conclusion**:
This project demonstrates the implementation of a robust data pipeline using Databricks and AWS leveraging the power of PySpark for data processing. The configured email alerting mechanism ensures that stakeholders are promptly informed of the pipeline's status, maintaining the reliability and efficiency of the production environment.
