from botocore.exceptions import ClientError
import boto3

class BedrockClient:
    def __init__(self, region_name='us-west-2'):
        self.client = boto3.client('bedrock', region_name=region_name)

    def invoke_model(self, model_id, input_data):
        try:
            response = self.client.invoke_model(
                modelId=model_id,
                body=input_data
            )
            return response['body']
        except ClientError as e:
            print(f"An error occurred: {e}")
            return None

    def list_models(self):
        try:
            response = self.client.list_models()
            return response['modelSummaries']
        except ClientError as e:
            print(f"An error occurred: {e}")
            return None

    def get_model_details(self, model_id):
        try:
            response = self.client.get_model(modelId=model_id)
            return response['model']
        except ClientError as e:
            print(f"An error occurred: {e}")
            return None