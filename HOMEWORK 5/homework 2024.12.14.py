# Question 4 - Difficulty - MEDIUM

def is_eligible_for_award_v2(gpa: float, major: str, 
                             req_gpa: float, req_major: str) -> bool:
    """
    Return True if and only if gpa is greater than or equal to req_gpa and 
    major is equal to req_major.
    
    >>> is_eligible_for_award_v2(3.0, 'CS', 3.5, 'CS')
    False
    >>> is_eligible_for_award_v2(4.0, 'Econ', 3.6, 'CS')
    False
    >>> is_eligible_for_award_v2(3.3, 'CS', 3.5, 'CS')
    False
    >>> is_eligible_for_award_v2(3.5, 'CS', 3.4, 'CS')
    True
    """
    pass 


# Question 5 Difficulty - HARD

def row(board: List[List[str]], row_num: int) -> List[str]:
    """
    Return row <row_num> of <board>
    
    >>> b = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    >>> row(b, 0)
    ['a', 'b', 'c']
    >>> row(b, 1)
    ['d', 'e', 'f']
    >>> row(b, 2)
    ['g', 'h', 'i']
    """
    pass 


# Question 6 Difficulty - EASY

def contains_names(lst: list) -> bool:
    """
    Return True if the list contains any of the names: "Alice", "Daniel", "Anthony", or "Minsoo".
    
    >>> x = ["London", "Chemistry", "Math"]
    >>> contains_names(x)
    False
    >>> x = ["Sydney", "Math", "Daniel"]
    >>> contains_names(x)
    True
    """
    pass