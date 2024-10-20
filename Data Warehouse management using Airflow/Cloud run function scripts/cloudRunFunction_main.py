
"""
Trigger a DAG in a Cloud Composer 2 environment in response to an event,
using Cloud Function.
"""

# Import required libraries
import dateutil.parser
from dateutil.parser import parse
from typing import Any
from datetime import datetime
import composer2_airflow_rest_api



def trigger_dag_gcf(data, context=None):
    """
    Trigger a DAG and pass event data.

    Args:
      data: A dictionary containing the data for the event. Its format depends
      on the event.
      context: The context object for the event.
    """
	# Get the date string from the file 
	# Eg: logistics_20241020.csv -> '20241020' (it's YYYYMMDD format)
    dateStr = data['name'].split("/")[-1].replace('.csv', "").replace('logistics_', "")
    
	
    try:
		# Try creating a datetime object out of the dateStr
        parse(dateStr, yearfirst=True)
		fileExtension = data['name'].split(".")[-1]
        # If either of the above raises an error, flow skips the folloing lines and executes the part of code 
        # present in 'except' block.
        
		if fileExtension != 'csv':
			raise TypeError(f'Expected csv file but recieved {fileExtension}')
			
		
        web_server_url = (
            "https://7058b8ab165e4425969bb9767faf3fca-dot-us-central1.composer.googleusercontent.com"
        )
        
        
        dag_id = 'hive_load_airflow_dag'

        composer2_airflow_rest_api.trigger_dag(web_server_url, dag_id, data)


    except:
        print('Inappropriate file name.')
        """
		Make imports only when necessary -- In the event of receiving a proper file, these package imports,
		were done at the beginning, would have unnecessarily increased the runtime of the 
		function, bloating the costs.
		"""
		
        import os
		import sendgrid
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail, Email
        from python_http_client.exceptions import HTTPError

        sg = SendGridAPIClient(os.environ['key-gcp-mail'])

        html_content = "<p>Pls send the file in the valid format</p>"

        message = Mail(
            to_emails=["devarapallivamsi789@gmail.com"],
            from_email=Email('vvitvamsi@gmail.com', "Vamsi Devarapalli"),
            subject="Hello world",
            html_content=html_content
            )
        
        try:
            response=sg.send(message)
            print(f"No Error. email.status_code={response.status_code}")
            
        except:
            print(f'sending failed with msg: {e}')
