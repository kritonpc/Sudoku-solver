import tkinter as tk
from tkinter import ttk
from tabulate import tabulate
 


def getGrid():
    sudoku_grid_in = [
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
    ret = sudoku_grid_in
 
    def clickMe():
        for i in range(9):
            for j in range(9):
                grid[i][j]=sudoku_grid[i][j].get()
                if grid[i][j] == '':
                    grid[i][j] = 0
                else:
                    grid[i][j] = int(grid[i][j])
        ret = grid
        window.destroy()
    
    
    window = tk.Tk()
     
    window.title("Python Tkinter Text Box")
    window.minsize(325,370)



    sudoku_grid = sudoku_grid_in
    grid = sudoku_grid
    name = sudoku_grid
    size = 35
    # nameEntered = ttk.Entry(window, width = 5, textvariable = name)
    # nameEntered.grid(column = 0, row = 1)
    for i in range(9):
            for j in range(9):
            	name[i][j] = tk.StringVar()
            	sudoku_grid[i][j] = ttk.Entry(window, width = 3, textvariable = name[i][j], justify='center')
            	sudoku_grid[i][j].place(x = 5+j*size ,y = 5 + i*size, height=size, width=size)
     
    button = ttk.Button(window, text = "Solve", command = clickMe)
    button.place(x = 130 ,y = 330, height=30, width=70)
    window.mainloop()
    return ret

