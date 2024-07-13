import unittest
from datastructures import TrieNode

class TrieTest(unittest.TestCase):
    def test_init_default(self):
        node = TrieNode()
        self.assertEqual(node.value, None)
    def test_init_value(self):
        node = TrieNode(5)
        self.assertEqual(node.value, 5)

    def test_setitem_getitem(self):
        root = TrieNode(3)
        a = TrieNode(5)
        root['a'] = a
        self.assertEqual(root['a'], a)
    def test_getitem_nonexistent(self):
        root = TrieNode(3)
        self.assertEqual(root['a'], None)

    def test_append(self):
        root = TrieNode()
        root.append_key('key', 5)
        self.assertEqual(root['k']['e']['y'].value, 5)
    
    def test_contains_true(self):
        root = TrieNode()
        root.append_key('key', 1)
        self.assertTrue('key' in root)
    def test_contains_false1(self):
        root = TrieNode()
        root.append_key('key', 1)
        self.assertFalse('keys' in root)
    def test_contains_false2(self):
        root = TrieNode()
        root.append_key('keys', 1)
        self.assertFalse('key' in root)
    def test_contains_false3(self):
        root = TrieNode()
        root.append_key('key', 1)
        self.assertFalse('ket' in root)
    def test_contains_wrong_type(self):
        root = TrieNode()
        root.append_key('key', 1)
        with self.assertRaises(TypeError):
            1 in root

    def test_find_longest_match_empty_trie(self):
        root = TrieNode()
        self.assertTupleEqual(root.find_longest_match('Hello'), (0, None))
    def test_find_longest_match_whole_string(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match('Hello'), (5, 4))
    def test_find_longest_match_long_string(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match("Hello, is it me you're looking for"), (5, 4))
    def test_find_longest_match_short_string(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match("He"), (2, 2))
    def test_find_longest_match_start(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match("Hello. Hell", start=7), (10, 3))
    def test_find_longest_match_end(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match("Hello", end=4), (3, 3))
    def test_find_longest_match_positive_step(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match("H e ll o", step=2), (6, 3))
    def test_find_longest_match_negative_step(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match("olleh olleH", start=-1, end=-12, step=-1), (-6, 4))
    def test_find_longest_match_s_not_str(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        with self.assertRaises(TypeError):
            root.find_longest_match(5, start=0, end=5, step=1)
    def test_find_longest_match_start_not_int(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        with self.assertRaises(TypeError):
            root.find_longest_match('Hello', start='0', end=5, step=1)
    def test_find_longest_match_end_not_int(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        with self.assertRaises(TypeError):
            root.find_longest_match('Hello', start=0, end='5', step=1)
    def test_find_longest_match_step_not_int(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        with self.assertRaises(TypeError):
            root.find_longest_match('5', start=0, end=5, step='1')
    def test_find_longest_match_step_zero(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        with self.assertRaises(ValueError):
            root.find_longest_match('Hello', start=0, end=5, step=0)
    def test_find_longest_match_out_of_range(self):
        root = TrieNode()
        root.append_key('H', 1)
        root.append_key('He', 2)
        root.append_key('Hel', 3)
        root.append_key('Hello', 4)
        self.assertEqual(root.find_longest_match('Hello', start=0, end=10, step=1), (5, 4))

if __name__ == '__main__':
    unittest.main()