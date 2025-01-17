# -*- coding: utf-8 -*-
"""tictactoe_proj.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b71dntRQaVKPP7uTIaS7P16z2rDD4sgS
"""

import os

def initialize_board():
    return [' ' for _ in range(9)]

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def check_draw(board):
    return ' ' not in board

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Enter a valid number (1-9).")

def play_game():
    scores = {'X': 0, 'O': 0}

    while True:
        board = initialize_board()
        current_player = 'X'
        game_over = False

        while not game_over:
            display_board(board)
            move = get_player_move(board, current_player)
            board[move] = current_player

            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                scores[current_player] += 1
                game_over = True
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

        print(f"Scores: Player X - {scores['X']}, Player O - {scores['O']}")
        if input("Play again? (y/n): ").lower() != 'y':
            break

play_game()