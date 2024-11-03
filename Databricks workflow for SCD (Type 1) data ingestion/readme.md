
# SCD (Type 1) Data ingestion using Databricks and PySpark on AWS

## Objective
This project is designed to automate a data pipeline that processes the daily-data files to maintain the latest and updated state of records ensuring efficient processing, loading, and updating of a target table while maintaining data integrity. It includes steps like staging, archiving, and configuring the alerting mechanism.

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
**Databricks**: To manage Spark cluster.
**PySpark**: To define the tasks involving procesing, transformation, and loading of data.
**Databricks Unity Catalog**: To manage the metadata like schema of the tables and adding external storage location for enabling event based pipeline triggering.
**Databricks Workflow**: To Orchestrate the pipeline and define the dependencies between tasks.
**AWS S3**: To store the files and as a root storage for Databricks (dbfs).
**Shell Scripting**: To moving files from the staging (or input) zone to the archive zone.

## Steps Followed
-> **Storage Setup**:
    Configured an AWS S3 bucket to receive daily data files. 
-> **Data Processing and Archiving**:
    _stage_delta_archive_load_ notebook: PySpark script to load the input file into a delta table and move the file to archive.
    _stage_ingest_SCD_merge_ notebook: PySpark script to merge the data in stage table with the target table modeling SCD (Type 1) data.

-> **Automating the pipeline**:
    A Databricks workflow is configured to trigger upon file arrival that conatains two tasks, one for each notebook.

    ![image](https://github.com/Devarapallivamsi/DE_projects/blob/master/Databricks%20workflow%20for%20SCD%20(Type%201)%20data%20ingestion/assets/pipeline%20run.png)


    
-> **Alerting**:
    Set up an email alerting system within Databricks to notify users upon the completion of the workflow. This ensures prompt attention to the pipeline's status, which is crucial for production environments.

    ![image](https://github.com/user-attachments/assets/928929c1-ce82-4443-be41-61ce157266e1)


**Conclusion**
This project demonstrates the implementation of a robust data pipeline using Databricks and AWS leveraging the power of PySpark for data processing. The configured email alerting mechanism ensures that stakeholders are promptly informed of the pipeline's status, maintaining the reliability and efficiency of the production environment.













