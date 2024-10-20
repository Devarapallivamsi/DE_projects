![image](https://github.com/user-attachments/assets/827221d6-d4ed-48c1-9e84-c04baecbb9c2)

# Airflow-orchestrated automated pipeline for data warehouse management using Google cloud platform


The objective is to manage Apache Hive data warehouse (built on top of GCP dataproc cluster) through an automated pipeline orchestrated on Apache Airflow

![dag_tasks_execution_status](https://github.com/user-attachments/assets/6e265e65-2a96-4bf1-8fdc-63f2623d14bf)

## Overview
1. Data lands in the GCP cloud storage bucket once per day with file name in the format logistics_YYYYMMDD.csv.
2. Google cloud run function(CRF) is configured (using Eventarc trigger in the backend) to trigger airflow DAG everytime upon object upload.
3. Using airflow's operators, DAG tasks are defined to load data into Hive.
   and load the data.

## Optimisations

✅ Upon succesfully loading the data, input file is moved to another bucket having lowest storage cost (archive class)--> 📉Costs.
✅ Airflow's deferred operator sensors can be alternative to CRF to trigger DAG upon file arrival. But, CRF gives the flexibility to the upstream user to send the file at any time and 
   charges are applied based on the number of executions and runtime.(Chances are, file may not arrive on festivals, National holidays and pipeline shouldn’t be running waiting for the file 
   which would happen if deferred operator sensor is used. ofcourse, uses less resources than a general sensor). -- 📉Costs
✅ Only upon validating the input file (name and extension), DAG is triggered --Minimising the pipeline failures ❌ (to an extent) caused by inappropriate data.
   (Addl. validations can also be put in place as required)
✅ Cluster details are safely stored in an encrypted fashion and fetched dynamically during runtime --
✅ In the event of receiving an inappropriate file, DAG trigger operation is skipped and upstream user is notified through :email: e-mail (sent using Sendgrid API) -- Aletring ⚠ mechanism 
    and 📉 use of computational power.
✅ Hive table is partitioned (on the date column) serving to reduce the query runtime during analytical workloads -- 📉time.

## Tech stack
1. Python
2. GCP Cloud storage
3. GCP Dataproc
4. GCP Cloud Run Functions
5. GCP Composer (managed Apache Airflow service)
7. Hive
8. Linux shell scripting

## Steps followed
1. Created two GCS buckets one for the input data and the other for data archiving.
2. Created a Cloud Run Function (to be triggered with object uploads in Cloud Storage).
3. Setup a Dataproc cluster to host Hive data warehouse.
4. Started an airflow cluster using GCP composer environment.
5. Created airflow python script defining all the tasks using airflow's operators.
6. Generated and stored the sendgrid API key. verified the sender's (self) mail address.
7. Used Airflow web server address and Sendgrid API key to configure Cloud Run Function to notify user or trigger the DAG post input data validation.

## Testing and verification
1. Upload a file to input bucket
2. If the filename is valid, verify that DAG is successfully triggered.Otherwise, check your mail.
3. Open the secureshell(SSH) of Dataproc cluster's master node and verify if data is present (using Hive Commands).
4. Check if the file is moved into the archiving bucket succesfully.





















