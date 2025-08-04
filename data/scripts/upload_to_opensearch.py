import json
import requests

def upload_data_to_opensearch(data, index_name, opensearch_url):
    headers = {
        'Content-Type': 'application/json',
    }
    
    for record in data:
        response = requests.post(f"{opensearch_url}/{index_name}/_doc", headers=headers, data=json.dumps(record))
        if response.status_code not in [200, 201]:
            print(f"Failed to upload record: {record}. Status code: {response.status_code}. Response: {response.text}")

if __name__ == "__main__":
    # Example usage
    opensearch_url = "http://localhost:9200"  # Replace with your OpenSearch URL
    index_name = "products"  # Replace with your index name
    data = [
        {"name": "Product 1", "description": "Description for product 1", "price": 10.99},
        {"name": "Product 2", "description": "Description for product 2", "price": 20.99},
    ]
    
    upload_data_to_opensearch(data, index_name, opensearch_url)