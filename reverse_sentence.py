#! python3

"""
Simeon Patton
CS362 OSU Spring 2021
Extra Credit 1.1 - Reverse sentence program

--Write a program that reverses a sentence. Input - ask the user for a sentence:
a long string containing multiple words. Return to the user the same string,
with the words in backward order.

"""

def user_input():
    string = input("\nPlease enter a sentence that you would like reversed:\n")
    string = str(string)
    return string


def reverse_string(user_input):
    ## Breaking the string into individual words using
    ## a space as the delimiter
    split_words = user_input.split(' ')
    
    reversed_string = split_words[::-1]

    return reversed_string


if __name__ == '__main__':
    print(reverse_string(user_input()))