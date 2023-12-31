#!/usr/bin/python3
'''
function that prints a text with 2 new lines after
each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    print 2 new lines after ?, ., :
    '''
    check = True
    i = 0
    if type(text) is not str:
        raise TypeError("text must be a string")

    for lett in text:
        if lett == "?" or lett == "." or lett == ":":
            print(lett)
            print()
            check = False
        else:
            if check:
                print(lett, end="")
            elif text[i + 1] != " ":
                print(lett.strip(), end="")
                check = True
        i += 1
