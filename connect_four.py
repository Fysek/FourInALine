class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
        print('-' * (self.cols * 2 - 1))

    def is_valid_move(self, col):
        return self.board[0][col] == ' '

    def make_move(self, col):
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = self.current_player
                return True
        return False

    def check_winner(self):
        # Check horizontally
        for i in range(self.rows):
            for j in range(self.cols - 3):
                if (
                    self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] != ' '
                ):
                    return True

        # Check vertically
        for i in range(self.rows - 3):
            for j in range(self.cols):
                if (
                    self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] != ' '
                ):
                    return True

        # Check diagonally (top-left to bottom-right)
        for i in range(self.rows - 3):
            for j in range(self.cols - 3):
                if (
                    self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != ' '
                ):
                    return True

        # Check diagonally (bottom-left to top-right)
        for i in range(3, self.rows):
            for j in range(self.cols - 3):
                if (
                    self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3] != ' '
                ):
                    return True

        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row)

# Example usage:
game = ConnectFour()
game.print_board()

while not game.is_draw() and not game.check_winner():
    col = int(input(f'{game.current_player}, choose a column (0-6): '))
    
    if 0 <= col < game.cols and game.is_valid_move(col):
        game.make_move(col)
        game.print_board()
        game.current_player = 'O' if game.current_player == 'X' else 'X'
    else:
        print("Invalid move. Try again.")

if game.check_winner():
    print(f"{game.current_player} wins!")
else:
    print("It's a draw!")
