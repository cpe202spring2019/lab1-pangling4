
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

    # raises ValueError if list is None
    if int_list == None:
        raise ValueError
    # returns None, if list is empty
    if len(int_list) == 0:
        return None
    else:
        maxi = int_list[0]                      # creates maximum variable (maxi) and assigns it to first term in list
        for i in range(1, len(int_list), 1):    # iteration by from second term to last term in list (if there is one)
            if int_list[i] > maxi:              # compares terms one by one
                maxi = int_list[i]              # assigns term to maxi if it is greater than the last maxi
        return maxi                             # returns maxi once code iterates through entire list

    pass


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    # raises ValueError if list is None
    if int_list == None:
        raise ValueError
    else:
        rev_list = list()                               # creates reversed list
        index = len(int_list)-1                         # defines initial index
        return recursion(index, rev_list, int_list)     # calls recursion function
    pass


# helper function that reverse_rec uses for recursion through list
def recursion(index, rev_list, int_list):
    if index == -1:                              # base case: when code has recursed through list, rev_list is returned
        return rev_list
    else:
        rev_list.append(int_list[index])                # adds next entry of original list to end of recursive list
        return recursion(index-1, rev_list, int_list)   # recurses through original list backwards


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """

    # raises ValueError if list is None
    if int_list == None:
        raise ValueError

    # Defines middle index to reference to when using binary search
    mid = (low+high)//2

    if target < int_list[mid] and low != high:          # Finds if target is below the middle
        high = mid-1                                    # Adjusts high boundary of range of search
        return bin_search(target, low, high, int_list)  # Calls recursion, having narrowed down search range

    elif target > int_list[mid] and low != high:        # Finds if target is above
        low = mid+1                                     # Adjusts low boundary of range of search
        return bin_search(target, low, high, int_list)  # Calls recursion, having narrowed down search range

    elif target == int_list[mid]:                       # When target number equals certain number in list, return mid
        return mid

    else:                                               # In case the target number does not exist in code, return None
        return None
    pass

