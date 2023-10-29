
def check_entry(board: list, player: str, verbose=True) -> str:
    """ Checks if game is over"""

    if check_win(board, player):
        if verbose:
            print(f"{player} печели!")
        return f"{player} Wins!"

    if check_draw(board):
        if verbose:
            print("Реми!")
        return "Draw"

    return ""


def check_win(board: list, player: str) -> bool:
    """Function to check if any player has won"""

    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False


def check_draw(board):
    """Function to check if the board is full"""

    return all([cell != " " for row in board for cell in row])

