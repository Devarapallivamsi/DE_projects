![image](https://github.com/user-attachments/assets/0ae1318d-815a-4b06-aa40-70e45a813c45)


# Stream data processing using Delta Live Tables (DLT) in Databricks

![DLT_workflow](https://github.com/user-attachments/assets/b74e845f-ff46-476c-be83-afd72dbbf447)

## Overview
This project involves creating a data pipeline that processes and organizes streaming data using the medallion lakehouse architecture thereby logically separating the data into three layers viz., bronze, silver and gold as per the quality of the data. 

## Features
**Data Ingestion**: Stream data is received from the upstream team into the delta tables of our team.
**Continuous run**: The pipeline is scheduled to run continuously to ensure real-time data processing.

**Delta Live Tables Workflow**: A workflow is created using Delta Live Tables to manage and process the data efficiently.
__Medallion Lakehouse Architecture__:
    **Bronze Layer**: Raw data is stored here.
    **Silver Layer**: Data is cleaned and enriched in this layer.
    **Gold Layer**: Final processed and aggregated data is stored here.

**Stream Processing**: Stream tables are used to process only the latest data from the delta tables.
**Data Aggregation**: The final processed and aggregated data is dumped into separate delta tables in the gold layer.


## Conclusion
This project demonstrates an efficient way to process and organize streaming data using lakehouse architecture. By using Delta Live Tables, setting up the pipeline, defining tasks and dependencies among them is automated

