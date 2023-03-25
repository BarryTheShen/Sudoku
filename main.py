import random
import tkinter as tk
from tkinter import ttk
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def seed_generator():
    # Seed the random number generator
    random.shuffle(random_list)
    seed = ''
    for i in random_list:
        seed = seed + str(i)
    for i in range(7):
        seed = seed + str(random.randint(1, 6))
    for i in range(4):
        seed = seed + str(random.randint(1, 2))
    return seed


def order_seed_decode(seed_num, code):
    if seed_num == 1:
        return [code[0], code[1], code[2]]
    elif seed_num == 2:
        return [code[0], code[2], code[1]]
    elif seed_num == 3:
        return [code[1], code[0], code[2]]
    elif seed_num == 4:
        return [code[1], code[2], code[0]]
    elif seed_num == 5:
        return [code[2], code[0], code[1]]
    elif seed_num == 6:
        return [code[2], code[1], code[0]]
    else:
        raise ValueError('Invalid seed number')


def move_seed_decode(seed_num, code):
    if seed_num == 1:
        return [code[2], code[0], code[1]]
    elif seed_num == 2:
        return [code[1], code[2], code[0]]
    else:
        raise ValueError('Invalid seed number')


def expansion_row(list):
    fixed_list = []
    for i in list:
        for j in i:
            fixed_list.append(j)

    return fixed_list

def generate_sudoku_grid(seed=seed_generator()):
    # Generate the sudoku grid
    tempseed = []
    for j in seed:
        tempseed.append(int(j))

    seed = tempseed.copy()
    group1 = order_seed_decode(seed[9], seed[0:3])
    group2 = order_seed_decode(seed[10], seed[3:6])
    group3 = order_seed_decode(seed[11], seed[6:9])

    for i in order_seed_decode(seed[15], [1, 2, 3]):
        tempRow1 = order_seed_decode(seed[12+i-1], [group1, group2, group3])
        tempRow2 = move_seed_decode(seed[19], tempRow1)
        tempRow3 = move_seed_decode(seed[19], tempRow2)

        if i == 1:
            row1 = tempRow1.copy()
            row2 = tempRow2.copy()
            row3 = tempRow3.copy()
        elif i == 2:
            row4 = tempRow1.copy()
            row5 = tempRow2.copy()
            row6 = tempRow3.copy()
        elif i == 3:
            row7 = tempRow1.copy()
            row8 = tempRow2.copy()
            row9 = tempRow3.copy()
        else:
            raise ValueError("Unknown Mistake, check function generate sudoku grid")

        group1 = move_seed_decode(seed[16], group1)
        group2 = move_seed_decode(seed[17], group2)
        group3 = move_seed_decode(seed[18], group3)

    return [expansion_row(row1), expansion_row(row2), expansion_row(row3), expansion_row(row4), expansion_row(row5),
            expansion_row(row6), expansion_row(row7), expansion_row(row8), expansion_row(row9)]


def display_sudoku(sudoku_grid, difficulty):
    # Display the sudoku grid
    root = tk.Tk()
    root.title("Sudoku")
    root.geometry("500x360")
    root.resizable(0, 0)
    missing = []
    for i in range(9):
        for j in range(9):
            frame = tk.Frame(root, width=2, height=1, bd=1, relief='flat', bg='black')
            frame.grid(row=i, column=j)
            style = ttk.Style()
            style.configure("Black.TSeparator", bg="black", bd=20, relief='flat', width=2, height=2)
            if j == 0 or j == 3 or j == 6:
                ttk.Separator(root, orient='vertical', style='Black.TSeparator').grid(sticky='w', row=i, column=j, ipady=19)
            if i == 0 or i == 3 or i == 6:
                ttk.Separator(root, orient='horizontal', style='Black.TSeparator').grid(sticky='n', row=i, column=j, ipadx=19)
            tf = random.choices((True, False), weights=[difficulty, 1-difficulty], k=1)
            if tf[0]:
                label = tk.Label(root, text=sudoku_grid[i][j], width=2, height=1, font=("Arial", 20), bg='green')
                label.grid(row=i, column=j)
            else:
                missing.append([i, j])
                entry = tk.Entry(root, width=2, font=("Arial", 20), bg='white', relief='flat')
                entry.grid(row=i, column=j)
    button = tk.Button(root, text="Check", width=10, height=1, font=("Arial", 20), bg='white', relief='flat', command=grid_check)
    button.grid(row=9, column=0, columnspan=9)
    root.update()
    return missing


def grid_check():
    # Check the grid
    pass


def player_operation(missing, grid):
    # Player operation
    pass



def ending():
    # Game end
    pass


def main():
    seed = seed_generator()
    grid = generate_sudoku_grid(seed)
    missing = display_sudoku(generate_sudoku_grid(seed), 0.5)
    game_end = False
    while not game_end:
        player_operation(missing, grid)
    ending()


if __name__ == '__main__':
    main()