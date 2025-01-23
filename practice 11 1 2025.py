if command == "down":
    for i in range(board_size):
        idx= get_string_index(i, col_row_num, board_size)
        result += board[idx]

if command == "across":
    for i in range(board_size):
        idx= get_string_index(col_row_num, i, board_size)
        result += board[idx]
        
if command == "down_diagonal":
    for i in range(board_size):
        idx= get_string_index(i, i, board_size)
        result += board[idx]

if command == "up_diagonal":
    for i in range(board_size):
        idx= get_string_index(board_size - i - 1, i, board_size)
        result += board[idx]
        
return result