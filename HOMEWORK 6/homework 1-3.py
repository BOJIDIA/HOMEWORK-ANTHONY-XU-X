# Difficulty: Easy
def zigzagzip(s1: str, s2: str) -> str:
    """ 
    Condition: len(s1) == len(s2)

    Combine s1 and s2 by alternating letters, starting with s1[0].

    >>> zigzagzip('abc', '123') -> 'a2c'
    >.> zigzagzip('abcd', '1234') -> 'a2c4'
    """
    for a, b in zip(s1, s2):
           result += a + b
       return result    

# Difficulty: Easy
def palindrome(s: str) -> bool:
    """
    Determine if a string is a palindrome.

    >>> palindrome('noon') -> True
    >>> palindrome('racecar') -> True
    >>> palindrome('dented') -> False
    """ 
        if s[left] = s[right]
            return True
    return False    

# Difficulty: Easy
def get_num_orders(meal_to_tables: Dict[str, List[int]], meal: str) -> int:
    """
    Find the number of orders for a specified meal based on table data.

    - m_to_t = {'stew': [4, 1], 'eggs': [6]}
      get_num_orders(m_to_t, 'stew') -> 2
      get_num_orders(m_to_t, 'eggs') -> 1
      get_num_orders(m_to_t, 'brussel sprouts') -> 0
    """
    return len(meal_to_tables.get(meal, []))