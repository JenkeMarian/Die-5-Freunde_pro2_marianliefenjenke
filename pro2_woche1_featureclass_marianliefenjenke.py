# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Prog2
#Übung 1
# Marian Liefen Jenke

class Features:
    
    def __init__(self, Input):
   
        self.Input = None
    
    
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

Eingabe = "Satz aus viiiiieln Wörtern"     

##################################################################

def main():
    Satz = Features("Satz")
    print(Satz.number_of_characters(Eingabe))
    print(Satz.number_of_letter(Eingabe))
    print(Satz.number_uppercase_letters(Eingabe))
    print(Satz.number_lowercase_letters(Eingabe))
    
##################################################################    
    
if __name__ == '__main__':
    main()
