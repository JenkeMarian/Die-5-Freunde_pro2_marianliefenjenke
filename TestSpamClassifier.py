# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:05:21 2021

@author: maria
"""

#Prog2
#Übung 4
# Marian Liefen Jenke

import unittest
from classifier_anlage import Classifier

class TestCharacterFeatures(unittest.TestCase):

    def setUp(self):
        self.nr1 = Classifier("Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's", "spam")
        self.nr2 = Classifier("You are a winner U have been specially selected 2 receive £1000 or a 4* holiday (flights inc) speak to a live operator 2 claim 0871277810910p/min (18+)", "spam")
        self.nr3 = Classifier("Hi Tom, viele Grüße von der Nordsee. Eine Karte ist bereits auf dem Weg zu dir.", "ham") 
        
    def predict(self):
        self.assertEqual(self.nr1.predict(), "spam")
        self.assertEqual(self.nr2.predict(), "spam")
        self.assertEqual(self.nr3.predict(), "ham")
    
    def test_train(self):
        pass
    
    def test_evaluation(self):
        pass
        
##################################################################
    
if __name__ == '__main__' :
    unittest.main()