# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:59:53 2021

@author: maria
"""

# Prog 2
# Übung 10
# Marian Liefen Jenke

from spam_classifier import SpamClassifier
from data_split import SplitData

######################################################################################################################################

class Evaluation:

    def __init__(self, data, gold):
        self.true = 0
        self.accuracy()
        self.gold = gold
        self.data = data

    def accuracy(self):
        for x, y in self.data.iterrows():
            if x["class_label"] == self.gold.loc[y, "class_label"]: self.true += 1
        print(self.true/len(self.data))
        
        
    def __str__(self):
        print(f"{self.true} von {len(self.data)} Labels wurden korrekt dentifiziert.\nIn Prozent: {round(self.accuracy()*100,2)}%")

######################################################################################################################################

if __name__ == '__main__':
    data = SplitData(r"C:\Users\maria\OneDrive\Desktop\prog2\code\woche6\smsspamcollection\SMSSpamCollection")
    train_data=data.split_whole_data
    test = data=data.split_whole_data
    classifier = SpamClassifier(train_data)
    predicted = classifier.predicted_labels(test, output=True)
    eval = Evaluation(predicted, data.test_data)
    print(eval)