#!/usr/bin/python3
'''
prints a text with 2 new lines after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each of these characters: ., ? and :
    '''

    '''check if text is a string'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i == ':' or i == '.' or i == '?':
            print(i)
            print()
        else:
            print(i, end='')
