'''
Created on Nov. 9, 2019
Sudoku Solver
@author: Stuart Isley 160757220 Erman Dinsel 160364040 Jiana Lin 161470860
'''


def read_file(fileName):
    f = open(fileName, "r")
    matrix = []
    line = f.readline()
    while line != "":
        line = line.strip("\n")
        temp = line.split(" ")
        matrix.append(temp)
        line = f.readline()
    return matrix


# 0 represents an empty space in the matrix
def solve(matrix):
    temp = findNext(matrix)
    row = temp[0]
    col = temp[1]
    if row == -1:
        return True
    for i in range(1, 10):
        if checkRow(matrix, row, str(i)) and checkCol(matrix, col, str(i)) and checkBox(matrix, row, col, str(i)):
            matrix[row][col] = str(i)
            if (solve(matrix)):
                return True
            matrix[row][col] = str(0)
    return False


# find the next index in the matrix that has a 0, if none is found return (-1,-1)
def findNext(matrix):
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == '0':
                return (row, col)

    return (-1, -1)


def checkRow(matrix, row, num):
    for i in range(9):
        if matrix[row][i] == num:
            return False
    return True


def checkCol(matrix, col, num):
    for i in range(9):
        if matrix[i][col] == num:
            return False
    return True


def checkBox(matrix, row, col, num):
    if row < 3:
        if col < 3:
            for i in range(3):
                for j in range(3):
                    if matrix[i][j] == num:
                        return False
        elif 3 <= col and col <= 5:
            for i in range(3):
                for j in range(3, 6):
                    if matrix[i][j] == num:
                        return False
        else:
            for i in range(3):
                for j in range(6, 9):
                    if matrix[i][j] == num:
                        return False
    elif 3 <= row and row <= 5:
        if col < 3:
            for i in range(3, 6):
                for j in range(3):
                    if matrix[i][j] == num:
                        return False
        elif 3 <= col and col <= 5:
            for i in range(3, 6):
                for j in range(3, 6):
                    if matrix[i][j] == num:
                        return False
        else:
            for i in range(3, 6):
                for j in range(6, 9):
                    if matrix[i][j] == num:
                        return False

    else:
        if col < 3:
            for i in range(6, 9):
                for j in range(3):
                    if matrix[i][j] == num:
                        return False
        elif 3 <= col and col <= 5:
            for i in range(6, 9):
                for j in range(3, 6):
                    if matrix[i][j] == num:
                        return False
        else:
            for i in range(6, 9):
                for j in range(6, 9):
                    if matrix[i][j] == num:
                        return False
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


matrix = read_file("test.txt")
check = solve(matrix)
if check:
    print_board(matrix)
else:
    print("No solution found for this puzzle")



