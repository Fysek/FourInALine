class FourInALine:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.current_player = 'X'
        self.player_pieces = {'X': 4, 'O': 4}

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
    
    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        if self.player_pieces[self.current_player] > 0:
            if self.is_valid_move(row, col):
                self.board[row][col] = self.current_player
                self.player_pieces[self.current_player] -= 1
                return True
        elif self.is_adjacent(row, col):
            adjacent_pieces = self.get_adjacent_pieces(row, col)
            if adjacent_pieces and all(piece != self.current_player for piece in adjacent_pieces):
                self.board[row][col] = self.current_player
                return True
        return False

    def is_adjacent(self, row, col):
        return any(self.board[i][j] != ' ' for i in range(row-1, row+2) for j in range(col-1, col+2))

    def get_adjacent_pieces(self, row, col):
        adjacent_pieces = []
        for i in range(max(0, row-1), min(5, row+2)):
            for j in range(max(0, col-1), min(5, col+2)):
                if self.board[i][j] != ' ':
                    adjacent_pieces.append(self.board[i][j])
        return adjacent_pieces

    def check_winner(self):
        for i in range(5):
            for j in range(2):
                if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3] != ' ':
                    return True

        for i in range(2):
            for j in range(5):
                if self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j] != ' ':
                    return True

        return False

    def is_draw(self):
        return all(cell != ' ' for row in self.board for cell in row) or self.check_winner()

game = FourInALine()
game.print_board()

while not game.is_draw() and not game.check_winner():
    row = int(input(f'Player {game.current_player}, enter row (0-4): '))
    col = int(input(f'Player {game.current_player}, enter column (0-4): '))
    
    if game.make_move(row, col):
        game.print_board()
        game.current_player = 'O' if game.current_player == 'X' else 'X'
    else:
        print("Invalid move. Try again.")

if game.check_winner():
    print(f"Player {game.current_player} wins!")
else:
    print("It's a draw!")
