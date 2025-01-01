from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitHiveJobOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'hive_load_airflow_dag',
    default_args=default_args,
    description='Load logistics data into Hive on GCP Dataproc',
    # No schedule. Only trigger.
    schedule_interval=None,
    start_date=datetime(2024, 10, 19),
    tags=['example']
)

cluster_details = Variable.get('cluster_details',deserialize_json=True)
cluster_name = cluster_details['name']
region = cluster_details['region']
projectId = cluster_details['project_id']


# Create Hive Database if not exists
create_hive_database = DataprocSubmitHiveJobOperator(
    task_id="create_hive_database_if_not_exists",
    query="CREATE DATABASE IF NOT EXISTS logistics_db;",
    cluster_name=cluster_name,
    region=region,
    project_id=projectId,
    dag=dag
)

# Create main Hive table
create_hive_table = DataprocSubmitHiveJobOperator(
    task_id="create_hive_table",
    query="""
        CREATE EXTERNAL TABLE IF NOT EXISTS logistics_db.logistics_data (
            delivery_id INT,
            `date` STRING,
            origin STRING,
            destination STRING,
            vehicle_type STRING,
            delivery_status STRING,
            delivery_time STRING
        )
        ROW FORMAT DELIMITED
        FIELDS TERMINATED BY ','
        STORED AS TEXTFILE
        LOCATION 'airflow-bucket-11/airflow-project-1/data/'
        tblproperties('skip.header.line.count'='1');
    """,
    cluster_name=cluster_name,
    region=region,
    project_id=projectId,
    dag=dag
)

# Create partitioned Hive table
create_partitioned_table = DataprocSubmitHiveJobOperator(
    task_id="create_partitioned_table",
    query="""
        CREATE TABLE IF NOT EXISTS logistics_db.logistics_data_partitioned (
            delivery_id INT,
            origin STRING,
            destination STRING,
            vehicle_type STRING,
            delivery_status STRING,
            delivery_time STRING
        )
        PARTITIONED BY (`date` STRING)
        STORED AS TEXTFILE;
    """,
    cluster_name=cluster_name,
    region=region,
    project_id=projectId,
    dag=dag
)

# Set Hive properties for dynamic partitioning and load data
set_hive_properties_and_load_partitioned = DataprocSubmitHiveJobOperator(
    task_id="set_hive_properties_and_load_partitioned",
    query=f"""
        SET hive.exec.dynamic.partition = true;
        SET hive.exec.dynamic.partition.mode = nonstrict;

        INSERT INTO logistics_db.logistics_data_partitioned PARTITION(`date`)
        SELECT delivery_id, origin,destination, vehicle_type, delivery_status, delivery_time, `date` FROM logistics_db.logistics_data;
    """,
    cluster_name=cluster_name,
    region=region,
    project_id=projectId,
    dag=dag
)

# Move processed files to archive bucket
archive_processed_file = BashOperator(
    task_id='archive_processed_file',
    bash_command=f"gsutil -m mv gs://airflow-bucket-11/airflow-project-1/data/logistics_*.csv gs://logistics-archive-data/",
    dag=dag
)


(create_hive_database >> create_hive_table >> create_partitioned_table >> set_hive_properties_and_load_partitioned
 >> archive_processed_file)


