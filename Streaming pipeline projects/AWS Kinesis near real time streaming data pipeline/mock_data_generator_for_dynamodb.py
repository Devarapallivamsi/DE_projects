import boto3
import random
import time
from decimal import Decimal

# Initialize the DynamoDB resource
# dynamodb = boto3.resource('dynamodb')
session = boto3.Session(profile_name='default', region_name='ap-south-1')
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('OrderTable')


def generate_order_data():
    """Generate random order data."""
    orderid = str(random.randint(1, 10000))  # Random order ID between 1 and 10000
    product_name = random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger'])
    quantity = random.randint(1, 5)
    price = Decimal(str(round(random.uniform(10.0, 500.0), 2)))

    return {
        'orderid': orderid,
        'product_name': product_name,
        'quantity': quantity,
        'price': price
    }


def insert_into_dynamodb(data):
    """Insert data into DynamoDB."""
    try:
        table.put_item(Item=data)
        print(f"Inserted data: {data}")
    except Exception as e:
        print(f"Error inserting data: {str(e)}")


if __name__ == '__main__':
    try:
        while True:
            data = generate_order_data()
            insert_into_dynamodb(data)
            time.sleep(3)  # Sleep for 3 seconds
    except KeyboardInterrupt:
        print("\nScript stopped by manual intervention!")
