# Deployment Instructions for Health Product Chatbot

## Prerequisites
Before deploying the Health Product Chatbot, ensure you have the following prerequisites installed:

- Node.js and npm
- Python 3.x
- AWS CLI configured with appropriate permissions
- Serverless Framework

## Deployment Steps

1. **Clone the Repository**
   Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd health-product-chatbot
   ```

2. **Set Up Environment Variables**
   Create a `.env` file based on the `.env.example` provided:
   ```
   cp .env.example .env
   ```
   Update the `.env` file with your specific environment variables.

3. **Install Backend Dependencies**
   Navigate to the `src` directory and install the required Python packages:
   ```
   cd src
   pip install -r requirements.txt
   ```

4. **Install Frontend Dependencies**
   Navigate to the `frontend` directory and install the required npm packages:
   ```
   cd frontend
   npm install
   ```

5. **Deploy Infrastructure**
   Use the Serverless Framework to deploy the backend services:
   ```
   serverless deploy
   ```

6. **Build Frontend**
   Build the frontend application:
   ```
   npm run build
   ```

7. **Run Tests**
   It is recommended to run tests before final deployment:
   ```
   cd ../tests
   ./run-tests.sh
   ```

8. **Access the Application**
   After successful deployment, access the application using the provided API Gateway URL.

## Rollback Instructions
In case of deployment failure, you can rollback to the previous version using:
```
serverless rollback
```

## Additional Notes
- Ensure that all AWS resources are properly configured and permissions are set.
- Monitor the logs for any issues during deployment using:
```
serverless logs -f <function-name>
```

This document provides a high-level overview of the deployment process for the Health Product Chatbot. For detailed configurations, refer to the respective configuration files and documentation.