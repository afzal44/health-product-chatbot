output "api_gateway_url" {
  value = aws_api_gateway_deployment.example.invoke_url
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.example.name
}

output "opensearch_endpoint" {
  value = aws_opensearch_domain.example.endpoint
}