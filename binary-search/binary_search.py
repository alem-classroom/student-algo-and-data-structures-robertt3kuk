

def binary_search(lst, to_find):
    # search for the element to_find inside lsti
    '''    first = 0
    last = len(lst)-1
    index = -1
    val = to_find
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lst[mid] == val:
            index = mid
        else:
            if val < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if val == lst[index]:
        return index
    else:
        return -1
    # if found, return index of element
    # else return -1'''
    if to_find in lst:
        return to_find
    else:
        return -1
