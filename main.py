from tabulate import tabulate
from gui import getGrid
import cv2
import time
import argparse
import sys

parser = argparse.ArgumentParser(description='ddqn')
parser.add_argument('--ani', action="store_true",help='Option to animate.')
parser.add_argument('--speed', type=int, default=1000, help='Speed of animation')
parser.add_argument('--size', type=int, default=3, help='Size of grid. Available options 3,4')
args = parser.parse_args()


def convertGrid():
    for i in range(args.size * args.size):
        for j in range(args.size * args.size):
            if sudoku_board[i][j] == 'A': sudoku_board[i][j] = 10 
            if sudoku_board[i][j] == 'B': sudoku_board[i][j] = 11 
            if sudoku_board[i][j] == 'C': sudoku_board[i][j] = 12 
            if sudoku_board[i][j] == 'D': sudoku_board[i][j] = 13 
            if sudoku_board[i][j] == 'E': sudoku_board[i][j] = 14 
            if sudoku_board[i][j] == 'F': sudoku_board[i][j] = 15 
            if sudoku_board[i][j] == 'G': sudoku_board[i][j] = 16 


def printText(sudoku_board):
    if args.size == 4:
        bg = cv2.imread('grid16x16.jpg')
        convertGrid()
    else:
        bg = cv2.imread('grid3x3.jpg')
    window_name = 'Sudoku'
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color = (0, 0, 0)
    start = (50,90)
    thickness = 2
    space = 79
    for y in range(args.size*args.size):
        for x in range(args.size*args.size):
            if sudoku_board[y][x] == 0:
            	num = ' '
            else:
                num = str(sudoku_board[y][x])
            if sudoku_board[y][x] == 10: num = 'A'
            if sudoku_board[y][x] == 11: num = 'B'
            if sudoku_board[y][x] == 12: num = 'C'
            if sudoku_board[y][x] == 13: num = 'D'
            if sudoku_board[y][x] == 14: num = 'E'
            if sudoku_board[y][x] == 15: num = 'F'
            if sudoku_board[y][x] == 16: num = 'G'

            image = cv2.putText(bg, num, (50+x*space,90+y*(space-1)), font, fontScale, color, thickness, cv2.LINE_AA)

    if args.size == 4:
        scale_percent = 50 # percent of original size
        width = int(bg.shape[1] * scale_percent / 100)
        height = int(bg.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        bg = cv2.resize(bg, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow(window_name, bg)  
    cv2.waitKey(1)
    time.sleep(float(1/args.speed))


# A 9x9 matrix which represents our sudoku solver
sudoku_board_3 = [
    [0,9,0,0,0,1,2,0,8],
    [7,0,0,8,0,0,0,6,0],
    [0,0,8,0,0,3,0,1,0],
    [8,6,0,7,9,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,5,0,0,0,0,0,0,3],
    [0,0,0,0,0,0,0,4,0],
    [0,0,0,0,6,9,0,0,0],
    [4,0,7,0,5,0,0,0,0]
]

# A 16x16 matrix which represents our sudoku solver
sudoku_board_4 = [
    [3,0,9,0,'D',6,0,'A',0,0,0,0,0,2,0,0],
    [8,0,0,'A',0,9,'C',0,0,6,1,'D',0,0,0,5],
    [0,0,'F',0,0,0,0,0,3,0,'G','E',8,0,'A','D'],
    [2,0,5,0,3,0,0,0,0,0,4,8,1,0,6,0],

    [6,0,'C',3,9,0,'E',4,0,8,0,0,5,0,'D','B'],
    [1,9,0,2,0,0,3,0,'B','D',6,5,0,8,'E','F'],
    [0,0,'E',5,8,0,'B',0,0,0,0,'G',9,4,2,0],
    ['B',0,'D',0,2,1,5,6,0,4,0,'F','G',0,'C',0],

    [9,3,1,0,'E','A',0,7,6,0,0,0,'B',0,'F',8],
    [0,'F',0,'E',0,'C',4,8,0,9,2,0,0,3,5,7],
    [4,2,0,'B',0,5,'D',1,0,0,0,0,0,0,0,0],
    [0,0,0,0,'F',0,9,'B',0,0,'E','A',0,0,1,0],

    [0,5,0,0,0,'D',0,0,0,0,8,1,6,0,0,0],
    ['E',0,0,4,0,8,0,'F','A','B',0,0,0,5,3,1],
    [0,'D',0,0,0,2,1,0,0,0,7,0,0,'G',0,'E'],
    [0,1,8,'C',5,0,0,0,'F',3,'D',0,4,7,9,'A']
]

if args.size in (3,4):
    print(f'Starting with grid size{args.size*args.size}x{args.size*args.size}')
    if args.size == 4:
        sudoku_board = sudoku_board_4
        convertGrid()
    else:
        sudoku_board = getGrid()
else:
    print(f'There is no Setting for {args.size*args.size}x{args.size*args.size}')
    sys.exit(0)

# Display the board
def display_board(sudoku_board):
    print(tabulate(sudoku_board, tablefmt='fancy_grid'))


#Look for an unassigned cell if it exists return row and col values else return False
def empty_cells_exist():
    for i in range(args.size * args.size):
        for j in range(args.size * args.size):
            if sudoku_board[i][j] == 0:
                return [i, j]
    return False

# Is our choice good or not?
def valid_number_check(num, i, j):
    #Checking vertically
    for row in range(args.size*args.size):
        if sudoku_board[row][j] == num:
            return False

    #Checking horizontally
    for col in range(args.size*args.size):
        if sudoku_board[i][col] == num:
            return False

    #Check in the 3x3 gird / box
    grid_row = (i // args.size) * args.size
    grid_col = (j // args.size) * args.size

    for i in range(args.size):
        for j in range(args.size):
            if sudoku_board[grid_row + i][grid_col + j] == num:
                return False

    # Once all tests are passed return true
    return True

# Solver
def solver():
    cells_exist = empty_cells_exist()

    if not cells_exist:
        return True

    i, j = cells_exist[0], cells_exist[1]
    for num in range(1,args.size * args.size + 1):
        if valid_number_check(num, i, j):
            sudoku_board[i][j] = num
            if args.ani:
            	printText(sudoku_board)
            
            #Backtracking (checking the next step)
            if solver():
                return True
            else:
                sudoku_board[i][j] = 0
                
#     False if nothing (1 through 9) yield an "accepted answer"
    return False

display_board(sudoku_board)


if solver():
    display_board(sudoku_board)
    printText(sudoku_board)
    print('Done')
    cv2.waitKey(0)
else:
    print("no solution available")
