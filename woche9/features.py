# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:42:33 2021

@author: maria
"""

#Prog2
#Übung 9
# Marian Liefen Jenke

import logging
import pandas as pd
import os
import sys
import nltk
from abc import ABC, abstractmethod
from nltk.corpus import stopwords

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from woche8.debug_decorator import decorator

logging.basicConfig(filename = 'output_featureclass' , level=logging.DEBUG)


class Template(ABC):
    
    def __init__(self, dataframe=None):
        self.df = dataframe
        self.stopwords = set(stopwords.words("english"))
    
##################################################################

class CharacterFeatures(Template):
    
    @decorator
    def in_df(self):
        
        self.df["data_split"] = self.df["text"].str.split()
        self.df["number_of_letter"] = self.df["text"].apply(self._number_of_letter)
        self.df["number_uppercase_letters"] = self.df["text"].apply(self._number_uppercase_letters)
        self.df["number_lowercase_letters"] = self.df["text"].apply(self._number_lowercase_letters)
        self.df["function_words"] = self.df["data_split"].apply(self._function_words)
        self.df["stop_words"] = self.df["data_split"].apply(self._stop_words)
        del self.df["data_split"]
        return self.df
    
    
    # Zählt die Anzahl bestimmter Buchstaben
    @classmethod
    def _number_of_letter(cls, text):
        return text.count("i")/len(text)
    
    # Zählt die Großbuchstaben
    @classmethod
    def _number_uppercase_letters(cls, text):
        return sum(1 for c in text if c.isupper())/len(text)
    
    # Zählt die Kleinbuchstaben
    @classmethod
    def _number_lowercase_letters(cls, text):
        return sum(1 for c in text if c.islower())/len(text)
    
    def _function_words(self, tokens):
        count = 0
        tagged = nltk.pos_tag(tokens)
        for tag in tagged:
            if tag[1] in {"CC", "DT", "IN", "MD", "PDT", "POS", "RP", "TO",
                          "UH"}:
                count += 1
        return (count/(len(tokens)))
    
   
    def _stop_words(self, tokens):
        count = 0
        for word in tokens:
            word = word.lower().strip(".,!?\"\'")
            if word in self.stopwords:
                count += 1
        return (count/(len(tokens)))
    
    
    def from_file(self, filename):
        self.df = pd.read_csv(filename, index_col="ID")
    
    @classmethod
    @decorator
    def features(cls, Input):
        features = [cls.number_of_characters(Input), cls.number_of_letter(Input),
                    cls.number_uppercase_letters(Input), cls.number_lowercase_letters(Input)]
        return features
       
##################################################################

    
if __name__ == '__main__':
   cf = CharacterFeatures()
   cf.from_file(r"C:\Users\maria\OneDrive\Desktop\prog2\code\woche6\training_data.csv")
   cf.in_df()
   print(cf.in_df())
    
    
    
    
   
