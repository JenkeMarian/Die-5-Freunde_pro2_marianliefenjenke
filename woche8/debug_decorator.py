# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:30:39 2021

@author: maria
"""

#Prog2
#Übung 8
# Marian Liefen Jenke

import logging 
import functools

# erstellen der log Datei
def get_logger(filename = "output.logger"):

    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s:%(funcName)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

# wrap und log Aufruf
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        logger = get_logger(filename=f'output_{func.__name__}.logger')
        logger.debug(f'Calling {func.__name__}...')
        logger.debug(str(func(*args, **kwargs)))
        return func(*args, **kwargs)
    
    return wrapper
