import math
from utils.utils import check_draw, check_win


class MinMaxModel:

    @staticmethod
    def find_best_move(board):
        """ Find the best move for the computer"""
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = MinMaxModel.minimax(board, 0, -math.inf, math.inf, False)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        row, col = best_move
        board[row][col] = "X"

    @staticmethod
    def minimax(board, depth, alpha, beta, is_maximizing):
        """ Minimax algorithm with alpha-beta pruning"""

        scores = {"X": 1, "O": -1, "Draw": 0}
        if check_win(board, "X"):
            return scores["X"]
        if check_win(board, "O"):
            return scores["O"]
        if check_draw(board):
            return scores["Draw"]

        if is_maximizing:
            max_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        score = MinMaxModel.minimax(board, depth + 1, alpha, beta, False)
                        board[i][j] = " "
                        max_score = max(max_score, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return max_score
        else:
            min_score = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        score = MinMaxModel.minimax(board, depth + 1, alpha, beta, True)
                        board[i][j] = " "
                        min_score = min(min_score, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return min_score




