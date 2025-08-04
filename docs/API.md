# API Documentation for Health Product Chatbot

## Overview

The Health Product Chatbot API provides a set of endpoints for interacting with the health product data and facilitating chat functionalities. This API allows users to query product information, manage chat sessions, and process data efficiently.

## Base URL

The base URL for accessing the API is:

```
https://api.healthproductchatbot.com/v1
```

## Endpoints

### 1. Chat Endpoints

#### POST /chat

- **Description**: Initiates a chat session.
- **Request Body**:
  ```json
  {
    "userId": "string",
    "message": "string"
  }
  ```
- **Response**:
  - **200 OK**: Returns the chat session details.
  - **400 Bad Request**: If the request body is invalid.

#### GET /chat/{sessionId}

- **Description**: Retrieves messages from a specific chat session.
- **Parameters**:
  - `sessionId`: The ID of the chat session.
- **Response**:
  - **200 OK**: Returns the chat messages.
  - **404 Not Found**: If the session ID does not exist.

### 2. Product Endpoints

#### GET /products

- **Description**: Retrieves a list of health products.
- **Query Parameters**:
  - `category`: (optional) Filter products by category.
- **Response**:
  - **200 OK**: Returns a list of products.
  - **500 Internal Server Error**: If there is an issue retrieving products.

#### GET /products/{productId}

- **Description**: Retrieves detailed information about a specific product.
- **Parameters**:
  - `productId`: The ID of the product.
- **Response**:
  - **200 OK**: Returns product details.
  - **404 Not Found**: If the product ID does not exist.

### 3. WebSocket Endpoints

#### WebSocket Connection

- **Description**: Establishes a WebSocket connection for real-time chat updates.
- **Endpoint**: `wss://api.healthproductchatbot.com/chat`
- **Response**:
  - **Connected**: Acknowledges the connection.
  - **Message**: Sends real-time chat messages.

## Error Handling

All API responses include an error code and message in the following format:

```json
{
  "error": {
    "code": "string",
    "message": "string"
  }
}
```

## Authentication

The API uses token-based authentication. Include the token in the `Authorization` header for all requests:

```
Authorization: Bearer <token>
```

## Rate Limiting

To ensure fair usage, the API enforces rate limits. Exceeding the limit will result in a `429 Too Many Requests` response.

## Conclusion

This API documentation provides a comprehensive guide to the endpoints available in the Health Product Chatbot. For further assistance, please refer to the deployment and architecture documentation.