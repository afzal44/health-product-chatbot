def is_valid_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def generate_random_string(length=10):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def read_json_file(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path, data):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]