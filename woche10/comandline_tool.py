# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:46:00 2021

@author: maria
"""

#Prog2
#Übung 10
#ComadlineTool

import argparse
import numpy as np
import pandas as pd

from spam_classifier import SpamClassifier
from errors import ArgumentNotFoundError, PathNotFoundError
from data_split import SplitData

def comandline_tool():
    parser = argparse.ArgumentParser(prog = "Unterscheidet SpamNachrichten von nicht SpamNachrichten",
                                     usage = "Das Programm arbeitet mit 2 Argumenten, sowie einer Eingabedatei und einem Sprachmodell. \n ProgrammStart: spam_classifier.py path/to/input path/to/model",
                                     description = "Das Programm sagt für SMSNachrichten vorraus, ob es sich um SpamNachrichten oder nicht SpamNachrichten handelt." )
    parser.add_argument("-i", "--input", type=str, help="path to input data")
    parser.add_argument("-m", "--model", type=str, help="path to model")
    parser.add_argument("-f", "--features", type=str, help="features for training a model")
    args = parser.parse_args()
    SC = SpamClassifier(args.model, features=set(args.features.split()))
    SC.predict(pd.read_csv(args.input))
    
if __name__ == '__main__':
    comandline_tool()