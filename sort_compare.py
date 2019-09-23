#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import random


def insertion_sort(a_list):
    """

    An algorithm which sorts a list and returns the sorted list as well
    as the amount of time the sort had taken.
    
    Args:
        a_list (list): A list of any data type.

    Returns:
        (tuple): A tuple containing the sorted list as well as the
        amount of time the sort had taken.

    """
    
    start_time = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, a_list)


def gap_insertion_sort(a_list, start, gap):
    """

    An algorithm that sorts a list using the GAP INSERTION method.
    
    Args:
        a_list (list): List containing data to be sorted.
        start (int): The starting position for the sub-list.
        end (int): The end position for the sub-list.

    Returns:
        N/A

    """

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def shell_sort(a_list):
    """

    An algorithm that sorts a list using the SHELL SORT method.
    
    Args:
        a_list(list): List containing data to be sorted.

    Returns:
        (tuple): A tuple containing the sorted list as well as the
        amount of time the sort had taken.

    """
    
    start_time = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, a_list)


def python_sort(a_list):
    """

    An algorithm that sorts a list using the PYTHON SORT method.

    Args:
        a_list(list): List containing data to be sorted.

    Returns:
        (tuple): A tuple containing the sorted list as well as the
        amount of time the sort had taken.

    """
    
    start_time = time.time()

    a_list.sort()

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, a_list)


def list_gen(value):
    """

    Generates a list of random values.

    Args:
        value (int): An integer representing the number of values in the list.

    Returns:
        sample_list (list): A list of integers in random order.
        The list length is based on the value argument.

    """

    sample_list = random.sample(xrange(1, (value + 1)), value)
    return sample_list


def main():
    """

    Tests the three sort functions by generating 100 test lists of three
    different sizes, calculates the average processing time for each search
    and returns the result in as a string.

    Args:
        None.

    Returns:
        (String): The average processing time for each search.

    """

    list_size = [500, 1000, 10000]
    sort = {'Insertion': 0, 'Shell': 0, 'Python': 0}

    for t_list in list_size:
        counter = 0
        while counter < 100:
            list_test = list_gen(t_list)
            sort['Insertion'] += insertion_sort(list_test)[0]
            sort['Shell'] += shell_sort(list_test)[0]
            sort['Python'] += python_sort(list_test)[0]
            counter += 1

        print 'For the list containing %s lines:' % (t_list)

        for st in sort:
            print ('The %s Search took %.5f seconds to run.') % (st, sort[st] / counter)


if __name__ == '__main__':
    main()





























#Author: Johnny Zgombic
#Date: September 23, 2019
