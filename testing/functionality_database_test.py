from functionality_database import FunctionalityDatabase
import unittest

class FunctionalityDatabaseTest(unittest.TestCase):
    def test_isletter_uppercase_letter(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_letter('X'))
    def test_isletter_lowercase_letter(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_letter('x'))
    def test_isletter_A(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_letter('A'))
    def test_isletter_a(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_letter('a'))
    def test_isletter_Z(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_letter('Z'))
    def test_isletter_z(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_letter('z'))
    def test_isletter_digit(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.is_letter('5'))
    def test_isletter_comma(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.is_letter(','))
    def test_isletter_space(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.is_letter(' '))
    
    def test_isdigit_digit(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_digit('4'))
    def test_isdigit_zero(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_digit('0'))
    def test_isdigit_nine(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.is_digit('9'))
    def test_isdigit_letter(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.is_digit('a'))
    def test_isdigit_comma(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.is_digit(','))
    def test_isdigit_space(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.is_digit(' '))
    
    def test_brackets_match_matching(self):
        fd = FunctionalityDatabase()
        self.assertTrue(fd.brackets_match('(', ')'))
    def test_brackets_match_not_matching(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.brackets_match('(', ']'))
    def test_brackets_match_not_a_bracket(self):
        fd = FunctionalityDatabase()
        self.assertFalse(fd.brackets_match('(', '.'))

if __name__ == '__main__':
    unittest.main()