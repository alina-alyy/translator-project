import unittest
from translator import french_to_english

class test_translator (unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(french_to_english("Bonjour cher"),"Hello dear")

class test_translator2(unittest.TestCase):
    def test_e2f2(self):
        self.assertNotEqual(french_to_english("Bonjour cher"),"hi")

if __name__ == '__main__':
     unittest.main()