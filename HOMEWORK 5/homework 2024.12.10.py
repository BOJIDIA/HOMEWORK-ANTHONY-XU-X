# TODO: Complete/create the functions

from typing import List

# Question 1
def for_grading(grade: float, req_grade: float) -> bool:
    """
    Return True if and only if grade is greater than or equal to req_grade.
    
    >>> for_grading(95, 80)
    True
    >>> for_grading(30, 90)
    False
    >>> for_grading(80, 80)
    True
    """
    if grade >= req_grade:
        return True
    return False    


# Question 2
def is_ae(msg: str) -> bool:
    """
    Return True if and only if msg begins with the letter a or A, followed by "aeAE".
    This function is case insensitive (i.e., treat "a" and "A" the same).
    
    >>> is_ae("aA!!!")
    True
    >>> is_ae("Ea")
    False
    >>> is_ae("Ea")
    False
    """
    if msg[0] in "aA" and msg[1] in "aeAE":
        return True
    return False    


# Question 3
# make a function that checks if a given string contains "x"
def contains_x(x: str) -> bool:
    '''
    Return True if the string contains x. In this case, x and X are not the same.
    >>> contains_x("xyz")
    True
    >>> contains_x("abc")
    False
    >>> contains_x("abx")
    True
    '''
    for char in x:
        if char == "x":  
            return True
    return False





   

