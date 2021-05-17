# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:21:29 2021

@author: maria
"""

# Marian Liefen Jenke
# Prog 2
# Übung 5

import os
class DataGenerator:
    
    def __init__(self, path):
        self.filepath = path
        self.data = []
        self.i = 0
        self.reader()
        
    def reader(self):
        with open(self.filepath, 'r', encoding= 'utf-8') as f:
            for i, line in enumerate(f, 1):
                gold, txt = line.split("\t")
                txt = txt.rstrip("\n")
                self.data.append((i, gold, txt))
    
    def __iter__(self):
        return self.data
    
    def __next__(self):
       for root, dirs, files in os.walk(self.filepath):
           for filename in files:
               for row in open(filename, encoding="utf-8"):
                   yield row
    
def main():
    data_generator = DataGenerator(r"C:\Users\maria\OneDrive\Desktop\prog2\code\woche5\smsspamcollection\SMSSpamCollection")
    print(next(data_generator))
        
if __name__ == "__main__":
    main()