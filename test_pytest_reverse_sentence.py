#! python3

"""
Simeon Patton
CS362 OSU Spring 2021
Extra Credit 1.2.1 - Unittest the Reverse sentence program

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

class testCase():
    """
    @pytest.fixture
    def user_input():
        user_input = reverse_sentence.user_input()
        reversed_input = reverse_sentence.reverse_string(user_input)
        return reversed_input, user_input
    """
    ## Testing to make sure that the user is passing through a
    ## String that is capable of being reversed.
    def test_input_type(self):
        assert type(user_input) == str
        ##self.assertTrue(type(user_input), str)
    ## Testing to make sure that the reversing function is actually
    ## doing the correct function.
    def test_reversing(self):
        ##self.assertEqual(user_input.split(' ')[::-1], reversed_input)
        assert user_input.split(' ')[::-1] == reversed_input

