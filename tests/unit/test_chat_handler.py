import unittest
from src.lambda.chat.handler import lambda_handler

class TestChatHandler(unittest.TestCase):

    def test_lambda_handler_success(self):
        event = {
            "body": '{"message": "Hello, chatbot!"}',
            "headers": {
                "Content-Type": "application/json"
            }
        }
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('body', response)
        self.assertIn('response', response['body'])

    def test_lambda_handler_invalid_json(self):
        event = {
            "body": 'invalid json',
            "headers": {
                "Content-Type": "application/json"
            }
        }
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 400)
        self.assertIn('error', response['body'])

    def test_lambda_handler_missing_message(self):
        event = {
            "body": '{"not_message": "Hello, chatbot!"}',
            "headers": {
                "Content-Type": "application/json"
            }
        }
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 400)
        self.assertIn('error', response['body'])

if __name__ == '__main__':
    unittest.main()