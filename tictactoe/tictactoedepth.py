import random


class TicTacToeDepth:
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
        if player == "X":
            self.take_manual_turn(player)
        if player == "O":
            self.take_minimax_turn(player)
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

    def take_random_turn(self, player):
        # TODO: Should randomly place a piece on the board
        random.randint(0,2)
        random.randint(0,2)
        row = random.randint(0,2)
        col = random.randint(0,2)
        if self.is_valid_move(row, col):
            self.place_player(player, row, col)
            self.print_board()
        else:
            self.take_random_turn(player)
        return

    def minimax(self, player, depth):
        #Base cases
        if self.check_win("O"):
            return (10, None, None)
        if self.check_win("X"):
            return (-10, None, None)
        if self.check_tie() or depth == 0:
            return (0, None, None)

        opt_row = -1
        opt_col = -1
        #The rest
        if player == "O":
            best = -10
            for r in range(3):
                for c in range(3):
                    if self.is_valid_move(r, c):
                        self.place_player("O", r, c)
                        score = self.minimax("X", depth-1)[0]
                        if best < score:
                            best = score
                            opt_row = r
                            opt_col = c
                        self.place_player("-", r, c)
            return best, opt_row, opt_col
        if player == "X":
            worst = 10
            for r in range(3):
                for c in range(3):
                    if self.is_valid_move(r, c):
                        self.place_player("X", r ,c)
                        score = self.minimax("O", depth-1)[0]
                        if worst > score:
                            worst = score
                            opt_row = r
                            opt_col = c
                        self.place_player("-", r, c)
            return worst, opt_row, opt_col

    def take_minimax_turn(self, player):
        score, row, col = self.minimax(player, 2)
        self.place_player(player, row, col)
        self.print_board()

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