from tkinter import W


def binary_search(lst, to_find):
    # search for the element to_find inside lst
    if to_find in lst:
        return lst.index(to_find)
    else:
        return lst.index(to_find-1)
    # if found, return index of element
    # else return -1
