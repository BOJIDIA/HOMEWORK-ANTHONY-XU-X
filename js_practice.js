Convert Python Codes to JavaScript Codes

This is mainly to practice the syntax of JavaScript Language

There must be aspects that you might not know. Please ask!!!

// Convert Python Codes to equivalent JavaScript Code
// This is also a good opportunity to study Python Codes


/* Question 1

def is_eligible_for_award(grade: float, req_grade: float) -> bool:
    return grade >= reqGrade

/*

1.
function isEligibleForAward(grade, reqGrade) {
    return grade >= reqGrade;
}

2.
const isEligibleForAward = (grade, reqGrade) => {
    return grade >= reqGrade;
}

3.
const isEligibleForAward = (grade, reqGrade) => grade >= reqGrade;



/* Question 2

def is_yes(msg: str) -> bool:
    vowel = "aeiou"
    if msg[0] == "y" or msg[0] == "Y":
        if msg[1] in vowel:
            return True
    return False

/*

1. 
function isYes(msg) {
    var vowel = "aeiou";
    if (msg[0] === "y" || msg[0] === "Y") {
        if (vowel.includes(msg[1])) {
            return true;
        }
    }
    return false;
}

2.
const isYes = (msg) => {
    var vowel = "aeiou";
    return (msg[0] === "y" || msg[0] === "Y") && vowel.includes(msg[1]);
}

3.
const isYes = (msg) => (msg[0] === "y" || msg[0] === "Y") && vowel.includes(msg[1]);




/* Question 3

def get_row(board: List[List[str]], row_num: int) -> List[str]:
    return board[row_num]
*/

1.
function getRow(board, rowNum) {
    return board[rowNum];
}

2.
const getRow = (board, rowNum) => {
    return board[rowNum];
}

3.
const getRow = (board, rowNum) => board[rowNum];




/* Question 4

def count_duplicates_v1(lst: List[int]) -> int:
    count = 0
    temp = []
    for num in lst:
        if num in temp:
            count += 1
        else:
            temp.append(num)
    return count
*/

1.
function countDuplicatesV1(lst) {
    var count = 0
    var temp = []
    for 
    
}









/* Question 5 (Challenge!)

def find_population(continent_info: Dict[str, Dict[str, Dict[str, int]]]) -> Dict[str, int]:
    result = {}
    for continent_key, continent_value in continent_info.items():
        continent_population = 0
        for country_value in continent_value.values():
            for city_value in country_value.values():
                continent_population += city_value
        result[continent_key] = continent_population
    return result
*/

