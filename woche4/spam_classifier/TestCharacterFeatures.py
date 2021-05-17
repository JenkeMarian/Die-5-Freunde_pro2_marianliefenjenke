# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:06:45 2021

@author: maria
"""

#Prog2
#Übung 4
# Marian Liefen Jenke

import unittest
from features import CharacterFeatures


class TestCharacterFeatures(unittest.TestCase):
    
    def setUp(self):
        self.nr1 = CharacterFeatures([])
        self.nr2 = CharacterFeatures([""])
        self.nr3 = (["Das ist ein Beispielsatz"])
      
    
    def test_number_of_characters(self):
        self.assertEqual(CharacterFeatures.number_of_characters(""), 0)
        self.assertEqual(CharacterFeatures.number_of_characters("hello"), 5)
        
    def test_number_of_letters(self):
        self.assertEqual(CharacterFeatures.number_of_letter(""), 0)
        self.assertEqual(CharacterFeatures.number_of_letter("hii"), 2)
        
    def test_number_of_uppercase_letters(self):
        self.assertEqual(CharacterFeatures.number_uppercase_letters(""), 0)
        self.assertEqual(CharacterFeatures.number_uppercase_letters("HELLO"), 5)
        
    def test_number_of_lowercase_letters(self):
        self.assertEqual(CharacterFeatures.number_lowercase_letters(""), 0)
        self.assertEqual(CharacterFeatures.number_lowercase_letters("hii"), 3)
 
##################################################################        
        
if __name__ == '__main__':
    unittest.main()