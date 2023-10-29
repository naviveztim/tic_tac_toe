import random


def print_board(title: str, board: list):
    """ Print the Tic Tac Toe board """
    print(title)
    for row in board:
        print(" | ".join(row))
        print("--+---+---")


def get_user_entry(board: list):
    """ Get and validate user's entry """

    user_row, user_col = map(int, input("Въведете ход (ред[0-2] колона[0-2]): ").split())
    while user_row not in [0, 1, 2] or user_col not in [0, 1, 2] or board[user_row][user_col] != " ":
        print("Невалиден ход. Опитайте отново.")
        user_row, user_col = map(int, input("Въведете ход (ред[0-2] колона[0-2]): ").split())
    board[user_row][user_col] = "O"


def get_random_user_entry(board: list, player: str):
    """ Imitate user's entry """

    # Get empty positions
    empty_positions = [(i, j) for i in [0, 1, 2] for j in [0, 1, 2] if board[i][j] == " "]
    random_empty_position = random.choice(empty_positions)
    user_row, user_col = random_empty_position
    while user_row not in [0, 1, 2] or user_col not in [0, 1, 2] or board[user_row][user_col] != " ":
        print("Невалиден ход. Опитайте отново.")
        user_row, user_col = map(int, input("Въведете ход (ред[0-2] колона[0-2]): ").split())
    board[user_row][user_col] = player