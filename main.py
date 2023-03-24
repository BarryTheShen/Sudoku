import random
import pygame
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def seed_generator():
    # Seed the random number generator
    random.shuffle(random_list)
    seed = ''
    for i in random_list:
        seed = seed + str(i)
    for i in range(5):
        seed = seed + str(random.randint(1, 6))
    for i in range(4):
        seed = seed + str(random.randint(1, 2))
    return seed


def order_seed_decode(seed_num, code):
    if seed_num == 1:
        return code[0], code[1], code[2]
    elif seed_num == 2:
        return code[0], code[2], code[1]
    elif seed_num == 3:
        return code[1], code[0], code[2]
    elif seed_num == 4:
        return code[1], code[2], code[0]
    elif seed_num == 5:
        return code[2], code[0], code[1]
    elif seed_num == 6:
        return code[2], code[1], code[0]
    else:
        raise ValueError('Invalid seed number')


def move_seed_decode(seed_num, code):
    if seed_num == 1:
        return code[2], code[0], code[1]
    elif seed_num == 2:
        return code[1], code[2], code[0]
    else:
        raise ValueError('Invalid seed number')


def generate_sudoku_grid(seed):
    # Generate the sudoku grid

    for i in order_seed_decode(seed[13], [1, 2, 3]):
        group1 = order_seed_decode(seed[9], seed[0:3])
        group2 = order_seed_decode(seed[10], seed[3:6])
        group3 = order_seed_decode(seed[11], seed[6:9])

        tempRow1 = order_seed_decode(seed[12], [group1, group2, group3])
        tempRow2 = move_seed_decode(seed[17], tempRow1)
        tempRow3 = move_seed_decode(seed[17], tempRow2)

        if i == 1:
            row1 = tempRow1
            row2 = tempRow2
            row3 = tempRow3
        elif i == 2:
            row4 = tempRow1
            row5 = tempRow2
            row6 = tempRow3
        elif i == 3:
            row7 = tempRow1
            row8 = tempRow2
            row9 = tempRow3
        else:
            raise ValueError("Unknown Mistake, check function generate sudoku grid")



def display_sudoku(sudoku_grid):
    # Display the sudoku grid
    pass


def generate_sudoku():
    # Generate the sudoku
    pass


def player_operation():
    # Player operation
    pass


def ending():
    # Game end
    pass


def main():
    seed = seed_generator()
    display_sudoku(generate_sudoku_grid(seed))
    generate_sudoku()
    game_end = False
    while not game_end:
        player_operation()
    ending()
