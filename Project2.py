# File: Project2.py
# Student: Asmit Chakraborty
# UT EID: ac83832
# Course Name: CS303E
#
# Date: November 3, 2022
# Description of Program: Creates a game of tic tac toe that the user can play
# with a bot

import random

# Some global constants:

HUMAN = 0
MACHINE = 1
WELCOME = "Welcome to our Tic-Tac-Toe game! \nPlease begin playing.\n"

ILLEGAL_MOVE = "Illegal move specified.  Try again!"
ILLEGAL_SYNTAX = "Response should be r, c. Try again!"

YOU_WON = "Congratulations! You won!"
YOU_TIED = "Looks like a tie.  Better luck next time!"
YOU_LOST = "Sorry!  You lost!"

def initialBoard():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


class TicTacToe:
    def __init__(self):
        # Initialize the game with the board and current player

        self.__board = initialBoard()
        self.__player = HUMAN

    def __str__(self):
        row_count = 0
        printed_board = ""

        # Loops through the board
        for row in self.__board:
            row_count += 1
            col_count = 0

            # Loops through each entry in the board and adds the entry + | to printed_board
            for entry in row:
                col_count += 1
                printed_board += entry

                if col_count < 3:
                    printed_board += "|"

            # At the end of the first two rows, adds "-----" in a new line to printed_board
            if row_count < 3:
                printed_board += "\n-----\n"

        return printed_board

    def getPlayer(self):
        return self.__player

    def isWin(self):
        # See if the board represents a win for the current
        # player. A win is three of the current player's tokens
        # in a single row, column, or either diagonal.

        win_char = "X"
        if self.__player == MACHINE:
            win_char = "O"

        # In the same row
        for row in self.__board:
            row_win = True

            for entry in row:
                if entry != win_char:
                    row_win = False
                    break
            if row_win:
                return True

        # In the same column
        for column in range(3):
            column_win = True

            for row in range(3):
                if self.__board[row][column] != win_char:
                    column_win = False
                    break
            if column_win:
                return True

        # In the main diagonal
        main_diagonal = True
        for index in range(3):
            if self.__board[index][index] != win_char:
                main_diagonal = False
        if main_diagonal:
            return True

        # In the other diagonal
        inverse_diagonal = True
        for index in range(3):
            if self.__board[2 - index][index] != win_char:
                inverse_diagonal = False
        if inverse_diagonal:
            return True

        # If none of the above are true, return false indicating that
        # nobody has won yet
        return False

    def swapPlayers(self):
        # Change the current player from HUMAN to MACHINE or
        # vice versa.

        if self.__player == HUMAN:
            self.__player = MACHINE
        else:
            self.__player = HUMAN

    def humanMove(self):
        # Ask the HUMAN to specify a move.  Check that it's
        # valid (syntactically, in range, and the space is
        # not occupied).  Update the board appropriately.

        print()
        print("Your turn:")

        # Infinite loop that keeps asking user for a move until a valid one is inputted
        while True:
            given = input("  Specify a move r, c: ").strip()
            print()

            # Check if input is correct syntactically
            if given.find(",") == -1:
                print(ILLEGAL_SYNTAX)
                continue

            move = given.split(",")

            # Check if input is in range after stripping white space
            r = int(move[0].strip())
            c = int(move[1].strip())
            if not (0 <= r <= 2) or not (0 <= c <= 2):
                print(ILLEGAL_MOVE)
                continue

            # Check if input space is empty
            if self.__board[r][c] != " ":
                print(ILLEGAL_MOVE)
                continue

            # If none of these conditions are true, add "X"
            # to the requested slot and break the loop
            self.__board[r][c] = "X"
            break

    def machineMove(self):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.

        print()
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.__board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                print()
                self.__board[r][c] = "O"
                return


def driver():
    """This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move."""

    print()

    # Print the welcome message
    print(WELCOME)

    # Initialize the board and current player
    ttt = TicTacToe()
    print(ttt)

    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # The current player may be HUMAN
        # or MACHINE
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print(ttt)
            if ttt.isWin():
                print()
                print(YOU_WON)
                print()
                return

        else:
            # Else MACHINE takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print(ttt)
            if ttt.isWin():
                print()
                print(YOU_LOST)
                print()
                return

        # Swap players.
        ttt.swapPlayers()

    # After nine moves with no winner, it's a tie.
    print()
    print(YOU_TIED)
    print()


driver()
