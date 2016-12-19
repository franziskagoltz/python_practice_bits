""" Remove duplicates in a list

For example::

    >>> remove_duplicates([6, 9, 7, 9, 2, 6, 0])
    [6, 9, 7, 2, 0]

    >>> remove_duplicates([])
    []

    >>> remove_duplicates([6, 9, 7])
    [6, 9, 7]

"""


def remove_duplicates(items):
    """Remove duplicates in the list items and return that list."""

    # keeoing track of individual items in order
    no_duplicates = []

    # using a set for faster look up of already seen items
    seen = set()

    if items:
        for item in items:
            if item not in seen:
                # adding to seen and appending to list to keep track of order
                no_duplicates.append(item)
                seen.add(item)

    return no_duplicates
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"



