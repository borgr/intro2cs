#############################################################
# FILE : GetToTheZero.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex1 200132014
# DESCRIPTION: A function that checks if a normal human
#              being can pass the board.
#############################################################


def is_solvable_new_board(start, board):
    """ This function checks if a normal human
    being can pass the board.

    Args:
    start - a position on the board, non negative int.
    board - a list with the possible steps (positive ints)
    from each cell(room) and a 0 in the last cell
    representing the goal.

    Return:
    True if the boaed is passable
    otherwise False
    Note that this function changes the board it gets.
    """
    if start < 0 or start >= len(board):
        return False
    move = board[start]
    board[start] = -float("inf")
    if move == 0:
        return True
    if move < 0:
        return False
    if (is_solvable(start + move, board) or
            is_solvable(start - move, board)):
        return True
    return False
    
    
def is_solvable(start, board):
    """ This function that checks if a normal human
    being can pass the board.

    Args:
    start - a position on the board, non negative int.
    board - a list with the possible steps (positive ints)
    from each cell(room) and a 0 in the last cell
    representing the goal.

    Return:
    True if the boaed is passable
    otherwise False
    """
    # If needed, a slower yet using less memory function can
    # be made with one function that multiplies visited cells by -1
    # and at the end corrects the whole list using abs().
    
    board = board[:]  
    return is_solvable_new_board(start, board)
