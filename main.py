from view.inout import print_board, get_user_entry, get_random_user_entry
from model.min_max_model import MinMaxModel
from utils.utils import check_entry
import pandas as pd
import numpy as np
import os

NUM_GAMEPLAYS = 5000
STATS_FILEPATH = 'games_collection.csv'
COLUMNS = ['0-0', '0-1', '0-2', '1-0', '1-1', '1-2', '2-0', '2-1', '2-2']


def play_tic_tac_toe_with_partner():
    """ Plays against user """

    for _ in range(9):

        # If computer starts first, it (almost) always win!
        # For fair game exchange below computer's and users blocks.

        # Computer's move
        MinMaxModel.find_best_move(board)
        print_board("Ходът на компютъра:", board)
        if check_entry(board, "X"):
            break

        # User's move
        get_user_entry(board)
        print_board("Вашият ход:", board)
        check_stats(board, "O")
        if check_entry(board, "O"):
            break


def compare_lines(line1: pd.Series, line2: pd.Series) -> bool:
    """ Compares two pandas series """

    for col in line1.index:
        if line2[col] != ' ' and line1[col] != line2[col]:
            return False
    return True


def find_matches(pattern: list) -> pd.DataFrame:
    """ Find rows from games collection that have current pattern """

    # Construct pandas dataframe from current board pattern
    df2 = pd.DataFrame([pattern], columns=COLUMNS)

    # Compare pattern dataframe to all games collection dataframe
    matches_indexes = [index for index, row in df_games_collection[COLUMNS].iterrows()
                       if compare_lines(row, df2.iloc[0])]

    return df_games_collection.loc[matches_indexes]


def check_stats(current_board: list, player: str):
    """From collected samples which match current game pattern- extract umber of wins/losses/draw"""

    opponent = "X" if player == "O" else "O"
    current_board = np.array(current_board).flatten().tolist()

    # Extract from stats dataframe only rows that match current board
    df_matches = find_matches(current_board)
    num_matches = df_matches.shape[0]

    # Find number of Wins in matched dataframe
    win_condition = df_matches['result'] == f"{player} Wins!"
    num_wins = df_matches[win_condition].shape[0]

    # Find number of Losses in matched dataframe
    lost_codition = df_matches['result'] == f"{opponent} Wins!"
    num_losses = df_matches[lost_codition].shape[0]

    # Find number of Draws in matched dataframe
    draw_codition = df_matches['result'] == "Draw"
    num_draws = df_matches[draw_codition].shape[0]

    if num_matches > 0:
        print(f"Tози ход в тази ситуация играч: '{player}' е побеждавал {100*round(num_wins/num_matches, 2)}%"
              f", давал реми {100*round(num_draws/num_matches, 2)}% "
              f"и губил в {100*round(num_losses/num_matches, 2)}% от случаите. ")
    else:
        print("Не може да даде заключение на базата на събраната информация. ")
    print()


def append_result(result: str):
    """ Collect game disposition and result """

    # Convert board + result in one flat array
    row = list(np.array(board).flatten()) + [result]

    # Add game to dataset
    df_games_collection.loc[len(df_games_collection.index)] = row


def play_tic_tac_toe_by_itself():
    """ Plays against itself. Do not use MinMax algorith or other optimized algorithm on
    first player because it will always win, which makes dataset unbalanced"""

    for _ in range(9):

        # Computer's Player1
        get_random_user_entry(board, "O")
        result = check_entry(board, "O", False)
        if result:
            append_result(result)
            break

        # Computer's Player2
        get_random_user_entry(board, "X")
        result = check_entry(board, "X", False)
        if result:
            append_result(result)
            break


if __name__ == "__main__":

    # Collect different game scenarios
    if not os.path.exists(STATS_FILEPATH):
        print(f'Събира се колекция от различни игрови комбинации. Моля изчакайте...')
        df_games_collection = pd.DataFrame(columns=COLUMNS + ['result'])
        # Play several games
        for _ in range(1, NUM_GAMEPLAYS+1):
            # Start new game
            board = [[" " for _ in range(3)] for _ in range(3)]
            # Play by itself
            play_tic_tac_toe_by_itself()

        # Remove already met combination
        df_games_collection = df_games_collection.drop_duplicates()

        # Save games' combinations and results
        df_games_collection.to_csv(STATS_FILEPATH, index=False)
    else:
        # Load if already game scenarios were collected
        df_games_collection = pd.read_csv(STATS_FILEPATH)
    print('Колекцията от игрови комбинации е събрана.')

    # Start new game
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board("Играта започва!", board)

    # Play with partner
    play_tic_tac_toe_with_partner()
