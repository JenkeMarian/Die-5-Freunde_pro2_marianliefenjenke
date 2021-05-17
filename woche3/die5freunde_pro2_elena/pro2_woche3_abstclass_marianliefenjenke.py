# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:35:36 2021

@author: maria
"""

#Prog2
#Übung 1
# Marian Liefen Jenke


from features import TemplateFeature
from abc import ABC, abstractmethod
import nltk


class Features(TemplateFeature):
    
    def normalize(self):
        pass
    
    # Zählt die Anzahl der Buchstaben 
    def number_of_characters(self, Input):
        return str(len(Input)) 
    
    # Zählt die Anzahl bestimmter Buchstaben
    def number_of_letter(self, Input):
        return Input.count("i")
    
    # Zählt die Großbuchstaben
    def number_uppercase_letters(self, Input):
        return sum(1 for c in Input if c.isupper())
    
    # Zählt die Kleinbuchstaben
    def number_lowercase_letters(self, Input):
        return sum(1 for c in Input if c.islower())
       
##################################################################        

Eingabe = ""     

##################################################################

def main():
    Satz = Features("Satz")
    print(Satz.number_of_characters(Eingabe))
    print(Satz.number_of_letter(Eingabe))
    print(Satz.number_uppercase_letters(Eingabe))
    print(Satz.number_lowercase_letters(Eingabe))
    
    
if __name__ == '__main__':
    main()