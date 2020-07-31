import tkinter as tk
from tkinter import ttk
from tabulate import tabulate
 


def getGrid(size):
    sudoku_grid_3 = [
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
    sudoku_grid_4 = [
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
    
    if size == 9:
        sudoku_grid = sudoku_grid_3
    else:
        sudoku_grid = sudoku_grid_4
    ret = sudoku_grid

    def clickMe():
        for i in range(size):
            for j in range(size):
                grid[i][j]=sudoku_grid[i][j].get()
                if grid[i][j] == '':
                    grid[i][j] = 0
                else:
                    if sudoku_grid[i][j] == 'A': sudoku_grid[i][j] = 10 
                    if sudoku_grid[i][j] == 'B': sudoku_grid[i][j] = 11 
                    if sudoku_grid[i][j] == 'C': sudoku_grid[i][j] = 12 
                    if sudoku_grid[i][j] == 'D': sudoku_grid[i][j] = 13 
                    if sudoku_grid[i][j] == 'E': sudoku_grid[i][j] = 14 
                    if sudoku_grid[i][j] == 'F': sudoku_grid[i][j] = 15 
                    if sudoku_grid[i][j] == 'G': sudoku_grid[i][j] = 16 
                    grid[i][j] = int(grid[i][j])
        ret = grid
        window.destroy()
    
    
    window = tk.Tk()
     
    window.title("Sudoku")
    window.minsize(size*36,size*41)


    grid = sudoku_grid
    name = sudoku_grid
    winSize = 35
    # nameEntered = ttk.Entry(window, width = 5, textvariable = name)
    # nameEntered.grid(column = 0, row = 1)
    for i in range(size):
            for j in range(size):
            	name[i][j] = tk.StringVar()
            	sudoku_grid[i][j] = ttk.Entry(window, width = 3, textvariable = name[i][j], justify='center')
            	sudoku_grid[i][j].place(x = 5+j*winSize ,y = 5 + i*winSize, height=winSize, width=winSize)
     
    button = ttk.Button(window, text = "Solve", command = clickMe)
    button.place(x = size*16 ,y = size*36, height=30, width=70)
    window.mainloop()
    return ret

