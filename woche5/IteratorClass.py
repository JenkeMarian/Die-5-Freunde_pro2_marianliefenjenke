# -*- coding: utf-8 -*-
"""
Created on Mon May 17 09:03:13 2021

@author: maria
"""

# Marian Liefen Jenke
# Prog 2
# Übung 5


class DataIterator:
    
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
        if self.i < len(self.data):
            self.i = self.i+1
            return self.data[self.i-1]
        else: 
            raise StopIteration
    
def main():
    data_iterator = DataIterator(r"C:\Users\maria\OneDrive\Desktop\prog2\code\woche5\smsspamcollection\SMSSpamCollection")
    print(next(data_iterator))
        
if __name__ == "__main__":
    main()