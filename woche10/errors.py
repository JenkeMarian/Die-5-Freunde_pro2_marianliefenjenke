# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:34:38 2021

@author: maria
"""

#Prog2
#Übung 10
#Error


class FeatureNotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
class ArgumentNotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
class PathNotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)