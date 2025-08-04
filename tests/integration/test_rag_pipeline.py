import unittest
from src.lambda.chat.handler import chat_handler
from src.lambda.data_processing.handler import data_processing_handler

class TestRAGPipeline(unittest.TestCase):

    def setUp(self):
        # Setup code to initialize any required resources or state
        self.chat_input = "What are the health benefits of turmeric?"
        self.expected_response = "Turmeric has anti-inflammatory properties and is rich in antioxidants."

    def test_chat_handler_integration(self):
        # Test the integration of the chat handler with the data processing handler
        response = chat_handler(self.chat_input)
        self.assertEqual(response, self.expected_response)

    def test_data_processing_handler_integration(self):
        # Test the integration of the data processing handler
        data = {"product": "turmeric", "benefits": ["anti-inflammatory", "antioxidants"]}
        processed_data = data_processing_handler(data)
        self.assertIn("processed", processed_data)

if __name__ == '__main__':
    unittest.main()