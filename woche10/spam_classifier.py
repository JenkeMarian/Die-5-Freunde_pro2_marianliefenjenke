# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:56:51 2021

@author: maria
"""

import numpy as np
import pandas as pd

from features import CharacterFeatures
from data_split import SplitData 
from woche10.errors import FeatureNotFoundError, ArgumentNotFoundError


class SpamClassifier:

    def __init__(self, train_dataframe):
        self.train_data = train_dataframe
        self.model = self.train_model()
        #feature column names + indices in the model
        self.feature_names = list(self.model.columns)[1:]
        self.feature_indices = list(range(1, len(self.model.columns)))

    def train_model(self):
        return self.train_data.groupby(["class_label"]).mean()

    def predict(self, test_dataframe, all_weights=1, output=False):
        predicted_labels = []
        
        
        # ham 
        v_ham = self.model.loc["ham"]
        print(v_ham)
        
        
        # spam
        v_spam = self.model.loc["spam"]
        for _, r in test_dataframe.iterrows():
            dist_ham = 0
            dist_spam = 0
            for i in self.feature_names:
              
                
                dist_ham += (abs(v_ham.loc[i] - r[i])) * all_weights
                dist_spam += (abs(v_spam.loc[i] - r[i])) * all_weights
            if dist_ham < dist_spam:
                predicted_labels.append("ham")
            else:
                predicted_labels.append("spam")
        return predicted_labels


if __name__ == '__main__':
    data = SplitData(r"C:\Users\maria\OneDrive\Desktop\prog2\code\woche6\smsspamcollection\SMSSpamCollection")
    train_data, val_data, test_data=data.split_whole_data
    cf=CharacterFeatures(train_data)
    train_features=cf.in_df()
    classifier = SpamClassifier(train_features)
    print(classifier.predict(train_features))
    
    