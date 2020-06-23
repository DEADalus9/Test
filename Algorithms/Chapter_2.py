#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:47:13 2020

@author: vladislav
CHOOSE SORT
"""

def find_smallest(array):
    """
    Resturns smallest element index in a list

    Parameters
    ----------
    array : TYPE
        List where to find smallest.

    Returns
    -------
    smallest_index : TYPE
        Index of smallest element.

    """
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def find_highest(array):
    """
    Returns highest element index in a list

    Parameters
    ----------
    array : TYPE
        List where to find highest.

    Returns
    -------
    highest_index : TYPE
        Index of highest element.

    """
    highest = array[0]
    highest_index = 0
    for i in range(1, len(array)):
        if array[i] > highest:
            highest = array[i]
            highest_index = i
    return highest_index


def choose_sort(array, direction = 'asc'):
    """
    Sorts list by ascending or descending

    Parameters
    ----------
    array : TYPE
        List to sort .
    direction : TYPE, optional
        Direction for sort.
        'asc' == ascending
        'dsc' == descending
        The default is 'asc'.

    Returns
    -------
    result : TYPE
        Sorted list.

    """
    result = []
    for i in range(len(array)):
        if direction == 'asc':
            smallest = find_smallest(array)
            result.append(array.pop(smallest))
        elif direction == 'dsc':
            highest = find_highest(array)
            result.append(array.pop(highest))
    return result


print(choose_sort([5, 3, 6, 2, 10], 'dsc'))



