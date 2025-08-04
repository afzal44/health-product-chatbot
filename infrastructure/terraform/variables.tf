variable "region" {
  description = "The AWS region where resources will be deployed"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "The environment for the deployment (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "db_table_name" {
  description = "The name of the DynamoDB table"
  type        = string
}

variable "opensearch_domain_name" {
  description = "The name of the OpenSearch domain"
  type        = string
}

variable "api_gateway_stage" {
  description = "The stage for the API Gateway"
  type        = string
  default     = "v1"
}