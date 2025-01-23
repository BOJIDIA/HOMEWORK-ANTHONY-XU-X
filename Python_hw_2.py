from typing import Dict, List

# Difficulties: 
# Easy -> Should be doable
# Medium -> Challenging
# Hard -> I will be happy if you can do these!
# Extra -> EXTREMELY DIFFICULT


# Difficulty: Easy
def zigzagzip(s1: str, s2: str) -> str:
    """ 
    Precondition: len(s1) == len(s2)
    
    Return a string made up of alternating letters from s1 and s2,
    starting with s1[0], then s2[1], s1[2], and so on
    
    >>> zigzagzip('abc', '123')
    'a2c'
    >>> zigzagzip('abcd', '1234')
    'a2c4'
    """
    pass  # erase this and write the function body


# Difficulty: Easy
def is_palindrome(s: str) -> bool:
    """Return True if and only if s is a palindrome.
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """
    pass  # erase this and write the function body


# Difficulty: Easy
def get_num_orders(meal_to_tables: Dict[str, List[int]], meal: str) -> int:
    """
    Return the number of orders for meal in meal_to_tables. 
    The values in the dictionary represents table numbers. 
    For example, {'stew': [4, 1], 'eggs': [6]} means table 4 and 1 ordered stew
    while table 6 ordered eggs.
    
    >>> m_to_t = {'stew': [4, 1], 'eggs': [6]}
    >>> get_num_orders(m_to_t, 'stew')
    2
    >>> get_num_orders(m_to_t, 'eggs')
    1
    >>> get_num_orders(m_to_t, 'brussel sprouts')
    0
    """
    pass


# Difficulty: Medium
def get_column(board: List[List[str]], column_num: int) -> List[str]:
    """Return column column_num of board.
    >>> b = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    >>> get_column(b, 0)
    ['a', 'd', 'g']
    >>> get_column(b, 2)
    ['c', 'f', 'i']
    """
    pass  # erase this and write the function body




# Difficulty: Medium
def count_duplicates_v1(lst: List[int]) -> int:
    """Return the number of duplicates in lst.
    
    Precondition: each item in lst occurs either once or twice.
    
    >>> count_duplicates_v1([1, 2, 3, 4])
    0
    >>> count_duplicates_v1([2, 4, 3, 3, 1, 4])
    2
    """
    pass  # erase this and write the function body


# Difficulty: Medium
def get_positions(text: str) -> Dict[str, List[int]]:
    """ 
    Return a dictionary where the keys are the individual words in text, and
    the values are the positions in the text where the words occur (starting
    at 1). Include punctuation and numbers in words, and convert alphabetic
    characters to lowercase.
    
    >>> result = get_positions('cats Cats CATS CATS!!!')
    >>> result == {'cats': [1, 2, 3], 'cats!!!': [4]}
    True
    >>> result = get_positions('I think I like CSC108.')
    >>> result == {'i': [1, 3], 'think': [2], 'like': [4], 'csc108.': [5]}
    True
    """
    # hint: use .split()
    pass  # erase this and write the function body


# Difficulty: Hard
def truncate_and_accumulate(values) -> float:
    """
    Modify values so that each number is rounded down to the nearest integer
    value, and return the accumulated lost amount.
    
    >>> values = [1, 2.5, 3.3, 4.01]
    >>> truncate_and_accumulate(values)
    0.81
    >>> values
    [1, 2, 3, 4]
    >>> values = [0.25, 0.5, 0, 1, 33]
    >>> truncate_and_accumulate(values)
    0.75
    >>> values
    [0, 0, 0, 1, 33]
    >>> values = [10, 15, 20]
    >>> truncate_and_accumulate(values)
    0.0
    >>> values
    [10, 15, 20]
    """
    pass  # erase this and write the function body


# Difficulty: Extra
def find_population(continent_info: Dict[str, Dict[str, Dict[str, int]]]) -> Dict[str, int]:
    """ 
    Precondition: continent_info has keys representing continents, and the
    values are dictionaries where the keys represent countries on that
    continent and the values are dictionaries where the keys represent cities
    in that country and the values represent city populations.
    
    Return a dictionary where the keys are continents from continent_info
    and the values are the total population of all cities on that continent.
    
    >>> data = {'Europe': {'France': {'Paris': 100, 'Nice': 50, 'Lyon': 4}, \
    'Bulgaria': {'Sofia': 3000}}}
    >>> result = find_population(data)
    >>> result == {'Europe': 3154}
    True
    >>> data = { \
    'North America': {'Canada': {'Toronto': 5000, 'Ottawa': 200}, \
    'USA': {'Portland': 400, 'New York': 5000, 'Chicago': 1000}, \
    'Mexico': {'Mexico City': 10000}}, \
    'Asia': {'Thailand': {'Bangkok': 456}, \
    'Japan': {'Tokyo': 10000, 'Osaka': 5000}}, \
    'Antarctica': {}}
    >>> result = find_population(data)
    >>> result == {'North America': 21600, 'Asia': 15456, 'Antarctica': 0}
    True
    """
    pass  # erase this and write the function body