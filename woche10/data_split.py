# -*- coding: utf-8 -*-
"""
Created on Sun May 30 14:02:03 2021

@author: maria
"""

import pandas as pd
import re



from sklearn.model_selection import train_test_split
from features import CharacterFeatures
from woche10.errors import FeatureNotFoundError, ArgumentNotFoundError

class SplitData:
    
    def __init__(self, path):
        self.filepath = path
        self.data = self.data_dataframe()
        self.i = 0
        self.split_whole_data = self.data_split()
        #self.features(self.train_data)
        #self.train_data_CharacterFeatures = self.features(self.training_data)
        
    def data_dataframe(self):
        data = []
        with open(self.filepath, 'r', encoding= 'utf-8') as f:
            for i, line in enumerate(f, 1):
                gold, txt = line.split("\t")
                txt = txt.rstrip("\n")
                data.append((i, gold, txt))

        df = pd.DataFrame(data=data, columns=(["ID", "class_label", "text"]))
        df.set_index("ID", inplace=True)
        return df
    
    
         
    def data_split(self):
    
        train = 0.5
        validation = 0.2
        test = 0.3
        
        train_data, test_data = train_test_split(self.data, test_size = 1 - train, random_state = 42)
        val_data, test_data = train_test_split(test_data, test_size = test/(test + validation), random_state = 42)
        print(self.data)
        
        train_data.to_csv("training_data.csv", encoding="utf-8")
        test_data.to_csv("testing_data.csv", encoding="utf-8")
        val_data.to_csv("validation_data.csv", encoding="utf-8")
        
        return train_data, val_data, test_data
    
        
        
                
def main():
    filepath = r"C:\Users\maria\OneDrive\Desktop\prog2\code\woche6\smsspamcollection\SMSSpamCollection"
    split_whole_data = SplitData(filepath)
    print(split_whole_data.data_split())
        
if __name__ == "__main__":
    main()
    
    