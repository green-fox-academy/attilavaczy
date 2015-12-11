

class Board():
    board = []
    def __init__(self):
        for n in range(10):
            self.board.append(['0'] * 10)

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

newBoard = Board()
print('Play Battleship')
print(newBoard.board)
