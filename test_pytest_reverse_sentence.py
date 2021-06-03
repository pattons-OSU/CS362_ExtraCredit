#! python3

"""
Simeon Patton
CS362 OSU Spring 2021
Extra Credit 1.2.2 - Pytest the Reverse sentence program

--Write tests for the reverse_sentence program using unittest and pytest. 
(do not run the tests with pytest alone - you should use pytest syntax as well.)

"""

import pytest
import reverse_sentence

## Could not get the pytest fixtures working correctly.
## as of this moment, you need to run pytest with the -s
## flag in order to obtain user input.
"""
@pytest.fixture
def user_input():
    user_input = reverse_sentence.user_input()
    return user_input

@pytest.fixture
def reversed_input():
    reversed_input = reverse_sentence.reverse_string(user_input)
    return reversed_input
"""

## Setting global variables
user_input = reverse_sentence.user_input()
reversed_input = reverse_sentence.reverse_string(user_input)

def test_input_type():
    assert type(user_input) == str
def test_reversing():
    assert user_input.split(' ')[::-1] == reversed_input
