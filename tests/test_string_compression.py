import unittest
import string_compression


class TestStringCompression(unittest.TestCase):
    """Test cases for the string compression LeetCode problem
    """
    def test_examples(self):
        """Tests cases for examples provided in the question
        """
        # Example 1
        chars = ["a","a","b","b","c","c","c"]
        expected_result = ["a","2","b","2","c","3"]
        solution = string_compression.Solution()
        solution.compress(chars)
        self.assertEqual(chars, expected_result)

        # Exmaple 2
        chars = ["a"]
        expected_result = ["a"]
        solution = string_compression.Solution()
        solution.compress(chars)
        self.assertEqual(chars, expected_result)
        
        # Exmaple 3
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected_result = ["a","b","1","2"]
        solution = string_compression.Solution()
        solution.compress(chars)
        self.assertEqual(chars, expected_result)
        
        # Test Case 4
        chars = ["a","a","a","b","b","a","a"]
        expected_result = ["a","3","b","2","a","2"]
        solution = string_compression.Solution()
        solution.compress(chars)
        self.assertEqual(chars, expected_result)
        
        # Test Case 5
        chars = ["a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]
        expected_result = ["a","6","b","2","1","c","1","4"]
        solution = string_compression.Solution()
        solution.compress(chars)
        self.assertEqual(chars, expected_result)
