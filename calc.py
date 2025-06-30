import sys
import random
import time
count = 0
start = time.time()


def sudoku(solution):
    global count
    new_array = [row[:] for row in solution]
    position = [i for i in range(81)]
    random.shuffle(position)

    for pos in position:
        ax = pos // 9
        ay = pos % 9
        old_value = new_array[ax][ay]
        new_array[ax][ay] = 0
        count = 0
        sudoku_solve(new_array)
        if count > 1:
            new_array[ax][ay] = old_value
    return new_array

def random_solution():
    arr = [[0 for j in range(9)] for i in range(9)]
    def fill(a = 0, b = 0):
        next_a = a + (b + 1) // 9
        next_b = (b + 1) % 9
        if a == 9:
            return True
        number_list = list(range(1, 10))
        random.shuffle(number_list)
        for number in number_list:
            if sudoku_check(a , b , number, arr):
                arr[a][b] = number
                if fill(next_a, next_b):
                    return True
        arr[a][b] = 0
        return False
    fill()
    return arr




def sudoku_check(a , b, val, arr):
    # check row and column
    for j in range(0 , 9, 1):
        if arr[a][j] == val or arr[j][b] == val:
            return False
    # check square
    square_owner = [a // 3, b // 3]
    for i in range(3):
        for j in range(3):
            if arr[square_owner[0] * 3 + i][square_owner[1] * 3 + j] == val:
                return  False
    return True


def sudoku_solve(arr, a = 0, b = 0):
    global count
    #next cell coordinate
    if count == 2:
        return
    if a == 9:
        count += 1
        return
    next_x = a + (b + 1 ) // 9
    next_y = (b + 1) % 9


    if arr[a][b]:
        sudoku_solve(arr, next_x, next_y) #recursion
    else:
        for value in range(1, 10, 1): # choose the value for the current cell;
            valid = sudoku_check(a , b, value, arr)
            if valid:
                arr[a][b] = value
                sudoku_solve(arr, next_x, next_y)
                arr[a][b] = 0


end = time.time()
elapsed  = (end- start) * 1000
print(f"Elapsed: {elapsed:.2f} ms")
