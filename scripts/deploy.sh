#!/bin/bash

# Deployment script for Health Product Chatbot

set -e

STAGE=${1:-dev}
REGION=${2:-us-east-1}

echo "🚀 Deploying Health Product Chatbot to $STAGE environment..."

# Activate virtual environment
source venv/bin/activate

# Build frontend
echo "🏗️  Building frontend..."
cd frontend && npm run build && cd ..

# Deploy infrastructure
echo "🏗️  Deploying infrastructure..."
serverless deploy --stage $STAGE --region $REGION

# Upload sample data (optional)
if [ "$STAGE" = "dev" ]; then
    echo "📊 Uploading sample data..."
    python data/scripts/upload_to_opensearch.py --stage $STAGE
fi

echo "✅ Deployment complete!"
echo "API Gateway URL: $(serverless info --stage $STAGE | grep 'HttpApi' | awk '{print $2}')"