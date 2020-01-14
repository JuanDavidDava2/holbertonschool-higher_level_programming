#!/usr/bin/python3
'''
prints a square with the character #.
'''


def print_square(size):
    '''
    prints a square with the character #.
    '''

    '''check if size is an integer'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    '''check if size is less that zero'''
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
