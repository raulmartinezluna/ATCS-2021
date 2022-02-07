import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Welcome to TicTacToe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing your pieces - the first to 3 in a row wins!")

        return

    def print_board(self):
        # TODO: Print the board
        print(" ","0","1", "2", sep= "\t")
        for row in range(3):
            print(row, self.board[row][0], self.board[row][1], self.board[row][2], sep="\t")

        return

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid

        validMove = False
        if row in [0, 1, 2] and col in [0, 1, 2]:
            if self.board[row][col] == "-":
                validMove = True

        return validMove

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player

        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = int(input("Enter a row: "))
        col = int(input("Enter a column: "))
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)
            self.print_board()
        else:
            print("Please enter a valid move.")
            self.take_manual_turn(player)
        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player, "'s  Turn")
        self.take_manual_turn(player)
        return

    def check_col_win(self, player):
        # TODO: Check col win
        for col in range(3):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        for row in range(3):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie0
        spotsUsed = 0
        for row in range(3):
            for col in range(3):
                if "-" != self.board[row][col]:
                    spotsUsed += 1
        if spotsUsed == 9:
            return True
        return False

    def play_game(self):
        # TODO: Play game
        self.print_instructions()
        self.print_board()
        player = "X"
        while not self.check_win("X") and not self.check_win("O") and not self.check_tie():
            self.take_turn(player)
            if player == "X":
                player = "O"
            elif player == "O":
                player = "X"
        if self.check_win("X"):
            print("X wins!")
        elif self.check_win("O"):
            print("O wins!")
        else:
            print("There is a tie!")
        return

