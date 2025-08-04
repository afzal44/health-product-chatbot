provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "health_product_chatbot_bucket" {
  bucket = "health-product-chatbot-bucket"
  acl    = "private"
}

resource "aws_dynamodb_table" "products" {
  name         = "Products"
  billing_mode = "PAY_PER_REQUEST"
  attribute {
    name = "product_id"
    type = "S"
  }
  hash_key = "product_id"
}

resource "aws_opensearch_domain" "health_product_chatbot" {
  domain_name = "health-product-chatbot"
  elasticsearch_version = "7.10"

  cluster_config {
    instance_type = "t2.small.search"
    instance_count = 1
  }

  ebs_options {
    ebs_enabled = true
    volume_size = 10
  }
}

output "s3_bucket_name" {
  value = aws_s3_bucket.health_product_chatbot_bucket.bucket
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.products.name
}

output "opensearch_domain_endpoint" {
  value = aws_opensearch_domain.health_product_chatbot.endpoint
}