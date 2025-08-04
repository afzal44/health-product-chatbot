import unittest
from src.shared.embedding_service import create_embeddings, load_embeddings

class TestEmbeddingService(unittest.TestCase):

    def test_create_embeddings(self):
        # Sample input data
        sample_data = ["product1", "product2", "product3"]
        embeddings = create_embeddings(sample_data)
        
        # Check if embeddings are created
        self.assertIsNotNone(embeddings)
        self.assertEqual(len(embeddings), len(sample_data))
        # Add more assertions based on expected embedding shape or values

    def test_load_embeddings(self):
        # Assuming embeddings are saved in a specific format
        embeddings = load_embeddings("path/to/embeddings/file")
        
        # Check if embeddings are loaded correctly
        self.assertIsNotNone(embeddings)
        # Add more assertions based on expected loaded data structure

if __name__ == '__main__':
    unittest.main()