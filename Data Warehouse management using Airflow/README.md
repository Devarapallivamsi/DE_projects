![image](https://github.com/user-attachments/assets/fe6cf0d0-5856-42dc-b57b-94981b9f5ef8)


# Airflow-orchestrated pipeline for data warehouse management on Google cloud platform<br/>

The objective is to manage Apache Hive data warehouse (built on top of GCP dataproc cluster) through an automated pipeline orchestrated on Apache Airflow

![dag_tasks_execution_status](https://github.com/user-attachments/assets/6e265e65-2a96-4bf1-8fdc-63f2623d14bf)

## Overview<br/>

1. Data lands in the GCP cloud storage bucket once per day with file name in the format logistics_YYYYMMDD.csv.
2. Google cloud run function(CRF) is configured (using Eventarc trigger in the backend) to trigger airflow DAG everytime upon object upload.
3. Using airflow's operators, DAG tasks are defined to load data into Hive.
   and load the data.

## Optimisations<br/>

✅ Upon succesfully loading the data, input file is moved to another bucket having lowest storage cost (archive class)-- ⏬:Costs.<br/>

✅ Ocaasionally, there is a possibility of not receiving the file on some days.But, sensor will unnecessarily increase the costs by pokinng the bucket.As a way around, implemented CRF to trigger the DAG.Here, charges are applied based on the number of executions and avg runtime. -- ⏬:Costs.<br/>

✅ Only post validating the input file (name and extension), DAG is triggered --Minimising the pipeline failures ❌ (to an extent) caused by inappropriate data.(Addl. validations can also be put in place as required)<br/>

✅ Cluster details are safely stored in airflow's 'Variables' in an encrypted fashion and fetched dynamically during runtime -- 🔒:Security<br/>

✅ In the event of receiving an inappropriate file, DAG trigger operation is skipped and upstream user is notified through :email: e-mail (sent using Sendgrid API) -- Aletring ⚠ mechanism and ⏬ use of computational power.<br/>

✅ Hive table is partitioned (on the date column) serving to reduce the query runtime during analytical workloads -- ⏬time.<br/>

## Tech stack<br/>
1. Python
2. GCP Cloud storage
3. GCP Dataproc
4. GCP Cloud Run Functions
5. GCP Composer (managed Apache Airflow service)
7. Hive
8. Linux shell scripting

## Steps followed<br/>
1. Created two GCS buckets one for the input data and the other for data archiving.<br/>
2. Created a Cloud Run Function (to be triggered with object uploads in Cloud Storage).<br/>
3. Setup a Dataproc cluster to host Hive data warehouse.<br/>
4. Started an airflow cluster using GCP composer environment.<br/>
5. Created airflow python script defining all the tasks using airflow's operators.<br/>
6. Generated and stored the sendgrid API key. verified the sender's (self) mail address.<br/>
7. Used Airflow web server address and Sendgrid API key to configure Cloud Run Function to notify user or trigger the DAG post input data validation.<br/>

## Testing and verification<br/>
1. Upload a file to input bucket
2. If the filename is valid, verify that DAG is successfully triggered.Otherwise, check your mail.
3. Open the secureshell(SSH) of Dataproc cluster's master node and verify if data is present (using Hive Commands).
4. Check if the file is moved into the archiving bucket succesfully.





















