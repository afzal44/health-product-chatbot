# Architecture Overview

The health-product-chatbot project is designed to provide a robust and scalable solution for health product inquiries through a chatbot interface. The architecture is divided into several key components, each serving a specific purpose in the overall functionality of the application.

## 1. Overview

The architecture consists of a serverless backend, a frontend application, data processing scripts, and infrastructure as code (IaC) for deployment. The system is designed to handle chat interactions, process data, and manage embeddings for improved response accuracy.

## 2. Components

### 2.1 Backend

- **Lambda Functions**: The backend is built using AWS Lambda functions, which are organized into three main categories:
  - **Chat**: Handles chat-related requests and interactions.
  - **Data Processing**: Processes incoming data and prepares it for use in the chatbot.
  - **WebSocket**: Manages real-time communication with clients.

- **Shared Services**: Common functionalities are encapsulated in shared modules, including:
  - **Client Implementations**: For interacting with external services like Bedrock, OpenSearch, and DynamoDB.
  - **Utility Functions**: General-purpose functions used across the application.

### 2.2 Frontend

- The frontend is a single-page application (SPA) that provides a user-friendly interface for interacting with the chatbot. It is built using modern JavaScript frameworks and includes components for chat widgets, message display, and typing indicators.

### 2.3 Data Management

- **Data Storage**: Raw product data is stored in a designated directory, while processed embeddings are stored separately for efficient retrieval.
- **Data Processing Scripts**: Python scripts are provided for extracting product data, creating embeddings, and uploading data to OpenSearch.

### 2.4 Infrastructure

- **CloudFormation Templates**: Infrastructure is defined using AWS CloudFormation, allowing for easy deployment and management of resources such as OpenSearch, DynamoDB, and API Gateway.
- **Terraform (Optional)**: An optional Terraform configuration is included for those who prefer using Terraform for infrastructure management.

## 3. Deployment

The deployment process is automated through shell scripts that handle environment setup, application deployment, and testing. This ensures a consistent and repeatable deployment process.

## 4. Conclusion

The architecture of the health-product-chatbot project is designed to be modular, scalable, and maintainable. Each component is carefully crafted to work together seamlessly, providing a robust solution for health product inquiries through a chatbot interface.