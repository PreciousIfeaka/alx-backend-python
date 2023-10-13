#!/usr/bin/env python3
"""This module contains a function that takes a string and an int or float
   as arguments and returns a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''this function returns the square of the value argument'''

    return (k, v**2)
