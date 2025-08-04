import boto3
from botocore.exceptions import ClientError

class DynamoDBClient:
    def __init__(self, table_name):
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb')

    def get_item(self, key):
        try:
            table = self.dynamodb.Table(self.table_name)
            response = table.get_item(Key=key)
            return response.get('Item')
        except ClientError as e:
            print(f"Error getting item: {e.response['Error']['Message']}")
            return None

    def put_item(self, item):
        try:
            table = self.dynamodb.Table(self.table_name)
            table.put_item(Item=item)
        except ClientError as e:
            print(f"Error putting item: {e.response['Error']['Message']}")

    def delete_item(self, key):
        try:
            table = self.dynamodb.Table(self.table_name)
            table.delete_item(Key=key)
        except ClientError as e:
            print(f"Error deleting item: {e.response['Error']['Message']}")