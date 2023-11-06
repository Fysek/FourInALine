class FourInALine:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.current_player = 'Player 1'
        self.piece = 'X'
        self.shared_pieces = 8

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
    
    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col):
        if self.shared_pieces > 0:
            if self.is_valid_move(row, col):
                self.board[row][col] = self.piece
                self.shared_pieces -= 1
                return True
        elif self.is_adjacent(row, col):
            adjacent_pieces = self.get_adjacent_pieces(row, col)
            if adjacent_pieces and all(piece != self.current_player for piece in adjacent_pieces):
                self.board[row][col] = self.piece
                return True
        return False

    def is_adjacent(self, row, col):
        return any(self.board[i][j] != ' ' for i in range(max(0, row-1), min(5, row+2)) for j in range(max(0, col-1), min(5, col+2)))

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

# Example usage:
game = FourInALine()
game.print_board()

while not game.is_draw():
    row = int(input(f'{game.current_player}, enter row (1-5): ')) - 1
    col = int(input(f'{game.current_player}, enter column (1-5): ')) - 1
    
    if game.make_move(row, col):
        game.print_board()
        if game.check_winner():
            break
        else:
            game.current_player = 'Player 2' if game.current_player == 'Player 1' else 'Player 1'
    else:
        print("Invalid move. Try again.")

if game.check_winner():
    print(f"{game.current_player} wins!")
else:
    print("It's a draw!")
