#! python3

"""
Simeon Patton
CS362 OSU Spring 2021
Extra Credit 1.2 - Unittest and pytest the Reverse sentence program

--Write tests for the reverse_sentence program using unittest and pytest. 
(do not run the tests with pytest alone - you should use pytest syntax as well.)

"""

import unittest
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

class testCase(unittest.TestCase):
    ## Testing to make sure that the user is passing through a
    ## String that is capable of being reversed.
    def test_input_type(self):
        self.assertTrue(type(user_input), str)
    ## Testing to make sure that the reversing function is actually
    ## doing the correct function.
    def test_reversing(self):
        self.assertEqual(user_input.split(' ')[::-1], reversed_input)


if __name__ == '__main__':
    unittest.main()