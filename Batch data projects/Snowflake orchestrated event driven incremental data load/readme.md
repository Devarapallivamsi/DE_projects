# Snowflake Snowpipe Auto-Ingestion from GCS

A real-time data ingestion pipeline that automatically loads CSV files from Google Cloud Storage (GCS) into Snowflake using Snowpipe and Google Pub/Sub notifications.

## 🚀 Overview

This project demonstrates an event-driven ingestion architecture where:

1. Files are uploaded to a GCS bucket.
2. GCS publishes object creation events to Pub/Sub.
3. Snowflake receives notifications through a Notification Integration.
4. Snowpipe automatically ingests new files into a Snowflake table.

## 🏗️ Architecture

```text
GCS Bucket
    │
    ▼
Google Pub/Sub
    │
    ▼
Snowflake Notification Integration
    │
    ▼
Snowpipe (Auto Ingest)
    │
    ▼
orders_data_lz
```

## 📋 Components

### Database
- `snowpipe_dev`

### Landing Table
- `orders_data_lz`

| Column | Type |
|---------|------|
| order_id | INT |
| product | VARCHAR |
| quantity | INT |
| order_status | VARCHAR |
| order_date | DATE |

### Integrations
- **Storage Integration**: `gcs_bucket_read_int`
- **Notification Integration**: `notification_from_pubsub_int`

### Stage
- `snowpipe_stage`

### Pipe
- `gcs_to_snowflake_pipe`

## ✅ Key Features

- Real-time file ingestion
- Event-driven architecture
- Automatic data loading using Snowpipe
- GCS to Snowflake integration
- Pub/Sub-based notifications
- Load monitoring and auditing
- Pipe pause/resume support

## 🔍 Monitoring

### Check Pipe Status

```sql
select system$pipe_status('gcs_to_snowflake_pipe');
```

### View Load History

```sql
select *
from table(
    information_schema.copy_history(
        table_name => 'orders_data_lz',
        start_time => dateadd(hours, -1, current_timestamp())
    )
);
```

### Verify Loaded Data

```sql
select * from orders_data_lz;
```

## ⚙️ Pipe Management

### Pause

```sql
alter pipe gcs_to_snowflake_pipe
set pipe_execution_paused = true;
```

### Resume

```sql
alter pipe gcs_to_snowflake_pipe
set pipe_execution_paused = false;
```

### Delete

```sql
drop pipe gcs_to_snowflake_pipe;
```

## 🛠️ Tech Stack

- Snowflake
- Snowpipe
- Google Cloud Storage (GCS)
- Google Pub/Sub
- SQL

## 🎯 Outcome

This implementation enables near real-time ingestion of files from GCS into Snowflake with minimal operational overhead, showcasing a production-grade cloud data engineering pattern.
