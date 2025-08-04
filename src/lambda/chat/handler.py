import json
import os
import logging
from typing import Dict, Any

from src.shared.bedrock_client import BedrockClient
from src.shared.opensearch_client import OpenSearchClient
from src.shared.dynamodb_client import DynamoDBClient
from src.shared.guardrails import GuardrailsService
from src.shared.utils import validate_input, generate_response_id

# Configure logging
logging.basicConfig(level=os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger(__name__)

# Initialize clients
bedrock_client = BedrockClient()
opensearch_client = OpenSearchClient()
dynamodb_client = DynamoDBClient()
guardrails_service = GuardrailsService()


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    Main chat handler for processing user queries
    """
    try:
        # Parse request
        body = json.loads(event.get('body', '{}'))
        user_query = body.get('message', '')
        session_id = body.get('session_id', '')
        user_id = body.get('user_id', 'anonymous')
        
        # Validate input
        if not validate_input(user_query):
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'error': 'Invalid input provided'
                })
            }
        
        # Apply input guardrails
        guardrail_result = guardrails_service.apply_input_guardrails(user_query)
        if guardrail_result['blocked']:
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'response': guardrail_result['safe_response'],
                    'response_id': generate_response_id(),
                    'guardrail_applied': True
                })
            }
        
        # Retrieve conversation context
        conversation_context = dynamodb_client.get_conversation_context(session_id)
        
        # Search for relevant product information
        search_results = opensearch_client.search_products(
            query=user_query,
            context=conversation_context
        )
        
        # Generate response using Bedrock
        response = bedrock_client.generate_response(
            query=user_query,
            context=search_results,
            conversation_history=conversation_context
        )
        
        # Apply output guardrails
        final_response = guardrails_service.apply_output_guardrails(response)
        
        # Store conversation
        dynamodb_client.store_conversation_turn(
            session_id=session_id,
            user_id=user_id,
            user_message=user_query,
            bot_response=final_response['response']
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'response': final_response['response'],
                'response_id': generate_response_id(),
                'sources': search_results.get('sources', []),
                'guardrail_applied': final_response.get('guardrail_applied', False)
            })
        }
        
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': 'Internal server error',
                'message': 'Please try again later'
            })
        }