#! python3

"""
Simeon Patton
CS362 OSU Spring 2021
Extra Credit 3.2 - Pytest the target sum program

--Write tests for the target sum program using unittest and pytest. 
(do not run the tests with pytest alone - you should use pytest syntax as well.)

"""

import pytest
import target_sum

## Setting global variables
test_array_size = target_sum.array_size()
target_sum_test = target_sum.target_sum()
test_array_list = target_sum.add_to_array(test_array_size)


def test_input_array_type():
    assert type(test_array_size) == int

def test_input_sum_type():
    assert type(target_sum_test) == int

def test_add_to_array():
    assert len(test_array_list) == test_array_size


    

