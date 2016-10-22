#############################################################
# FILE: battleship.py
# WRITER : Leshem Choshen + borgr + 305385338
# EXERCISE : intro2cs ex4 200132014
# Description: Battleshipe game
#############################################################

"""Implement the following function according the description in ex4"""

def print_board(board):
    for ind in board:
        print(ind)

def new_board(width=10, height=None):
    """creates a new board game for a Battleship game.

    Args:
    -width: a positive int - the width of the board - default value 10
    -height: a positive int - the height of the board - if not spcified
    should be as width

    return: a NEW enpty board - each inner arrays is a list of 'None's.

    n case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    if height is None:
        height = width
    if height <= 0 or width <= 0:
        return
    ls = []
    for ind in range(height):
        ls.append(list(None for leng in range(width)))
    return ls
    
def place_ship(board, ship_length, bow, ship_direction):
    """Put a new ship on the board

    put a new ship (with unique index) on the board.
    in case of successful placing edit the board according to the definitions
    in the ex description.

    Args:
    -board - battleshipe board - you can assume its legal
    -ship_length: a positive int the length of the ship
    -bow: a tuple of ints the index of the ship's bow
    -ship_direction: a tuple of ints representing the direction the ship
    is facing (dx,dy) - should be out of the 4 options(E,N,W,S):
    (1,0) -facing east, rest of ship is to west of bow,
    (0,-1) - facing north, rest of ship is to south of bow, and etc.

    return: the index of the placed ship, if the placement was successful,
    and 'None' otherwise.

    In case of bad input: values are out of range returns None

     You can assume the board is legal. You can assume the other inputs
     are of the right form. You need to check that they are legal."""
    
    #Check if input is right
    if (ship_direction[0]*ship_direction[1] != 0 or
        abs(ship_direction[0]+ship_direction[1]) != 1 or
        ship_length < 1 or bow[0] < 0 or bow[1] < 0):
        return
    
    #Check if there is no ship and not out of bounds
    for ind in range(ship_length):
        x = bow[0] - ship_direction[0]*ind 
        y = bow[1] - ship_direction[1]*ind
        if (len(board) <= y or len(board[0]) <= x or
            x+y < abs(x)+abs(y) or board[y][x] is not None):
            return
              
    #looks for highest index
    indx = 0
    for y in board:
        for x in y:
            if x is not None and x[0] > indx:
                indx = x[0]
            
    #places the ship
    indx += 1
    list_length = [ship_length]
    for run in range(ship_length-1, -1, -1):
        x = bow[0] - ship_direction[0]*run 
        y = bow[1] - ship_direction[1]*run
        board[y][x] = (indx, run, list_length)
        run -= 1
    return indx


def fire(board, target):
    """implement a fire in battleship game

    Calling this function will try to destroy a part in one of the ships on the
    board. In case of successful fire destroy the relevant part
    in the damaged ship by deleting it from the board. deal also with the case
    of a ship which was completely destroyed

    -board - battleshipe board - you can assume its legal
    -target: a tuple of ints (x,y) indices on the board
    in case of illegal target return None

    returns: a tuple (hit,ship), where hit is True/False depending if the the
    shot hit, and ship is the index of the ship which was completely
    destroyed, or 0 if no ship was completely destroyed. or 0 if no ship
    was completely destroyed.

    Return None in case of bad input

    You can assume the board is legal. You can assume the other inputs
    are of the right form. You need to check that they are legal."""
    #ready - start variables
    x = target[0]
    y = target[1]

    #aim - check where you fire
    if (len(board) <= y or len(board[0]) <= x or
        x < 0 or y < 0):
        return

    #fire!
    if board[y][x] is None:
        return False, 0
    board[y][x][2][0] -= 1
    indx = board[y][x][0]
    if board[y][x][2][0] == 0:
        board[y][x] = None
        return True, indx
    board[y][x] = None
    return True, 0
