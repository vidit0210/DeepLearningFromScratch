from typing import List
from typing import Callable
import numpy as np


def deriv(func: Callable[[ndarray], ndarray], input_: ndarray, delta: float = 0.001):
    """
    Evaluates the value of a function "func" at every element in the array 
    """
    return (func(input_+delta)-func(input_ - delta))/(2*delta)


# A Function takes in an ndarray as an argument and produces an ndarray
Array_Function = Callable[[ndarray], ndarray]

# A chain is a list of functions
Chain = List[Array_Function]


def chain_length_2(chain: Chain, a: ndarray) -> ndarray:
    """
    Evaluates two functions in a row, in a "Chain"
    """
    assert len(chain) == 2
    "The length of input chain should be 2"
    f1 = chain[0]
    f2 = chain[1]

    return f2(f1(x))
