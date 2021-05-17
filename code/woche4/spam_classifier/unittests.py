# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:06:45 2021

@author: maria
"""
import unittest
from features import CharacterFeatures


class TestCharacterFeatures(unittest.TestCase):
    
    def setUp(self):
        self.nr1 = CharacterFeatures([])
        self.nr2 = CharacterFeatures([""])
        self.nr3 = (["Das ist ein Beispielsatz"])
      
    
    def number_of_characters(self):
        self.assertEqual(CharacterFeatures.num_characters("", 0))
        self.assertEqual(CharacterFeatures.num_characters("hello"), 5)
        
    def number_of_letters(self):
        self.assertEqual(CharacterFeatures.num_characters("", 0))
        self.assertEqual(CharacterFeatures.num_characters("hii"), 2)
        
    def number_of_uppercase_letters(self):
        self.assertEqual(CharacterFeatures.num_characters("", 0))
        self.assertEqual(CharacterFeatures.num_characters("HELLO"), 5)
        
    def number_of_lowercase_letters(self):
        self.assertEqual(CharacterFeatures.num_characters("", 0))
        self.assertEqual(CharacterFeatures.num_characters("hii"), 3)
 
##################################################################        
        
if __name__ == '__main__':
    unittest.main()