# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:42:33 2021

@author: maria
"""

#Prog2
#Übung 2
# Marian Liefen Jenke

from abc import ABC, abstractmethod


class Template(ABC):
    
    def __init__(self, Input):
        self.Input = Input
    
    """
    #An dieser Stelle bin ich mir unsicher. Was gehört denn nun tatsächlich in die abstrakte Klasse?
    Wenn ich die Aufgabe so löse wie im Video, müssten hier die  Methoden folgen, oder? Intuitiv würde ich aber hier 
    nur die __init__ hinverschieben.
    @abstractmethod
    def number_of_characters(self): 
        pass
    
    @abstractmethod
    def number_of_letters(self):
        pass
    @abstractmethod
    def number_of_uppercase_letters(self):
        pass
    
    @abstractmethod 
    def number_lowercase_letters(self):
        pass
    """
    
##################################################################

class CharacterFeatures(Template):
    
    @classmethod
    # Zählt die Anzahl der Buchstaben 
    def number_of_characters(cls, Input):
        return(len(Input)) 
    
    @classmethod
    # Zählt die Anzahl bestimmter Buchstaben
    def number_of_letter(cls, Input):
        return Input.count("i")
    
    @classmethod
    # Zählt die Großbuchstaben
    def number_uppercase_letters(cls, Input):
        return sum(1 for c in Input if c.isupper())
    
    @classmethod
    # Zählt die Kleinbuchstaben
    def number_lowercase_letters(cls, Input):
        return sum(1 for c in Input if c.islower())
       
##################################################################        

Eingabe = ""     

##################################################################

def main():
    Satz = CharacterFeatures("Satz")
    print(Satz.number_of_characters(Eingabe))
    print(Satz.number_of_letter(Eingabe))
    print(Satz.number_uppercase_letters(Eingabe))
    print(Satz.number_lowercase_letters(Eingabe))
    
    
if __name__ == '__main__':
    main()