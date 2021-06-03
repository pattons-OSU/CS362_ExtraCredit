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
test_target_sum = target_sum.target_sum()
test_array_list = target_sum.add_to_array(test_array_size)
test_pair_value = target_sum.pair_values(test_array_list, test_array_size, test_target_sum)


def test_input_array_type():
    assert type(test_array_size) == int

def test_input_sum_type():
    assert type(test_target_sum) == int

def test_add_to_array():
    assert len(test_array_list) == test_array_size

def test_pair_vs_sum():
    assert test_pair_value[0][0] + test_pair_value[0][1] == test_target_sum

    

