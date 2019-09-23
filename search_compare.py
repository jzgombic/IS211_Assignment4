#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import random


def sequential_search(a_list, item):
    """

    The function searches a list and returns a boolean value
    as to whether an item is present as well as the amount of
    time the search had taken.

    Args:
        a_list (list): List containing data to be searched.
        item (int): A value to be searched for in the given list.

    Returns:
        (Tuple): A tuple containing a boolean value if the value is
        present and the processing time in seconds.

    """

    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def ordered_sequential_search(a_list, item):
    """

    The function searches a list and returns a boolean value
    as to whether an item is present as well as the amount of
    time the search had taken.

    Args:
        a_list (list): List containing data to be searched.
        item (int): A value to be searched for in the given list.

    Returns:
        (Tuple): A tuple containing a boolean value if the value is
        present and the processing time in seconds.

    """

    a_list = sorted(a_list)

    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def binary_search_iterative(a_list, item):
    """

    The function searches a list and returns a boolean value
    as to whether an item is present as well as the amount of
    time the search had taken.

    Args:
        a_list (list): List containing data to be searched.
        item (int): A value to be searched for in the given list.

    Returns:
        (Tuple): A tuple containing a boolean value if the value is
        present and the processing time in seconds.

    """

    a_list = sorted(a_list)

    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


def binary_search_recursive(a_list, item):
    """

    The function searches a list and returns a boolean value
    as to whether an item is present as well as the amount of
    time the search had taken.

    Args:
        a_list (list): List containing data to be searched.
        item (int): A value to be searched for in the given list.

    Returns:
        (Tuple): A tuple containing a boolean value if the value is
        present and the processing time in seconds.

    """

    a_list = sorted(a_list)

    start_time = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()

    run_time = end_time - start_time

    return (run_time, found)


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

    Tests the four search algorithms by generating 100 test lists of three
    different sizes, calculates the average processing time for each search
    and returns the result in as a string.

    Args:
        None.

    Returns:
        (String): The average processing time for each search.

    """

    list_size = [500, 1000, 10000]
    search = {'Sequential': 0, 'Ordered': 0, 'Binary Iterative': 0, 'Binary Recursive': 0}

    for t_list in list_size:
        counter = 0
        while counter < 100:
            list_test = list_gen(t_list)
            search['Sequential'] += sequential_search(list_test, -1)[0]
            search['Ordered'] += ordered_sequential_search(list_test, -1)[0]
            search['Binary Iterative'] += binary_search_iterative(list_test, -1)[0]
            search['Binary Recursive'] += binary_search_recursive(list_test, -1)[0]
            counter += 1

        print 'For the list containing %s lines:' % (t_list)

        for st in search:
            print ('%s Search took %10.7f seconds to run, on average.') % (st, search[st] / counter)


if __name__ == '__main__':
    main()





























#Author: Johnny Zgombic
#Date: September 23, 2019
