# Data warehouse management using Apache Airflow

This objective of this project is to manage the Apache Hive data warehouse (built on top of GCP dataproc cluster) through an automated pipeline, orchestrated on Apache Airflow

![dag_tasks_execution_status](https://github.com/user-attachments/assets/6e265e65-2a96-4bf1-8fdc-63f2623d14bf)

## Overview
1. Data lands in the GCP cloud storage bucket once per day with file name in the format logistics_YYYYMMDD.csv.
2. Google cloud run function(CRF) is configured (using Eventarc trigger in the backend) to trigger airflow DAG everytime upon object upload.
3. Using airflow's operators, DAG tasks are defined and designed to use cluster details fetched dynamically during runtime so as to access Hive tables
   and load the data.

## Optimisations

1. Upon succesfully loading the data, input file is moved to another bucket having lowest storage cost (archive class)--> Saves Cost.
2. Only upon validating the input file (name and extension), DAG is triggered --Minimising the pipeline failure caused by inappropriate data.
3. Sendgrid API is used to notify the upstream user in the event of receiving an inappropriate file.
4. Hive table is partitioned (on the date column) serving to reduce the query runtime during analytical workload.

