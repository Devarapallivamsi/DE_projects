-- use role
use role accountadmin;


create or replace database snowpipe_dev;


create or replace table orders_data_lz(
    order_id int,
    product varchar(20),
    quantity int,
    order_status varchar(30),
    order_date date
);

-- create storage integration between snowflake and GCP such that snowflake can read data from GCS
create or replace storage integration gcs_bucket_read_int
 type = external_stage
 storage_provider = gcs
 enabled = true
storage_allowed_locations = ('gcs://snowflake-gds/');

-- To check the service account created. and whitelist it in the GCP.
describe storage integration gcs_bucket_read_int


-- Create stage for snowflake pointing to the data path in GCS bucket.
create or replace stage snowpipe_stage
url = 'gcs://snowflake-gds/'
storage_integration = gcs_bucket_read_int;


show stages;


list @snowpipe_stage

-- Create integration between Snowflake and GCP Pub/Sub such that snowflake will get the trigger to pull the newly created data from
-- GCS bucket upon a create event message gets published.
create or replace notification integration notification_from_pubsub_int
 type = queue
 notification_provider = gcp_pubsub
 enabled = true
 gcp_pubsub_subscription_name = 'projects/project-c5baa6b3-1de5-41ad-a8e/subscriptions/gcs-to-pubsub-notification-sub';

-- Check this to fetch the service account created by this integration to whitelist in GCP.
desc integration notification_from_pubsub_int


-- Create the main snowpipe.
Create or replace pipe gcs_to_snowflake_pipe
auto_ingest = true
integration = notification_from_pubsub_int
as
copy into orders_data_lz
from @snowpipe_stage
file_format = (type = 'CSV');


show pipes;


select system$pipe_status('gcs_to_snowflake_pipe');

-- Helps in checking the copy history for the orders_data_lz table in the past hour. such that we shall get to know
-- whether data load is initiated to the table.
Select * 
from table(information_schema.copy_history(table_name=>'orders_data_lz', start_time=> dateadd(hours, -1, current_timestamp())));


-- Check the loaded data.
select * from orders_data_lz;


-- Stop snowpipe
ALTER PIPE gcs_to_snowflake_pipe SET PIPE_EXECUTION_PAUSED = true;


-- To restart (resume) the pipe, you just flip the flag back to FALSE:
-- ALTER PIPE gcs_to_snowflake_pipe SET PIPE_EXECUTION_PAUSED = FALSE;

-- Terminate or delete a pipe
drop pipe gcs_to_snowflake_pipe;
