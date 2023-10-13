#!/usr/bin/env python3
"""This module contains a function that takes a float as an argument and
   returns a function that multiplies a float by a multiplier.
"""

from typing import Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''this returns another function'''

    def mult_fxn(x: float) -> float:
        '''returns a float and it\'s to be returned by a function'''
        return x*multiplier
    return mult_fxn
