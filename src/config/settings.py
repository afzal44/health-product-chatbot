# settings.py

class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///app.db'
    SECRET_KEY = 'your_secret_key_here'
    AWS_ACCESS_KEY_ID = 'your_aws_access_key_id_here'
    AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key_here'
    OPENSEARCH_HOST = 'your_opensearch_host_here'
    DYNAMODB_TABLE_NAME = 'your_dynamodb_table_name_here'

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///prod.db'