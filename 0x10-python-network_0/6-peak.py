#!/usr/bin/python3
"""has function find_peak"""


def find_peak(list_of_integers):
    """finds the peak in a list of integers unsorted"""
    list_int = list_of_integers
    l = len(list_int)
    if l == 0:
        return
    mid = l // 2
    if (mid == l - 1 or list_int[mid] >= list_int[mid + 1]) and (mid == 0 or list_int[mid] >= list_int[mid - 1]):
        return list_int[mid]
    if mid != l - 1 and list_int[mid + 1] > list_int[mid]:
        return find_peak(list_int[m + 1:])
    return find_peak(list_int[:mid])
