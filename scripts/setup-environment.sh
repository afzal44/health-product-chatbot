#!/bin/bash

# Health Product Chatbot - Environment Setup Script

set -e

echo "🚀 Setting up Health Product Chatbot environment..."

# Check if required tools are installed
command -v python3 >/dev/null 2>&1 || { echo "Python 3 is required but not installed. Aborting." >&2; exit 1; }
command -v npm >/dev/null 2>&1 || { echo "Node.js/npm is required but not installed. Aborting." >&2; exit 1; }
command -v aws >/dev/null 2>&1 || { echo "AWS CLI is required but not installed. Aborting." >&2; exit 1; }

# Create virtual environment
echo "📦 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend && npm install && cd ..

# Create environment file
if [ ! -f .env ]; then
    echo "📝 Creating environment file..."
    cp .env.example .env
    echo "⚠️  Please update .env file with your AWS configuration"
fi

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p data/raw/product_data
mkdir -p data/processed/embeddings
mkdir -p logs

# Set up pre-commit hooks (optional)
echo "🔧 Setting up development tools..."
pip install pre-commit
pre-commit install

echo "✅ Environment setup complete!"
echo ""
echo "Next steps:"
echo "1. Update .env file with your AWS configuration"
echo "2. Run 'source venv/bin/activate' to activate virtual environment"
echo "3. Run 'npm run deploy-dev' to deploy to AWS"
echo "4. Start developing! 🎉"