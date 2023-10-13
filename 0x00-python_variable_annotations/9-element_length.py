#!/usr/bin/env python3
"""This module annotates the below function parameters and returns values with
   the appropriate types
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a sequential tuple'''
    return [(i, len(i)) for i in lst]
