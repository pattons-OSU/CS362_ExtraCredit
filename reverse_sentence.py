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
    string = input("\nPlease enter a sentence that you would like reversed:\n\n")
    string = str(string)
    return string


def reverse_string(user_input):
    ## Breaking the string into individual words using
    ## a space as the delimiter
    split_words = user_input.split(' ')
    ## Reversing the list of strings
    reversed_string = split_words[::-1]
    return reversed_string

def merge_reversed(reversed_string):
    word_list = reversed_string
    deliminator = ' '
    ## Using .join method to concantinate into a new string
    merged_string = deliminator.join(word_list)
    return merged_string


if __name__ == '__main__':
    string_input = user_input()
    separated_reversed_list = reverse_string(string_input)
    concantinated_reversed_list = merge_reversed(separated_reversed_list)
    print("\nYour reversed sentence is:\n\n")
    print(concantinated_reversed_list)
    print("\n")