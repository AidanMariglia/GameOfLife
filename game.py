import random
import sys
import time


def dead_state(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


def random_state(width, height):
    board = dead_state(width, height)

    for i in range(height):
        for j in range(width):
            if random.random() >= 0.9:
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board


def render(board):
    print("-"*(len(board[0])+2))
    for row in board:
        print("|", end="")
        for cell in row:
            if cell:
                print(chr(9608), end="")
            else:
                print(" ", end="")

        print("|", end="")
        print("")
    print("-"*(len(board[0])+2))


def next_board_state(board):
    new_board = dead_state(len(board[0]), len(board))
    width = len(board[0])
    height = len(board)

    for i in range(height):
        for j in range(width):
            count = count_neighbors(board, i, j)

            if count <= 1:
                new_board[i][j] = 0
            elif count <= 3:
                new_board[i][j] = 1
            else:
                new_board[i][j] = 0

    return new_board



def count_neighbors(board, row, col):
    width = len(board[0])
    height = len(board)
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if row + i  < height and width + j < width:
                count += board[row + i][col + j]
            elif row + i <  height:
                count += board[row + i][0]
            elif width + j < width:
                count += board[0][col + j]
            else:
                count += board[0][0]


    return count


if __name__ == "__main__":
    current_state = random_state(int(sys.argv[1]), int(sys.argv[2]))
    while 1:
        render(current_state)
        current_state = next_board_state(current_state)
        time.sleep(1)