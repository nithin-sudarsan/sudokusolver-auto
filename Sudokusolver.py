import numpy as np
import pyautogui as pg
import time



grid=[]



while True:
    row=list(input("rows: "))
    ints=[]
    for n in row:
        ints.append(int(n))

    grid.append(ints)
    if len(grid)==9:
        break



#print(grid)
time.sleep(4)



'''str_fin=[]
for i in range(0,9):
    for j in range(0,9):
        str_fin.append(grid[i][j])
print(str_fin)'''



def possible(row,col,number):
    global grid
    #check if the same number is present on the row
    for i in range(0,9):
        if grid[row][i]==number:
            return False
    #check if the same number is present on the col
    for i in range(0,9):
        if grid[i][col]==number:
            return False
    #check if the same number is present on the square
    x0=(row//3)*3
    y0=(col//3)*3
    for i in  range(0,3):
        for j in range(0,3):
            if grid[x0+i][y0+j]==number:
                return False
    return True


def Print(matrix):
    counter=[]
    '''str_fin=[]
    for i in range(0,9):
        for j in range(0,9):
            str_fin.append(grid[i][j])'''
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))
    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter)%9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


def solve():
    global grid
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]==0:
                for number in range(1,10):
                    if possible(i,j,number):
                        grid[i][j]=number
                        solve()
                        grid[i][j]=0
                return
    Print(grid)
    input('More possible solutions')
solve()  
