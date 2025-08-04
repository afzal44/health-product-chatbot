from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
import os

class OpenSearchClient:
    def __init__(self):
        self.host = os.getenv('OPENSEARCH_HOST')
        self.region = os.getenv('AWS_REGION')
        self.service = 'es'
        
        # Get AWS credentials
        credentials = boto3.Session().get_credentials()
        self.auth = AWS4Auth(credentials.access_key, credentials.secret_key, self.region, self.service, session_token=credentials.token)

        self.client = OpenSearch(
            hosts=[{'host': self.host, 'port': 443}],
            http_auth=self.auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

    def index_document(self, index, document, doc_id=None):
        response = self.client.index(
            index=index,
            body=document,
            id=doc_id
        )
        return response

    def search(self, index, query):
        response = self.client.search(
            index=index,
            body=query
        )
        return response

    def delete_document(self, index, doc_id):
        response = self.client.delete(
            index=index,
            id=doc_id
        )
        return response

    def update_document(self, index, doc_id, document):
        response = self.client.update(
            index=index,
            id=doc_id,
            body={'doc': document}
        )
        return response
