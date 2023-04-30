import unittest
from translator import english_to_french

class test_translator (unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french("Hello dear"),"Bonjour chère")

class test_translator2(unittest.TestCase):
    def test_e2f2(self):
        self.assertNotEqual(english_to_french("hi"),"Bonjour cher")

if __name__ == '__main__':
     unittest.main()
        