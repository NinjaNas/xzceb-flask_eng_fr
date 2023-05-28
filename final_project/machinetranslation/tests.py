import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
        def testNull(self):
            self.assertNotEqual(english_to_french("None"), '')
            self.assertNotEqual(english_to_french(0), 0)
            with self.assertRaises(ValueError) as exc:
                english_to_french(None)
            self.assertEqual(str(exc.exception), 'text must be provided')
        def testTranslate(self): 
            self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
        def testNull(self): 
            self.assertNotEqual(french_to_english("None"), '')
            self.assertNotEqual(french_to_english(0), 0)
            with self.assertRaises(ValueError) as exc:
                french_to_english(None)
            self.assertEqual(str(exc.exception), 'text must be provided')
        def testTranslate(self): 
            self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()