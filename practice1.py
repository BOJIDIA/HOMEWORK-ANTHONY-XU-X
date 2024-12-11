def count_even(lst: list) -> int:
    """
    Count the number of even numbers inside a list<list>
    
    Precondition: the elements inside the list are all integers
    
    >>> count_even([1, 2, 3, 4, 4, 6])
    3
    
    >>> count_even([100, 1000, 10000, 100000])
    4
    """
    
    count =0 
    for num in lst:
        if num % 2 == 0:
            count += 1 # count = count + 1
    return count


# create a function counts the number of elements that are valid DNA sequences
# a valid DNA sequences means a string with characters "T", "A", "C", "G" only

def count_valid_DNA(list: list) -> int:
    """
    
    Return the number 