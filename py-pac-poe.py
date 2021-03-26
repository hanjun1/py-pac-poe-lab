class Board():
    def __init__(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]

    def turn(self, player):
        while True:
            player_move = input(
                f"Player {player.marker}'s Move (example B2): ")
            if len(player_move) != 2:
                print("Invalid Move! Try again!")
            elif player_move[0].lower() not in ["a", "b", "c"] and player_move[1] not in ["1", "2", "3"]:
                print('hello')
                print("Invalid Move! Try again!")
            else:
                row = int(player_move[1]) - 1
                if (player_move[0].lower() == "a"):
                    column = 0
                elif (player_move[0].lower() == "b"):
                    column = 1
                else:
                    column = 2
                if self.board[row][column] != "":
                    print("Invalid Move! Try again!")
                else:
                    self.board[row][column] = player.marker
                    break

    def checkTie(self):
        for i in range(0, 3):
            for y in range(0, 3):
                if self.board[i][y] == "":
                    return False
        return True

    def checkWin(self):
        if self.checkDiagonalWin() or self.checkHorizontalWin() or self.checkDiagonalWin():
            return True
        return False

    def checkDiagonalWin(self):
        win = ["XXX", "OOO"]
        dia1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        dia2 = self.board[2][0] + self.board[1][1] + self.board[0][2]
        if dia1 in win or dia2 in win:
            return True
        return False

    def checkHorizontalWin(self):
        win = ["XXX", "OOO"]
        for i in range(0, 3):
            hor = ""
            for j in range(0, 3):
                hor += self.board[i][j]
            if hor in win:
                return True
        return False

    def checkVerticalWin(self):
        win = ["XXX", "OOO"]
        for i in range(0, 3):
            hor = ""
            for j in range(0, 3):
                hor += self.board[j][i]
            if hor in win:
                return True
        return False

    def print(self):
        print("    A   B   C  ")
        print("               ")
        print(
            f"1)  {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("   ----------- ")
        print(
            f"2)  {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("   ----------- ")
        print(
            f"3)  {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")
        print("")
        print("")


class Player():
    def __init__(self, marker):
        self.marker = marker


class Game():
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.win_cap = 0
        self.ties = 0

    def play(self):
        while True:
            wins = input("How many wins do you want to play up until?: ")
            try:
                wins = int(wins)
                if (wins > 0):
                    self.win_cap = wins
                    break
                else:
                    print("Enter a valid number")
            except ValueError:
                print("Not a valid number")
        while self.win_cap > self.player1_score and self.win_cap > self.player2_score:
            board = Board()
            player1 = Player("X")
            player2 = Player("O")
            board.print()
            while True:
                board.turn(player1)
                board.print()
                if board.checkWin():
                    print(f"Player {player1.marker} Wins!")
                    self.player1_score += 1
                    break
                if board.checkTie():
                    print("Tie Game!")
                    self.ties += 1
                    break
                board.turn(player2)
                board.print()
                if board.checkWin():
                    print(f"Player {player2.marker} Wins!")
                    self.player2_score += 1
                    break
                if board.checkTie():
                    print("Tie Game!")
                    self.ties += 1
                    break
            self.show_score_board()
        if (self.player1_score == self.win_cap):
            winner = player1.marker
        else:
            winner = player2.marker
        print(f"Congrats to player {winner} for winning {self.win_cap} games!")

    def show_score_board(self):
        print("")
        print("SCORE:")
        print(
            f"Player X: {self.player1_score}    Player O: {self.player2_score}    Tie: {self.ties}")
        print("")


# Main Game
print("----------------------")
print("Let's play Py-Pac-Poe!")
print("----------------------")

game = Game()
game.play()
