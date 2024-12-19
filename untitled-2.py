# for loop
# this runs until it reaches to the end or termination in the middle.
# specific command "break" it called
# 






# i=0
#b while i < something:
#     do the job
#     i = i + 1




for i in rnage ((
    
    
    
i=0



# make a function that counts 

def add_num(lst: List [int]) -> int:
    """
    Calculate the sum of the numbers that are in odd index of <lst>
    
    >>> add_num([1, 2, 3, 4, 5, 6, 7])
    12
    >>> add_num([-1, 1, -1, 1, -1, 1, -1, 1])
    4
    """
    #Try while loop!
    #total = 0
    #for i in range(len(lst))
    #    if i % 2 == 1：
    #        toatal += lst[i]
    # return total
    
    total = 0
    i = 1
    while i < len(lst)
        total += lst[i]
        i += 2
    return total

# List <==> Array, Dictionay <==> Hashmap
# => abstract data types

# {key1: value1, key2: value2, key3
    
    
def count_perfect(student_dct: Dict[str , int]) -> int:
    """
    Count the number of people in <student_dct> who received a perfect grade (100)\
    
    >>> count_perfect({"Alice": 99, "Sean": 100})
    1
    >>> count_perfect({"Alice": 100, "Anthony" : 100, "Daniel": 98, "Minsoo": 100})
    3
    """
    
    count = 0
    for value in student_dct.values()
        if value == 100:
            count += 1
    return count

def check_login(login_attempt: Dict[str , str], database: Dict[str, List[str]]) -> bool:
    """
    Check if the account information in login_attempt exist in database
    with a matching password
    
    Precondition: both dictionaries have two keys which are 
                  account_name and password
                  
    >>> db = {"account_name": ["aki
    
    
def mut_string_to_string(L: List[str]) -> str:
    """
    Given a list of chars <L>, returns a string which matches the contents
    of <L>.
    
    >>> lst = ["a", "c", "d"]
    >>> mut_string_to_string(lst)
    "acd"
    
    >>> x = ["A", "B", "C", "d"]
    >>> mut_string_to_string(x)
    "ABCd"
    """
    
    lst=
    
    