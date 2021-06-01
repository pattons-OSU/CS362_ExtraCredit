#! python3

"""
Simeon Patton
CS362 OSU Spring 2021
Extra Credit 3 - Array and target sum

--Write a program that takes an array of integers - array and an integer target_sum.
Your program should return an array containing two numbers that add up to the target.

    inspiration for array iteration can be found at https://tinyurl.com/cryw3wnj
"""

import math

def array_size():
    array_size = input("\nHow big would you like the array?\n")
    array_size = int(array_size)

    return array_size

def target_sum():
    target_sum = input("\nWhat would you like the target sum to be?\n")
    target_sum = int(target_sum)
    return target_sum


def add_to_array(array_size):
    num_array = []

    for i in range(0, array_size):
        add_to_array = input("\nPlease enter a number to add to the array:\n")
        add_to_array = int(add_to_array)
        num_array.append(add_to_array)
    
    return num_array


def pair_values(num_array, arr_size, sum):
 
    ## Creating empty list and iterating through user given array
    pair_list = []
    for i in range(0, arr_size):
        for j in range(i + 1, arr_size):
            if (num_array[i] + num_array[j] == sum):
                list_value = (num_array[i], num_array[j])
                pair_list.append(list_value)
                
    return pair_list


if __name__ == '__main__':
    arr_size = array_size()
    sum = target_sum()
    array = add_to_array(arr_size)
    pair_list = pair_values(array, arr_size, sum)
    print(f"\nYour entered array is {array}, and the value that these numbers must add up to is {sum}.\n")
    print(f"\nThe pair(s) from the given array that will sum to {sum} is/are {pair_list}.\n")
    