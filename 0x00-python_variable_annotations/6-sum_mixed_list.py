#!/usr/bin/env python3
"""This mmodule takes a list of integers and floats and returns
   their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''sums a list and returns a float'''
    return sum(mxd_lst)
