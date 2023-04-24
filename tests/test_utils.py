import unittest
from utils.common_utils import merge_dicts

class TestUtils(unittest.TestCase):
    def test_merge_dicts(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merged_dict = merge_dicts(dict1, dict2)
        self.assertEqual(merged_dict, {'a': 1, 'b': 3, 'c': 4})

if __name__ == '__main__':
    unittest.main()
