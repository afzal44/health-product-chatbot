# 📁 Health Product Chatbot - Project Structure

This document provides a comprehensive overview of the project directory structure and the purpose of each component.

## 🏗️ High-Level Architecture

```
health-product-chatbot/
├── 📦 Backend (Python/Serverless)
├── 🎨 Frontend (JavaScript/WebPack)
├── 🗃️ Data Processing Pipeline
├── ☁️ Infrastructure as Code
├── 🧪 Testing Framework
├── 📚 Documentation
└── 🔧 Automation Scripts
```

## 📂 Complete Directory Structure

```
health-product-chatbot/
├── README.md                          # Project overview and setup instructions
├── .gitignore                         # Git ignore rules for security and cleanup
├── package.json                       # Node.js dependencies and scripts
├── serverless.yml                     # Serverless Framework configuration
├── .env.example                       # Environment variables template
├── requirements.txt                   # Python dependencies (root level)
│
├── 📁 src/                           # Source code directory
│   ├── 📁 lambda/                    # AWS Lambda functions
│   │   ├── 📁 chat/                  # Main chat handler
│   │   │   ├── handler.py            # Chat logic and RAG pipeline
│   │   │   ├── requirements.txt      # Chat-specific dependencies
│   │   │   └── __init__.py           # Python package initialization
│   │   ├── 📁 data-processing/       # Data ingestion and processing
│   │   │   ├── handler.py            # Process uploaded product data
│   │   │   ├── requirements.txt      # Data processing dependencies
│   │   │   └── __init__.py           # Python package initialization
│   │   └── 📁 websocket/             # Real-time chat WebSocket handlers
│   │       ├── handler.py            # WebSocket connection management
│   │       ├── requirements.txt      # WebSocket dependencies
│   │       └── __init__.py           # Python package initialization
│   │
│   ├── 📁 shared/                    # Shared utilities and services
│   │   ├── __init__.py               # Python package initialization
│   │   ├── bedrock_client.py         # AWS Bedrock integration
│   │   ├── opensearch_client.py      # OpenSearch Serverless client
│   │   ├── dynamodb_client.py        # DynamoDB operations
│   │   ├── guardrails.py             # Content filtering and safety
│   │   ├── embedding_service.py      # Text embedding generation
│   │   └── utils.py                  # Common utility functions
│   │
│   └── 📁 config/                    # Configuration files
│       ├── __init__.py               # Python package initialization
│       ├── settings.py               # Application settings
│       └── guardrails_config.json    # Guardrails rules and policies
│
├── 📁 frontend/                      # Frontend chat widget
│   ├── package.json                  # Frontend dependencies and build scripts
│   ├── index.html                    # Main HTML file for testing
│   ├── 📁 src/                       # Frontend source code
│   │   ├── 📁 components/            # React-like components
│   │   │   ├── ChatWidget.js         # Main chat interface component
│   │   │   ├── MessageBubble.js      # Individual message display
│   │   │   └── TypingIndicator.js    # Typing animation component
│   │   ├── 📁 services/              # API and WebSocket services
│   │   │   ├── chatService.js        # HTTP API communication
│   │   │   └── websocketService.js   # Real-time messaging
│   │   ├── 📁 styles/                # CSS stylesheets
│   │   │   └── main.css              # Main stylesheet
│   │   └── main.js                   # Application entry point
│   └── webpack.config.js             # Webpack build configuration
│
├── 📁 data/                          # Data management directory
│   ├── 📁 raw/                       # Raw data storage
│   │   └── 📁 product_data/          # Original product information files
│   ├── 📁 processed/                 # Processed data storage
│   │   └── 📁 embeddings/            # Generated vector embeddings
│   └── 📁 scripts/                   # Data processing scripts
│       ├── extract_products.py       # Extract product data from sources
│       ├── create_embeddings.py      # Generate vector embeddings
│       └── upload_to_opensearch.py   # Upload data to OpenSearch
│
├── 📁 infrastructure/                # Infrastructure as Code
│   ├── 📁 cloudformation/            # AWS CloudFormation templates
│   │   ├── opensearch.yaml           # OpenSearch Serverless setup
│   │   ├── dynamodb.yaml             # DynamoDB table configuration
│   │   ├── api-gateway.yaml          # API Gateway setup
│   │   └── iam-roles.yaml            # IAM roles and policies
│   └── 📁 terraform/                 # Terraform alternative (optional)
│       ├── main.tf                   # Main Terraform configuration
│       ├── variables.tf              # Input variables
│       └── outputs.tf                # Output values
│
├── 📁 tests/                         # Testing framework
│   ├── 📁 unit/                      # Unit tests
│   │   ├── test_chat_handler.py      # Test chat logic
│   │   ├── test_guardrails.py        # Test safety mechanisms
│   │   └── test_embedding_service.py # Test embedding generation
│   ├── 📁 integration/               # Integration tests
│   │   └── test_rag_pipeline.py      # End-to-end pipeline testing
│   └── 📁 fixtures/                  # Test data
│       └── sample_data.json          # Sample product data for testing
│
├── 📁 docs/                          # Project documentation
│   ├── API.md                        # API reference documentation
│   ├── DEPLOYMENT.md                 # Deployment instructions
│   ├── ARCHITECTURE.md               # System architecture overview
│   └── GUARDRAILS.md                 # Safety and compliance guide
│
└── 📁 scripts/                       # Automation and utility scripts
    ├── deploy.sh                     # Deployment automation script
    ├── setup-environment.sh          # Environment setup script
    └── run-tests.sh                  # Test execution script
```

## 🔍 Directory Purpose & Responsibilities

### 📁 `/src/lambda/`
**Purpose:** Serverless function implementations
- **`chat/`**: Main conversational AI logic with RAG pipeline
- **`data-processing/`**: Automated data ingestion and processing
- **`websocket/`**: Real-time communication handlers

### 📁 `/src/shared/`
**Purpose:** Reusable business logic and AWS integrations
- **`bedrock_client.py`**: LLM interactions and response generation
- **`opensearch_client.py`**: Vector search and knowledge retrieval
- **`guardrails.py`**: Content filtering and health compliance
- **`embedding_service.py`**: Text-to-vector conversion

### 📁 `/frontend/`
**Purpose:** User interface and chat experience
- **`components/`**: Modular UI components
- **`services/`**: API communication layers
- **`styles/`**: Visual design and theming

### 📁 `/data/`
**Purpose:** Data pipeline and storage management
- **`raw/`**: Original product data files
- **`processed/`**: Transformed data ready for search
- **`scripts/`**: ETL (Extract, Transform, Load) processes

### 📁 `/infrastructure/`
**Purpose:** Cloud resource definitions
- **`cloudformation/`**: AWS resource templates
- **`terraform/`**: Alternative infrastructure option

## 🎯 Key Design Principles

### 🔄 **Separation of Concerns**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Presentation   │    │   Business Logic │    │   Data Layer    │
│   (Frontend)     │◄──►│   (Lambda/Shared)│◄──►│ (OpenSearch/DDB)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 🧩 **Modular Architecture**
- **Independent Lambda functions** for different responsibilities
- **Shared libraries** to avoid code duplication
- **Plugin-ready design** for future AI agents

### 🛡️ **Security-First Design**
- **Guardrails integration** at multiple layers
- **Environment-based configuration** (dev/staging/prod)
- **Secrets management** via AWS Parameter Store

### 🚀 **Scalability & Performance**
- **Serverless architecture** for auto-scaling
- **Vector search optimization** with OpenSearch
- **Conversation caching** via DynamoDB

## 📋 File Naming Conventions

### Python Files
```
snake_case.py           # All Python files
handler.py              # Lambda entry points
client.py               # AWS service clients
service.py              # Business logic services
utils.py                # Utility functions
```

### JavaScript Files
```
camelCase.js            # All JavaScript files
ComponentName.js        # React-style components
serviceName.js          # API service files  
```

### Configuration Files
```
kebab-case.yaml         # Infrastructure files
lowercase.json          # Configuration files
UPPERCASE.md           # Documentation files
```

## 🔧 Development Workflow

### 1. **Local Development**
```bash
# Activate environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

### 2. **Feature Development**
```bash
# Create feature branch
git checkout -b feature/new-capability

# Develop in appropriate directory
# - Backend: /src/lambda/ or /src/shared/
# - Frontend: /frontend/src/
# - Infrastructure: /infrastructure/
```

### 3. **Testing**
```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# Frontend tests
cd frontend && npm test
```

### 4. **Deployment**
```bash
# Deploy to development
npm run deploy-dev

# Deploy to production
npm run deploy-prod
```

## 🎨 Customization Points

### Adding New Features
- **New Lambda function**: Create folder in `/src/lambda/`
- **New shared service**: Add to `/src/shared/`
- **New frontend component**: Add to `/frontend/src/components/`

### Configuration Changes
- **Environment variables**: Update `.env.example`
- **Guardrails rules**: Modify `/src/config/guardrails_config.json`
- **Infrastructure**: Update CloudFormation templates

### Data Sources
- **New data types**: Add processors to `/data/scripts/`
- **New embeddings**: Modify `/src/shared/embedding_service.py`

## 🚀 Getting Started

1. **Clone repository**
2. **Run setup script**: `./scripts/setup-environment.sh`
3. **Configure environment**: Update `.env` file
4. **Deploy infrastructure**: `npm run deploy-dev`
5. **Start developing!**

This structure provides a solid foundation for building, testing, and scaling your health product chatbot while maintaining clean code organization and deployment automation.