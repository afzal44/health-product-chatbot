import json
import os

def extract_product_data(raw_data_directory):
    product_data = []
    
    # Iterate through all files in the raw data directory
    for filename in os.listdir(raw_data_directory):
        if filename.endswith('.json'):  # Assuming product data is in JSON format
            file_path = os.path.join(raw_data_directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                product_data.extend(data.get('products', []))  # Adjust based on actual data structure

    return product_data

def main():
    raw_data_directory = 'data/raw/product_data'
    extracted_data = extract_product_data(raw_data_directory)
    
    # Save extracted data to a new file or process it as needed
    output_file = 'data/processed/extracted_products.json'
    with open(output_file, 'w') as outfile:
        json.dump(extracted_data, outfile, indent=4)

if __name__ == '__main__':
    main()