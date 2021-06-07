# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:42:33 2021

@author: maria
"""

#Prog2
#Übung 2
# Marian Liefen Jenke

import logging
import pandas as pd
import os
import sys
from abc import ABC, abstractmethod

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from woche8.debug_decorator import decorator

logging.basicConfig(filename = 'output_featureclass' , level=logging.DEBUG)


class Template(ABC):
    
    def __init__(self, Input):
        self.Input = Input
    
##################################################################

class CharacterFeatures(Template):
    
    # Zählt die Anzahl der Buchstaben 
    @classmethod
    def number_of_characters(cls, Input):
        return(len(Input)) 
    
    # Zählt die Anzahl bestimmter Buchstaben
    @classmethod
    def number_of_letter(cls, Input):
        return Input.count("i") 
    
    # Zählt die Großbuchstaben
    @classmethod
    def number_uppercase_letters(cls, Input):
        return sum(1 for c in Input if c.isupper())
    
    # Zählt die Kleinbuchstaben
    @classmethod
    def number_lowercase_letters(cls, Input):
        return sum(1 for c in Input if c.islower())
    
    def normalize(cls, Input, test):
        return round(Input/len(test), 2)
    
    def output_into_df(self, df, output=True):
        pass
    
    @classmethod
    @decorator
    def features(cls, Input):
        features = [cls.number_of_characters(Input), cls.number_of_letter(Input),
                    cls.number_uppercase_letters(Input), cls.number_lowercase_letters(Input)]
        return features
       
##################################################################

    
if __name__ == '__main__':
    test = "Das ist ein Satz"
    logging.debug(CharacterFeatures(test))
    new_test = CharacterFeatures(test)
    CharacterFeatures.features(test)
    logging.debug(new_test)
    
    
    
    
   
