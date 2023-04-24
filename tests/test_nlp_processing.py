import unittest
from nlp_processing.nlp_utils import process_text

class TestNLPProcessing(unittest.TestCase):
    def test_process_text(self):
        processed_text = process_text('Example Text')
        self.assertEqual(processed_text, 'example text')

if __name__ == '__main__':
    unittest.main()
