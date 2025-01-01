import base64
import json

def lambda_handler(event, context):
    output_records = []

    for record in event['records']:
        # Try to decode and transform the record
        try:
            # Decode the input data from base64
            payload = base64.b64decode(record['data'])
            payload_json = json.loads(payload)

            # Access the data in the 'dynamodb' key
            dynamodb_data = payload_json['dynamodb']
            new_image = dynamodb_data['NewImage']
            print(new_image)

            # Extract required fields from NewImage
            transformed_data = {
                'orderid': new_image['orderid']['S'],
                'product_name': new_image['product_name']['S'],
                'quantity': int(new_image['quantity']['N']),
                'price': float(new_image['price']['N'])
            }

            # Convert the transformed data to a JSON string and then encode it as base64
            transformed_data_str = json.dumps(transformed_data) + '\n'
            transformed_data_encoded = base64.b64encode(transformed_data_str.encode('utf-8')).decode('utf-8')

            # Append the transformed record to the output using 'eventID' as 'recordId'
            output_records.append({
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': transformed_data_encoded
            })

        except Exception as e:
            # If there's any error with processing the record, mark it as ProcessingFailed but still return the recordId
            output_records.append({
                'recordId': record['recordId'],
                'result': 'ProcessingFailed',
                'data': record['data']  # simply pass the original data back
            })

    return {
        'records': output_records
    }